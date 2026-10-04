const { renderDiagram } = window.LectureDiagrams;
const LectureTTS = window.LectureTTS;

const STORAGE_KEY = "cs-xii-cinema-progress-v1";

const state = {
  chapters: [],
  chapterId: 1,
  goldenOnly: false,
  lang: "en",
  autoLecture: false,
  sceneIndex: 0,
};

const els = {
  chapterNav: document.getElementById("chapterNav"),
  sceneList: document.getElementById("sceneList"),
  progressBar: document.getElementById("progressBar"),
  progressLabel: document.getElementById("progressLabel"),
  ttsStatus: document.getElementById("ttsStatus"),
  filterGolden: document.getElementById("filterGolden"),
  btnAutoLecture: document.getElementById("btnAutoLecture"),
  btnStop: document.getElementById("btnStop"),
  langEn: document.getElementById("langEn"),
  langUr: document.getElementById("langUr"),
};

const tts = new LectureTTS({
  onStart: () => {},
  onEnd: () => {
    document.querySelectorAll(".scene.speaking").forEach((el) => el.classList.remove("speaking"));
    if (state.autoLecture) advanceAutoLecture();
  },
  onStatus: (msg) => {
    if (els.ttsStatus) els.ttsStatus.textContent = msg;
  },
});

function loadProgress() {
  try {
    return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
  } catch {
    return {};
  }
}

function saveProgress(progress) {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(progress));
}

function getVisibleScenes(chapter) {
  return chapter.scenes.filter((s) => !state.goldenOnly || s.golden);
}

function escapeHtml(str) {
  return str
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");
}

function formatEnglish(text) {
  return escapeHtml(text).replace(/\n/g, "<br>");
}

function renderScenes() {
  const chapter = state.chapters.find((c) => c.id === state.chapterId);
  if (!chapter) return;

  const scenes = getVisibleScenes(chapter);
  const progress = loadProgress();
  const seen = progress[chapter.id] || [];

  els.sceneList.innerHTML = scenes
    .map((scene, idx) => {
      const diagram = scene.diagram ? renderDiagram(scene.diagram) : "";
      const urduBlock = scene.urdu
        ? `<div class="content-ur" lang="ur">${escapeHtml(scene.urdu)}</div>`
        : `<div class="content-ur" lang="ur"><em>Urdu TTS uses scene narration when available.</em></div>`;

      return `
        <article class="scene" id="${scene.id}" data-index="${idx}" data-scene-id="${scene.id}">
          <div class="scene-header">
            <h3>${escapeHtml(scene.title)}</h3>
            ${scene.golden ? '<span class="badge">★ Golden</span>' : ""}
            ${seen.includes(scene.id) ? '<span class="badge" style="background:rgba(94,234,212,.15);color:#5eead4;border-color:#5eead4">Done</span>' : ""}
          </div>
          ${diagram ? `<div class="diagram-wrap">${diagram}</div>` : ""}
          <div class="content-en">${formatEnglish(scene.english)}</div>
          ${urduBlock}
          <div class="scene-actions">
            <button type="button" class="btn btn-primary" data-speak="${scene.id}">▶ Hear teacher</button>
            <button type="button" class="btn" data-mark="${scene.id}">Mark win ✓</button>
          </div>
        </article>`;
    })
    .join("");

  observeScenes();
  typesetMath();
  bindSceneButtons();
  updateProgressUI();
}

function bindSceneButtons() {
  els.sceneList.querySelectorAll("[data-speak]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-speak");
      const chapter = state.chapters.find((c) => c.id === state.chapterId);
      const scene = getVisibleScenes(chapter).find((s) => s.id === id);
      if (scene) {
        state.autoLecture = false;
        els.btnAutoLecture?.classList.remove("active");
        tts.setLanguage(state.lang);
        document.getElementById(id)?.classList.add("speaking");
        tts.speakScene(scene, state.lang);
        scrollToScene(id);
      }
    });
  });

  els.sceneList.querySelectorAll("[data-mark]").forEach((btn) => {
    btn.addEventListener("click", () => {
      const id = btn.getAttribute("data-mark");
      const progress = loadProgress();
      const set = new Set(progress[state.chapterId] || []);
      set.add(id);
      progress[state.chapterId] = [...set];
      saveProgress(progress);
      renderScenes();
    });
  });
}

function scrollToScene(id) {
  document.getElementById(id)?.scrollIntoView({ behavior: "smooth", block: "center" });
}

