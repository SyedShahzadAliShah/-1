"""Render LaTeX with MathJax (SVG output) through headless Chrome."""

from __future__ import annotations

import json
import os
import shutil
import signal
import subprocess
import tempfile
import time
import urllib.request
from pathlib import Path

import websocket

ROOT = Path(__file__).resolve().parent
MATHJAX = ROOT / "vendor" / "mathjax" / "es5" / "tex-svg-full.js"
MATHJAX_URL = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg-full.js"


def ensure_mathjax() -> Path:
    if MATHJAX.exists() and MATHJAX.stat().st_size > 100_000:
        return MATHJAX
    MATHJAX.parent.mkdir(parents=True, exist_ok=True)
    urllib.request.urlretrieve(MATHJAX_URL, MATHJAX)
    return MATHJAX


def _free_port() -> int:
    import socket

    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


def _cdp(ws, method: str, params: dict | None = None, session: str | None = None) -> dict:
    _cdp.counter += 1
    message = {"id": _cdp.counter, "method": method}
    if params:
        message["params"] = params
    if session:
        message["sessionId"] = session
    ws.send(json.dumps(message))
    while True:
        data = json.loads(ws.recv())
        if data.get("id") != _cdp.counter:
            continue
        if "error" in data:
            raise RuntimeError(f"{method} failed: {data['error']}")
        return data.get("result") or {}


_cdp.counter = 0


def render_formulas(formulas: list[str]) -> dict[str, str]:
    """Return each unique formula's MathJax SVG markup."""
    unique = []
    seen = set()
    for formula in formulas:
        key = formula.strip()
        if key and key not in seen:
            seen.add(key)
            unique.append(key)
    if not unique:
        return {}
    script = ensure_mathjax().as_uri()
    blocks = []
    for index, formula in enumerate(unique):
        safe = (
            formula.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
        )
        blocks.append(f'<div id="m{index}" class="formula">\\[{safe}\\]</div>')
    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['\\\\(', '\\\\)']],
    displayMath: [['\\\\[', '\\\\]']],
    packages: {{'[+]': ['ams']}}
  }},
  svg: {{ fontCache: 'none' }},
  startup: {{
    pageReady: () => MathJax.startup.defaultPageReady().then(() => {{
      document.documentElement.setAttribute('data-ready', '1');
    }})
  }}
}};
</script>
<script src="{script}"></script>
</head>
<body>
{''.join(blocks)}
</body>
</html>
"""
    work = Path(tempfile.mkdtemp(prefix="biek-mathjax-"))
    page = work / "formulas.html"
    page.write_text(html, encoding="utf-8")
    port = _free_port()
    profile = work / "profile"
    proc = subprocess.Popen(
        [
            "google-chrome",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            f"--user-data-dir={profile}",
            f"--remote-debugging-port={port}",
            "--remote-allow-origins=*",
            "about:blank",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        start_new_session=True,
    )
    try:
        version = None
        for _ in range(80):
            try:
                with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=0.5) as response:
                    version = json.load(response)
                break
            except Exception:
                time.sleep(0.1)
        if version is None:
            raise RuntimeError("Chrome did not open a debugging port for MathJax.")
        ws = websocket.create_connection(version["webSocketDebuggerUrl"], timeout=20)
        _cdp.counter = 0
        target = _cdp(ws, "Target.createTarget", {"url": page.as_uri()})
        attached = _cdp(
            ws,
            "Target.attachToTarget",
            {"targetId": target["targetId"], "flatten": True},
        )
        session = attached["sessionId"]
        ready = False
        for _ in range(100):
            evaluated = _cdp(
                ws,
                "Runtime.evaluate",
                {
                    "expression": "document.documentElement.getAttribute('data-ready')",
                    "returnByValue": True,
                },
                session=session,
            )
            if evaluated.get("result", {}).get("value") == "1":
                ready = True
                break
            time.sleep(0.1)
        if not ready:
            raise RuntimeError("MathJax did not finish typesetting.")
        payload = _cdp(
            ws,
            "Runtime.evaluate",
            {
                "expression": """JSON.stringify([...document.querySelectorAll('.formula')].map(node => ({
                    id: node.id,
                    svg: (node.querySelector('svg') || {}).outerHTML || ''
                })))""",
                "returnByValue": True,
            },
            session=session,
        )
        ws.close()
        rows = json.loads(payload["result"]["value"])
    finally:
        try:
            os.killpg(proc.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        proc.wait(timeout=5)
        shutil.rmtree(work, ignore_errors=True)
    rendered = {}
    for row in rows:
        index = int(row["id"][1:])
        svg = row.get("svg") or ""
        if "<svg" not in svg:
            raise RuntimeError(f"MathJax produced no SVG for: {unique[index]}")
        rendered[unique[index]] = svg
    return rendered
