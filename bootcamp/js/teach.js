/** Teach Yourself edition: a study plan, a spaced flashcard deck, teach-it-back checks, and the study book. */

import { lectures, tracks, lectureById, minutesFor } from "./curriculum.js";

const DAY = 86400000;
const LAB_FOR = { "xi-gates": "gates", "xi-search": "search", "xii-linear": "structures" };
const LAB_TITLE = { gates: "Logic gate bench", search: "Binary search bench", structures: "Stack and queue bench" };

/** Days until a card returns after each successful recall. */
export const BOX_DAYS = [0, 1, 3, 7, 21];

export function dayKey(ms = Date.now()) {
  return new Date(ms).toISOString().slice(0, 10);
}

export function buildPlan() {
  const sessions = [];
  for (const track of tracks) {
    const trackIds = track.chapters.flatMap((chapter) => chapter.lectureIds);
    for (const chapter of track.chapters) {
      for (let index = 0; index < chapter.lectureIds.length; index += 2) {
        const ids = chapter.lectureIds.slice(index, index + 2);
        const previous = sessions.length ? sessions[sessions.length - 1] : null;
        sessions.push({
          n: sessions.length + 1,
          kind: "learn",
          track: track.id,
          grade: track.grade,
          chapter: chapter.title,
          title: ids.map((id) => lectureById(id)?.title || id).join(" · "),
          lectureIds: ids,
          lab: ids.map((id) => LAB_FOR[id]).find(Boolean) || null,
          reviewIds: previous && previous.kind === "learn" ? previous.lectureIds : [],
          minutes: ids.reduce((total, id) => total + minutesFor(lectureById(id)), 0) + 10,
        });
      }
    }
    sessions.push({
      n: sessions.length + 1,
      kind: "review",
      track: track.id,
      grade: track.grade,
      chapter: "Review",
      title: `Class ${track.grade} review: every card, every trap`,
      lectureIds: [],
      lab: null,
      reviewIds: trackIds,
      minutes: 40,
    });
  }
  return sessions;
}

export function labTitle(id) {
  return LAB_TITLE[id] || "Practice bench";
}

export function buildCards(list = lectures) {
  const cards = [];
  for (const lecture of list) {
    const base = { lectureId: lecture.id, lecture: lecture.title, track: lecture.track };
    if (lecture.drill?.q) {
      cards.push({ ...base, id: `${lecture.id}:drill`, kind: "Drill", front: lecture.drill.q, back: lecture.drill.reveal });
    }
    const trap = lecture.beats.find((beat) => beat.role === "trap");
    if (trap?.scene?.wrong) {
      cards.push({
        ...base,
        id: `${lecture.id}:trap`,
        kind: "Trap",
        front: `A classmate says: “${trap.scene.wrong}” What is the truth?`,
        back: `${trap.scene.right} ${trap.scene.note || ""}`.trim(),
      });
    }
    if (lecture.sheet?.lines?.length) {
      cards.push({
        ...base,
        id: `${lecture.id}:sheet`,
        kind: "Recite",
        front: `Say back the ${lecture.sheet.lines.length} lines of the exam sheet for “${lecture.title}”.`,
        back: lecture.sheet.lines,
      });
    }
    (lecture.quiz || []).forEach((question, index) => {
      cards.push({
        ...base,
        id: `${lecture.id}:q${index}`,
        kind: "Checkpoint",
        front: question.q,
        back: `${question.choices[question.answer]}. ${question.why}`,
      });
    });
  }
  return cards;
}

export function rate(state, good, now = Date.now()) {
  const box = good ? Math.min(BOX_DAYS.length - 1, (state?.box ?? 0) + 1) : 0;
  const due = good ? now + BOX_DAYS[box] * DAY : now + 10 * 60 * 1000;
  return { box, due, seen: (state?.seen || 0) + 1, last: now };
}

export function dueCards(cards, progress, now = Date.now()) {
  return cards
    .filter((card) => progress.decks[card.lectureId])
    .filter((card) => {
      const state = progress.cards[card.id];
      return !state || state.due <= now;
    })
    .sort((a, b) => (progress.cards[a.id]?.due ?? 0) - (progress.cards[b.id]?.due ?? 0));
}

