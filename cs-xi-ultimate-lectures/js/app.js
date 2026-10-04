import { CURRICULUM, COACH_MESSAGES, allModules } from "./curriculum.js";
import { renderDiagram } from "./diagrams.js";
import { LectureTTS } from "./tts.js";

const state = {
  displayLang: "both",
  ttsLang: "en",
  flatIndex: 0,
  slideIndex: 0,
  completedSlides: new Set(),
  microWin: true
};

const flat = allModules();

const $ = (id) => document.getElementById(id);

const els = {
  chapterNav: $("chapterNav"),
  moduleId: $("moduleId"),
  moduleTitle: $("moduleTitle"),
  goldenBadge: $("goldenBadge"),
  slideIndex: $("slideIndex"),
  slideContent: $("slideContent"),
  diagramFrame: $("diagramFrame"),
  diagramHost: $("diagramHost"),
  diagramCaption: $("diagramCaption"),
  karaokeLine: $("karaokeLine"),
  coachMessage: $("coachMessage"),
  progressArc: $("progressArc"),
  progressPct: $("progressPct"),
  btnPlayPause: $("btnPlayPause"),
  slideCard: $("slideCard")
};

const tts = new LectureTTS({
  onStart: () => setPlayState(true),
  onEnd: () => setPlayState(false),
  onBoundary: (idx, full) => {
    const snippet = full.slice(Math.max(0, idx - 20), idx + 60);
    els.karaokeLine.textContent = snippet + "…";
  }
});

function setPlayState(playing) {
  els.btnPlayPause.setAttribute("aria-pressed", String(playing));
  els.btnPlayPause.querySelector(".play-label").textContent = playing ? "⏸ Pause" : "▶ Narrate";
}

function currentEntry() {
  return flat[state.flatIndex] || flat[0];
}

function flatIndexFor(chapterId, moduleId) {
  return flat.findIndex((e) => e.chapter.id === chapterId && e.module.id === moduleId);
}

function currentModule() {
  return currentEntry()?.module;
}

function currentSlides() {
  const slides = currentModule()?.slides || [];
  if (state.microWin && slides.length > 2) {
    return slides.slice(0, 2);
  }
  return slides;
}

function slideKey() {
  const e = currentEntry();
  return `${e.chapter.id}:${e.module.id}:${state.slideIndex}`;
}

function updateProgress() {
  let total = 0;
  let done = 0;
  for (const entry of flat) {
    const count = entry.module.slides.length;
    total += count;
    for (let i = 0; i < count; i++) {
      const key = `${entry.chapter.id}:${entry.module.id}:${i}`;
      if (state.completedSlides.has(key)) done++;
    }
  }
  const pct = total ? Math.round((done / total) * 100) : 0;
  els.progressPct.textContent = `${pct}%`;
  els.progressArc.setAttribute("stroke-dasharray", `${pct}, 100`);
}

function randomCoach() {
  const lang = state.ttsLang === "ur" ? "ur" : "en";
  const list = COACH_MESSAGES[lang];
  const slide = currentSlides()[state.slideIndex];
  const custom = lang === "ur" ? slide?.coachUr : slide?.coachEn;
  els.coachMessage.textContent = custom || list[Math.floor(Math.random() * list.length)];
}

function applyDisplayLangClass() {
  document.body.classList.remove("lang-en-only", "lang-ur-only");
  if (state.displayLang === "en") document.body.classList.add("lang-en-only");
  if (state.displayLang === "ur") document.body.classList.add("lang-ur-only");
}

function buildNav() {
  els.chapterNav.innerHTML = "";
  const active = currentEntry();
  CURRICULUM.chapters.forEach((ch) => {
    const details = document.createElement("details");
    if (ch.id === active.chapter.id) details.open = true;
    const summary = document.createElement("summary");
    summary.textContent = `Ch ${ch.number}: ${ch.titleEn}`;
    details.appendChild(summary);
    ch.modules.forEach((m) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "module-link";
      btn.innerHTML = `${m.golden ? '<span class="star">★</span> ' : ""}${m.titleEn}`;
      btn.addEventListener("click", () => {
        const idx = flatIndexFor(ch.id, m.id);
        if (idx >= 0) state.flatIndex = idx;
        state.slideIndex = 0;
        renderSlide();
      });
      if (ch.id === active.chapter.id && m.id === active.module.id) {
        btn.classList.add("active");
      }
      details.appendChild(btn);
    });
    els.chapterNav.appendChild(details);
  });
}

