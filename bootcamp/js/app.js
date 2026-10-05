import { lectures, tracks, lectureById, neighbors, minutesFor } from "./curriculum.js";
import { labs, bindLab } from "./labs.js";
import { Narrator } from "./narrator.js";
import { createPlayer, captionOf } from "./player.js";
import { gradeQuiz, loadProgress, saveProgress } from "./progress.js";
import { esc, mountScene } from "./scenes.js";
import { citationHaystack, formatSupport } from "./citations.js";
import { ROLE_LABEL, ROLE_ORDER } from "./lectures/mastery.js";
import { rich, typeset } from "./mathtext.js";
import { printBook, saveBook } from "./book.js";
import {
  aheadCards, buildCards, buildPlan, coverage, dayKey, deckStats, dueCards,
  hoursUntil, labTitle, rate, sessionState, streak,
} from "./teach.js";

const allCards = buildCards();
const plan = buildPlan();

const narrator = new Narrator();
const progress = loadProgress();
const app = document.querySelector("#app");
let cleanup = () => {};
let heroStop = () => {};
const session = { lectureId: "", beat: 0, playing: false, autoplay: false };

const previewScenes = [
  { type: "steps", title: "Worked while you listen", problem: "$Y = (A \\cdot B) + \\overline{A}$, with $A=0$, $B=1$.", steps: [
    { do: "$A \\cdot B = 0$", why: "AND needs both 1." },
    { do: "$\\overline{A} = 1$", why: "NOT flips 0." },
    { do: "$Y = 1$", why: "0 OR 1 is 1." },
  ], note: "Each lecture now works an example, then names the trap." },
  { type: "whiteboard", title: "Drawn while you listen", ink: [
    { t: "line", x1: 36, y1: 130, x2: 470, y2: 130 },
    { t: "dot", x: 80, y: 130 },
    { t: "dot", x: 400, y: 130, pen: "gold" },
    { t: "dot", x: 180, y: 72, pen: "gold" },
    { t: "arrow", x1: 180, y1: 84, x2: 96, y2: 118, pen: "gold" },
    { t: "text", x: 150, y: 44, label: "snap to the nearer level", pen: "gold" },
  ], note: "A deeper rule is still drawn on the board." },
  { type: "wave", title: "Analog and digital", mode: "both", note: "A voice is a smooth wave. A file stores jumps between 0 and 1." },
  { type: "gate", gate: "AND", title: "AND gate", steps: [{ a: 0, b: 0, y: 0, note: "Both off. The lamp stays dark." }, { a: 1, b: 1, y: 1, note: "Both on. AND lights the lamp." }] },
];

function percent() {
  const passed = lectures.filter((lecture) => progress.done[lecture.id]).length;
  return { passed, total: lectures.length, pct: Math.round((passed / lectures.length) * 100) };
}

