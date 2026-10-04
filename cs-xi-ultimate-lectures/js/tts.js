/**
 * Text-to-speech: English and Urdu only (no other locales).
 */

const ALLOWED = new Set(["en", "ur"]);

const LOCALE_MAP = {
  en: ["en-US", "en-GB", "en"],
  ur: ["ur-PK", "ur-IN", "ur"]
};

export class LectureTTS {
  constructor({ onStart, onEnd, onBoundary }) {
    this.onStart = onStart;
    this.onEnd = onEnd;
    this.onBoundary = onBoundary;
    this.synth = window.speechSynthesis;
    this.voices = [];
    this.speaking = false;
    this._loadVoices();
    if (this.synth) {
      this.synth.onvoiceschanged = () => this._loadVoices();
    }
  }

  _loadVoices() {
    if (!this.synth) return;
    this.voices = this.synth.getVoices();
  }

  _pickVoice(lang) {
    if (!ALLOWED.has(lang)) return null;
    const prefs = LOCALE_MAP[lang];
    for (const code of prefs) {
      const v = this.voices.find((voice) => voice.lang && voice.lang.toLowerCase().startsWith(code.toLowerCase()));
      if (v) return v;
    }
    return this.voices.find((v) => prefs.some((p) => v.lang?.toLowerCase().includes(p.split("-")[0]))) || null;
  }

  get isSupported() {
    return !!this.synth;
  }

  stop() {
    if (!this.synth) return;
    this.synth.cancel();
    this.speaking = false;
    this.onEnd?.();
  }

  speak(text, lang) {
    if (!this.synth || !text?.trim()) return false;
    if (!ALLOWED.has(lang)) {
      console.warn("TTS language not allowed:", lang);
      return false;
    }

    this.stop();

    const utter = new SpeechSynthesisUtterance(text.trim());
    const voice = this._pickVoice(lang);
    if (voice) utter.voice = voice;
    utter.lang = lang === "ur" ? "ur-PK" : "en-US";
    utter.rate = lang === "ur" ? 0.88 : 0.92;
    utter.pitch = 1;

    utter.onstart = () => {
      this.speaking = true;
      this.onStart?.();
    };
    utter.onend = () => {
      this.speaking = false;
      this.onEnd?.();
    };
    utter.onerror = () => {
      this.speaking = false;
      this.onEnd?.();
    };
    utter.onboundary = (e) => {
      this.onBoundary?.(e.charIndex, text);
    };

    this.synth.speak(utter);
    return true;
  }
}
