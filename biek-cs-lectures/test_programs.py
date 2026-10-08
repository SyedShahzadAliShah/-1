"""Compile and run every lecture program."""

import subprocess
import tempfile
from pathlib import Path

from programs import PROGRAMS


def cases_for(source):
    cases = []
    stdin_lines = []
    expects = []
    seen = False

    def flush():
        nonlocal stdin_lines, expects, seen
        if seen:
            cases.append(("\n".join(stdin_lines) + ("\n" if stdin_lines else ""), expects[:]))
        stdin_lines = []
        expects = []

    for line in source.splitlines():
        if line.strip() == "":
            continue
        if not line.startswith("//"):
            break
        if line.startswith("// CASE:"):
            flush()
            seen = True
            text = line.split(":", 1)[1].strip()
            stdin_lines = [text] if text else []
        elif line.startswith("// STDIN:"):
            seen = True
            stdin_lines.append(line.split(":", 1)[1].strip())
        elif line.startswith("// EXPECT:"):
            seen = True
            expects.append(line.split(":", 1)[1].strip())
    flush()
    if not cases:
        cases.append(("", []))
    return cases


def main():
    failures = 0
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        for name, source in PROGRAMS.items():
            src = tmp / f"{name}.cpp"
            exe = tmp / name
            src.write_text(source)
            compile_run = subprocess.run(
                ["g++", "-std=c++17", "-Wall", "-Wextra", "-o", str(exe), str(src)],
                capture_output=True,
                text=True,
            )
            if compile_run.returncode != 0:
                print(f"COMPILE FAIL {name}\n{compile_run.stderr}")
                failures += 1
                continue
            for index, (stdin, expects) in enumerate(cases_for(source), start=1):
                run = subprocess.run(
                    [str(exe)],
                    input=stdin,
                    capture_output=True,
                    text=True,
                    timeout=5,
                    cwd=tmp,
                )
                if run.returncode != 0:
                    print(f"RUN FAIL {name} case {index}\n{run.stderr}\n{run.stdout}")
                    failures += 1
                    continue
                missing = [item for item in expects if item not in run.stdout]
                if missing:
                    print(f"EXPECT FAIL {name} case {index}: missing {missing}")
                    print(run.stdout)
                    failures += 1
                    continue
                print(f"ok {name} case {index}")
    if failures:
        raise SystemExit(f"{failures} failure(s)")
    print(f"All {len(PROGRAMS)} programs passed.")


if __name__ == "__main__":
    main()
