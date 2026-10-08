(function (root) {
  let speaking = false;
  let timer = 0;

  function hasAndroid() {
    return !!(root.AndroidTts && typeof root.AndroidTts.speakUrdish === "function");
  }

  function setNow(text, lang) {
    const el = document.getElementById("tts-now");
    if (!el) return;
    el.textContent = text || "";
    el.classList.toggle("ur", lang === "ur");
    el.lang = lang === "ur" ? "ur" : "en";
  }

  function setLive(on) {
    speaking = on;
    document.querySelectorAll(".speak-btn").forEach((btn) => {
      btn.classList.toggle("live", on);
      btn.textContent = on ? "Stop voice" : "Urdish TTS";
    });
  }

  function stop() {
    speaking = false;
    clearTimeout(timer);
    if (hasAndroid()) {
      try { AndroidTts.stop(); } catch (e) {}
    } else if (root.speechSynthesis) {
      speechSynthesis.cancel();
    }
    setLive(false);
    setNow("Voice idle", "en");
  }

  function speakBrowser(segments) {
    if (!root.speechSynthesis) return;
    speechSynthesis.cancel();
    segments.forEach((seg, index) => {
      const u = new SpeechSynthesisUtterance(seg.t);
      u.lang = seg.l === "ur" ? "ur-PK" : "en-US";
      u.rate = 0.94;
      u.onstart = () => setNow(seg.t, seg.l);
      if (index === 0) u.onerror = () => setLive(false);
      if (index === segments.length - 1) u.onend = () => setLive(false);
      speechSynthesis.speak(u);
    });
  }

  function speakSegments(segments) {
    if (!segments || !segments.length) return;
    stop();
    speaking = true;
    setLive(true);
    setNow(segments[0].t, segments[0].l);
    if (hasAndroid()) {
      AndroidTts.speakUrdish(JSON.stringify(segments));
      return;
    }
    speakBrowser(segments);
  }

  function speakTopic(topic) {
    const segs = root.Urdish.mixUrdish(topic.speakEn, topic.speakUr);
    speakSegments(segs);
  }

  root.onAndroidTtsEvent = function (kind, payload) {
    if (kind === "start") {
      try {
        const data = JSON.parse(payload || "{}");
        setNow(data.t || "", data.l || "en");
      } catch (e) {
        setNow(String(payload || ""), "en");
      }
    }
    if (kind === "done" || kind === "error") setLive(false);
    if (kind === "issue") setNow(String(payload || "Voice issue"), "en");
  };

  root.TtsBridge = { speakSegments, speakTopic, stop, setLive, hasAndroid };
})(typeof window !== "undefined" ? window : globalThis);
