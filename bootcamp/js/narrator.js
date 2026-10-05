/** Spoken lecture engine. Uses the browser speech API, with a timed caption fallback. */

export function beatDurationMs(text, rate = 1) {
  const words = String(text || "")
    .trim()
    .split(/\s+/)
    .filter(Boolean).length;
  const safeRate = Math.min(1.6, Math.max(0.7, Number(rate) || 1));
  return Math.max(2400, Math.round((words / (2.35 * safeRate)) * 1000));
}

export function speechChunks(text) {
  const clean = String(text || "").replace(/\s+/g, " ").trim();
  if (!clean) return [];
  const parts = clean.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [clean];
  const chunks = [];
  let buf = "";
  for (const part of parts) {
    const piece = part.trim();
    if (!piece) continue;
    if ((buf + " " + piece).trim().split(/\s+/).length > 32 && buf) {
      chunks.push(buf.trim());
      buf = piece;
    } else {
      buf = `${buf} ${piece}`.trim();
    }
  }
  if (buf) chunks.push(buf.trim());
  return chunks;
}

function nativeVoice() {
  if (typeof window === "undefined" || !window.BootcampVoice) return null;
  return typeof window.BootcampVoice.speak === "function" ? window.BootcampVoice : null;
}

function pickVoice(voices, lang) {
  const list = (voices || []).filter((voice) => voice && voice.lang);
  if (lang === "ur") {
    return list.find((voice) => /^ur([-_]|$)/i.test(voice.lang)) || null;
  }
  return (
    list.find((voice) => /en[-_]US/i.test(voice.lang) && /natural|google|samantha|aria|jenny/i.test(voice.name)) ||
    list.find((voice) => /en[-_]GB/i.test(voice.lang) && /natural|google/i.test(voice.name)) ||
    list.find((voice) => /en[-_]US/i.test(voice.lang)) ||
    list.find((voice) => /^en([-_]|$)/i.test(voice.lang)) ||
    null
  );
}

export class Narrator {
  constructor() {
    this.synth = typeof window !== "undefined" ? window.speechSynthesis : null;
    this.voices = [];
    this.token = 0;
    this._ready = this._loadVoices();
  }

  async _loadVoices() {
    if (!this.synth) return [];
    const existing = this.synth.getVoices();
    if (existing.length) {
      this.voices = existing;
      return existing;
    }
    await new Promise((resolve) => {
      const finish = () => {
        this.voices = this.synth.getVoices();
        resolve();
      };
      this.synth.addEventListener("voiceschanged", finish, { once: true });
      setTimeout(finish, 900);
    });
    return this.voices;
  }

  async ready() {
    await this._ready;
    if (this.synth) this.voices = this.synth.getVoices();
    return this.voices;
  }

  supports(lang) {
    const native = nativeVoice();
    if (native && typeof native.hasLanguage === "function") {
      try {
        return Boolean(native.hasLanguage(lang === "ur" ? "ur" : "en"));
      } catch {
        return false;
      }
    }
    return Boolean(pickVoice(this.voices, lang));
  }

  cancel() {
    this.token += 1;
    const native = nativeVoice();
    if (native && typeof native.stop === "function") {
      try {
        native.stop();
      } catch {
        /* ignore a bridge that is not ready */
      }
    }
    if (this.synth) {
      try {
        this.synth.cancel();
      } catch {
        /* ignore engines that throw on cancel */
      }
    }
  }

  /**
   * Speak `text`. Resolves with "end", "timer", or "cancel".
   * Pass `fallbackText` (English) when `lang` is Urdu so a missing Urdu voice
   * still reads the lecture aloud.
   */
  speak(text, options = {}) {
    if (nativeVoice()) return this.speakNative(text, options);
    return this.speakWeb(text, options);
  }

