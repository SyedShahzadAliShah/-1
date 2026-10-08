(function () {
  const state = {
    data: null,
    view: "home",
    trackId: null,
    chapterId: null,
    topicIndex: 0,
    chapterHtml: "",
    progress: JSON.parse(localStorage.getItem("sketchnote-progress") || "{}")
  };

  const $ = (id) => document.getElementById(id);

  function saveProgress() {
    localStorage.setItem("sketchnote-progress", JSON.stringify(state.progress));
  }

  function markDone(topicId) {
    state.progress[topicId] = true;
    saveProgress();
  }

  function trackById(id) {
    return state.data.tracks.find((t) => t.id === id);
  }

  function chapterById(track, id) {
    return track.chapters.find((c) => c.id === id);
  }

  function doneCount(chapter) {
    return chapter.topics.filter((t) => state.progress[t.id]).length;
  }

  function renderHome() {
    state.view = "home";
    $("view-home").classList.remove("hidden");
    $("view-chapters").classList.add("hidden");
    $("view-lesson").classList.add("hidden");
    const grid = $("track-grid");
    grid.innerHTML = state.data.tracks.map((track) => {
      const beats = track.chapters.reduce((n, ch) => n + ch.topics.length, 0);
      const svgs = track.chapters.reduce((n, ch) => n + (ch.svgCount || 0), 0);
      return `<button class="track-card" data-track="${track.id}">
        <span class="kicker">${track.id === "studio" ? "START HERE" : track.id.toUpperCase()}</span>
        <h3>${track.titleEn}</h3>
        <p class="ur">${track.titleUr}</p>
        <p class="meta">${track.subtitleEn}</p>
        <p class="meta">${beats} sketchnote beats · ${svgs} SVG diagrams</p>
      </button>`;
    }).join("");
  }

  function renderChapters(trackId) {
    state.view = "chapters";
    state.trackId = trackId;
    const track = trackById(trackId);
    $("view-home").classList.add("hidden");
    $("view-lesson").classList.add("hidden");
    $("view-chapters").classList.remove("hidden");
    $("chapter-title").textContent = track.titleEn;
    $("chapter-ur").textContent = track.titleUr;
    $("chapter-sub").textContent = track.subtitleEn;
    $("chapter-grid").innerHTML = track.chapters.map((ch) => {
      const done = doneCount(ch);
      const kicker = ch.kind === "recap" ? "Recap & mock" : (ch.number ? "Chapter " + ch.number : "Studio");
      return `<button class="chapter-card ${ch.goldenCount ? "golden" : ""}" data-chapter="${ch.id}">
        <span class="kicker">${kicker}</span>
        <h3>${ch.titleEn}</h3>
        <p class="ur">${ch.titleUr}</p>
        <p class="meta">${ch.topicCount || ch.topics.length} topics · ${ch.svgCount || 0} SVGs
          ${ch.goldenCount ? ' · <span class="star">★ ' + ch.goldenCount + " golden</span>" : ""}</p>
        <p class="progress-ring">${done}/${ch.topics.length} heard</p>
      </button>`;
    }).join("");
  }

  function topicHtml(chapter, topic, index) {
    if (!state.chapterDoc) return "<p>Loading sketchnote…</p>";
    const doc = state.chapterDoc;
    if (topic.kind === "opener") {
      const opener = doc.querySelector(".ch-opener, .front") || doc.querySelector("h1");
      const objectives = doc.querySelector("ul.objectives");
      return (opener ? opener.outerHTML : "") + (objectives ? "<h3>What you will learn</h3>" + objectives.outerHTML : "");
    }
    const topics = [...doc.querySelectorAll(".topic")];
    if (topics[index - (chapter.topics[0].kind === "opener" ? 1 : 0)]) {
      const shift = chapter.topics[0].kind === "opener" ? 1 : 0;
      const node = topics[index - shift];
      if (node) return node.innerHTML;
    }
    if (topic.kind === "section") {
      const headings = [...doc.querySelectorAll("h2")];
      const h = headings[topic.index - 1];
      if (!h) return `<h2>${topic.titleEn}</h2>`;
      let html = h.outerHTML;
      let n = h.nextElementSibling;
      while (n && n.tagName !== "H2") {
        html += n.outerHTML;
        n = n.nextElementSibling;
      }
      return html;
    }
    return `<h2>${topic.titleEn}</h2><p>${topic.speakEn || ""}</p><p class="ur">${topic.speakUr || ""}</p>`;
  }

  function renderLesson() {
    const track = trackById(state.trackId);
    const chapter = chapterById(track, state.chapterId);
    const topic = chapter.topics[state.topicIndex];
    $("view-home").classList.add("hidden");
    $("view-chapters").classList.add("hidden");
    $("view-lesson").classList.remove("hidden");
    $("lesson-kicker").textContent = track.titleEn + (chapter.number ? " · Ch " + chapter.number : "");
    $("lesson-title").textContent = topic.titleEn;
    $("topic-rail").innerHTML = chapter.topics.map((t, i) => {
      return `<button class="topic-card ${i === state.topicIndex ? "active" : ""}" data-topic="${i}">
        ${t.golden ? '<span class="star">★</span> ' : ""}${t.titleEn}
      </button>`;
    }).join("");
    const body = $("lesson-body");
    body.classList.remove("show-answers");
    body.innerHTML = topicHtml(chapter, topic, state.topicIndex);
    if (window.EnhanceMath) EnhanceMath.typeset(body);
    markDone(topic.id);
  }

  async function openChapter(trackId, chapterId, topicIndex) {
    const track = trackById(trackId);
    const chapter = chapterById(track, chapterId);
    state.trackId = trackId;
    state.chapterId = chapterId;
    state.topicIndex = topicIndex || 0;
    const res = await fetch(chapter.file);
    const html = await res.text();
    state.chapterHtml = html;
    state.chapterDoc = new DOMParser().parseFromString(html, "text/html");
    renderLesson();
  }

  function bind() {
    document.body.addEventListener("click", (ev) => {
      const track = ev.target.closest("[data-track]");
      if (track) return renderChapters(track.dataset.track);
      const chapter = ev.target.closest("[data-chapter]");
      if (chapter) return openChapter(state.trackId, chapter.dataset.chapter, 0);
      const topic = ev.target.closest("[data-topic]");
      if (topic) {
        state.topicIndex = Number(topic.dataset.topic);
        return renderLesson();
      }
      if (ev.target.id === "btn-home" || ev.target.id === "back-home") return renderHome();
      if (ev.target.id === "back-chapters") return renderChapters(state.trackId);
      if (ev.target.id === "btn-prev") {
        state.topicIndex = Math.max(0, state.topicIndex - 1);
        return renderLesson();
      }
      if (ev.target.id === "btn-next") {
        const track = trackById(state.trackId);
        const chapter = chapterById(track, state.chapterId);
        state.topicIndex = Math.min(chapter.topics.length - 1, state.topicIndex + 1);
        return renderLesson();
      }
      if (ev.target.id === "btn-speak" || ev.target.id === "btn-speak-bar") {
        if (document.querySelector(".speak-btn.live")) return TtsBridge.stop();
        const track = trackById(state.trackId);
        const chapter = chapterById(track, state.chapterId);
        return TtsBridge.speakTopic(chapter.topics[state.topicIndex]);
      }
      if (ev.target.id === "btn-stop") return TtsBridge.stop();
      if (ev.target.id === "btn-answers") {
        $("lesson-body").classList.toggle("show-answers");
      }
      if (ev.target.id === "flex-row") {
        $("flex-playground")?.classList.remove("column");
      }
      if (ev.target.id === "flex-col") {
        $("flex-playground")?.classList.add("column");
      }
    });
  }

  window.goBack = function () {
    if (state.view === "lesson") {
      renderChapters(state.trackId);
      return true;
    }
    if (state.view === "chapters") {
      renderHome();
      return true;
    }
    return false;
  };

  fetch("data/curriculum.json")
    .then((r) => r.json())
    .then((data) => {
      state.data = data;
      bind();
      renderHome();
    })
    .catch((err) => {
      $("track-grid").innerHTML = "<p>Could not load curriculum: " + err + "</p>";
    });
})();
