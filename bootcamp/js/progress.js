const KEY = "roshni-bootcamp-progress-v1";

export function loadProgress() {
  try {
    const raw = localStorage.getItem(KEY);
    const data = raw ? JSON.parse(raw) : {};
    return {
      done: data.done || {},
      scores: data.scores || {},
      lastId: data.lastId || "",
      lang: data.lang === "ur" ? "ur" : "en",
      rate: [0.85, 1, 1.2].includes(data.rate) ? data.rate : 1,
    };
  } catch {
    return { done: {}, scores: {}, lastId: "", lang: "en", rate: 1 };
  }
}

export function saveProgress(progress) {
  localStorage.setItem(KEY, JSON.stringify(progress));
}

export function gradeQuiz(quiz, picks) {
  let correct = 0;
  quiz.forEach((question, index) => {
    if (picks[index] === question.answer) correct += 1;
  });
  const total = quiz.length;
  const passed = total > 0 && correct * 3 >= total * 2;
  return { correct, total, passed };
}
