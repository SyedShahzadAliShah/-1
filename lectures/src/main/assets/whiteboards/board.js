(function () {
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var shots = document.querySelectorAll(
    "h1, h3, .box, figure.diagram, table, pre, .flow, .two-col"
  );
  shots.forEach(function (el, i) {
    el.classList.add("enter");
    el.style.setProperty("--d", (0.18 + i * 0.28) + "s");
    if (reduced) el.classList.add("enter-now");
  });

  function canStroke(node) {
    return typeof node.getTotalLength === "function";
  }

  function draw(svg, baseDelay) {
    var nodes = svg.querySelectorAll("path, line, polyline, polygon, circle, ellipse, rect");
    nodes.forEach(function (node, i) {
      if (reduced) return;
      var delay = (baseDelay || 0.45) + i * 0.18;
      var fill = (node.getAttribute("fill") || "").trim();
      if (fill && fill !== "none") {
        node.style.fillOpacity = "0";
        node.classList.add("ink-fill");
        node.style.setProperty("--d", delay + "s");
      }
      try {
        if (!canStroke(node)) {
          node.classList.add("ink-fade");
          node.style.setProperty("--d", delay + "s");
          return;
        }
        var len = Math.max(node.getTotalLength(), 1);
        if (!node.getAttribute("stroke") || node.getAttribute("stroke") === "none") {
          node.setAttribute("stroke", fill && fill !== "none" ? fill : "#0e7490");
          node.setAttribute("stroke-width", node.getAttribute("stroke-width") || "1.6");
        }
        node.style.strokeDasharray = String(len);
        node.style.strokeDashoffset = String(len);
        node.classList.add("ink-draw");
        node.style.setProperty("--d", delay + "s");
      } catch (e) {
        node.classList.add("ink-fade");
        node.style.setProperty("--d", delay + "s");
      }
    });
  }

  document.querySelectorAll("figure.diagram svg").forEach(function (svg, i) {
    draw(svg, 0.7 + i * 0.35);
  });

  function typeset(el) {
    if (!window.MathJax || !MathJax.typesetPromise || !el) return;
    MathJax.typesetClear && MathJax.typesetClear([el]);
    MathJax.typesetPromise([el]).catch(function () {});
  }

  window.LectureBoard = {
    showBeat: function (index) {
      var nodes = document.querySelectorAll("[data-beat]");
      var current = null;
      nodes.forEach(function (el) {
        var n = parseInt(el.getAttribute("data-beat"), 10);
        var on = n === index;
        el.classList.toggle("live-beat", on);
        if (!on) return;
        current = el;
        el.classList.add("enter-now");
        var svg = el.querySelector("svg");
        if (svg) draw(svg, 0.05);
      });
      var note = document.getElementById("urdishNote");
      if (note) {
        var raw = current ? (current.getAttribute("data-note") || "") : "";
        var safe = raw.replace(/&/g, "&amp;").replace(/</g, "&lt;");
        note.innerHTML = safe.replace(/[A-Za-z0-9][A-Za-z0-9 .:+#\/-]*/g, function (word) {
          return '<bdi dir="ltr">' + word + "</bdi>";
        });
      }
      var board = document.querySelector(".board");
      if (board) board.scrollTop = 0;
      typeset(current);
    },
    clearLive: function () {
      /* Keep the last note on screen at full size after the voice stops. */
    }
  };

  if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
    MathJax.startup.promise.then(function () {
      window.LectureBoard.showBeat(0);
    });
  }
  window.LectureBoard.showBeat(0);
})();