function renderSlide() {
  tts.stop();
  const entry = currentEntry();
  const mod = entry.module;
  const slides = currentSlides();
  const slide = slides[state.slideIndex] || slides[0];
  if (!slide) return;

  els.moduleId.textContent = mod.id;
  els.moduleTitle.textContent =
    state.displayLang === "ur" ? mod.titleUr : state.displayLang === "en" ? mod.titleEn : `${mod.titleEn} / ${mod.titleUr}`;
  els.goldenBadge.hidden = !mod.golden;
  els.slideIndex.textContent = `Slide ${state.slideIndex + 1} of ${slides.length}${state.microWin && mod.slides.length > 2 ? " (2-min mode)" : ""}`;

  const parts = [];
  if (slide.headlineEn) parts.push(`<div class="en-block"><h3>${slide.headlineEn}</h3></div>`);
  if (slide.headlineUr) parts.push(`<div class="urdu-block"><h3>${slide.headlineUr}</h3></div>`);
  if (slide.bodyEn) parts.push(`<div class="en-block">${slide.bodyEn}</div>`);
  if (slide.bodyUr) parts.push(slide.bodyUr.includes("urdu-block") ? slide.bodyUr : `<div class="urdu-block">${slide.bodyUr}</div>`);
  els.slideContent.innerHTML = parts.join("");

  if (slide.diagram) {
    const d = renderDiagram(slide.diagram);
    if (d) {
      els.diagramFrame.hidden = false;
      els.diagramHost.innerHTML = d.html;
      const cap = state.displayLang === "ur" ? d.captionUr : state.displayLang === "en" ? d.captionEn : `${d.captionEn} · ${d.captionUr}`;
      els.diagramCaption.textContent = cap;
    } else {
      els.diagramFrame.hidden = true;
    }
  } else {
    els.diagramFrame.hidden = true;
    els.diagramHost.innerHTML = "";
  }

  els.karaokeLine.textContent = "";
  randomCoach();
  state.completedSlides.add(slideKey());
  updateProgress();

  els.slideCard.classList.remove("cinematic-reveal");
  void els.slideCard.offsetWidth;
  els.slideCard.classList.add("cinematic-reveal");

  if (window.MathJax?.typesetPromise) {
    window.MathJax.typesetPromise([els.slideContent]).catch(() => {});
  }

  buildNav();
}

function narrateCurrent() {
  const slide = currentSlides()[state.slideIndex];
  if (!slide) return;
  const text = state.ttsLang === "ur" ? slide.narratorUr : slide.narratorEn;
  if (!tts.speak(text, state.ttsLang)) {
    els.karaokeLine.textContent = state.ttsLang === "ur"
      ? "اردو آواز دستیاب نہیں — Chrome میں Urdu TTS انسٹال کریں۔"
      : "Speech not available in this browser.";
  }
}

function goSlide(delta) {
  const slides = currentSlides();
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
  document.querySelectorAll(".lang-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".lang-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      state.displayLang = btn.dataset.lang;
      applyDisplayLangClass();
      renderSlide();
    });
  });

  document.querySelectorAll(".tts-btn").forEach((btn) => {
    btn.addEventListener("click", () => {
      document.querySelectorAll(".tts-btn").forEach((b) => b.classList.remove("active"));
      btn.classList.add("active");
      state.ttsLang = btn.dataset.tts;
      randomCoach();
    });
  });

  $("microWinMode").addEventListener("change", (e) => {
    state.microWin = e.target.checked;
    state.slideIndex = 0;
    renderSlide();
  });

  $("btnPrevSlide").addEventListener("click", () => goSlide(-1));
  $("btnNextSlide").addEventListener("click", () => goSlide(1));
  $("btnPrevModule").addEventListener("click", () => goModule(-1));
  $("btnNextModule").addEventListener("click", () => goModule(1));

  els.btnPlayPause.addEventListener("click", () => {
    if (tts.speaking) tts.stop();
    else narrateCurrent();
  });

  document.addEventListener("keydown", (e) => {
    if (e.key === "ArrowRight") goSlide(1);
    if (e.key === "ArrowLeft") goSlide(-1);
    if (e.key === " ") {
      e.preventDefault();
      if (tts.speaking) tts.stop();
      else narrateCurrent();
    }
  });
}

function init() {
  applyDisplayLangClass();
  bindUI();
  buildNav();
  renderSlide();
  if (!tts.isSupported) {
    els.karaokeLine.textContent = "Web Speech API unavailable — use Chrome/Edge for narration.";
  }
}

init();
