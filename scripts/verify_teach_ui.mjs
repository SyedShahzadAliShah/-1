import { spawn } from "node:child_process";
import { writeFileSync } from "node:fs";

const PORT = 9223;
const OUT = "/opt/cursor/artifacts";

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

const chrome = spawn("google-chrome", [
  "--headless=new",
  "--disable-gpu",
  "--no-sandbox",
  "--remote-debugging-port=" + PORT,
  "--user-data-dir=/tmp/chrome-teach-ui",
  "about:blank"
], { stdio: "ignore" });

async function connect() {
  for (let i = 0; i < 40; i++) {
    try {
      const version = await fetch(`http://127.0.0.1:${PORT}/json/version`).then((r) => r.json());
      const ws = new WebSocket(version.webSocketDebuggerUrl);
      await new Promise((resolve, reject) => {
        ws.addEventListener("open", resolve);
        ws.addEventListener("error", reject);
      });
      return ws;
    } catch {
      await sleep(250);
    }
  }
  throw new Error("chrome debug port did not open");
}

const ws = await connect();
let seq = 0;
const pending = new Map();
ws.addEventListener("message", (event) => {
  const msg = JSON.parse(event.data);
  if (msg.id && pending.has(msg.id)) {
    const { resolve, reject } = pending.get(msg.id);
    pending.delete(msg.id);
    if (msg.error) reject(new Error(JSON.stringify(msg.error)));
    else resolve(msg.result);
  }
});

function send(method, params = {}, sessionId) {
  const id = ++seq;
  const payload = { id, method, params };
  if (sessionId) payload.sessionId = sessionId;
  ws.send(JSON.stringify(payload));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}

const { targetId } = await send("Target.createTarget", { url: "about:blank" });
const { sessionId } = await send("Target.attachToTarget", { targetId, flatten: true });
await send("Page.enable", {}, sessionId);
await send("Network.enable", {}, sessionId);
await send("Runtime.enable", {}, sessionId);

const requests = [];
ws.addEventListener("message", (event) => {
  const msg = JSON.parse(event.data);
  if (msg.method === "Network.requestWillBeSent" && msg.sessionId === sessionId) {
    requests.push(msg.params.request.url);
  }
});

async function go(url) {
  await send("Page.navigate", { url }, sessionId);
  await sleep(1200);
}

async function evalJs(expression) {
  const result = await send("Runtime.evaluate", {
    expression,
    awaitPromise: true,
    returnByValue: true
  }, sessionId);
  if (result.exceptionDetails) {
    throw new Error(JSON.stringify(result.exceptionDetails));
  }
  return result.result.value;
}

async function shot(name, width, height) {
  await send("Emulation.setDeviceMetricsOverride", {
    width, height, deviceScaleFactor: 1, mobile: width < 700
  }, sessionId);
  await sleep(300);
  const { data } = await send("Page.captureScreenshot", { format: "png" }, sessionId);
  writeFileSync(`${OUT}/${name}.png`, Buffer.from(data, "base64"));
}

await go("http://127.0.0.1:8765/index.html");
await shot("home-phone", 390, 844);
const home = await evalJs(`({
  cards: document.querySelectorAll("[data-ch]").length,
  flex: getComputedStyle(document.querySelector(".grid")).display,
  chips: [...document.querySelectorAll(".chip")].map(n => n.textContent)
})`);

await evalJs(`document.querySelector('[data-ch="2"]').click()`);
await sleep(400);
await shot("chapter-phone", 390, 844);
await evalJs(`document.querySelector('[data-lec="c2-bigo"]').click()`);
await sleep(1800);
const math = await evalJs(`({
  mjx: document.querySelectorAll("mjx-container").length,
  svg: document.querySelectorAll("mjx-container svg").length,
  figure: document.querySelectorAll("figure svg").length,
  dir: document.documentElement.dir,
  title: document.querySelector("h1").textContent
})`);
await shot("lecture-bigo-phone", 390, 844);
await send("Emulation.setDeviceMetricsOverride", {
  width: 1100, height: 900, deviceScaleFactor: 1, mobile: false
}, sessionId);
await sleep(300);
await shot("lecture-bigo-desktop", 1100, 900);

const grade = await evalJs(`(() => {
  const boxes = [...document.querySelectorAll(".check")];
  boxes.forEach((box) => {
    const buttons = [...box.querySelectorAll(".choice")];
    buttons[1].click();
  });
  document.getElementById("grade").click();
  return {
    good: document.querySelectorAll(".choice.good").length,
    done: JSON.parse(localStorage.getItem("csxii-ty-done-v1") || "[]")
  };
})()`);

const speech = await evalJs(`(() => {
  const sheet = document.getElementById("sheet");
  const segs = [];
  function push(lang, text) {
    text = text.replace(/\\s+/g, " ").trim();
    if (!text) return;
    const last = segs[segs.length - 1];
    if (last && last.lang === lang) last.text += " " + text;
    else segs.push({ lang, text: text.slice(0, 80) });
  }
  function walk(node, lang) {
    if (node.nodeType === 3) { push(lang, node.textContent); return; }
    if (node.nodeType !== 1) return;
    if (node.matches("script,style,svg,mjx-container")) return;
    if (node.classList.contains("math")) { push("ur", node.getAttribute("data-speak") || ""); return; }
    if (node.matches("pre")) { push("ur", node.getAttribute("data-speak") || ""); return; }
    const next = node.classList.contains("en") || node.tagName === "CODE" ? "en" : lang;
    node.childNodes.forEach((child) => walk(child, next));
  }
  walk(sheet, "ur");
  return { langs: [...new Set(segs.map(s => s.lang))], sample: segs.slice(0, 6) };
})()`);

await evalJs(`document.getElementById("back").click()`);
await sleep(300);
await evalJs(`document.getElementById("back").click()`);
await sleep(300);
await evalJs(`document.getElementById("q").value = "Big"; document.getElementById("q").dispatchEvent(new Event("input"));`);
await sleep(300);
const search = await evalJs(`document.querySelectorAll("[data-lec]").length`);
await shot("search-phone", 390, 844);

const remote = requests.filter((url) => !url.startsWith("http://127.0.0.1:8765/") && !url.startsWith("data:"));
const report = { home, math, grade, speech, search, remote };
writeFileSync(`${OUT}/ui-report.json`, JSON.stringify(report, null, 2));
console.log(JSON.stringify(report, null, 2));
chrome.kill();
process.exit(0);
