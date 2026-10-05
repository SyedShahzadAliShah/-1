import { xiLectures } from "./lectures/xi.js";
import { xiiLectures } from "./lectures/xii.js";
import { applyDepth } from "./lectures/depth.js";
import { applyCitations } from "./citations.js";

export const lectures = [...xiLectures, ...xiiLectures];
applyDepth(lectures);
applyCitations(lectures);

export const tracks = [
  {
    id: "xi",
    grade: "XI",
    title: "Computer Science XI",
    edition: "Sindh Computer Science, 2026",
    blurb: "Digital systems, computational thinking, Python, databases, impacts, and a careful digital inquiry.",
    chapters: [
      { code: "1", title: "Computer Systems", lectureIds: ["xi-digital", "xi-signals", "xi-boolean", "xi-gates", "xi-kmap", "xi-sdlc", "xi-osi"] },
      { code: "2", title: "Computational Thinking", lectureIds: ["xi-ct", "xi-sort", "xi-search", "xi-eval"] },
      { code: "3", title: "Programming Fundamentals", lectureIds: ["xi-python", "xi-control", "xi-debug"] },
      { code: "4", title: "Data and Analysis", lectureIds: ["xi-db", "xi-er", "xi-queries"] },
      { code: "5", title: "Applications and Impacts", lectureIds: ["xi-impacts"] },
      { code: "6", title: "Digital Literacy", lectureIds: ["xi-literacy"] },
    ],
  },
  {
    id: "xii",
    grade: "XII",
    title: "Computer Science XII",
    edition: "Sindh Computer Science, 2024 / 2025–27",
    blurb: "HCI, algorithms and data structures, Python collections and files, analysis, security, and a venture.",
    chapters: [
      { code: "1", title: "Human Computer Interaction", lectureIds: ["xii-hci", "xii-design"] },
      { code: "2", title: "Algorithms and Data Structures", lectureIds: ["xii-correct", "xii-linear", "xii-nonlinear"] },
      { code: "3", title: "Programming", lectureIds: ["xii-structs", "xii-files"] },
      { code: "4", title: "Data Analysis", lectureIds: ["xii-pandas", "xii-stats"] },
      { code: "5", title: "AI, Security, and Equity", lectureIds: ["xii-ml", "xii-security"] },
      { code: "6", title: "Digital Entrepreneurship", lectureIds: ["xii-venture", "xii-mvp"] },
    ],
  },
];

const byId = new Map(lectures.map((lecture) => [lecture.id, lecture]));

export function lectureById(id) {
  return byId.get(id) || null;
}

export function flatIds() {
  return tracks.flatMap((track) => track.chapters.flatMap((chapter) => chapter.lectureIds));
}

export function neighbors(id) {
  const ids = flatIds();
  const index = ids.indexOf(id);
  return {
    prev: index > 0 ? ids[index - 1] : null,
    next: index >= 0 && index < ids.length - 1 ? ids[index + 1] : null,
    index,
    total: ids.length,
  };
}

export function minutesFor(lecture) {
  const words = (lecture?.beats || []).reduce((count, beat) => count + String(beat.say || "").split(/\s+/).filter(Boolean).length, 0);
  return Math.max(2, Math.round(words / 130));
}
