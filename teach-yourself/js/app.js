const CURRICULUM = window.CURRICULUM;
const COACH_LINES = window.COACH_LINES;
const allModules = window.allModules;
const renderDiagram = window.renderDiagram;
const LectureTTS = window.LectureTTS;

const STORAGE_KEY = "csxi-tye-progress-v1";

const state = {
  flatIndex: 0,
  slideIndex: 0,
  completed: new Set(JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]"))
};

const flat = allModules();
const $ = (id) => document.getElementById(id);

const els = {
  sidebar: $("sidebar"),
  chapterNav: $("chapterNav"),
  moduleId: $("moduleId"),
  moduleTitle: $("moduleTitle"),
  goldenBadge: $("goldenBadge"),
  slideIndex: $("slideIndex"),
  slideContent: $("slideContent"),
  diagramFrame: $("diagramFrame"),
  diagramHost: $("diagramHost"),
  diagramCaption: $("diagramCaption"),
  quizBox: $("quizBox"),
  karaokeLine: $("karaokeLine"),
  coachMessage: $("coachMessage"),
  progressArc: $("progressArc"),
  progressPct: $("progressPct"),
  btnPlayPause: $("btnPlayPause"),
  slideCard: $("slideCard"),
  btnMenu: $("btnMenu")
};

const tts = new LectureTTS({
  onStart: () => setPlayState(true),
  onEnd: () => setPlayState(false),
  onBoundary: (idx, full) => {
    const snippet = full.slice(Math.max(0, idx - 12), idx + 48);
    els.karaokeLine.textContent = snippet ? `… ${snippet}` : "";
  }
});

function setPlayState(playing) {
  els.btnPlayPause.setAttribute("aria-pressed", String(playing));
  els.btnPlayPause.querySelector(".play-label").textContent = playing ? "⏸ روکیں" : "▶ سبق سنیں";
}

function currentEntry() {
  return flat[state.flatIndex] || flat[0];
}

function slideKey() {
  const e = currentEntry();
  return `${e.chapter.id}:${e.module.id}:${state.slideIndex}`;
}

function saveProgress() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify([...state.completed]));
}

function updateProgress() {
  let total = 0;
  for (const entry of flat) total += entry.module.slides.length;
  const pct = total ? Math.round((state.completed.size / total) * 100) : 0;
  els.progressPct.textContent = `${Math.min(pct, 100)}%`;
  els.progressArc.setAttribute("stroke-dasharray", `${Math.min(pct, 100)}, 100`);
}

function coachFor(slide) {
  els.coachMessage.textContent =
    slide.coach || COACH_LINES[Math.floor(Math.random() * COACH_LINES.length)];
}

function buildNav() {
  const active = currentEntry();
  els.chapterNav.innerHTML = "";
  CURRICULUM.chapters.forEach((ch) => {
    const details = document.createElement("details");
    if (ch.id === active.chapter.id) details.open = true;
    const summary = document.createElement("summary");
    summary.textContent = `باب ${ch.number}: ${ch.title}`;
    details.appendChild(summary);
    ch.modules.forEach((m) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "module-link";
      btn.innerHTML = `${m.golden ? "★ " : ""}${m.title}`;
      btn.addEventListener("click", () => {
        const idx = flat.findIndex((e) => e.chapter.id === ch.id && e.module.id === m.id);
        if (idx >= 0) state.flatIndex = idx;
        state.slideIndex = 0;
        renderSlide();
      });
      if (ch.id === active.chapter.id && m.id === active.module.id) btn.classList.add("active");
      details.appendChild(btn);
    });
    els.chapterNav.appendChild(details);
  });
}