function advanceAutoLecture() {
  const chapter = state.chapters.find((c) => c.id === state.chapterId);
  const scenes = getVisibleScenes(chapter);
  state.sceneIndex += 1;
  if (state.sceneIndex >= scenes.length) {
    state.autoLecture = false;
    els.btnAutoLecture?.classList.remove("active");
    if (els.ttsStatus) {
      els.ttsStatus.textContent = "Lecture complete — mark your wins and pick the next chapter.";
    }
    return;
  }
  const scene = scenes[state.sceneIndex];
  scrollToScene(scene.id);
  document.getElementById(scene.id)?.classList.add("speaking");
  tts.speakScene(scene, state.lang);
}

function observeScenes() {
  const io = new IntersectionObserver(
    (entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) e.target.classList.add("visible");
      });
    },
    { threshold: 0.12 }
  );
  els.sceneList.querySelectorAll(".scene").forEach((el) => io.observe(el));
}

function typesetMath() {
  if (window.MathJax?.typesetPromise) {
    window.MathJax.typesetPromise([els.sceneList]).catch(() => {});
  }
}

function updateProgressUI() {
  const allScenes = state.chapters.flatMap((c) => c.scenes);
  const progress = loadProgress();
  let done = 0;
  state.chapters.forEach((ch) => {
    done += (progress[ch.id] || []).length;
  });
  const total = allScenes.length;
  const pct = total ? Math.round((done / total) * 100) : 0;
  if (els.progressBar) els.progressBar.style.width = `${pct}%`;
  if (els.progressLabel) els.progressLabel.textContent = `${done} / ${total} scenes marked (${pct}%)`;
}

function renderChapterNav() {
  els.chapterNav.innerHTML = state.chapters
    .map((ch) => {
      const short = ch.title.replace(/^CHAPTER \d+:\s*/i, "").replace(/ BILINGUAL.*/, "");
      return `<button type="button" data-ch="${ch.id}" class="${ch.id === state.chapterId ? "active" : ""}">Ch${ch.id}: ${escapeHtml(short)}</button>`;
    })
    .join("");

  els.chapterNav.querySelectorAll("[data-ch]").forEach((btn) => {
    btn.addEventListener("click", () => {
      state.chapterId = parseInt(btn.getAttribute("data-ch"), 10);
      state.sceneIndex = 0;
      tts.stop();
      renderChapterNav();
      renderScenes();
    });
  });
}

function bindGlobalControls() {
  els.filterGolden?.addEventListener("click", () => {
    state.goldenOnly = !state.goldenOnly;
    els.filterGolden.classList.toggle("active", state.goldenOnly);
    state.sceneIndex = 0;
    renderScenes();
  });

  els.btnAutoLecture?.addEventListener("click", () => {
    state.autoLecture = !state.autoLecture;
    els.btnAutoLecture.classList.toggle("active", state.autoLecture);
    if (state.autoLecture) {
      state.sceneIndex = 0;
      const chapter = state.chapters.find((c) => c.id === state.chapterId);
      const scenes = getVisibleScenes(chapter);
      if (scenes.length) {
        tts.setLanguage(state.lang);
        scrollToScene(scenes[0].id);
        document.getElementById(scenes[0].id)?.classList.add("speaking");
        tts.speakScene(scenes[0], state.lang);
      }
    } else {
      tts.stop();
    }
  });

  els.btnStop?.addEventListener("click", () => {
    state.autoLecture = false;
    els.btnAutoLecture?.classList.remove("active");
    tts.stop();
  });

  const setLang = (lang) => {
    state.lang = lang;
    tts.setLanguage(lang);
    els.langEn?.classList.toggle("active", lang === "en");
    els.langUr?.classList.toggle("active", lang === "ur");
  };
  els.langEn?.addEventListener("click", () => setLang("en"));
  els.langUr?.addEventListener("click", () => setLang("ur"));
  setLang("en");
}

async function init() {
  const jsonUrl = new URL("./data/chapters.json", window.location.href).href;
  const res = await fetch(jsonUrl, { cache: "no-cache" });
  if (!res.ok) {
    throw new Error(`Could not load chapters (${res.status})`);
  }
  state.chapters = await res.json();
  if (!Array.isArray(state.chapters) || state.chapters.length === 0) {
    throw new Error("Lecture data is empty");
  }
  bindGlobalControls();
  renderChapterNav();
  renderScenes();
}

init().catch((err) => {
  console.error(err);
  els.sceneList.innerHTML = `<p><strong>Failed to load lecture data.</strong><br>${escapeHtml(String(err))}<br><br>If you are on Android, reinstall CS XII Lecture Cinema v1.0.1+.</p>`;
});
