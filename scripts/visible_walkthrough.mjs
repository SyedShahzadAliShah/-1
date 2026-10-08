import { spawn } from "node:child_process";

const PORT = 9225;
function sleep(ms) { return new Promise((r) => setTimeout(r, ms)); }

const chrome = spawn("google-chrome", [
  "--new-window",
  "--no-first-run",
  "--no-default-browser-check",
  "--disable-gpu",
  "--disable-component-update",
  "--disable-background-networking",
  "--disable-sync",
  "--start-maximized",
  "--window-size=1400,1000",
  "--window-position=40,20",
  "--remote-debugging-port=" + PORT,
  "--user-data-dir=/tmp/chrome-teach-visible-2",
  "http://127.0.0.1:8765/index.html"
], { env: { ...process.env, DISPLAY: ":1" }, stdio: "ignore" });

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
    } catch { await sleep(250); }
  }
  throw new Error("no chrome");
}

const ws = await connect();
let seq = 0;
const pending = new Map();
ws.addEventListener("message", (event) => {
  const msg = JSON.parse(event.data);
  if (msg.id && pending.has(msg.id)) {
    const item = pending.get(msg.id);
    pending.delete(msg.id);
    if (msg.error) item.reject(new Error(JSON.stringify(msg.error)));
    else item.resolve(msg.result);
  }
});
function send(method, params = {}, sessionId) {
  const id = ++seq;
  const payload = { id, method, params };
  if (sessionId) payload.sessionId = sessionId;
  ws.send(JSON.stringify(payload));
  return new Promise((resolve, reject) => pending.set(id, { resolve, reject }));
}
const targets = await send("Target.getTargets");
const page = targets.targetInfos.find((t) => t.type === "page" && t.url.includes("8765")) || targets.targetInfos.find((t) => t.type === "page");
const { sessionId } = await send("Target.attachToTarget", { targetId: page.targetId, flatten: true });
await send("Runtime.enable", {}, sessionId);
await send("Page.enable", {}, sessionId);
async function js(expression) {
  const result = await send("Runtime.evaluate", { expression, awaitPromise: true, returnByValue: true }, sessionId);
  if (result.exceptionDetails) throw new Error(JSON.stringify(result.exceptionDetails));
  return result.result.value;
}

await sleep(1500);
await js(`document.querySelector('[data-ch="2"]').click()`);
await sleep(1200);
await js(`document.querySelector('[data-lec="c2-bigo"]').click()`);
await sleep(1800);
await js(`document.getElementById("sheet").scrollTo({ top: 520, behavior: "smooth" })`);
await sleep(1400);
await js(`document.getElementById("sheet").scrollTo({ top: document.getElementById("sheet").scrollHeight, behavior: "smooth" })`);
await sleep(1400);
const grade = await js(`(() => {
  document.querySelectorAll(".check").forEach((box) => box.querySelectorAll(".choice")[1].click());
  document.getElementById("grade").click();
  return document.querySelectorAll(".choice.good").length;
})()`);
await sleep(1600);
await js(`document.getElementById("play").click()`);
await sleep(900);
await js(`document.getElementById("stop").click()`);
await sleep(600);
await js(`document.getElementById("back").click()`);
await sleep(800);
await js(`document.getElementById("back").click()`);
await sleep(800);
await js(`(() => { const q = document.getElementById("q"); q.focus(); q.value = "Big"; q.dispatchEvent(new Event("input")); return document.querySelectorAll("[data-lec]").length; })()`);
await sleep(1500);
console.log(JSON.stringify({ grade }));
chrome.kill();
process.exit(0);
