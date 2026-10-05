import { lectures, tracks, lectureById, neighbors, minutesFor } from "./curriculum.js";
import { labs, bindLab } from "./labs.js";
import { Narrator } from "./narrator.js";
import { createPlayer, captionOf } from "./player.js";
import { gradeQuiz, loadProgress, saveProgress } from "./progress.js";
import { esc, mountScene } from "./scenes.js";

const narrator = new Narrator();
const progress = loadProgress();
const app = document.querySelector("#app");
let cleanup = () => {};
let heroStop = () => {};
const session = { lectureId: "", beat: 0, playing: false, autoplay: false };

const previewScenes = [
  { type: "wave", title: "Analog and digital", mode: "both", note: "A voice is a smooth wave. A file stores jumps between 0 and 1." },
  { type: "gate", gate: "AND", title: "AND gate", steps: [{ a: 0, b: 0, y: 0, note: "Both off. The lamp stays dark." }, { a: 1, b: 1, y: 1, note: "Both on. AND lights the lamp." }] },
  { type: "bars", title: "Selection sort", frames: [{ values: [8, 4, 1, 9, 3], hi: [2], note: "Find the smallest." }, { values: [1, 4, 8, 9, 3], hi: [0], placed: [0], note: "Swap it into place." }] },
];

function percent() {
  const passed = lectures.filter((lecture) => progress.done[lecture.id]).length;
  return { passed, total: lectures.length, pct: Math.round((passed / lectures.length) * 100) };
}

function ring(pct) {
  const c = 2 * Math.PI * 18;
  const dash = (pct / 100) * c;
  return `<svg class="ring" viewBox="0 0 44 44" aria-hidden="true"><circle class="ring-bg" cx="22" cy="22" r="18"></circle><circle class="ring-fg" cx="22" cy="22" r="18" stroke-dasharray="${dash} ${c}"></circle></svg>`;
}

function header(route) {
  const { pct, passed, total } = percent();
  const link = (href, label) => `<a href="${href}" ${route === href ? 'aria-current="page"' : ""}>${label}</a>`;
  return `<header class="app-header">
    <a class="brand" href="#/"><span class="lamp" aria-hidden="true"></span><span><strong>Self-taught Bootcamp</strong><small>Computer Science XI &amp; XII</small></span></a>
    <nav class="nav-links">${link("#/track/xi", "Class XI")}${link("#/track/xii", "Class XII")}${link("#/labs", "Benches")}</nav>
    <div class="top-actions">
      <button class="lang-btn" type="button" data-lang aria-pressed="${progress.lang === "ur" ? "true" : "false"}">${progress.lang === "ur" ? "اردو" : "EN"}</button>
      <a class="progress-pill" href="#/track/xi" title="${passed} of ${total} checkpoints passed">${ring(pct)}<span>${pct}%</span></a>
    </div>
  </header>`;
}

