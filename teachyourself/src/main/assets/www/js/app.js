(function () {
  const stage = document.getElementById("stage");
  const titleEl = document.getElementById("title");
  const backBtn = document.getElementById("nav-back");
  const player = document.getElementById("player");
  const playBtn = document.getElementById("play");
  const stopBtn = document.getElementById("stop");
  const rateInput = document.getElementById("rate");
  const statusEl = document.getElementById("player-status");
  const voiceBadge = document.getElementById("voice-badge");

  const course = window.COURSE;
  const DONE_KEY = "csxi-ty-done";
  let activeBlocks = [];
  let speakingIndex = -1;
  let ttsReady = false;

  function doneSet() {
    try {
      return new Set(JSON.parse(localStorage.getItem(DONE_KEY) || "[]"));
    } catch (err) {
      return new Set();
    }
  }

  function saveDone(set) {
    localStorage.setItem(DONE_KEY, JSON.stringify(Array.from(set)));
  }

  function chapterById(id) {
    return course.chapters.find((chapter) => chapter.id === id);
  }

  function findLecture(id) {
    for (const chapter of course.chapters) {
      const lecture = chapter.lectures.find((item) => item.id === id);
      if (lecture) return { chapter, lecture };
    }
    return null;
  }

  function parseRoute() {
    const hash = location.hash.replace(/^#/, "") || "/";
    const parts = hash.split("/").filter(Boolean);
    if (parts[0] === "c" && parts[1]) return { name: "chapter", id: parts[1] };
    if (parts[0] === "l" && parts[1]) return { name: "lecture", id: parts[1] };
    if (parts[0] === "quiz" && parts[1]) return { name: "quiz", id: parts[1] };
    return { name: "home" };
  }

  function esc(text) {
    return String(text)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function allLectures() {
    return course.chapters.flatMap((chapter) => chapter.lectures);
  }

  window.tyBack = function () {
    const route = parseRoute();
    if (route.name === "lecture") {
      const found = findLecture(route.id);
      location.hash = found ? "#/c/" + found.chapter.id : "#/";
      return true;
    }
    if (route.name === "chapter" || route.name === "quiz") {
      location.hash = "#/";
      return true;
    }
    return false;
  };

  window.onTtsReady = function (ok) {
    ttsReady = !!ok;
    voiceBadge.textContent = ok ? "TTS ready" : "TTS off";
    voiceBadge.classList.toggle("warn", !ok);
  };

  window.onTtsMissing = function () {
    ttsReady = false;
    voiceBadge.textContent = "TTS missing";
    voiceBadge.classList.add("warn");
    statusEl.textContent = "Is device pe Urdish voice engine nahi mili. Lecture phir bhi parh sakte hain.";
    speakingIndex = -1;
    paintSpeaking();
  };

  window.onBlockStart = function (index) {
    speakingIndex = index;
    paintSpeaking();
    const node = stage.querySelector('[data-block="' + index + '"]');
    if (node) node.scrollIntoView({ block: "center", behavior: "smooth" });
    statusEl.textContent = "Sun rahe hain, block " + (index + 1);
  };

  window.onBlockDone = function (index) {
    if (speakingIndex === index) {
      const pending = activeBlocks.find((block) => block.i > index);
      if (!pending) {
        speakingIndex = -1;
        statusEl.textContent = "Lecture khatam.";
        paintSpeaking();
      }
    }
  };

  window.onSpeakIdle = function () {
    speakingIndex = -1;
    paintSpeaking();
  };

  function paintSpeaking() {
    stage.querySelectorAll("[data-block]").forEach((node) => {
      node.classList.toggle("is-speaking", Number(node.dataset.block) === speakingIndex);
    });
    playBtn.textContent = speakingIndex >= 0 ? "Chal rahi hai" : "Sunain";
  }

  function stopSpeech() {
    speakingIndex = -1;
    if (window.UrdishTts) window.UrdishTts.stop();
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    paintSpeaking();
  }

  function speakQueue(blocks) {
    stopSpeech();
    const queue = blocks.filter((block) => block.text && block.text.trim());
    if (!queue.length) return;
    if (window.UrdishTts && ttsReady) {
      window.UrdishTts.speakBlocks(JSON.stringify(queue));
      return;
    }
    if (window.speechSynthesis) {
      queue.forEach((block, offset) => {
        const utter = new SpeechSynthesisUtterance(block.text);
        utter.lang = "en-IN";
        utter.rate = Number(rateInput.value) || 0.92;
        utter.onstart = () => window.onBlockStart(block.i);
        utter.onend = () => window.onBlockDone(block.i);
        window.speechSynthesis.speak(utter);
        if (offset === 0) statusEl.textContent = "Browser voice se Urdish sunai de rahi hai.";
      });
      return;
    }
    window.onTtsMissing();
  }

  function blockHtml(block, index) {
    const open = `<article class="block" data-block="${index}">`;
    const close = "</article>";
    if (block.type === "p") {
      return `${open}<p>${block.html || esc(block.say)}</p>${close}`;
    }
    if (block.type === "math") {
      const tex = block.display === false ? `\\(${block.tex}\\)` : `\\[${block.tex}\\]`;
      return `${open}<div class="math-block"><div class="formula">${tex}</div><p class="say-note">${esc(block.say)}</p></div>${close}`;
    }
    if (block.type === "svg") {
      const picture = window.TYDiagrams.draw(block);
      return `${open}<div class="diagram">${picture}<p class="caption">${esc(block.caption || "")}</p></div><p>${esc(block.say)}</p>${close}`;
    }
    if (block.type === "table") {
      const head = block.headers.map((cell) => `<th>${cell}</th>`).join("");
      const rows = block.rows.map((row) => `<tr>${row.map((cell) => `<td>${cell}</td>`).join("")}</tr>`).join("");
      return `${open}<div class="table-wrap"><table><thead><tr>${head}</tr></thead><tbody>${rows}</tbody></table></div>${close}`;
    }
    if (block.type === "steps") {
      const items = block.items.map((item, i) => `<li><b>${i + 1}</b><span>${esc(item)}</span></li>`).join("");
      return `${open}<h3>${esc(block.title || "Steps")}</h3><ol class="steps">${items}</ol>${close}`;
    }
    if (block.type === "code") {
      return `${open}<pre><code>${esc(block.text)}</code></pre>${close}`;
    }
    if (block.type === "tip") {
      return `${open.replace("block", "block tip")}<strong>Yaad rakhein</strong><p>${esc(block.say)}</p>${close}`;
    }
    if (block.type === "check") {
      return `${open}<details class="check"><summary>${esc(block.q)}</summary><p>${esc(block.a)}</p></details>${close}`;
    }
    return "";
  }

  async function typeset() {
    if (window.MathJax && MathJax.typesetPromise) {
      try {
        MathJax.typesetClear([stage]);
      } catch (err) {
        /* first paint */
      }
      await MathJax.typesetPromise([stage]);
    }
  }

  function renderHome() {
    titleEl.textContent = "Teach Yourself Edition";
    backBtn.hidden = true;
    player.hidden = true;
    stopSpeech();
    const done = doneSet();
    const total = allLectures().length;
    const finished = allLectures().filter((lecture) => done.has(lecture.id)).length;
    const pct = total ? Math.round((finished / total) * 100) : 0;
    stage.innerHTML = `
      <section class="hero">
        <div class="hero-copy">
          <p class="chip">Urdish lectures only</p>
          <h2>Sindh Curriculum 2026, Computer Science XI</h2>
          <p class="lede">Teacher ke notes ko khud parhne layak lectures bana diya gaya hai. Har lecture Roman Urdish mein hai, formulas MathJax SVG se render hoti hain, diagrams flexbox layout mein baithe hain, aur Sunain button poori lecture bol kar sunata hai.</p>
          <div class="progress-track" aria-label="Progress"><span style="width:${pct}%"></span></div>
          <p class="meta">${finished} of ${total} lectures mukammal · ${pct}%</p>
        </div>
        <div class="diagram">${window.TYDiagrams.draw({ name: "waves" })}</div>
      </section>
      <section class="chapter-list">
        ${course.chapters.map((chapter) => {
          const count = chapter.lectures.length;
          const got = chapter.lectures.filter((lecture) => done.has(lecture.id)).length;
          return `<button class="chapter" type="button" data-go="#/c/${chapter.id}">
            <span class="chapter-num">${chapter.num}</span>
            <span class="chapter-body">
              <strong>${esc(chapter.title)}</strong>
              <p>${esc(chapter.blurb)}</p>
              <p class="meta">${got}/${count} lectures</p>
            </span>
          </button>`;
        }).join("")}
      </section>`;
  }

  function renderChapter(id) {
    const chapter = chapterById(id);
    if (!chapter) return renderHome();
    titleEl.textContent = chapter.title;
    backBtn.hidden = false;
    player.hidden = true;
    stopSpeech();
    const done = doneSet();
    stage.innerHTML = `
      <div class="head-row">
        <p class="lede">${esc(chapter.blurb)}</p>
        <a class="text-btn alt" href="#/quiz/${chapter.id}">Chapter check</a>
      </div>
      <section class="lecture-list">
        ${chapter.lectures.map((lecture) => `<button class="lecture-row" type="button" data-go="#/l/${lecture.id}">
          <span class="done-dot ${done.has(lecture.id) ? "on" : ""}"></span>
          <span>
            <strong>${esc(lecture.title)}</strong>
            <span class="meta">${esc(lecture.code)} · ${lecture.minutes} min${lecture.golden ? " · golden" : ""}</span>
          </span>
          ${lecture.golden ? '<span class="golden">Exam</span>' : ""}
        </button>`).join("")}
      </section>`;
  }

  function renderLecture(id) {
    const found = findLecture(id);
    if (!found) return renderHome();
    const { chapter, lecture } = found;
    titleEl.textContent = lecture.title;
    backBtn.hidden = false;
    player.hidden = false;
    statusEl.textContent = lecture.golden ? "Golden topic. Exam mein yeh zyada aata hai." : "Urdish lecture taiyar hai.";
    activeBlocks = lecture.blocks.map((block, index) => ({ i: index, text: block.say || "" }));
    const done = doneSet();
    stage.innerHTML = `
      <div class="mini-meta">
        <span class="chip">${esc(lecture.code)}</span>
        ${lecture.golden ? '<span class="golden">Golden topic</span>' : ""}
        <span class="chip">${lecture.minutes} min</span>
        <span class="chip">${esc(chapter.title)}</span>
      </div>
      <section class="stack">
        ${lecture.blocks.map((block, index) => blockHtml(block, index)).join("")}
      </section>
      <div class="choice-row">
        <button class="text-btn" type="button" id="mark-done">${done.has(lecture.id) ? "Done mark hai" : "Lecture done mark karein"}</button>
        <a class="text-btn alt" href="#/quiz/${chapter.id}">Checks kholen</a>
      </div>`;
    document.getElementById("mark-done").addEventListener("click", () => {
      const set = doneSet();
      set.add(lecture.id);
      saveDone(set);
      document.getElementById("mark-done").textContent = "Done mark hai";
    });
  }

  function renderQuiz(id) {
    const chapter = chapterById(id);
    if (!chapter) return renderHome();
    titleEl.textContent = chapter.title + " checks";
    backBtn.hidden = false;
    player.hidden = false;
    const checks = [];
    chapter.lectures.forEach((lecture) => {
      lecture.blocks.forEach((block) => {
        if (block.type === "check") checks.push({ lecture, block });
      });
    });
    activeBlocks = checks.map((item, index) => ({ i: index, text: item.block.say }));
    statusEl.textContent = "Pehle khud sochen, phir Sunain se jawab sunain.";
    stage.innerHTML = `
      <p class="lede">${checks.length} self-checks. Jawab tab kholen jab aap khud try kar chuke hon.</p>
      <section class="stack">
        ${checks.map((item, index) => `<article class="block" data-block="${index}">
          <p class="meta">${esc(item.lecture.code)}</p>
          <details class="check"><summary>${esc(item.block.q)}</summary><p>${esc(item.block.a)}</p></details>
        </article>`).join("")}
      </section>`;
  }

  async function render() {
    stopSpeech();
    const route = parseRoute();
    if (route.name === "chapter") renderChapter(route.id);
    else if (route.name === "lecture") renderLecture(route.id);
    else if (route.name === "quiz") renderQuiz(route.id);
    else renderHome();
    stage.querySelectorAll("[data-go]").forEach((node) => {
      node.addEventListener("click", () => {
        location.hash = node.getAttribute("data-go");
      });
    });
    await typeset();
  }

  backBtn.addEventListener("click", () => window.tyBack());
  playBtn.addEventListener("click", () => speakQueue(activeBlocks));
  stopBtn.addEventListener("click", stopSpeech);
  rateInput.addEventListener("input", () => {
    const rate = Number(rateInput.value);
    if (window.UrdishTts) window.UrdishTts.setRate(rate);
    statusEl.textContent = "Speed " + rate.toFixed(2);
  });

  window.addEventListener("hashchange", render);
  if (!window.UrdishTts) {
    voiceBadge.textContent = "Browser voice";
  }
  render();
})();