function beatTotal() {
  return lectures.reduce((count, lecture) => count + (lecture.beats || []).length, 0);
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
    <nav class="nav-links">${link("#/track/xi", "Class XI")}${link("#/track/xii", "Class XII")}${link("#/labs", "Benches")}${link("#/plan", "Teach yourself")}${link("#/review", "Review")}</nav>
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
  if (parts[0] === "plan") return { name: "plan" };
  if (parts[0] === "review") return { name: "review", id: parts[1] || "" };
  if (parts[0] === "book") return { name: "book" };
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
      <h1>Learn computer science by watching a worked example, then hearing the trap.</h1>
      <p class="lede">A self-taught path through Classes XI and XII. Each lecture teaches the idea, draws a deeper rule, works an exam-style example, names the trap, and leaves a one-page sheet. Then you try a drill and a checkpoint.</p>
      <div class="hero-actions">
        <a class="solid-btn" href="#/lecture/${next.id}">${passed ? "Continue" : "Start the first lecture"}</a>
        <a class="ghost-btn" href="#/labs">Open a practice bench</a>
      </div>
      <ul class="stats">
        <li><strong>${total}</strong><span>lectures</span></li>
        <li><strong>${beatTotal()}</strong><span>teaching beats</span></li>
        <li><strong>${passed}</strong><span>passed</span></li>
      </ul>
    </div>
    <div class="hero-stage"><div class="scene-host"></div></div>
  </section>
  <div class="section-head"><h2>The two classes</h2></div>
  <div class="track-grid">${cards}</div>
  <div class="section-head"><h2>How a lecture works</h2></div>
  <div class="how">
    <article><h3>1. Ideas</h3><p>The board animates the syllabus idea while a voice reads it in English or Urdu.</p></article>
    <article><h3>2. Deeper rule</h3><p>A whiteboard draws one extra rule, with the Sindh SLO and a supporting source named beside it.</p></article>
    <article><h3>3. Worked example</h3><p>A short exam-style problem is solved step by step, so you see the moves, not only the definition.</p></article>
    <article><h3>4. Trap and sheet</h3><p>The common mistake is named, then a one-page exam sheet. Try a drill before the checkpoint.</p></article>
    <article><h3>5. Checkpoint</h3><p>Three questions. Two correct marks the lecture complete on this device. Wrong picks explain the trap.</p></article>
  </div>
  <div class="section-head"><h2>Teach Yourself edition</h2></div>
  <div class="edition-grid">
    <a class="edition-card" href="#/plan"><p class="kicker">Plan</p><h3>${plan.length} study sessions</h3><p>Two lectures a sitting, a bench when one fits, and recall of the last session. Two review weeks close each class.</p></a>
    <a class="edition-card" href="#/review"><p class="kicker">Recall</p><h3>${allCards.length} flashcards</h3><p>Drills, traps, sheets, and checkpoint questions return on a 1, 3, 7, 21 day schedule. Pass a checkpoint and its cards join your deck.</p></a>
    <a class="edition-card" href="#/book"><p class="kicker">Book</p><h3>The printable study book</h3><p>Every exam sheet, trap, and drill in syllabus order, with your own teach-back notes. Print it or save as PDF.</p></a>
  </div>
  <div class="section-head"><h2>Find a topic</h2></div>
  <input class="search" data-search placeholder="Search, for example K-map, Fitts, or 1.1.7" aria-label="Search lectures" />
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

function citesHtml(lecture) {
  const cites = lecture.citations;
  if (!cites?.curriculum) return "";
  const slos = (cites.slos || []).map((item) =>
    `<li><span class="slo-code">${esc(item.code)}</span> ${esc(item.title)}</li>`
  ).join("");
  const extra = cites.support
    ? `<li>
        <span class="cite-kind">Deeper board</span>
        <strong>${esc(formatSupport(cites.support))}</strong>
        <span class="cite-why">${esc(cites.support.why)}</span>
      </li>`
    : "";
  return `<section class="cites">
    <h2>Sources</h2>
    <p class="cite-note">The lecture is an original briefing. Name these if you reuse the idea.</p>
    <ul>
      <li>
        <span class="cite-kind">Syllabus</span>
        <strong>${esc(cites.curriculum.work)} (${esc(cites.curriculum.year)}).</strong>
        <ul class="slo-list">${slos}</ul>
      </li>
      ${extra}
    </ul>
  </section>`;
}

function sheetHtml(lecture) {
  const sheet = lecture.sheet;
  if (!sheet?.lines?.length) return "";
  const lines = sheet.lines.map((line) => `<li>${rich(line)}</li>`).join("");
  return `<section class="study-sheet">
    <h2>Exam sheet</h2>
    <ol>${lines}</ol>
    ${sheet.formula ? `<p class="sheet-formula">${rich(sheet.formula)}</p>` : ""}
    ${sheet.sayThis ? `<p class="say-this"><b>Say it back.</b> ${rich(sheet.sayThis)}</p>` : ""}
  </section>`;
}

function drillHtml(lecture, revealed) {
  const drill = lecture.drill;
  if (!drill?.q) return "";
  return `<section class="drill">
    <h2>Try this first</h2>
    <p>${esc(drill.q)}</p>
    ${revealed
      ? `<p class="drill-out">${esc(drill.reveal)}</p>`
      : `<button class="ghost-btn" type="button" data-drill>Reveal the answer</button>`}
  </section>`;
}

function teachBackHtml(lecture) {
  const note = progress.notes[lecture.id] || "";
  const inDeck = Boolean(progress.decks[lecture.id]);
  return `<section class="teach-back">
    <h2>Teach it back</h2>
    <p>Explain this lecture in two or three sentences, as if to a classmate. Your words stay on this device.</p>
    <textarea data-note rows="4" placeholder="In my own words…">${esc(note)}</textarea>
    <div class="row-actions">
      <button class="ghost-btn" type="button" data-check-note>Check against the sheet</button>
      <button class="ghost-btn" type="button" data-deck aria-pressed="${inDeck ? "true" : "false"}">${inDeck ? "In your flashcard deck" : "Add to flashcards"}</button>
    </div>
    <div data-note-result></div>
  </section>`;
}

function coverageHtml(lecture, text) {
  const result = coverage(text, lecture);
  if (!String(text || "").trim()) return `<p class="meta">Write a few sentences first, then check.</p>`;
  const chips = result.terms.map((term) =>
    `<span class="term ${result.hit.includes(term) ? "hit" : "miss"}">${esc(term)}</span>`
  ).join("");
  const verdict = result.score >= 0.6
    ? "That covers the sheet. Try the flashcards next."
    : result.score >= 0.3
      ? "Partway there. Reread the exam sheet and add the missing ideas."
      : "The sheet uses different words. Replay the exam-sheet beat, then try again.";
  return `<p class="meta">You used ${result.hit.length} of ${result.terms.length} key terms.</p>
    <div class="term-row">${chips}</div>
    <p class="drill-out">${esc(verdict)}</p>
    <p><a href="#/review/${lecture.id}">Review this lecture's cards</a></p>`;
}

function lectureView(id) {
  const lecture = lectureById(id);
  if (!lecture) return `<p>That lecture is not in the bootcamp. <a href="#/">Back home</a></p>`;
  const near = neighbors(id);
  const dots = lecture.beats.map((beat, index) =>
    `<li><button type="button" class="role-${esc(beat.role || "idea")}" data-act="beat" data-beat="${index}" title="${esc(ROLE_LABEL[beat.role] || beat.title || `Beat ${index + 1}`)}" aria-label="${esc(beat.title || `Beat ${index + 1}`)}">${index + 1}</button></li>`
  ).join("");
  const arc = ROLE_ORDER.map((role) =>
    `<li data-phase="${role}"><span>${esc(ROLE_LABEL[role])}</span></li>`
  ).join("");
  const transcript = lecture.beats.map((beat) =>
    `<li><strong>${esc(ROLE_LABEL[beat.role] || "Idea")} · ${esc(beat.title || "Beat")}</strong><br />${esc(captionOf(beat, progress.lang))}</li>`
  ).join("");
  const outcomes = (lecture.outcomes || []).map((item) => `<li>${esc(item)}</li>`).join("");
  const prev = near.prev ? `<a class="ghost-btn" href="#/lecture/${near.prev}">Previous lecture</a>` : "";
  const next = near.next ? `<a class="ghost-btn" href="#/lecture/${near.next}">Next lecture</a>` : "";
  return `<div class="player-top">
      <a href="#/track/${lecture.track}">← Class ${esc(lecture.level)}</a>
      <span class="meta">${esc(lecture.chapter)} ${lecture.golden ? "· Golden topic" : ""} · ${minutesFor(lecture)} min</span>
    </div>
    <ol class="lesson-arc">${arc}</ol>
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
          <span class="beat-phase"></span>
          <span class="speed" role="group" aria-label="Speaking speed">
            ${[0.85, 1, 1.2].map((rate) => `<button type="button" data-rate="${rate}" aria-pressed="${progress.rate === rate ? "true" : "false"}">${rate === 1 ? "1×" : `${rate}×`}</button>`).join("")}
          </span>
        </div>
        <p class="voice-note"></p>
        <ol class="beat-list">${dots}</ol>
        <p class="meta">Space plays and pauses. Arrow keys move between beats. Gold is the deeper rule, teal the example, rose the trap.</p>
        <div class="row-actions">${prev}${next}</div>
        <details class="transcript"><summary>Read the lecture</summary><ol>${transcript}</ol></details>
      </section>
      <aside class="panel">
        <p class="kicker">${esc(lecture.citations?.curriculum?.short || `Class ${lecture.level}`)} · ${esc((lecture.covers || []).join(" · "))}</p>
        <h2>You will be able to</h2>
        <ul class="outcomes">${outcomes}</ul>
        ${sheetHtml(lecture)}
        <div data-drill></div>
        ${teachBackHtml(lecture)}
        ${citesHtml(lecture)}
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
    const trap = submitted && question.trap ? `<p class="trap-why">Tempting mistake: ${esc(question.trap)}</p>` : "";
    return `<fieldset class="quiz-q"><legend>${esc(question.q)}</legend><div class="choices">${buttons}</div>${why}${trap}</fieldset>`;
  }).join("");
  const result = score
    ? `<p class="${score.passed ? "score-ok" : "score-no"}">${score.correct} / ${score.total}. ${score.passed ? "Checkpoint passed." : "Two correct answers mark this lecture complete. Try again."}</p>`
    : "";
  const action = submitted
    ? `<button class="ghost-btn" type="button" data-retry>Try again</button>`
    : `<button class="solid-btn" type="button" data-submit>Check answers</button>`;
  return `<h2>Checkpoint</h2><p>Answer from the lecture. Two of three passes it. After you check, the tempting mistake is named.</p>${questions}${result}<div class="row-actions">${action}</div>`;
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

function planView() {
  const states = plan.map((item) => sessionState(item, progress, allCards));
  const doneCount = states.filter((state) => state.done).length;
  const nextIndex = states.findIndex((state) => !state.done);
  const next = plan[nextIndex === -1 ? 0 : nextIndex];
  const stats = deckStats(allCards, progress);
  const days = streak(progress.log);
  const rows = plan.map((item, index) => {
    const state = states[index];
    const lecturesHtml = item.lectureIds.map((lectureId) => {
      const lecture = lectureById(lectureId);
      return `<li>Learn: <a href="#/lecture/${lectureId}">${esc(lecture?.title || lectureId)}</a>${progress.done[lectureId] ? ' <span class="done-mark">Passed</span>' : ""}</li>`;
    }).join("");
    const lab = item.lab ? `<li>Practice: <a href="#/lab/${item.lab}">${esc(labTitle(item.lab))}</a></li>` : "";
    const recall = item.kind === "review"
      ? `<li>Recall: <a href="#/review/${item.track}">every Class ${esc(item.grade)} card</a>, until none is due.</li><li>Reread the <a href="#/book">study book</a> for this class and fix any teach-back note that missed its terms.</li>`
      : item.reviewIds.length
        ? `<li>Recall: <a href="#/review/${item.reviewIds[0]}">cards from session ${item.n - 1}</a></li>`
        : "";
    const pair = item.lectureIds.length > 1;
    const teach = item.kind === "learn" ? `<li>Teach it back: two sentences in ${pair ? "each lecture's" : "the lecture's"} sidebar, then check them against the sheet.</li><li>Check: pass ${pair ? "both checkpoints" : "the checkpoint"}. The cards join your deck.</li>` : "";
    return `<article class="session ${state.done ? "is-done" : ""} ${item === next ? "is-next" : ""}">
      <div class="session-n">${item.n}</div>
      <div>
        <p class="kicker">Class ${esc(item.grade)} · ${esc(item.chapter)} · about ${item.minutes} min</p>
        <h3>${esc(item.title)}</h3>
        <ol class="session-steps">${lecturesHtml}${lab}${recall}${teach}</ol>
      </div>
      <div class="session-state">${state.done ? '<span class="done-mark">Done</span>' : esc(state.label)}</div>
    </article>`;
  }).join("");
  return `<p class="eyebrow">Teach Yourself edition</p>
    <div class="section-head"><h2>${plan.length} sessions, in syllabus order</h2></div>
    <p class="lede">One sitting is two lectures, a bench when one fits, recall of the last session, and a teach-back in your own words. Each class ends with a review week.</p>
    <div class="today">
      <div>
        <p class="kicker">Up next</p>
        <h3>Session ${next.n}: ${esc(next.title)}</h3>
        <p>${doneCount} of ${plan.length} sessions done · ${stats.due} cards due now · streak ${days} day${days === 1 ? "" : "s"}</p>
      </div>
      <div class="row-actions">
        <a class="solid-btn" href="${next.kind === "review" ? `#/review/${next.track}` : `#/lecture/${next.lectureIds[0]}`}">Start session ${next.n}</a>
        <a class="ghost-btn" href="#/review">Review due cards</a>
        <a class="ghost-btn" href="#/book">Open the book</a>
      </div>
    </div>
    <div class="sessions">${rows}</div>`;
}

function scopeFor(id) {
  if (id === "xi" || id === "xii") {
    const track = tracks.find((item) => item.id === id);
    return { label: `Class ${track.grade}`, cards: allCards.filter((card) => card.track === id), lectureIds: track.chapters.flatMap((chapter) => chapter.lectureIds) };
  }
  const lecture = lectureById(id);
  if (lecture) return { label: lecture.title, cards: allCards.filter((card) => card.lectureId === id), lectureIds: [id] };
  return { label: "Every lecture", cards: allCards, lectureIds: lectures.map((item) => item.id) };
}

function reviewView(id) {
  const scope = scopeFor(id);
  const stats = deckStats(scope.cards, progress);
  const missing = scope.lectureIds.filter((lectureId) => !progress.decks[lectureId]);
  return `<p class="eyebrow">Teach Yourself edition · recall</p>
    <div class="section-head"><h2>Flashcards · ${esc(scope.label)}</h2>
      <div class="filters">
        <a class="ghost-btn" href="#/review">All</a>
        <a class="ghost-btn" href="#/review/xi">Class XI</a>
        <a class="ghost-btn" href="#/review/xii">Class XII</a>
      </div>
    </div>
    <p class="lede">Say the answer out loud before you flip. Got it moves the card out by 1, 3, 7, then 21 days. Again brings it back in ten minutes.</p>
    <ul class="stats deck-stats">
      <li><strong data-stat="due">${stats.due}</strong><span>due now</span></li>
      <li><strong data-stat="total">${stats.total}</strong><span>in your deck</span></li>
      <li><strong data-stat="mastered">${stats.mastered}</strong><span>mastered</span></li>
      <li><strong data-stat="fresh">${stats.fresh}</strong><span>never seen</span></li>
    </ul>
    <div class="deck-controls">
      ${missing.length ? `<button class="ghost-btn" type="button" data-add-scope>Add ${missing.length} lecture${missing.length === 1 ? "" : "s"} to the deck now</button>` : `<span class="meta">Every lecture here is in your deck.</span>`}
      <span class="meta">Space flips. 1 is Again. 2 is Got it.</span>
    </div>
    <div class="flash-host" data-flash></div>`;
}

function cardHtml(card, flipped, left, done) {
  if (!card) return "";
  const back = Array.isArray(card.back)
    ? `<ol class="sheet-lines">${card.back.map((line) => `<li>${rich(line)}</li>`).join("")}</ol>`
    : `<p>${rich(card.back)}</p>`;
  return `<article class="flashcard ${flipped ? "is-flipped" : ""}">
    <p class="kicker">${esc(card.kind)} · ${esc(card.lecture)} · ${left} left${done ? ` · ${done} done` : ""}</p>
    <div class="flash-front"><p>${rich(card.front)}</p></div>
    ${flipped ? `<div class="flash-back">${back}</div>` : ""}
    <div class="row-actions">
      ${flipped
        ? `<button class="ghost-btn" type="button" data-rate="again">Again</button><button class="solid-btn" type="button" data-rate="good">Got it</button>`
        : `<button class="solid-btn" type="button" data-flip>Show the answer</button>`}
      <button class="ghost-btn" type="button" data-read>Read aloud</button>
      <a class="ghost-btn" href="#/lecture/${card.lectureId}">Open the lecture</a>
    </div>
  </article>`;
}

function emptyDeckHtml(scope, stats, done) {
  if (!stats.total) {
    return `<div class="flash-empty"><h3>No cards in this deck yet.</h3><p>Pass a checkpoint and its six cards join automatically, or add the lectures above and start today.</p></div>`;
  }
  const when = stats.next ? `The next card returns in about ${hoursUntil(stats.next)} hour${hoursUntil(stats.next) === 1 ? "" : "s"}.` : "";
  return `<div class="flash-empty"><h3>${done ? `Session done: ${done} answer${done === 1 ? "" : "s"}.` : "Nothing is due."}</h3><p>${esc(when)} You can pull the next ten cards early if you want more.</p><button class="ghost-btn" type="button" data-ahead>Study ten cards ahead</button></div>`;
}

function bookView() {
  const chapters = tracks.map((track) => {
    const parts = track.chapters.map((chapter) => {
      const items = chapter.lectureIds.map((lectureId) => {
        const lecture = lectureById(lectureId);
        if (!lecture) return "";
        const trap = lecture.beats.find((beat) => beat.role === "trap")?.scene;
        const note = progress.notes[lecture.id];
        return `<article class="book-lecture">
          <h4>${esc(lecture.title)} <small>${esc((lecture.covers || []).join(" · "))}</small></h4>
          <p class="book-summary">${esc(lecture.summary)}</p>
          <div class="book-cols">
            <div>
              <h5>Exam sheet</h5>
              <ol>${(lecture.sheet?.lines || []).map((line) => `<li>${rich(line)}</li>`).join("")}</ol>
              ${lecture.sheet?.formula ? `<p class="book-formula">${rich(lecture.sheet.formula)}</p>` : ""}
              ${lecture.sheet?.sayThis ? `<p><b>Say it back.</b> ${rich(lecture.sheet.sayThis)}</p>` : ""}
            </div>
            <div>
              <h5>The trap</h5>
              <p><span class="book-wrong">${esc(trap?.wrong || "")}</span><br />${esc(trap?.right || "")}<br /><small>${esc(trap?.note || "")}</small></p>
              <h5>Drill</h5>
              <p>${esc(lecture.drill?.q || "")}<br /><small>Answer: ${esc(lecture.drill?.reveal || "")}</small></p>
              ${note ? `<h5>Your teach-back</h5><p class="book-note">${esc(note)}</p>` : ""}
            </div>
          </div>
          <p class="book-key"><b>Checkpoint.</b> ${lecture.quiz.map((question, index) => `${index + 1}. ${esc(question.q)} <i>${esc(question.choices[question.answer])}.</i>`).join(" ")}</p>
        </article>`;
      }).join("");
      return `<section class="book-chapter"><h3>${esc(chapter.code)}. ${esc(chapter.title)}</h3>${items}</section>`;
    }).join("");
    return `<section class="book-track"><h2>Computer Science ${esc(track.grade)}</h2><p class="meta">${esc(track.edition)}</p>${parts}</section>`;
  }).join("");
  return `<div class="player-top no-print"><div><p class="eyebrow">Teach Yourself edition · book</p><h1>The study book</h1></div>
      <div class="row-actions"><button class="solid-btn" type="button" data-save-book>Download the book</button><button class="ghost-btn" type="button" data-print>Print or save as PDF</button></div></div>
    <p class="lede no-print">Every exam sheet, trap, drill, and checkpoint answer, in syllabus order. Teach-back notes you have written appear under their lecture.</p>
    <p class="meta no-print" data-book-status aria-live="polite">Download gives you one HTML file that opens in any browser, offline. Print or save as PDF uses your device's print sheet.</p>
    <div class="book">${chapters}</div>`;
}

let lastRouteKey = "";
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
  else if (route.name === "plan") body = planView();
  else if (route.name === "review") body = reviewView(route.id);
  else if (route.name === "book") body = bookView();
  const navKey = route.name === "track"
    ? `#/track/${route.id}`
    : route.name === "labs" || route.name === "lab"
      ? "#/labs"
      : route.name === "review" || route.name === "book" || route.name === "plan"
        ? (route.name === "plan" ? "#/plan" : "#/review")
        : routeKey;
  app.innerHTML = `${header(navKey)}${`<main class="wrap ${route.name === "book" ? "wrap-book" : ""}">${body}</main>`}`;
  cleanup = bind(route);
  if (route.name === "book") typeset(app.querySelector(".book"));
  if (routeKey !== lastRouteKey) window.scrollTo(0, 0);
  lastRouteKey = routeKey;
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
        [lecture.title, lecture.chapter, lecture.summary, ...(lecture.covers || []), ...(lecture.outcomes || []), ...(lecture.sheet?.lines || []), lecture.drill?.q, citationHaystack(lecture)]
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
      const drillHost = app.querySelector("[data-drill]");
      let picks = [];
      let submitted = false;
      let drillOpen = false;
      const paintQuiz = () => {
        quiz.innerHTML = quizHtml(lecture, picks, submitted);
      };
      const paintDrill = () => {
        if (drillHost) drillHost.innerHTML = drillHtml(lecture, drillOpen);
      };
      paintQuiz();
      paintDrill();
      typeset(app.querySelector(".study-sheet"));
      drillHost?.addEventListener("click", (event) => {
        if (event.target.closest("[data-drill]")) {
          drillOpen = true;
          paintDrill();
        }
      });
      const noteBox = app.querySelector("[data-note]");
      const noteResult = app.querySelector("[data-note-result]");
      let noteTimer = 0;
      noteBox?.addEventListener("input", () => {
        clearTimeout(noteTimer);
        noteTimer = setTimeout(() => {
          const text = noteBox.value.trim();
          if (text) progress.notes[lecture.id] = text;
          else delete progress.notes[lecture.id];
          saveProgress(progress);
        }, 300);
      });
      app.querySelector("[data-check-note]")?.addEventListener("click", () => {
        if (noteResult) noteResult.innerHTML = coverageHtml(lecture, noteBox?.value || "");
      });
      app.querySelector("[data-deck]")?.addEventListener("click", (event) => {
        const button = event.currentTarget;
        const on = !progress.decks[lecture.id];
        if (on) progress.decks[lecture.id] = true;
        else delete progress.decks[lecture.id];
        saveProgress(progress);
        button.textContent = on ? "In your flashcard deck" : "Add to flashcards";
        button.setAttribute("aria-pressed", on ? "true" : "false");
      });
      stops.push(() => clearTimeout(noteTimer));
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
          if (score.passed) {
            progress.done[lecture.id] = Date.now();
            progress.decks[lecture.id] = true;
            const deckBtn = app.querySelector("[data-deck]");
            if (deckBtn) {
              deckBtn.textContent = "In your flashcard deck";
              deckBtn.setAttribute("aria-pressed", "true");
            }
          } else {
            delete progress.done[lecture.id];
          }
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

  if (route.name === "review") {
    const scope = scopeFor(route.id);
    const host = app.querySelector("[data-flash]");
    let queue = dueCards(scope.cards, progress);
    let flipped = false;
    let done = 0;
    const refreshStats = () => {
      const stats = deckStats(scope.cards, progress);
      for (const [key, value] of Object.entries(stats)) {
        const cell = app.querySelector(`[data-stat="${key}"]`);
        if (cell) cell.textContent = value;
      }
    };
    const paint = () => {
      if (!host) return;
      host.innerHTML = queue.length
        ? cardHtml(queue[0], flipped, queue.length, done)
        : emptyDeckHtml(scope, deckStats(scope.cards, progress), done);
      typeset(host);
    };
    const grade = (good) => {
      const card = queue[0];
      if (!card) return;
      progress.cards[card.id] = rate(progress.cards[card.id], good);
      progress.log[dayKey()] = (progress.log[dayKey()] || 0) + 1;
      saveProgress(progress);
      queue.shift();
      if (!good) queue.push(card);
      flipped = false;
      done += 1;
      refreshStats();
      paint();
    };
    const flip = () => {
      if (!queue.length || flipped) return;
      flipped = true;
      paint();
    };
    paint();
    app.addEventListener("click", onReviewClick);
    function onReviewClick(event) {
      if (event.target.closest("[data-flip]")) flip();
      else if (event.target.closest("[data-rate]")) grade(event.target.closest("[data-rate]").dataset.rate === "good");
      else if (event.target.closest("[data-read]")) {
        const card = queue[0];
        if (!card) return;
        const text = flipped ? (Array.isArray(card.back) ? card.back.join(". ") : card.back) : card.front;
        narrator.cancel();
        narrator.speak(text.replace(/\$[^$]*\$/g, "formula"), { lang: "en", rate: progress.rate });
      } else if (event.target.closest("[data-add-scope]")) {
        scope.lectureIds.forEach((lectureId) => { progress.decks[lectureId] = true; });
        saveProgress(progress);
        queue = dueCards(scope.cards, progress);
        flipped = false;
        event.target.closest("[data-add-scope]").replaceWith(Object.assign(document.createElement("span"), { className: "meta", textContent: "Every lecture here is in your deck." }));
        refreshStats();
        paint();
      } else if (event.target.closest("[data-ahead]")) {
        queue = aheadCards(scope.cards, progress, 10);
        flipped = false;
        paint();
      }
    }
    const onKey = (event) => {
      const tag = document.activeElement?.tagName;
      if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
      if (event.key === " " || event.code === "Space") {
        event.preventDefault();
        flip();
      } else if (flipped && event.key === "1") grade(false);
      else if (flipped && event.key === "2") grade(true);
    };
    window.addEventListener("keydown", onKey);
    stops.push(() => {
      app.removeEventListener("click", onReviewClick);
      window.removeEventListener("keydown", onKey);
    });
  }

  if (route.name === "book") {
    const status = app.querySelector("[data-book-status]");
    const say = (text) => { if (status) status.textContent = text; };
    const bookEl = app.querySelector(".book");
    const fileOptions = () => {
      const stats = percent();
      return { title: "The study book", subtitle: `${stats.passed} of ${stats.total} checkpoints passed` };
    };
    app.querySelector("[data-print]")?.addEventListener("click", () => {
      const how = printBook("Self-taught Bootcamp study book");
      say(how === "native" ? "Opening the print sheet. Choose Save as PDF to keep a copy." : "Opening the print dialog. Choose Save as PDF as the destination to keep a copy.");
    });
    app.querySelector("[data-save-book]")?.addEventListener("click", async (event) => {
      const button = event.currentTarget;
      button.disabled = true;
      say("Preparing the book…");
      try {
        const how = await saveBook(bookEl, fileOptions());
        say(how === "native" ? "Choose where to save the book. It opens in any browser, offline." : "The book is downloading as one HTML file. Open it in any browser, offline.");
      } catch {
        say("The book could not be saved. Try Print or save as PDF instead.");
      } finally {
        button.disabled = false;
      }
    });
    if (typeof window !== "undefined") {
      window.__bootcampBookSaved = (ok) => say(ok ? "Saved. The book is in the folder you chose." : "Saving was cancelled.");
      stops.push(() => { delete window.__bootcampBookSaved; });
    }
  }

  return () => {
    stops.forEach((stop) => stop());
    narrator.cancel();
  };
}

window.addEventListener("hashchange", render);
narrator.ready();
render();