  speakNative(text, { lang = "en", rate = 1, fallbackText = "", onstart, onfallback } = {}) {
    this.token += 1;
    const token = this.token;
    const bridge = nativeVoice();
    try {
      bridge.stop();
    } catch {
      /* the engine may already be idle */
    }
    let spoken = String(text || "").trim();
    let speakLang = lang === "ur" ? "ur" : "en";
    if (!spoken) return Promise.resolve("end");
    let urduMissing = false;
    try {
      urduMissing = lang === "ur" && typeof bridge.hasLanguage === "function" && !bridge.hasLanguage("ur");
    } catch {
      urduMissing = lang === "ur";
    }
    if (urduMissing) {
      onfallback?.("no-urdu-voice");
      if (fallbackText && fallbackText.trim()) {
        spoken = fallbackText.trim();
        speakLang = "en";
      }
    }

    return new Promise((resolve) => {
      let settled = false;
      let hang = 0;
      const finish = (reason) => {
        if (settled || token !== this.token) return;
        settled = true;
        clearTimeout(hang);
        resolve(reason);
      };
      window.__bootcampOnStart = (id) => {
        if (String(id) !== String(token)) return;
        onstart?.();
      };
      window.__bootcampOnDone = (id) => {
        if (String(id) !== String(token)) return;
        finish("end");
      };
      hang = setTimeout(() => finish("end"), Math.max(25000, beatDurationMs(spoken, rate) + 8000));
      let accepted = false;
      try {
        accepted = bridge.speak(String(token), spoken, speakLang, Number(rate) || 1) !== false;
      } catch {
        accepted = false;
      }
      if (!accepted) {
        clearTimeout(hang);
        onfallback?.("no-engine");
        setTimeout(() => finish("timer"), beatDurationMs(spoken, rate));
      }
    });
  }

  speakWeb(text, { lang = "en", rate = 1, fallbackText = "", onstart, onfallback } = {}) {
    const wasSpeaking = Boolean(this.synth?.speaking);
    if (wasSpeaking) this.cancel();
    else this.token += 1;
    const token = this.token;
    let spoken = String(text || "").trim();
    let speakLang = lang === "ur" ? "ur-PK" : "en-US";
    let voice = pickVoice(this.voices, lang);

    if (!spoken) return Promise.resolve("end");

    if (lang === "ur" && !voice) {
      onfallback?.("no-urdu-voice");
      if (fallbackText && fallbackText.trim()) {
        spoken = fallbackText.trim();
        speakLang = "en-US";
        voice = pickVoice(this.voices, "en");
      }
    }

    const finishers = [];
    let settled = false;
    const finish = (reason) => {
      if (settled || token !== this.token) return null;
      settled = true;
      finishers.forEach((fn) => fn());
      return reason;
    };

    return new Promise((resolve) => {
      const done = (reason) => {
        const result = finish(reason);
        if (result) resolve(result);
      };

      const timed = () => {
        onfallback?.("no-engine");
        const timer = setTimeout(() => done("timer"), beatDurationMs(spoken, rate));
        finishers.push(() => clearTimeout(timer));
      };

      if (!this.synth) {
        timed();
        return;
      }

      const chunks = speechChunks(spoken);
      let index = 0;
      let started = false;

      const startWatch = setTimeout(() => {
        if (!started && token === this.token) {
          try {
            this.synth.cancel();
          } catch {
            /* ignore */
          }
          timed();
        }
      }, 900);
      finishers.push(() => clearTimeout(startWatch));

      const hang = setTimeout(() => {
        if (!settled) done(started ? "end" : "timer");
      }, Math.max(25000, beatDurationMs(spoken, rate) + 10000));
      finishers.push(() => clearTimeout(hang));

      const speakNext = () => {
        if (token !== this.token) {
          done("cancel");
          return;
        }
        if (index >= chunks.length) {
          done("end");
          return;
        }
        const utterance = new SpeechSynthesisUtterance(chunks[index]);
        utterance.lang = speakLang;
        utterance.rate = Math.min(1.6, Math.max(0.7, Number(rate) || 1));
        utterance.pitch = 1;
        if (voice) utterance.voice = voice;
        utterance.onstart = () => {
          started = true;
          if (index === 0) onstart?.();
        };
        utterance.onend = () => {
          index += 1;
          speakNext();
        };
        utterance.onerror = () => {
          if (!started) {
            timed();
            return;
          }
          index += 1;
          speakNext();
        };
        try {
          this.synth.speak(utterance);
        } catch {
          timed();
        }
      };

      // Chrome drops an utterance that starts in the same turn as cancel().
      // The first play of a lecture stays synchronous so the user gesture still counts.
      if (wasSpeaking) {
        const kick = setTimeout(speakNext, 50);
        finishers.push(() => clearTimeout(kick));
      } else {
        speakNext();
      }
    });
  }
}
