import { lectures, tracks, flatIds, lectureById } from "./js/curriculum.js";
import { SCENE_TYPES } from "./js/scenes.js";
import { beatDurationMs, speechChunks } from "./js/narrator.js";
import { gradeQuiz } from "./js/progress.js";

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

if (errors.length) {
  console.error(errors.join("\n"));
  process.exit(1);
}
console.log(`ok ${lectures.length} lectures, ${lectures.reduce((n, lecture) => n + lecture.beats.length, 0)} beats, scenes ${used.size}`);