function renderQuiz(quiz) {
  if (!quiz) {
    els.quizBox.hidden = true;
    els.quizBox.innerHTML = "";
    return;
  }
  els.quizBox.hidden = false;
  els.quizBox.innerHTML = `
    <strong>خود آزمائی</strong>
    <p>${quiz.q}</p>
    <div class="quiz-options"></div>
    <p class="quiz-explain" hidden></p>
  `;
  const box = els.quizBox.querySelector(".quiz-options");
  const explain = els.quizBox.querySelector(".quiz-explain");
  quiz.options.forEach((opt, i) => {
    const b = document.createElement("button");
    b.type = "button";
    b.textContent = opt;
    b.addEventListener("click", () => {
      [...box.children].forEach((el) => el.classList.remove("correct", "wrong"));
      if (i === quiz.answer) {
        b.classList.add("correct");
        explain.hidden = false;
        explain.textContent = "درست! " + (quiz.explain || "");
      } else {
        b.classList.add("wrong");
        explain.hidden = false;
        explain.textContent = "دوبارہ سوچیں۔ " + (quiz.explain || "");
      }
    });
    box.appendChild(b);
  });
}

function typesetMath(root) {
  if (window.MathJax?.typesetPromise) {
    window.MathJax.typesetClear?.([root]);
    window.MathJax.typesetPromise([root]).catch(() => {});
  }
}

function renderSlide() {
  tts.stop();
  const entry = currentEntry();
  const mod = entry.module;
  const slides = mod.slides;
  const slide = slides[state.slideIndex] || slides[0];
  if (!slide) return;

  els.moduleId.textContent = mod.id;
  els.moduleTitle.textContent = mod.title;
  els.goldenBadge.hidden = !mod.golden;
  els.slideIndex.textContent = `سلائیڈ ${state.slideIndex + 1} از ${slides.length} · باب ${entry.chapter.number}`;

  els.slideContent.innerHTML = `
    <h3>${slide.headline}</h3>
    ${slide.body}
    ${slide.tip ? `<p class="tip">★ سنہری نکتہ: ${slide.tip}</p>` : ""}
  `;

  if (slide.diagram) {
    const d = renderDiagram(slide.diagram);
    if (d) {
      els.diagramFrame.hidden = false;
      els.diagramHost.innerHTML = d.html;
      els.diagramCaption.textContent = d.caption;
    } else {
      els.diagramFrame.hidden = true;
    }
  } else {
    els.diagramFrame.hidden = true;
    els.diagramHost.innerHTML = "";
  }

  renderQuiz(slide.quiz);
  els.karaokeLine.textContent = "";
  coachFor(slide);
  state.completed.add(slideKey());
  saveProgress();
  updateProgress();
  buildNav();
  typesetMath(els.slideContent);
}

function narrateCurrent() {
  const slide = currentEntry().module.slides[state.slideIndex];
  if (!slide) return;
  const text = slide.narrator || `${slide.headline}۔ ${slide.body}`;
  const ok = tts.speak(text);
  if (!ok) {
    els.karaokeLine.textContent = "اردو TTS دستیاب نہیں۔ فون کی Text-to-speech سیٹنگز میں Urdu آواز انسٹال کریں۔";
  }
}

function goSlide(delta) {
  const slides = currentEntry().module.slides;
  const next = state.slideIndex + delta;
  if (next < 0 || next >= slides.length) return false;
  state.slideIndex = next;
  renderSlide();
  return true;
}

function goModule(delta) {
  const idx = state.flatIndex + delta;
  if (idx < 0 || idx >= flat.length) return false;
  state.flatIndex = idx;
  state.slideIndex = 0;
  renderSlide();
  return true;
}

function bindUI() {
  $("btnPrevSlide").addEventListener("click", () => goSlide(-1));
  $("btnNextSlide").addEventListener("click", () => goSlide(1));
  $("btnPrevModule").addEventListener("click", () => goModule(-1));
  $("btnNextModule").addEventListener("click", () => goModule(1));
  els.btnPlayPause.addEventListener("click", () => {
    if (tts.speaking) tts.stop();
    else narrateCurrent();
  });
  els.btnMenu.addEventListener("click", () => {
    els.sidebar.classList.toggle("collapsed");
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowLeft") goSlide(1);
    if (e.key === "ArrowRight") goSlide(-1);
    if (e.key === " ") {
      e.preventDefault();
      if (tts.speaking) tts.stop();
      else narrateCurrent();
    }
  });
}

function init() {
  bindUI();
  renderSlide();
}

init();