function parseRoute() {
  const hash = location.hash || "#/";
  const parts = hash.replace(/^#\/?/, "").split("/").filter(Boolean);
  if (parts[0] === "track" && (parts[1] === "xi" || parts[1] === "xii")) return { name: "track", id: parts[1] };
  if (parts[0] === "lecture" && parts[1]) return { name: "lecture", id: parts[1] };
  if (parts[0] === "labs") return { name: "labs" };
  if (parts[0] === "lab" && parts[1]) return { name: "lab", id: parts[1] };
  return { name: "home" };
}

function homeView() {
  const { passed, total } = percent();
  const next = lectures.find((lecture) => !progress.done[lecture.id]) || lectures[0];
  const cards = tracks.map((track) => {
    const ids = track.chapters.flatMap((chapter) => chapter.lectureIds);
    const done = ids.filter((id) => progress.done[id]).length;
    return `<a class="track-card" href="#/track/${track.id}"><p class="kicker">Class ${esc(track.grade)}</p><h2>${esc(track.title)}</h2><p>${esc(track.blurb)}</p><p><strong>${done} / ${ids.length}</strong> checkpoints passed</p></a>`;
  }).join("");
  return `<section class="hero">
    <div>
      <p class="eyebrow">Sindh curriculum · spoken lectures</p>
      <h1>Learn computer science by watching the board draw, then hearing the idea.</h1>
      <p class="lede">A self-taught path through Classes XI and XII. Each lecture animates the idea, reads it aloud, and locks it in with a short checkpoint.</p>
      <div class="hero-actions">
        <a class="solid-btn" href="#/lecture/${next.id}">${passed ? "Continue" : "Start the first lecture"}</a>
        <a class="ghost-btn" href="#/labs">Open a practice bench</a>
      </div>
      <ul class="stats">
        <li><strong>${total}</strong><span>lectures</span></li>
        <li><strong>${passed}</strong><span>passed</span></li>
        <li><strong>2</strong><span>languages</span></li>
      </ul>
    </div>
    <div class="hero-stage"><div class="scene-host"></div></div>
  </section>
  <div class="section-head"><h2>The two classes</h2></div>
  <div class="track-grid">${cards}</div>
  <div class="section-head"><h2>How a lecture works</h2></div>
  <div class="how">
    <article><h3>1. The board draws</h3><p>Signals, gates, sorts, stacks, and charts move while the idea is explained.</p></article>
    <article><h3>2. A voice reads it</h3><p>Press play for English or Urdu. If this device has no voice, captions still advance.</p></article>
    <article><h3>3. You check it</h3><p>Three questions close the lecture. Two correct marks it complete on this device.</p></article>
  </div>
  <div class="section-head"><h2>Find a topic</h2></div>
  <input class="search" data-search placeholder="Search, for example K-map, queue, or 1.1.7" aria-label="Search lectures" />
  <div data-results></div>`;
}

function trackView(id, goldenOnly) {
  const track = tracks.find((item) => item.id === id);
  if (!track) return `<p>That class is not on this bootcamp.</p>`;
  const chapters = track.chapters.map((chapter) => {
    const rows = chapter.lectureIds.map((lectureId) => {
      const lecture = lectureById(lectureId);
      if (!lecture || (goldenOnly && !lecture.golden)) return "";
      const done = progress.done[lecture.id];
      return `<a class="lecture-row" href="#/lecture/${lecture.id}">
        <span class="badge">Class ${esc(lecture.level)}</span>
        <span><strong>${esc(lecture.title)}</strong><br /><small>${esc(lecture.summary)}</small></span>
        <span class="meta">${lecture.golden ? '<span class="star">Golden</span> ' : ""}${minutesFor(lecture)} min ${done ? '<span class="done-mark">Passed</span>' : ""}</span>
      </a>`;
    }).join("");
    if (!rows) return "";
    return `<section class="chapter"><h3>${esc(chapter.code)}. ${esc(chapter.title)}</h3>${rows}</section>`;
  }).join("");
  return `<p class="eyebrow">Class ${esc(track.grade)} · ${esc(track.edition)}</p>
    <div class="section-head"><h2>${esc(track.title)}</h2>
      <div class="filters"><button class="ghost-btn" type="button" data-golden aria-pressed="${goldenOnly ? "true" : "false"}">${goldenOnly ? "Showing golden topics" : "Show golden topics"}</button></div>
    </div>
    <p class="lede">${esc(track.blurb)}</p>
    ${chapters}`;
}

function lectureView(id) {
  const lecture = lectureById(id);
  if (!lecture) return `<p>That lecture is not in the bootcamp. <a href="#/">Back home</a></p>`;
  const near = neighbors(id);
  const dots = lecture.beats.map((beat, index) =>
    `<li><button type="button" data-act="beat" data-beat="${index}" aria-label="${esc(beat.title || `Beat ${index + 1}`)}">${index + 1}</button></li>`
  ).join("");
  const transcript = lecture.beats.map((beat) =>
    `<li><strong>${esc(beat.title || "Beat")}</strong><br />${esc(captionOf(beat, progress.lang))}</li>`
  ).join("");
  const outcomes = (lecture.outcomes || []).map((item) => `<li>${esc(item)}</li>`).join("");
  const prev = near.prev ? `<a class="ghost-btn" href="#/lecture/${near.prev}">Previous lecture</a>` : "";
  const next = near.next ? `<a class="ghost-btn" href="#/lecture/${near.next}">Next lecture</a>` : "";
  return `<div class="player-top">
      <a href="#/track/${lecture.track}">← Class ${esc(lecture.level)}</a>
      <span class="meta">${esc(lecture.chapter)} ${lecture.golden ? "· Golden topic" : ""} · ${minutesFor(lecture)} min</span>
    </div>
    <div class="player-grid">
      <section>
        <h1 style="font-size:2rem">${esc(lecture.title)}</h1>
        <div class="stage ${session.playing ? "is-speaking" : ""}"><div class="scene-host"></div></div>
        <p class="caption" aria-live="polite"></p>
        <div class="transport">
          <button class="ghost-btn" type="button" data-act="prev">Back</button>
          <button class="solid-btn" type="button" data-act="play" aria-pressed="false">Play lecture</button>
          <button class="ghost-btn" type="button" data-act="next">Next beat</button>
          <span class="beat-count"></span>
          <span class="speed" role="group" aria-label="Speaking speed">
            ${[0.85, 1, 1.2].map((rate) => `<button type="button" data-rate="${rate}" aria-pressed="${progress.rate === rate ? "true" : "false"}">${rate === 1 ? "1×" : `${rate}×`}</button>`).join("")}
          </span>
        </div>
        <p class="voice-note"></p>
        <ol class="beat-list">${dots}</ol>
        <p class="meta">Space plays and pauses. Arrow keys move between beats.</p>
        <div class="row-actions">${prev}${next}</div>
        <details class="transcript"><summary>Read the lecture</summary><ol>${transcript}</ol></details>
      </section>
      <aside class="panel">
        <p class="kicker">${esc((lecture.covers || []).join(" · "))}</p>
        <h2>You will be able to</h2>
        <ul class="outcomes">${outcomes}</ul>
        <div data-quiz></div>
      </aside>
    </div>`;
}

function quizHtml(lecture, picks, submitted) {
  const score = submitted ? gradeQuiz(lecture.quiz, picks) : null;
  const questions = lecture.quiz.map((question, qIndex) => {
    const buttons = question.choices.map((choice, cIndex) => {
      const classes = [
        picks[qIndex] === cIndex ? "picked" : "",
        submitted && cIndex === question.answer ? "correct" : "",
        submitted && picks[qIndex] === cIndex && cIndex !== question.answer ? "wrong" : "",
      ].filter(Boolean).join(" ");
      return `<button type="button" class="${classes}" data-q="${qIndex}" data-c="${cIndex}" ${submitted ? "disabled" : ""}>${esc(choice)}</button>`;
    }).join("");
    const why = submitted ? `<p class="why">${esc(question.why)}</p>` : "";
    return `<fieldset class="quiz-q"><legend>${esc(question.q)}</legend><div class="choices">${buttons}</div>${why}</fieldset>`;
  }).join("");
  const result = score
    ? `<p class="${score.passed ? "score-ok" : "score-no"}">${score.correct} / ${score.total}. ${score.passed ? "Checkpoint passed." : "Two correct answers mark this lecture complete. Try again."}</p>`
    : "";
  const action = submitted
    ? `<button class="ghost-btn" type="button" data-retry>Try again</button>`
    : `<button class="solid-btn" type="button" data-submit>Check answers</button>`;
  return `<h2>Checkpoint</h2><p>Answer from the lecture. Two of three passes it.</p>${questions}${result}<div class="row-actions">${action}</div>`;
}

function labsView() {
  const cards = labs.map((lab) =>
    `<a class="lab-card" href="#/lab/${lab.id}"><p class="kicker">Class ${esc(lab.level)} bench</p><h2>${esc(lab.title)}</h2><p>${esc(lab.summary)}</p></a>`
  ).join("");
  return `<p class="eyebrow">Practice</p><h1>Benches</h1><p class="lede">The lectures draw the idea. The benches let you change the inputs yourself.</p><div class="lab-grid">${cards}</div>`;
}

function labView(id) {
  const lab = labs.find((item) => item.id === id);
  if (!lab) return `<p>That bench is not set up. <a href="#/labs">All benches</a></p>`;
  return `<div class="player-top"><a href="#/labs">← Benches</a><button class="solid-btn" type="button" data-explain>Read this aloud</button></div>
    <div class="lab-layout"><div data-bench></div><aside class="panel"><p class="kicker">Class ${esc(lab.level)}</p><h2>${esc(lab.title)}</h2><p>${esc(lab.summary)}</p><p>${esc(lab.say)}</p></aside></div>`;
}

function render() {
  cleanup();
  heroStop();
  const route = parseRoute();
  const routeKey = route.name === "home" ? "#/" : `#/${route.name}${route.id ? `/${route.id}` : ""}`;
  const goldenOnly = session.goldenOnly && route.name === "track";
  let body = "";
  if (route.name === "home") body = homeView();
  else if (route.name === "track") body = trackView(route.id, goldenOnly);
  else if (route.name === "lecture") body = lectureView(route.id);
  else if (route.name === "labs") body = labsView();
  else if (route.name === "lab") body = labView(route.id);
  app.innerHTML = `${header(route.name === "track" ? `#/track/${route.id}` : route.name === "labs" || route.name === "lab" ? "#/labs" : routeKey)}${`<main class="wrap">${body}</main>`}`;
  cleanup = bind(route);
}

function bind(route) {
  const stops = [];
  app.querySelector("[data-lang]")?.addEventListener("click", () => {
    progress.lang = progress.lang === "ur" ? "en" : "ur";
    saveProgress(progress);
    if (route.name === "lecture") {
      session.lectureId = route.id;
      session.autoplay = session.playing;
    }
    render();
  });

  if (route.name === "home") {
    const host = app.querySelector(".scene-host");
    let index = 0;
    const draw = () => {
      heroStop();
      heroStop = mountScene(host, previewScenes[index]);
      index = (index + 1) % previewScenes.length;
    };
    draw();
    const timer = setInterval(draw, 4200);
    stops.push(() => clearInterval(timer));
    const search = app.querySelector("[data-search]");
    const results = app.querySelector("[data-results]");
    search?.addEventListener("input", () => {
      const query = search.value.trim().toLowerCase();
      if (!query) {
        results.innerHTML = "";
        return;
      }
      const found = lectures.filter((lecture) =>
        [lecture.title, lecture.chapter, lecture.summary, ...(lecture.covers || []), ...(lecture.outcomes || [])]
          .join(" ")
          .toLowerCase()
          .includes(query)
      ).slice(0, 8);
      results.innerHTML = found.map((lecture) =>
        `<a class="lecture-row" href="#/lecture/${lecture.id}"><span class="badge">${esc(lecture.level)}</span><span><strong>${esc(lecture.title)}</strong><br /><small>${esc(lecture.chapter)}</small></span><span>${lecture.golden ? "Golden" : ""}</span></a>`
      ).join("") || `<p>No lecture uses that word yet.</p>`;
    });
  }

  if (route.name === "track") {
    app.querySelector("[data-golden]")?.addEventListener("click", () => {
      session.goldenOnly = !session.goldenOnly;
      render();
    });
  }

  if (route.name === "lecture") {
    const lecture = lectureById(route.id);
    if (lecture) {
      if (session.lectureId !== lecture.id) {
        session.lectureId = lecture.id;
        session.beat = 0;
        session.playing = false;
        session.autoplay = false;
      }
      progress.lastId = lecture.id;
      saveProgress(progress);
      const player = createPlayer(app, lecture, {
        narrator,
        lang: () => progress.lang,
        rate: () => progress.rate,
        startBeat: session.beat,
        autoplay: session.autoplay,
        onBeat: (beat) => {
          session.beat = beat;
        },
        onFinished: () => {
          session.playing = false;
          session.autoplay = false;
          app.querySelector("[data-quiz]")?.scrollIntoView({ behavior: "smooth", block: "nearest" });
        },
      });
      session.autoplay = false;
      const quiz = app.querySelector("[data-quiz]");
      let picks = [];
      let submitted = false;
      const paintQuiz = () => {
        quiz.innerHTML = quizHtml(lecture, picks, submitted);
      };
      paintQuiz();
      quiz.addEventListener("click", (event) => {
        const choice = event.target.closest("[data-q]");
        if (choice && !submitted) {
          picks[Number(choice.dataset.q)] = Number(choice.dataset.c);
          paintQuiz();
          return;
        }
        if (event.target.matches("[data-submit]")) {
          submitted = true;
          const score = gradeQuiz(lecture.quiz, picks);
          progress.scores[lecture.id] = score;
          if (score.passed) progress.done[lecture.id] = Date.now();
          else delete progress.done[lecture.id];
          saveProgress(progress);
          paintQuiz();
          const pill = app.querySelector(".progress-pill");
          if (pill) {
            const stats = percent();
            pill.title = `${stats.passed} of ${stats.total} checkpoints passed`;
            pill.innerHTML = `${ring(stats.pct)}<span>${stats.pct}%</span>`;
          }
          return;
        }
        if (event.target.closest("[data-retry]")) {
          submitted = false;
          picks = [];
          paintQuiz();
        }
      });
      app.querySelector(".speed")?.addEventListener("click", (event) => {
        const rate = Number(event.target.dataset?.rate);
        if (!rate) return;
        progress.rate = rate;
        saveProgress(progress);
        session.beat = player.beat;
        session.playing = player.playing;
        session.autoplay = player.playing;
        session.lectureId = lecture.id;
        render();
      });
      const watch = setInterval(() => {
        session.playing = player.playing;
        session.beat = player.beat;
      }, 200);
      stops.push(() => {
        clearInterval(watch);
        player.destroy();
      });
    }
  }

  if (route.name === "lab") {
    const bench = app.querySelector("[data-bench]");
    if (bench) stops.push(bindLab(bench, route.id, narrator, () => ({ lang: progress.lang, rate: progress.rate })));
  }

  return () => {
    stops.forEach((stop) => stop());
    narrator.cancel();
  };
}

window.addEventListener("hashchange", render);
narrator.ready();
render();
