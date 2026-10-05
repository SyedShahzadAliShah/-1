import { mountScene } from "./scenes.js";
import { beatDurationMs } from "./narrator.js";
import { ROLE_LABEL } from "./lectures/mastery.js";

export function captionOf(beat, lang) {
  if (lang === "ur") return beat.captionUr || beat.sayUr || beat.caption || beat.say;
  return beat.caption || beat.say;
}

export function speechOf(beat, lang) {
  if (lang === "ur") return beat.sayUr || beat.say;
  return beat.say;
}

export function createPlayer(root, lecture, options) {
  const beats = lecture.beats || [];
  let beat = Math.min(options.startBeat || 0, Math.max(0, beats.length - 1));
  let playing = false;
  let stopScene = () => {};
  let run = 0;
  const narrator = options.narrator;

  const stage = root.querySelector(".stage");
  const host = root.querySelector(".scene-host");
  const caption = root.querySelector(".caption");
  const note = root.querySelector(".voice-note");
  const playBtn = root.querySelector("[data-act=play]");
  const dots = [...root.querySelectorAll("[data-beat]")];

  function renderBeat() {
    stopScene();
    const current = beats[beat];
    if (!current) return;
    stage.classList.remove("swap");
    void stage.offsetWidth;
    stage.classList.add("swap");
    stopScene = mountScene(host, current.scene || { type: "board", title: current.title || "Lecture" });
    caption.textContent = captionOf(current, options.lang());
    dots.forEach((dot, index) => {
      dot.setAttribute("aria-current", index === beat ? "true" : "false");
    });
    const counter = root.querySelector(".beat-count");
    if (counter) counter.textContent = `${beat + 1} / ${beats.length}`;
    const phase = root.querySelector(".beat-phase");
    if (phase) phase.textContent = ROLE_LABEL[current.role] || current.title || "Idea";
    root.querySelectorAll("[data-phase]").forEach((item) => {
      item.setAttribute("aria-current", item.dataset.phase === (current.role || "idea") ? "true" : "false");
    });
    options.onBeat?.(beat);
  }

  function setPlayingUi() {
    playBtn.textContent = playing ? "Pause" : "Play lecture";
    playBtn.setAttribute("aria-pressed", playing ? "true" : "false");
    stage.classList.toggle("is-speaking", playing);
  }

  function play() {
    if (!beats.length) return;
    playing = true;
    const token = ++run;
    setPlayingUi();
    const current = beats[beat];
    const lang = options.lang();
    const text = speechOf(current, lang);
    const english = current.say;
    note.textContent = "";
    narrator.speak(text, {
      lang,
      rate: options.rate(),
      fallbackText: english,
      onstart: () => {
        if (lang === "ur" && narrator.supports("ur")) note.textContent = "";
      },
      onfallback: (reason) => {
        if (token !== run) return;
        if (reason === "no-urdu-voice") {
          note.textContent = "No Urdu voice on this device. The English lecture is read aloud, and the Urdu line stays on screen.";
        } else if (reason === "no-engine") {
          const ms = beatDurationMs(text, options.rate());
          note.textContent = `This browser has no speech engine. Captions advance on a timer (about ${Math.round(ms / 1000)}s this beat).`;
        }
      },
    }).then((reason) => {
      if (token !== run || !playing) return;
      if (reason === "cancel") return;
      if (beat < beats.length - 1) {
        beat += 1;
        renderBeat();
        play();
      } else {
        playing = false;
        setPlayingUi();
        options.onFinished?.();
      }
    });
  }

  function pause() {
    playing = false;
    run += 1;
    narrator.cancel();
    setPlayingUi();
  }

  function seek(index) {
    beat = Math.max(0, Math.min(beats.length - 1, index));
    renderBeat();
    if (playing) play();
  }

  function onClick(event) {
    const act = event.target.closest("[data-act]")?.dataset.act;
    if (!act) return;
    if (act === "play") {
      if (playing) pause();
      else play();
    } else if (act === "prev") {
      seek(beat - 1);
    } else if (act === "next") {
      seek(beat + 1);
    } else if (act === "beat") {
      seek(Number(event.target.dataset.beat));
    }
  }

  function onKey(event) {
    const tag = document.activeElement?.tagName;
    if (tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT") return;
    if (event.key === " " || event.code === "Space") {
      event.preventDefault();
      if (playing) pause();
      else play();
    } else if (event.key === "ArrowRight") {
      seek(beat + 1);
    } else if (event.key === "ArrowLeft") {
      seek(beat - 1);
    }
  }

  root.addEventListener("click", onClick);
  window.addEventListener("keydown", onKey);
  renderBeat();
  setPlayingUi();
  if (options.autoplay) play();

  return {
    destroy() {
      pause();
      stopScene();
      root.removeEventListener("click", onClick);
      window.removeEventListener("keydown", onKey);
    },
    seek,
    get beat() {
      return beat;
    },
    get playing() {
      return playing;
    },
  };
}