export function aheadCards(cards, progress, limit = 10, now = Date.now()) {
  return cards
    .filter((card) => progress.decks[card.lectureId])
    .filter((card) => (progress.cards[card.id]?.due ?? 0) > now)
    .sort((a, b) => progress.cards[a.id].due - progress.cards[b.id].due)
    .slice(0, limit);
}

export function deckStats(cards, progress, now = Date.now()) {
  const inDeck = cards.filter((card) => progress.decks[card.lectureId]);
  const due = dueCards(cards, progress, now).length;
  const mastered = inDeck.filter((card) => (progress.cards[card.id]?.box ?? 0) >= 3).length;
  const fresh = inDeck.filter((card) => !progress.cards[card.id]).length;
  const next = inDeck
    .map((card) => progress.cards[card.id]?.due)
    .filter((due) => due && due > now)
    .sort((a, b) => a - b)[0];
  return { total: inDeck.length, due, mastered, fresh, next: next || null };
}

export function sessionState(session, progress, cards) {
  if (session.kind === "review") {
    const reviewed = session.reviewIds.filter((id) =>
      cards.some((card) => card.lectureId === id && progress.cards[card.id])
    );
    return {
      done: reviewed.length > 0 && reviewed.length === session.reviewIds.length,
      label: `${reviewed.length} / ${session.reviewIds.length} reviewed`,
    };
  }
  const passed = session.lectureIds.filter((id) => progress.done[id]).length;
  return { done: passed === session.lectureIds.length, label: `${passed} / ${session.lectureIds.length} passed` };
}

const STOP = new Set((
  "the a an and or of to in is are be not it its for with when that this then than only any all one two " +
  "you your they them from into onto on at by as if so do does did can may must still also such like each " +
  "every which what who how more most less same other both just their there here very will would should " +
  "about after before again once never always because while where those these some have has had was were " +
  "been being over under between many much use used using make makes made need needs keep keeps even " +
  "becomes going coming interesting hands talks acts already matters another including part spend down " +
  "taken sits uses meeting allowed versus"
).split(" "));

export function keyTerms(lecture) {
  const trap = lecture.beats?.find((item) => item.role === "trap")?.scene;
  const worked = lecture.beats?.find((item) => item.role === "example")?.scene;
  const text = [
    ...(lecture.sheet?.lines || []),
    lecture.sheet?.sayThis || "",
    trap?.right || "",
    ...(worked?.steps || []).map((step) => step.why || ""),
  ].join(" ").replace(/\$[^$]*\$/g, " ");
  // Acronyms such as AND, CPU, or TCP are the concept names, so they come first and skip the stop list.
  const acronyms = text.match(/\b[A-Z][A-Z0-9]+\b/g) || [];
  const words = text.toLowerCase().match(/[a-z][a-z-]{3,}/g) || [];
  const seen = new Set();
  const out = [];
  for (const word of [...acronyms, ...words]) {
    const key = stem(word.toLowerCase());
    if (seen.has(key) || (STOP.has(word) && word === word.toLowerCase())) continue;
    seen.add(key);
    out.push(word);
  }
  return out.slice(0, 10);
}

function stem(word) {
  const short = word.replace(/(ing|es|ed|s)$/, "");
  return short.length >= 3 ? short : word;
}

// AND, OR, and NOT are ordinary English words too, so they only count in the textbook's capitals.
function mentions(raw, term) {
  if (term !== term.toLowerCase()) {
    const flags = STOP.has(term.toLowerCase()) ? "" : "i";
    return new RegExp(`\\b${term}\\b`, flags).test(raw);
  }
  return raw.toLowerCase().includes(stem(term));
}

export function coverage(text, lecture) {
  const terms = keyTerms(lecture);
  const body = String(text || "");
  const hit = terms.filter((term) => mentions(body, term));
  const missed = terms.filter((term) => !hit.includes(term));
  return { terms, hit, missed, score: terms.length ? hit.length / terms.length : 0 };
}

export function streak(log = {}, now = Date.now()) {
  let days = 0;
  let cursor = now;
  if (!log[dayKey(cursor)]) cursor -= DAY;
  while (log[dayKey(cursor)]) {
    days += 1;
    cursor -= DAY;
  }
  return days;
}

export function hoursUntil(ms, now = Date.now()) {
  return Math.max(1, Math.round((ms - now) / 3600000));
}
