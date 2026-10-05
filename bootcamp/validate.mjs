import { lectures, tracks, flatIds, lectureById } from "./js/curriculum.js";
import { SCENE_TYPES } from "./js/scenes.js";
import { beatDurationMs, speechChunks } from "./js/narrator.js";
import { gradeQuiz } from "./js/progress.js";
import { rich } from "./js/mathtext.js";
import { DIAGRAM_NAMES, chartMarkup, renderDiagram } from "./js/diagrams.js";
import { whiteboardSvg } from "./js/whiteboard.js";
import { depthIds } from "./js/lectures/depth.js";

const errors = [];
const fail = (message) => errors.push(message);

const ids = lectures.map((lecture) => lecture.id);
if (new Set(ids).size !== ids.length) fail("Duplicate lecture ids");

const listed = flatIds();
if (listed.length !== lectures.length) fail(`Track list has ${listed.length} ids, lecture catalog has ${lectures.length}`);
for (const id of listed) {
  if (!lectureById(id)) fail(`Missing lecture ${id}`);
}
for (const lecture of lectures) {
  if (!listed.includes(lecture.id)) fail(`Lecture ${lecture.id} is not on a track`);
  if (!lecture.beats?.length) fail(`${lecture.id} has no beats`);
  if (lecture.quiz?.length !== 3) fail(`${lecture.id} should have 3 quiz items`);
  lecture.beats.forEach((beat, index) => {
    if (!beat.say || !beat.sayUr) fail(`${lecture.id} beat ${index} missing speech`);
    if (!SCENE_TYPES.includes(beat.scene?.type)) fail(`${lecture.id} beat ${index} bad scene ${beat.scene?.type}`);
    const words = beat.say.split(/\s+/).length;
    if (words > 80) fail(`${lecture.id} beat ${index} is long for speech (${words} words)`);
  });
  lecture.quiz.forEach((question, index) => {
    if (!Array.isArray(question.choices) || question.choices.length < 2) fail(`${lecture.id} quiz ${index} choices`);
    if (question.answer < 0 || question.answer >= question.choices.length) fail(`${lecture.id} quiz ${index} answer`);
    if (!question.why) fail(`${lecture.id} quiz ${index} missing why`);
  });
}

const used = new Set(lectures.flatMap((lecture) => lecture.beats.map((beat) => beat.scene.type)));
for (const type of SCENE_TYPES) {
  if (!used.has(type)) fail(`Scene type ${type} is never used`);
}

const many = Array.from({ length: 40 }, (_, index) => `Sentence ${index} is long enough.`).join(" ");
if (speechChunks(many).length < 2) fail("speechChunks split");
if (speechChunks("").length !== 0) fail("speechChunks empty");
if (beatDurationMs("one two three", 1) < 2400) fail("duration floor");

const quiz = lectures[0].quiz;
const good = gradeQuiz(quiz, quiz.map((question) => question.answer));
if (!good.passed || good.correct !== 3) fail("grade all correct");
const bad = gradeQuiz(quiz, [0, 0, 0].map((n, i) => (quiz[i].answer === 0 ? 1 : 0)));
if (bad.passed) fail("grade all wrong should fail");
const two = gradeQuiz(quiz, [quiz[0].answer, quiz[1].answer, quiz[2].answer === 0 ? 1 : 0]);
if (!two.passed || two.correct !== 2) fail("two of three should pass");

if (tracks.length !== 2) fail("expected two tracks");

function walkStrings(value, visit) {
  if (typeof value === "string") visit(value);
  else if (Array.isArray(value)) value.forEach((item) => walkStrings(item, visit));
  else if (value && typeof value === "object") Object.values(value).forEach((item) => walkStrings(item, visit));
}

for (const lecture of lectures) {
  lecture.beats.forEach((beat, index) => {
    if (beat.scene?.type === "diagram" && !DIAGRAM_NAMES.includes(beat.scene.diagram)) {
      fail(`${lecture.id} beat ${index} unknown diagram ${beat.scene?.diagram}`);
    }
    walkStrings(beat.scene, (text) => {
      const marks = text.match(/\$/g);
      if (marks && marks.length % 2 !== 0) fail(`${lecture.id} beat ${index} has unbalanced $`);
    });
  });
}

const rendered = rich("See $E = mc^2$ and $$\\bar{x} = \\sum x / n$$");
if (!rendered.includes("\\(E = mc^2\\)") || !rendered.includes("\\[\\bar{x} = \\sum x / n\\]")) fail("rich math");
if (rich("a < b").includes("<")) fail("rich escapes html");
if (rich("plain").includes("math-inline")) fail("rich plain");
for (const name of DIAGRAM_NAMES) {
  if (!renderDiagram(name).includes("<svg")) fail(`diagram ${name} missing svg`);
}
if (depthIds.length !== lectures.length) fail(`depth beats ${depthIds.length}, lectures ${lectures.length}`);
for (const lecture of lectures) {
  const boards = lecture.beats.filter((beat) => beat.scene?.type === "whiteboard");
  if (boards.length !== 1) fail(`${lecture.id} should have one whiteboard`);
  if (!boards[0]?.scene.ink?.length) fail(`${lecture.id} whiteboard has no ink`);
  if ((lecture.outcomes || []).length < 4) fail(`${lecture.id} missing deeper outcome`);
}
const board = whiteboardSvg([{ t: "box", x: 10, y: 10, w: 40, h: 20, label: "A" }, { t: "arrow", x1: 0, y1: 0, x2: 10, y2: 10 }]);
if (!board.includes("<svg") || !board.includes("pathLength")) fail("whiteboard svg");

for (const kind of ["bar", "line", "pie", "box", "scatter", "hist"]) {
  const markup = chartMarkup({ kind, values: [1, 2], labels: ["a", "b"], points: [{ x: 10, y: 20 }], min: 0, q1: 1, median: 2, q3: 3, max: 4 });
  if (!markup.includes("<svg")) fail(`chart ${kind} missing svg`);
}

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}
console.log(`ok ${lectures.length} lectures, ${lectures.reduce((n, lecture) => n + lecture.beats.length, 0)} beats, scenes ${used.size}`);
