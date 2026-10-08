(function () {
  const DONE_KEY = "csxii-ty-done-v1";
  const app = document.getElementById("app");
  const chapters = window.LECTURES.chapters;
  const lectures = window.LECTURES.lectures;
  let stack = [{ name: "home" }];
  let playing = false;
  let urduReady = null;
  let rate = 0.92;

  function doneSet() {
    try { return new Set(JSON.parse(localStorage.getItem(DONE_KEY) || "[]")); }
    catch (e) { return new Set(); }
  }
  function saveDone(set) {
    localStorage.setItem(DONE_KEY, JSON.stringify([...set]));
  }
  function lectureDoneCount(chapterId) {
    const done = doneSet();
    return lectures.filter((lec) => lec.chapter === chapterId && done.has(lec.id)).length;
  }
  function byId(id) { return lectures.find((lec) => lec.id === id); }
  function inChapter(id) { return lectures.filter((lec) => lec.chapter === id); }

  function esc(text) {
    return String(text).replace(/[&<>"]/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]));
  }

  function topbar(title, canBack) {
    return `<header class="topbar">
      ${canBack ? `<button class="icon-btn" id="back" type="button" aria-label="واپس">←</button>` : ""}
      <h1>${esc(title)}</h1>
    </header>`;
  }

  function engineRow() {
    const voice = urduReady === false
      ? `<span class="chip warn">Urdu voice غائب ہے</span>`
      : `<span class="chip">Urdish TTS</span>`;
    return `<div class="engine">
      <span class="chip">MathJax SVG</span>
      <span class="chip">Flexbox</span>
      <span class="chip">SVG</span>
      ${voice}
    </div>`;
  }

  function show(nodeHtml, after, reader) {
    app.className = reader ? "app reader" : "app";
    app.innerHTML = nodeHtml;
    if (after) after();
    const back = document.getElementById("back");
    if (back) back.addEventListener("click", () => goBack());
  }

  function renderHome(query) {
    const q = (query || "").trim();
    const matched = q
      ? lectures.filter((lec) => (lec.title + " " + lec.html.replace(/<[^>]+>/g, " ")).includes(q))
      : [];
    const cards = chapters.map((ch) => {
      const total = inChapter(ch.id).length;
      const have = lectureDoneCount(ch.id);
      const pct = total ? Math.round((have / total) * 100) : 0;
      return `<button class="card" data-ch="${ch.id}" type="button">
        <span class="chip">باب ${ch.id}</span>
        <h2>${esc(ch.title)}</h2>
        <p dir="ltr">${esc(ch.en)}</p>
        <p>${esc(ch.blurb)}</p>
        <div class="bar" aria-hidden="true"><span style="width:${pct}%"></span></div>
        <span class="muted">${have} / ${total} لیکچر</span>
      </button>`;
    }).join("");
    const hits = matched.map((lec) =>
      `<button class="row-link card" data-lec="${lec.id}" type="button"><strong>${esc(lec.title)}</strong><span class="muted">باب ${lec.chapter}</span></button>`
    ).join("");
    show(`${topbar("CS XII خود پڑھو", false)}
      <main class="screen">
        <p class="lede">Teach Yourself Edition۔ لیکچر صرف <b>اردش</b> میں ہیں: اردو جملے، اور امتحان والے English terms۔ فارمولا MathJax کے SVG میں، خاکہ SVG میں، صفحہ Flexbox میں۔</p>
        ${engineRow()}
        <label class="search"><input id="q" type="search" placeholder="عنوان یا لفظ ڈھونڈو" value="${esc(q)}" /></label>
        ${q ? `<div class="grid">${hits || `<p>کوئی لیکچر نہیں ملا۔</p>`}</div>` : `<div class="grid">${cards}</div>`}
      </main>`, () => {
      document.querySelectorAll("[data-ch]").forEach((btn) => {
        btn.addEventListener("click", () => openChapter(Number(btn.dataset.ch)));
      });
      document.querySelectorAll("[data-lec]").forEach((btn) => {
        btn.addEventListener("click", () => openLecture(btn.dataset.lec));
      });
      const input = document.getElementById("q");
      input.addEventListener("input", () => renderHome(input.value));
      input.focus();
      const pos = input.value.length;
      input.setSelectionRange(pos, pos);
    });
  }

  function openChapter(id) {
    stack.push({ name: "chapter", id });
    renderChapter(id);
  }

  function renderChapter(id) {
    const ch = chapters.find((item) => item.id === id);
    const done = doneSet();
    const rows = inChapter(id).map((lec, index) => `<button class="card" data-lec="${lec.id}" type="button">
      <div class="meta">${lec.golden ? `<span class="chip gold">سنہری</span>` : `<span class="chip">لیکچر ${index + 1}</span>`}
      ${done.has(lec.id) ? `<span class="chip">مکمل</span>` : ""}</div>
      <h3>${esc(lec.title)}</h3>
      <span class="muted">${lec.minutes} منٹ</span>
    </button>`).join("");
    show(`${topbar(ch.title, true)}
      <main class="screen">
        <p class="lede" dir="ltr">${esc(ch.en)}</p>
        <div class="meta">
          <button class="text-btn primary" id="review" type="button">باب کا خود امتحان</button>
        </div>
        <div class="grid">${rows}</div>
      </main>`, () => {
      document.getElementById("review").addEventListener("click", () => openReview(id));
      document.querySelectorAll("[data-lec]").forEach((btn) => {
        btn.addEventListener("click", () => openLecture(btn.dataset.lec));
      });
    });
  }

  function openLecture(id) {
    stack.push({ name: "lecture", id });
    renderLecture(id);
  }

  function renderLecture(id) {
    const lec = byId(id);
    const fig = window.DIAGRAMS[lec.diagram]
      ? `<figure class="figure">${window.DIAGRAMS[lec.diagram]()}<figcaption>${lec.caption}</figcaption></figure>`
      : "";
    const checks = lec.checks.map((item, index) => `<fieldset class="check" data-check="${index}">
      <legend>${esc(item.q)}</legend>
      <div class="choice-row" style="display:flex;flex-direction:column;gap:8px">
        ${item.options.map((opt, oi) => `<button type="button" class="choice" data-i="${oi}">${esc(opt)}</button>`).join("")}
      </div>
      <p class="why hidden"></p>
    </fieldset>`).join("");
    show(`${topbar(lec.title, true)}
      <article class="screen lecture" id="sheet">
        <div class="meta">
          <span class="chip">باب ${lec.chapter}</span>
          ${lec.golden ? `<span class="chip gold">Golden topic</span>` : ""}
          <span class="chip">${lec.minutes} منٹ</span>
        </div>
        ${fig}
        <div id="body">${lec.html}</div>
        <section class="checks" id="checks">
          <h2>خود جانچو</h2>
          ${checks}
          <button class="text-btn primary" id="grade" type="button">جواب دیکھو</button>
        </section>
      </article>
      <div class="ttsbar">
        <button class="primary" id="play" type="button">سنو</button>
        <button id="pause" type="button">روکو</button>
        <button id="stop" type="button">بند</button>
        <label>رفتار <input id="rate" type="range" min="0.7" max="1.2" step="0.05" value="${rate}" /></label>
        <button id="voice" type="button" class="${urduReady === false ? "" : "hidden"}">Urdu voice</button>
      </div>`, () => {
      tagBlocks(document.getElementById("sheet"));
      typeset(document.getElementById("body"));
      document.getElementById("play").addEventListener("click", () => speakLecture());
      document.getElementById("pause").addEventListener("click", () => pauseSpeech());
      document.getElementById("stop").addEventListener("click", () => stopSpeech());
      document.getElementById("rate").addEventListener("input", (event) => {
        rate = Number(event.target.value);
        if (window.AndroidTTS) AndroidTTS.setRate(rate);
      });
      const voice = document.getElementById("voice");
      if (voice) voice.addEventListener("click", () => {
        if (window.AndroidTTS) AndroidTTS.openTtsSettings();
      });
      document.getElementById("grade").addEventListener("click", () => grade(lec));
      document.getElementById("sheet").scrollTop = 0;
      document.querySelectorAll(".check").forEach((box) => {
        box.querySelectorAll(".choice").forEach((btn) => {
          btn.addEventListener("click", () => {
            box.querySelectorAll(".choice").forEach((peer) => peer.classList.remove("picked"));
            btn.classList.add("picked");
          });
        });
      });
    }, true);
  }

  function openReview(chapterId) {
    stack.push({ name: "review", id: chapterId });
    renderReview(chapterId);
  }

  function renderReview(chapterId) {
    const items = inChapter(chapterId).flatMap((lec) => lec.checks.map((item) => ({ ...item, from: lec.title })));
    const html = items.map((item, index) => `<fieldset class="check" data-check="${index}">
      <legend>${esc(item.q)}</legend>
      <p class="muted">${esc(item.from)}</p>
      <div style="display:flex;flex-direction:column;gap:8px">
        ${item.options.map((opt, oi) => `<button type="button" class="choice" data-i="${oi}">${esc(opt)}</button>`).join("")}
      </div>
      <p class="why hidden"></p>
    </fieldset>`).join("");
    const ch = chapters.find((item) => item.id === chapterId);
    show(`${topbar("خود امتحان · " + ch.title, true)}
      <main class="screen">
        <section class="checks" id="checks">${html}
          <button class="text-btn primary" id="grade" type="button">نتیجہ</button>
          <p id="score" class="lede"></p>
        </section>
      </main>`, () => {
      document.querySelectorAll(".check").forEach((box) => {
        box.querySelectorAll(".choice").forEach((btn) => {
          btn.addEventListener("click", () => {
            box.querySelectorAll(".choice").forEach((peer) => peer.classList.remove("picked"));
            btn.classList.add("picked");
          });
        });
      });
      document.getElementById("grade").addEventListener("click", () => {
        let correct = 0;
        items.forEach((item, index) => {
          if (markBox(document.querySelector(`[data-check="${index}"]`), item)) correct += 1;
        });
        document.getElementById("score").textContent = `${correct} / ${items.length} درست`;
      });
    });
  }

  function markBox(box, item) {
    const picked = box.querySelector(".choice.picked");
    const chosen = picked ? Number(picked.dataset.i) : -1;
    box.querySelectorAll(".choice").forEach((btn) => {
      const i = Number(btn.dataset.i);
      btn.disabled = true;
      if (i === item.answer) btn.classList.add("good");
      else if (i === chosen) btn.classList.add("bad");
    });
    const why = box.querySelector(".why");
    why.classList.remove("hidden");
    why.textContent = item.why;
    return chosen === item.answer;
  }

  function grade(lec) {
    const allRight = lec.checks.every((item, index) => markBox(document.querySelector(`[data-check="${index}"]`), item));
    if (allRight) {
      const done = doneSet();
      done.add(lec.id);
      saveDone(done);
    }
  }

  function tagBlocks(root) {
    let n = 0;
    root.querySelectorAll("p,li,h2,h3,figcaption,.callout,.col,.step").forEach((el) => {
      el.dataset.mark = "m" + (n++);
    });
  }

  function nearestMark(node) {
    const el = node.nodeType === 1 ? node : node.parentElement;
    const block = el && el.closest("[data-mark]");
    return block ? block.dataset.mark : "m0";
  }

  function speechSegments(root) {
    const segs = [];
    function push(lang, text, mark) {
      text = text.replace(/\s+/g, " ").trim();
      if (!text) return;
      const last = segs[segs.length - 1];
      if (last && last.lang === lang && last.mark === mark) last.text += " " + text;
      else segs.push({ lang, text, mark });
    }
    function walk(node, lang) {
      if (node.nodeType === 3) {
        push(lang, node.textContent, nearestMark(node));
        return;
      }
      if (node.nodeType !== 1) return;
      if (node.matches("script,style,svg,mjx-container,.no-speak")) return;
      if (node.classList.contains("math")) {
        push("ur", node.getAttribute("data-speak") || "فارمولا دیکھو", nearestMark(node));
        return;
      }
      if (node.matches("pre")) {
        push("ur", node.getAttribute("data-speak") || "کوڈ اسکرین پر دیکھو", nearestMark(node));
        return;
      }
      const next = node.classList.contains("en") || node.tagName === "CODE" ? "en" : lang;
      node.childNodes.forEach((child) => walk(child, next));
    }
    walk(root, "ur");
    return segs;
  }

  async function typeset(node) {
    for (let i = 0; !(window.MathJax && MathJax.startup) && i < 40; i++) {
      await new Promise((resolve) => setTimeout(resolve, 100));
    }
    if (!window.MathJax || !MathJax.startup) return;
    try {
      await MathJax.startup.promise;
      MathJax.typesetClear([node]);
      await MathJax.typesetPromise([node]);
      const svgs = node.querySelectorAll("mjx-container svg");
      if (svgs.length) {
        const badge = document.querySelector(".engine");
        if (badge && !badge.querySelector("[data-svgcount]")) {
          badge.insertAdjacentHTML("beforeend", `<span class="chip" data-svgcount="1">${svgs.length} فارمولا SVG</span>`);
        }
      }
    } catch (err) {
      console.error(err);
    }
  }

  function currentSheet() {
    return document.getElementById("sheet") || document.getElementById("body");
  }

  function speakLecture() {
    const sheet = currentSheet();
    if (!sheet) return;
    const title = document.querySelector(".topbar h1");
    const segs = [{ lang: "ur", text: title ? title.textContent : "", mark: "title" }].concat(speechSegments(sheet));
    playing = true;
    if (window.AndroidTTS && AndroidTTS.embedded()) {
      AndroidTTS.setRate(rate);
      AndroidTTS.speak(JSON.stringify(segs));
      return;
    }
    speakWithWeb(segs, 0);
  }

  function speakWithWeb(segs, index) {
    if (!playing || index >= segs.length) {
      playing = false;
      clearMark();
      return;
    }
    const seg = segs[index];
    window.__ttsMark(seg.mark);
    if (!window.speechSynthesis) return;
    const utter = new SpeechSynthesisUtterance(seg.text);
    utter.lang = seg.lang === "en" ? "en-US" : "ur-PK";
    utter.rate = rate;
    utter.onend = () => speakWithWeb(segs, index + 1);
    utter.onerror = () => speakWithWeb(segs, index + 1);
    speechSynthesis.speak(utter);
  }

  function pauseSpeech() {
    playing = false;
    if (window.AndroidTTS) AndroidTTS.pause();
    if (window.speechSynthesis) speechSynthesis.cancel();
  }
  function stopSpeech() {
    playing = false;
    clearMark();
    if (window.AndroidTTS) AndroidTTS.stop();
    if (window.speechSynthesis) speechSynthesis.cancel();
  }
  function clearMark() {
    document.querySelectorAll(".speaking").forEach((el) => el.classList.remove("speaking"));
  }
  window.__ttsMark = function (mark) {
    clearMark();
    if (!mark) return;
    document.querySelectorAll(`[data-mark="${mark}"]`).forEach((el) => el.classList.add("speaking"));
  };
  window.__ttsDone = function () {
    playing = false;
    clearMark();
  };
  window.__ttsReady = function () {
    urduReady = window.AndroidTTS ? AndroidTTS.urduAvailable() : null;
    const voice = document.getElementById("voice");
    if (voice) voice.classList.toggle("hidden", urduReady !== false);
  };

  function goBack() {
    if (stack.length <= 1) return false;
    stopSpeech();
    stack.pop();
    const top = stack[stack.length - 1];
    if (top.name === "home") renderHome("");
    else if (top.name === "chapter") renderChapter(top.id);
    else if (top.name === "lecture") renderLecture(top.id);
    else if (top.name === "review") renderReview(top.id);
    return true;
  }
  window.appBack = function () { return goBack(); };

  const params = new URLSearchParams(location.search);
  if (params.get("lec") && byId(params.get("lec"))) openLecture(params.get("lec"));
  else if (params.get("ch")) openChapter(Number(params.get("ch")));
  else renderHome("");
})();
