/** Urdu / Urdish narration only. Native Android TTS preferred. */

const URDU_LOCALES = ["ur-PK", "ur-IN", "ur"];

class LectureTTS {
  constructor({ onStart, onEnd, onBoundary }) {
    this.onStart = onStart;
    this.onEnd = onEnd;
    this.onBoundary = onBoundary;
    this.synth = window.speechSynthesis;
    this.voices = [];
    this.speaking = false;
    this._nativeEnd = null;
    this._loadVoices();
    if (this.synth) {
      this.synth.onvoiceschanged = () => this._loadVoices();
    }
  }

  _loadVoices() {
    if (!this.synth) return;
    this.voices = this.synth.getVoices();
  }

  _pickUrduVoice() {
    for (const code of URDU_LOCALES) {
      const v = this.voices.find(
        (voice) => voice.lang && voice.lang.toLowerCase().startsWith(code.toLowerCase())
      );
      if (v) return v;
    }
    return this.voices.find((v) => v.lang?.toLowerCase().startsWith("ur")) || null;
  }

  get isSupported() {
    return !!this.synth || typeof window.AndroidLecture !== "undefined";
  }

  get usesNative() {
    return typeof window.AndroidLecture !== "undefined" && !!window.AndroidLecture.speak;
  }

  stop() {
    if (this._nativeEnd) {
      window.removeEventListener("native-tts-end", this._nativeEnd);
      this._nativeEnd = null;
    }
    if (this.usesNative) {
      window.AndroidLecture.stop();
    }
    this.synth?.cancel();
    this.speaking = false;
    this.onEnd?.();
  }

  speak(text) {
    const clean = (text || "").replace(/<[^>]+>/g, " ").replace(/\s+/g, " ").trim();
    if (!clean) return false;

    if (this.usesNative) {
      this.stop();
      const ok = window.AndroidLecture.speak(clean, "ur");
      if (ok) {
        this.speaking = true;
        this.onStart?.();
        this.onBoundary?.(0, clean);
        this._nativeEnd = () => {
          window.removeEventListener("native-tts-end", this._nativeEnd);
          this._nativeEnd = null;
          this.speaking = false;
          this.onEnd?.();
        };
        window.addEventListener("native-tts-end", this._nativeEnd);
      }
      return !!ok;
    }

    if (!this.synth) return false;
    this.stop();
    const utter = new SpeechSynthesisUtterance(clean);
    const voice = this._pickUrduVoice();
    if (voice) utter.voice = voice;
    utter.lang = "ur-PK";
    utter.rate = 0.88;
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
    utter.onboundary = (e) => this.onBoundary?.(e.charIndex, clean);
    this.synth.speak(utter);
    return true;
  }
}

window.LectureTTS = LectureTTS;
