/** Text-to-speech: English and Urdu only. Uses native Android bridge when available. */

let voicesCache = [];
let voicesReady = false;

function loadVoices() {
  if (!window.speechSynthesis) return;
  voicesCache = window.speechSynthesis.getVoices().filter((v) => {
    const lang = (v.lang || "").toLowerCase();
    return lang.startsWith("en") || lang.startsWith("ur");
  });
  voicesReady = voicesCache.length > 0;
}

if (typeof window !== "undefined" && window.speechSynthesis) {
  loadVoices();
  window.speechSynthesis.onvoiceschanged = loadVoices;
}

function pickVoice(langPrefix) {
  const pref = langPrefix.toLowerCase();
  const exact = voicesCache.find((v) => v.lang.toLowerCase().startsWith(pref));
  if (exact) return exact;
  if (pref.startsWith("ur")) {
    return voicesCache.find((v) => v.lang.toLowerCase().startsWith("ur"));
  }
  return voicesCache.find((v) => v.lang.toLowerCase().startsWith("en"));
}

function nativeBridgeReady() {
  try {
    return (
      window.AndroidLecture &&
      typeof window.AndroidLecture.isTtsReady === "function" &&
      window.AndroidLecture.isTtsReady()
    );
  } catch {
    return false;
  }
}

class LectureTTS {
  constructor({ onStart, onEnd, onStatus }) {
    this.onStart = onStart || (() => {});
    this.onEnd = onEnd || (() => {});
    this.onStatus = onStatus || (() => {});
    this.running = false;
    this.currentLang = "en";
    this._nativePendingEnd = null;
  }

  setLanguage(lang) {
    this.currentLang = lang === "ur" ? "ur" : "en";
  }

  stop() {
    if (nativeBridgeReady()) {
      try {
        window.AndroidLecture.stopSpeak();
      } catch {
        /* ignore */
      }
    }
    if (window.speechSynthesis) {
      window.speechSynthesis.cancel();
    }
    this.running = false;
    this._nativePendingEnd = null;
    window.__lectureNativeTtsDone = null;
    this.onEnd();
    this.onStatus("Ready");
  }

  speak(text, langOverride) {
    if (!text?.trim()) {
      this.onStatus("No narration text for this language.");
      return false;
    }

    const lang = langOverride || this.currentLang;
    const prefix = lang === "ur" ? "ur" : "en";

    if (nativeBridgeReady()) {
      try {
        window.__lectureNativeTtsDone = (hadError) => {
          this.running = false;
          this.onEnd();
          this.onStatus(hadError ? "Speech error — try again." : "Ready");
          window.__lectureNativeTtsDone = null;
        };
        this.running = true;
        this.onStart(lang);
        this.onStatus(`Speaking (${lang === "ur" ? "Urdu" : "English"})…`);
        window.AndroidLecture.speak(text.trim(), prefix);
        return true;
      } catch (e) {
        this.onStatus("Native TTS failed: " + String(e));
      }
    }

    if (!window.speechSynthesis) {
      this.onStatus("Speech not supported. Use the Android app build with TTS installed.");
      return false;
    }
    if (!voicesReady) loadVoices();

    const voice = pickVoice(prefix);
    if (!voice && prefix === "ur") {
      this.onStatus("Urdu voice not installed — try English or add Urdu TTS on your device.");
      return false;
    }

    window.speechSynthesis.cancel();
    this.running = false;
    const utter = new SpeechSynthesisUtterance(text.trim());
    utter.voice = voice || null;
    utter.lang = voice?.lang || (prefix === "ur" ? "ur-PK" : "en-US");
    utter.rate = lang === "ur" ? 0.88 : 0.92;
    utter.pitch = 1;

    utter.onstart = () => {
      this.running = true;
      this.onStart(lang);
      this.onStatus(`Speaking (${lang === "ur" ? "Urdu" : "English"})…`);
    };
    utter.onend = () => {
      this.running = false;
      this.onEnd();
      this.onStatus("Ready");
    };
    utter.onerror = () => {
      this.running = false;
      this.onEnd();
      this.onStatus("Speech error — try again.");
    };

    window.speechSynthesis.speak(utter);
    return true;
  }

  speakScene(scene, lang) {
    const l = lang === "ur" ? "ur" : "en";
    const text =
      l === "ur"
        ? scene.ttsUrdu || scene.urdu
        : scene.ttsEnglish || scene.english;
    return this.speak(text, l);
  }
}

window.LectureTTS = LectureTTS;
