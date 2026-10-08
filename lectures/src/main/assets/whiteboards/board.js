(function () {
  var reduced = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var shots = document.querySelectorAll(
    "h1, h3, .box, figure.diagram, table, pre, .flow, .two-col, .term-row"
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

  function fitBoard() {
    var cinema = document.querySelector(".cinema");
    if (cinema) cinema.style.transform = "none";
  }

  if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
    MathJax.startup.promise.then(function () {
      document.querySelectorAll("mjx-container").forEach(function (el, i) {
        el.classList.add("enter");
        el.style.setProperty("--d", (0.12 * i) + "s");
      });
      fitBoard();
    });
  }
  window.addEventListener("resize", fitBoard);
  setTimeout(fitBoard, 80);
  setTimeout(fitBoard, 600);

  window.LectureBoard = {
    showBeat: function (index) {
      var nodes = document.querySelectorAll("[data-beat]");
      nodes.forEach(function (el) {
        var n = parseInt(el.getAttribute("data-beat"), 10);
        var on = n === index;
        el.classList.toggle("live-beat", on);
        if (!on) return;
        el.classList.remove("enter");
        void el.offsetWidth;
        el.classList.add("enter");
        el.style.setProperty("--d", "0s");
        var svg = el.tagName === "FIGURE" ? el.querySelector("svg") : null;
        if (svg) draw(svg, 0.12);
      });
      fitBoard();
    },
    clearLive: function () {
      document.querySelectorAll(".live-beat").forEach(function (el) {
        el.classList.remove("live-beat");
      });
    }
  };
})();
