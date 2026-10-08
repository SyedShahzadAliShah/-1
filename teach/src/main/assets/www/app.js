/* Teach Yourself Sketchnotes — flexbox lesson player. */
(function () {
  "use strict";

  var course = null;
  var stack = [{ name: "home" }];
  var voice = localStorage.getItem("tys-voice") || "urdish";
  var rate = Number(localStorage.getItem("tys-rate") || "0.92");
  var speaking = false;
  var toastTimer = 0;

  function esc(value) {
    return String(value == null ? "" : value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function rich(value) {
    var parts = String(value || "").split(/(\\\([\s\S]*?\\\))/g);
    return parts.map(function (part, index) {
      return index % 2 === 1 ? part : esc(part);
    }).join("");
  }

  function speakable(value) {
    return String(value || "")
      .replace(/\\\(|\\\)/g, " ")
      .replace(/\\cdot/g, " dot ")
      .replace(/\\bar\{A\}/g, " A bar ")
      .replace(/\\log/g, " log ")
      .replace(/\\/g, " ")
      .replace(/[{}]/g, "")
      .replace(/\s+/g, " ")
      .trim();
  }

  function seen() {
    try { return JSON.parse(localStorage.getItem("tys-seen") || "[]"); }
    catch (error) { return []; }
  }

  function markSeen(id) {
    var list = seen();
    if (list.indexOf(id) === -1) list.push(id);
    localStorage.setItem("tys-seen", JSON.stringify(list));
    localStorage.setItem("tys-last", id);
  }

  function findLesson(id) {
    var ci, hi, li;
    for (ci = 0; ci < course.classes.length; ci++) {
      var cls = course.classes[ci];
      for (hi = 0; hi < cls.chapters.length; hi++) {
        var chapter = cls.chapters[hi];
        for (li = 0; li < chapter.lessons.length; li++) {
          if (chapter.lessons[li].id === id) {
            return { cls: cls, chapter: chapter, lesson: chapter.lessons[li], index: li };
          }
        }
      }
    }
    return null;
  }

  function lessonCount() {
    var total = 0;
    var golden = 0;
    course.classes.forEach(function (cls) {
      cls.chapters.forEach(function (chapter) {
        total += chapter.lessons.length;
        golden += chapter.lessons.filter(function (lesson) { return lesson.golden; }).length;
      });
    });
    return { total: total, golden: golden };
  }

  function route() {
    return stack[stack.length - 1];
  }

  function go(next) {
    stack.push(next);
    render();
  }

  function showToast(message) {
    var host = document.getElementById("toast");
    if (!host) {
      host = document.createElement("div");
      host.id = "toast";
      host.className = "toast";
      document.body.appendChild(host);
    }
    host.textContent = message;
    host.hidden = false;
    clearTimeout(toastTimer);
    toastTimer = setTimeout(function () { host.hidden = true; }, 4200);
  }

  function modesHtml() {
    return (
      '<div class="modes" role="group" aria-label="Voice language">' +
      modeButton("urdish", "Urdish") +
      modeButton("en", "English") +
      modeButton("ur", "اردو") +
      "</div>"
    );
  }

  function modeButton(id, label) {
    return '<button type="button" data-act="voice" data-mode="' + id + '" aria-pressed="' + (voice === id) + '">' + label + "</button>";
  }

  function homeHtml() {
    var counts = lessonCount();
    var last = localStorage.getItem("tys-last");
    var found = last ? findLesson(last) : null;
    var cards = course.classes.map(function (cls) {
      var lessons = 0;
      cls.chapters.forEach(function (chapter) { lessons += chapter.lessons.length; });
      return (
        '<button type="button" class="class-card" data-act="class" data-id="' + esc(cls.id) + '">' +
        '<span class="badge">' + esc(cls.curriculum) + "</span>" +
        "<strong>" + esc(cls.title) + "</strong>" +
        '<span class="urdu">' + esc(cls.urdu) + "</span>" +
        "<small>" + cls.chapters.length + " chapters · " + lessons + " sketchnotes</small>" +
        "</button>"
      );
    }).join("");
    return (
      '<main class="shell">' +
      '<header class="hero">' +
      '<p class="eyebrow">Sindh computer science</p>' +
      "<h1>Teach Yourself Sketchnotes</h1>" +
      '<p class="lede">Bilingual lecture notes you can hear. Urdish voice reads the Urdu title, the English idea, then the Urdu recap. Formulas use MathJax. Pictures are SVG. The page is flexbox.</p>' +
      '<div class="stats"><span class="badge soft">Version ' + esc(course.version) + "</span>" +
      '<span class="badge">' + counts.total + " lessons</span>" +
      '<span class="badge gold">' + counts.golden + " golden</span></div>" +
      "</header>" +
      modesHtml() +
      '<form class="search" id="search-form"><input type="search" name="q" placeholder="Search gates, Big O, MVP…" aria-label="Search lessons" />' +
      '<button class="solid" type="submit">Search</button></form>' +
      (found ? '<button type="button" class="solid" data-act="lesson" data-id="' + esc(found.lesson.id) + '">Continue · ' + esc(found.lesson.title) + "</button>" : "") +
      '<button type="button" class="ghost" data-act="tts">Urdu voice settings</button>' +
      '<section class="class-grid">' + cards + "</section>" +
      '<label class="rate">Voice speed <input id="rate" type="range" min="0.75" max="1.15" step="0.01" value="' + rate + '" /></label>' +
      "</main>"
    );
  }

  function classHtml(classId) {
    var cls = course.classes.filter(function (item) { return item.id === classId; })[0];
    var done = seen();
    var cards = cls.chapters.map(function (chapter) {
      var golden = chapter.lessons.filter(function (lesson) { return lesson.golden; }).length;
      var read = chapter.lessons.filter(function (lesson) { return done.indexOf(lesson.id) !== -1; }).length;
      return (
        '<button type="button" class="chapter-card" data-act="chapter" data-class="' + esc(cls.id) + '" data-id="' + esc(chapter.id) + '">' +
        '<span class="badge">Chapter ' + chapter.number + "</span>" +
        "<strong>" + esc(chapter.title) + "</strong>" +
        '<span class="urdu">' + esc(chapter.urdu) + "</span>" +
        "<small>" + chapter.lessons.length + " sketchnotes · " + golden + " golden · " + read + " opened</small>" +
        "</button>"
      );
    }).join("");
    return (
      '<main class="shell">' +
      '<header class="topbar"><button type="button" class="icon-btn" data-act="back" aria-label="Back">←</button>' +
      '<div class="grow"><h1>' + esc(cls.title) + '</h1><p class="urdu" style="margin:0">' + esc(cls.urdu) + "</p></div></header>" +
      '<section class="chapter-list">' + cards + "</section></main>"
    );
  }

  function chapterHtml(classId, chapterId) {
    var cls = course.classes.filter(function (item) { return item.id === classId; })[0];
    var chapter = cls.chapters.filter(function (item) { return item.id === chapterId; })[0];
    var filter = route().filter || "all";
    var lessons = chapter.lessons.filter(function (lesson) {
      return filter !== "golden" || lesson.golden;
    });
    var done = seen();
    var cards = lessons.map(function (lesson) {
      return (
        '<button type="button" class="lesson-card' + (lesson.golden ? " golden" : "") + '" data-act="lesson" data-id="' + esc(lesson.id) + '">' +
        (lesson.golden ? '<span class="badge gold">Golden</span>' : '<span class="badge soft">Sketch</span>') +
        "<strong>" + esc(lesson.title) + "</strong>" +
        '<span class="urdu">' + esc(lesson.urduTitle) + "</span>" +
        "<small>" + (done.indexOf(lesson.id) === -1 ? "Not opened yet" : "Opened") +
        (lesson.diagram ? " · SVG diagram" : "") + "</small></button>"
      );
    }).join("");
    return (
      '<main class="shell">' +
      '<header class="topbar"><button type="button" class="icon-btn" data-act="back" aria-label="Back">←</button>' +
      '<div class="grow"><h1>' + esc(chapter.title) + '</h1><p class="urdu" style="margin:0">' + esc(chapter.urdu) + "</p></div></header>" +
      '<div class="modes" role="group" aria-label="Filter lessons">' +
      '<button type="button" data-act="filter" data-filter="all" aria-pressed="' + (filter === "all") + '">All</button>' +
      '<button type="button" data-act="filter" data-filter="golden" aria-pressed="' + (filter === "golden") + '">Golden only</button>' +
      "</div>" +
      '<section class="lesson-list">' + cards + "</section></main>"
    );
  }

  function blockHtml(block) {
    if (block.type === "h") return '<h2>' + rich(block.text) + "</h2>";
    if (block.type === "p") return "<p>" + rich(block.text) + "</p>";
    if (block.type === "list") {
      return '<ul class="list">' + block.items.map(function (item) {
        return "<li>" + rich(item) + "</li>";
      }).join("") + "</ul>";
    }
    if (block.type === "code") return '<pre class="code">' + esc(block.text) + "</pre>";
    if (block.type === "callout") {
      return (
        '<aside class="callout ' + esc(block.kind || "note") + '">' +
        "<p>" + rich(block.text) + "</p>" +
        '<button type="button" class="tiny" data-act="speak" data-plain="' + esc(speakable(block.text)) + '">Listen</button>' +
        "</aside>"
      );
    }
    if (block.type === "table") {
      return '<div class="ftable" role="table">' + block.rows.map(function (row) {
        return '<div class="frow' + (row.header ? " head" : "") + '" role="row">' +
          row.cells.map(function (cell) {
            return '<div class="fcell" role="' + (row.header ? "columnheader" : "cell") + '">' + rich(cell) + "</div>";
          }).join("") + "</div>";
      }).join("") + "</div>";
    }
    if (block.type === "split") {
      return '<div class="split">' +
        '<div class="split-col">' + block.left.map(blockHtml).join("") + "</div>" +
        '<div class="split-col">' + block.right.map(blockHtml).join("") + "</div>" +
        "</div>";
    }
    return "";
  }

  function plainBlocks(blocks, chunks) {
    blocks.forEach(function (block) {
      if (block.text) chunks.push(speakable(block.text));
      if (block.items) block.items.forEach(function (item) { chunks.push(speakable(item)); });
      if (block.rows) block.rows.forEach(function (row) { chunks.push(row.cells.join(", ")); });
      if (block.left) plainBlocks(block.left, chunks);
      if (block.right) plainBlocks(block.right, chunks);
    });
  }

  function lessonEnglish(lesson) {
    var chunks = [];
    plainBlocks(lesson.blocks, chunks);
    return chunks.join(" ").replace(/\s+/g, " ").trim();
  }

  function segmentsFor(english, urduTitle, blurb) {
    var segments = [];
    if (voice !== "en" && urduTitle) segments.push({ lang: "ur", text: urduTitle + "۔" });
    if (voice !== "ur" && english) segments.push({ lang: "en", text: english });
    if (voice !== "en" && blurb) segments.push({ lang: "ur", text: blurb });
    if (voice === "ur" && !blurb && urduTitle) {
      segments.push({ lang: "ur", text: "بورڈ پلیٹ پر اردو سکیچ نوٹ بھی دیکھیں۔" });
    }
    return segments.filter(function (segment) { return segment.text && segment.text.trim(); });
  }

  function lessonHtml(id) {
    var found = findLesson(id);
    var lesson = found.lesson;
    var diagram = lesson.diagram && window.SketchDiagrams ? SketchDiagrams.render(lesson.diagram) : "";
    var english = lessonEnglish(lesson);
    var prev = found.index > 0 ? found.chapter.lessons[found.index - 1] : null;
    var next = found.index < found.chapter.lessons.length - 1 ? found.chapter.lessons[found.index + 1] : null;
    return (
      '<main class="shell">' +
      '<header class="topbar">' +
      '<button type="button" class="icon-btn" data-act="back" aria-label="Back">←</button>' +
      '<div class="grow"><h1>' + esc(lesson.title) + "</h1>" +
      '<p class="urdu" style="margin:4px 0 0">' + esc(lesson.urduTitle) + "</p></div>" +
      '<button type="button" class="solid" id="play-lesson" data-act="play-lesson" data-plain="' + esc(english) + '" data-urdu="' + esc(lesson.urduTitle) + '" data-blurb="' + esc(lesson.blurb || "") + '">' +
      (voice === "ur" ? "اردو سنیں" : voice === "en" ? "Play English" : "Play Urdish") + "</button>" +
      '<button type="button" class="ghost" data-act="stop">Stop</button>' +
      "</header>" +
      modesHtml() +
      (lesson.golden ? '<div class="golden-banner">★ Golden topic · امتحانی ٹاپک</div>' : "") +
      (lesson.blurb ? '<p class="urdish">' + esc(lesson.blurb) + "</p>" : "") +
      (diagram ? '<figure class="diagram">' + diagram + "</figure>" : "") +
      '<div class="flow">' + lesson.blocks.map(function (block) {
        if (block.type === "h") return '<h2 class="flow-title">' + rich(block.text) + "</h2>";
        var inner = blockHtml(block);
        if (!inner || block.type === "callout") return inner;
        var plain = [];
        plainBlocks([block], plain);
        return '<section class="card">' + inner +
          '<button type="button" class="tiny" data-act="speak" data-plain="' + esc(plain.join(" ")) + '">Listen</button></section>';
      }).join("") + "</div>" +
      (lesson.recall ? '<button type="button" class="recall" data-act="recall" aria-expanded="false"><span class="prompt">Cover the key line. Say it, then tap.</span><span class="answer" hidden>' + esc(lesson.recall) + "</span></button>" : "") +
      '<button type="button" class="ghost" data-act="plate" data-src="' + esc(lesson.plate) + '" aria-expanded="false">Show the original Urdu sketchnote</button>' +
      '<figure class="plate" id="plate" hidden><img alt="Original bilingual sketchnote for ' + esc(lesson.title) + '" /><figcaption>Teacher’s plate. Urdu is on this page in the original Nastaliq layout.</figcaption></figure>' +
      '<nav class="footer-nav">' +
      (prev ? '<button type="button" class="ghost" data-act="lesson" data-id="' + esc(prev.id) + '" data-replace="1">← ' + esc(prev.title) + "</button>" : "<span></span>") +
      (next ? '<button type="button" class="ghost" data-act="lesson" data-id="' + esc(next.id) + '" data-replace="1">' + esc(next.title) + " →</button>" : "<span></span>") +
      "</nav>" +
      '<label class="rate">Voice speed <input id="rate" type="range" min="0.75" max="1.15" step="0.01" value="' + rate + '" /></label>' +
      "</main>"
    );
  }

  function searchHtml(query) {
    var q = query.toLowerCase();
    var hits = [];
    course.classes.forEach(function (cls) {
      cls.chapters.forEach(function (chapter) {
        chapter.lessons.forEach(function (lesson) {
          var blob = (lesson.title + " " + lesson.urduTitle + " " + lesson.blurb + " " + lessonEnglish(lesson)).toLowerCase();
          if (blob.indexOf(q) !== -1) {
            hits.push({ lesson: lesson, cls: cls, chapter: chapter });
          }
        });
      });
    });
    var cards = hits.slice(0, 40).map(function (hit) {
      return (
        '<button type="button" class="search-hit" data-act="lesson" data-id="' + esc(hit.lesson.id) + '">' +
        "<small>" + esc(hit.cls.title) + " · " + esc(hit.chapter.title) + "</small>" +
        "<strong>" + esc(hit.lesson.title) + "</strong>" +
        '<span class="urdu">' + esc(hit.lesson.urduTitle) + "</span></button>"
      );
    }).join("");
    return (
      '<main class="shell">' +
      '<header class="topbar"><button type="button" class="icon-btn" data-act="back" aria-label="Back">←</button>' +
      '<div class="grow"><h1>Search</h1><p class="muted" style="margin:0">' + hits.length + ' matches for “' + esc(query) + '”</p></div></header>' +
      '<section class="lesson-list">' + (cards || "<p>No sketchnote used those words.</p>") + "</section></main>"
    );
  }

  function pathFor(current) {
    if (!current || current.name === "home") return "#/";
    if (current.name === "class") return "#/" + current.id;
    if (current.name === "chapter") return "#/" + current.classId + "/" + current.id;
    if (current.name === "lesson") return "#/lesson/" + current.id;
    if (current.name === "search") return "#/search/" + encodeURIComponent(current.q);
    return "#/";
  }

  var ignoreHash = false;

  function applyHash() {
    var raw = decodeURIComponent((location.hash || "#/").replace(/^#/, ""));
    var parts = raw.split("/").filter(Boolean);
    stack = [{ name: "home" }];
    if (parts[0] === "lesson" && parts[1] && findLesson(parts[1])) {
      var found = findLesson(parts[1]);
      stack.push({ name: "class", id: found.cls.id });
      stack.push({ name: "chapter", classId: found.cls.id, id: found.chapter.id, filter: "all" });
      stack.push({ name: "lesson", id: found.lesson.id });
      markSeen(found.lesson.id);
    } else if (parts[0] === "search" && parts[1]) {
      stack.push({ name: "search", q: decodeURIComponent(parts.slice(1).join("/")) });
    } else if (parts[0]) {
      var cls = course.classes.filter(function (item) { return item.id === parts[0]; })[0];
      if (cls) {
        stack.push({ name: "class", id: cls.id });
        if (parts[1]) {
          var chapter = cls.chapters.filter(function (item) { return item.id === parts[1]; })[0];
          if (chapter) stack.push({ name: "chapter", classId: cls.id, id: chapter.id, filter: "all" });
        }
      }
    }
    render();
  }

  function render() {
    var current = route();
    var html = "";
    if (!course) {
      html = '<main class="shell"><h1>Teach Yourself Sketchnotes</h1><p>The course file did not open.</p></main>';
    } else if (current.name === "home") html = homeHtml();
    else if (current.name === "class") html = classHtml(current.id);
    else if (current.name === "chapter") html = chapterHtml(current.classId, current.id);
    else if (current.name === "lesson") html = lessonHtml(current.id);
    else if (current.name === "search") html = searchHtml(current.q);
    document.getElementById("app").innerHTML = html;
    var nextHash = pathFor(route());
    if (location.hash !== nextHash) {
      ignoreHash = true;
      location.hash = nextHash;
    }
    var heading = document.querySelector("h1");
    if (heading) heading.setAttribute("tabindex", "-1");
    if (heading) heading.focus();
    typeset();
  }

  var mathTries = 0;
  function typeset() {
    if (!window.MathJax || !MathJax.typesetPromise) {
      if (mathTries < 40) {
        mathTries += 1;
        setTimeout(typeset, 150);
      }
      return;
    }
    mathTries = 0;
    var run = function () {
      if (MathJax.typesetClear) {
        try { MathJax.typesetClear(); } catch (error) { /* stale nodes */ }
      }
      MathJax.typesetPromise().catch(function () {});
    };
    if (MathJax.startup && MathJax.startup.promise) MathJax.startup.promise.then(run);
    else run();
  }

  function speak(segments) {
    if (!segments.length) return;
    speaking = true;
    var play = document.getElementById("play-lesson");
    if (play) play.classList.add("speaking");
    if (window.Android && Android.speak) {
      Android.setRate(rate);
      Android.speak(JSON.stringify(segments));
      return;
    }
    if (!window.speechSynthesis) {
      showToast("This browser has no speech engine. The APK uses Android Urdish TTS.");
      speaking = false;
      return;
    }
    window.speechSynthesis.cancel();
    var index = 0;
    var next = function () {
      if (!speaking || index >= segments.length) {
        speaking = false;
        if (play) play.classList.remove("speaking");
        return;
      }
      var segment = segments[index++];
      var utterance = new SpeechSynthesisUtterance(segment.text);
      utterance.lang = segment.lang === "ur" ? "ur-PK" : "en-US";
      utterance.rate = rate;
      utterance.onend = next;
      utterance.onerror = next;
      window.speechSynthesis.speak(utterance);
    };
    next();
  }

  function stopSpeech() {
    speaking = false;
    var play = document.getElementById("play-lesson");
    if (play) play.classList.remove("speaking");
    if (window.Android && Android.stop) Android.stop();
    if (window.speechSynthesis) window.speechSynthesis.cancel();
  }

  function onClick(event) {
    var target = event.target.closest("[data-act]");
    if (!target) return;
    var act = target.getAttribute("data-act");
    if (act === "back") {
      if (stack.length > 1) {
        stack.pop();
        render();
      }
      return;
    }
    if (act === "class") {
      go({ name: "class", id: target.getAttribute("data-id") });
      return;
    }
    if (act === "chapter") {
      go({ name: "chapter", classId: target.getAttribute("data-class"), id: target.getAttribute("data-id"), filter: "all" });
      return;
    }
    if (act === "filter") {
      route().filter = target.getAttribute("data-filter");
      render();
      return;
    }
    if (act === "lesson") {
      var id = target.getAttribute("data-id");
      markSeen(id);
      if (target.getAttribute("data-replace") && route().name === "lesson") {
        stack[stack.length - 1] = { name: "lesson", id: id };
      } else {
        stack.push({ name: "lesson", id: id });
      }
      render();
      return;
    }
    if (act === "voice") {
      voice = target.getAttribute("data-mode");
      localStorage.setItem("tys-voice", voice);
      render();
      return;
    }
    if (act === "play-lesson" || act === "speak") {
      speak(segmentsFor(
        target.getAttribute("data-plain"),
        target.getAttribute("data-urdu") || (route().name === "lesson" ? findLesson(route().id).lesson.urduTitle : ""),
        target.getAttribute("data-blurb") || ""
      ));
      return;
    }
    if (act === "stop") {
      stopSpeech();
      return;
    }
    if (act === "tts") {
      if (window.Android && Android.openTtsSettings) Android.openTtsSettings();
      else showToast("On the phone, this opens Android text-to-speech so you can install Urdu.");
      return;
    }
    if (act === "recall") {
      var answer = target.querySelector(".answer");
      var open = answer.hidden;
      answer.hidden = !open;
      target.setAttribute("aria-expanded", open ? "true" : "false");
      return;
    }
    if (act === "plate") {
      var figure = document.getElementById("plate");
      var openPlate = figure.hidden;
      if (openPlate) {
        var image = figure.querySelector("img");
        if (!image.getAttribute("src")) image.src = target.getAttribute("data-src");
      }
      figure.hidden = !openPlate;
      target.setAttribute("aria-expanded", openPlate ? "true" : "false");
      target.textContent = openPlate ? "Hide the original plate" : "Show the original Urdu sketchnote";
    }
  }

  document.addEventListener("click", onClick);
  document.addEventListener("submit", function (event) {
    if (!event.target.closest("#search-form")) return;
    event.preventDefault();
    var query = new FormData(event.target).get("q");
    query = String(query || "").trim();
    if (!query) return;
    go({ name: "search", q: query });
  });
  document.addEventListener("input", function (event) {
    if (event.target.id !== "rate") return;
    rate = Number(event.target.value);
    localStorage.setItem("tys-rate", String(rate));
    if (window.Android && Android.setRate) Android.setRate(rate);
  });

  window.App = {
    back: function () {
      if (stack.length <= 1) return false;
      stack.pop();
      render();
      return true;
    }
  };

  window.Urdish = {
    onState: function (state) {
      speaking = state === "speaking";
      var play = document.getElementById("play-lesson");
      if (play) play.classList.toggle("speaking", speaking);
    },
    onVoiceIssue: function (message) {
      showToast(message);
    }
  };

  window.addEventListener("hashchange", function () {
    if (ignoreHash) {
      ignoreHash = false;
      return;
    }
    if (course) applyHash();
  });

  fetch("course.json")
    .then(function (response) { return response.json(); })
    .then(function (data) {
      course = data;
      if (location.hash && location.hash !== "#" && location.hash !== "#/") applyHash();
      else render();
    })
    .catch(function () {
      document.getElementById("app").innerHTML = "<main class='shell'><h1>Teach Yourself Sketchnotes</h1><p>Could not load course.json.</p></main>";
    });
})();
