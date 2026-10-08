/* Inline teaching diagrams. Each sketch is SVG, so the APK stays offline. */
(function (global) {
  "use strict";

  var ink = "#1c3148";
  var navy = "#243e73";
  var teal = "#0f766e";
  var amber = "#c4840a";
  var rose = "#c2415c";
  var paper = "#fffdf8";
  var mint = "#d7f3ee";
  var sky = "#e4ecfb";
  var blush = "#fde7ee";
  var cream = "#fff4d6";

  function esc(value) {
    return String(value)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function text(x, y, value, size, fill, anchor, weight) {
    return (
      '<text x="' + x + '" y="' + y + '" text-anchor="' + (anchor || "middle") +
      '" font-family="ui-sans-serif,sans-serif" font-size="' + (size || 13) +
      '" font-weight="' + (weight || 650) + '" fill="' + (fill || ink) + '">' +
      esc(value) + "</text>"
    );
  }

  function round(x, y, w, h, fill) {
    return (
      '<rect x="' + x + '" y="' + y + '" width="' + w + '" height="' + h +
      '" rx="12" fill="' + fill + '" stroke="' + ink + '" stroke-width="1.6"/>'
    );
  }

  function frame(w, h, title, body) {
    return (
      '<svg viewBox="0 0 ' + w + " " + h + '" role="img" aria-label="' + esc(title) + '">' +
      "<title>" + esc(title) + "</title>" +
      '<rect x="1" y="1" width="' + (w - 2) + '" height="' + (h - 2) +
      '" rx="18" fill="' + paper + '" stroke="' + ink + '" stroke-width="1.6"/>' +
      text(18, 28, title, 15, navy, "start", 800) +
      body + "</svg>"
    );
  }

  function builders() {
    return {
      "stairs-ramp": function () {
        return frame(640, 230, "Stairs are discrete. A ramp is continuous.",
          '<path d="M70 180 H150 V140 H210 V100 H270 V60 H330" fill="none" stroke="' + navy + '" stroke-width="4" stroke-linejoin="round"/>' +
          text(190, 205, "Discrete (stairs)", 13, navy) +
          '<path d="M390 180 L560 60" fill="none" stroke="' + teal + '" stroke-width="4" stroke-linecap="round"/>' +
          text(480, 205, "Continuous (ramp)", 13, teal) +
          '<path d="M340 110 H378" stroke="' + amber + '" stroke-width="3" marker-end="url(#arrow)"/>' +
          '<defs><marker id="arrow" markerWidth="8" markerHeight="8" refX="6" refY="3" orient="auto"><path d="M0 0 L6 3 L0 6 Z" fill="' + amber + '"/></marker></defs>'
        );
      },
      waves: function () {
        return frame(640, 280, "Analog sine wave and digital square wave",
          text(70, 78, "V", 12, rose, "start") +
          '<path d="M90 120 C130 40 170 40 210 120 S290 200 330 120 S410 40 450 120" fill="none" stroke="' + rose + '" stroke-width="3.5"/>' +
          '<path d="M90 150 H520" stroke="' + ink + '" stroke-width="1.4"/>' +
          text(530, 154, "t", 12, ink, "start") +
          text(300, 190, "Analog · any value", 13, rose) +
          text(70, 230, "V", 12, navy, "start") +
          '<path d="M90 250 H150 V214 H230 V250 H310 V214 H390 V250 H470" fill="none" stroke="' + navy + '" stroke-width="3.5"/>' +
          text(160, 208, "HIGH 1", 11, navy, "start") +
          text(240, 268, "LOW 0", 11, teal, "start")
        );
      },
      truth: function () {
        var cells = "";
        var values = ["A", "B", "Y", "0", "0", "0", "0", "1", "0", "1", "0", "0", "1", "1", "1"];
        for (var i = 0; i < values.length; i++) {
          var col = i % 3;
          var row = Math.floor(i / 3);
          var x = 180 + col * 70;
          var y = 58 + row * 32;
          cells += '<rect x="' + x + '" y="' + y + '" width="70" height="32" fill="' + (row === 0 ? navy : paper) + '" stroke="' + ink + '"/>';
          cells += text(x + 35, y + 21, values[i], 14, row === 0 ? "#fff" : ink);
        }
        return frame(640, 250, "Truth table · rows = 2ⁿ",
          text(40, 90, "Count inputs n.", 14, ink, "start", 600) +
          text(40, 116, "Make 2ⁿ rows.", 14, ink, "start", 600) +
          text(40, 142, "List every pattern.", 14, ink, "start", 600) +
          text(40, 168, "Write the output.", 14, ink, "start", 600) +
          cells +
          text(320, 230, "AND is 1 only on the last row", 13, teal)
        );
      },
      boolean: function () {
        return frame(640, 220, "Boolean algebra uses only 0 and 1",
          round(24, 58, 180, 120, cream) + text(114, 100, "AND ·", 18, navy) + text(114, 128, "both must be 1", 13, ink, "middle", 500) +
          round(224, 58, 180, 120, mint) + text(314, 100, "OR +", 18, teal) + text(314, 128, "either can be 1", 13, ink, "middle", 500) +
          round(424, 58, 180, 120, blush) + text(514, 100, "NOT '", 18, rose) + text(514, 128, "flip the bit", 13, ink, "middle", 500)
        );
      },
      "gates-basic": function () {
        return frame(640, 250, "Basic gates",
          '<path d="M40 70 H90 V150 H40 M90 70 Q150 70 150 110 Q150 150 90 150" fill="' + sky + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<path d="M150 110 H190" stroke="' + ink + '" stroke-width="2"/>' +
          text(110, 185, "AND", 14, navy) + text(110, 206, "Y = A · B", 13, ink, "middle", 500) +
          '<path d="M250 70 Q310 70 340 110 Q310 150 250 150 Q280 110 250 70" fill="' + mint + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<path d="M340 110 H380" stroke="' + ink + '" stroke-width="2"/>' +
          text(310, 185, "OR", 14, teal) + text(310, 206, "Y = A + B", 13, ink, "middle", 500) +
          '<path d="M460 70 L540 110 L460 150 Z" fill="' + blush + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<circle cx="552" cy="110" r="8" fill="' + paper + '" stroke="' + ink + '" stroke-width="2"/>' +
          text(510, 185, "NOT", 14, rose) + text(510, 206, "Y = A'", 13, ink, "middle", 500)
        );
      },
      "gates-universal": function () {
        return frame(640, 230, "NAND and NOR can build every gate",
          '<path d="M50 60 H110 V140 H50 M110 60 Q170 60 170 100 Q170 140 110 140" fill="' + cream + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<circle cx="184" cy="100" r="10" fill="' + paper + '" stroke="' + ink + '" stroke-width="2"/>' +
          text(120, 185, "NAND", 16, navy) + text(120, 208, "AND then NOT", 13, ink, "middle", 500) +
          '<path d="M340 60 Q410 60 440 100 Q410 140 340 140 Q370 100 340 60" fill="' + mint + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<circle cx="456" cy="100" r="10" fill="' + paper + '" stroke="' + ink + '" stroke-width="2"/>' +
          text(400, 185, "NOR", 16, teal) + text(400, 208, "OR then NOT", 13, ink, "middle", 500)
        );
      },
      "gates-xor": function () {
        return frame(640, 220, "XOR is 1 when the inputs differ",
          '<path d="M80 50 Q140 50 180 100 Q140 150 80 150 Q120 100 80 50" fill="' + sky + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<path d="M60 50 Q100 100 60 150" fill="none" stroke="' + ink + '" stroke-width="2"/>' +
          text(140, 185, "XOR · odd number of 1s", 14, navy) +
          round(360, 55, 220, 100, cream) +
          text(470, 95, "0 XOR 0 = 0", 14, ink) +
          text(470, 120, "1 XOR 0 = 1", 14, teal)
        );
      },
      "logic-diagram": function () {
        return frame(640, 220, "Read a logic diagram left to right",
          text(40, 90, "A", 16, navy, "start") +
          text(40, 140, "B", 16, navy, "start") +
          '<path d="M70 84 H120 M70 134 H120" stroke="' + ink + '" stroke-width="2"/>' +
          '<path d="M120 60 H170 V150 H120 M170 60 Q230 60 230 105 Q230 150 170 150" fill="' + sky + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<path d="M230 105 H280" stroke="' + ink + '" stroke-width="2"/>' +
          text(250, 96, "AND", 12, navy) +
          '<path d="M280 80 L340 105 L280 130 Z" fill="' + blush + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<circle cx="352" cy="105" r="8" fill="' + paper + '" stroke="' + ink + '" stroke-width="2"/>' +
          '<path d="M360 105 H420" stroke="' + ink + '" stroke-width="2"/>' +
          text(500, 110, "Y", 18, teal, "start") +
          text(320, 190, "Inputs enter. One output leaves.", 14, ink)
        );
      },
      kmap: function () {
        var grid = "";
        var vals = ["1", "0", "1", "1"];
        var tags = ["A'B'", "A'B", "AB'", "AB"];
        for (var i = 0; i < 4; i++) {
          var x = 250 + (i % 2) * 90;
          var y = 70 + Math.floor(i / 2) * 60;
          grid += '<rect x="' + x + '" y="' + y + '" width="90" height="60" fill="' + (vals[i] === "1" ? mint : paper) + '" stroke="' + ink + '" stroke-width="1.6"/>';
          grid += text(x + 45, y + 28, vals[i], 20, navy);
          grid += text(x + 45, y + 48, tags[i], 11, ink, "middle", 500);
        }
        return frame(640, 240, "Group the 1s. Neighbours differ by one bit.",
          text(36, 90, "Groups of", 15, ink, "start") +
          text(36, 116, "1, 2, 4, 8", 18, teal, "start") +
          text(36, 148, "Overlap is allowed.", 14, ink, "start", 500) +
          grid +
          '<ellipse cx="385" cy="160" rx="70" ry="28" fill="none" stroke="' + rose + '" stroke-width="2.5"/>'
        );
      },
      kmap3: function () {
        var body = text(24, 70, "BC", 13, navy, "start") + text(250, 58, "00   01   11   10", 13, navy);
        var bits = ["0", "1", "0", "1", "1", "1", "1", "0"];
        for (var i = 0; i < 8; i++) {
          var x = 160 + (i % 4) * 70;
          var y = 78 + Math.floor(i / 4) * 52;
          body += '<rect x="' + x + '" y="' + y + '" width="70" height="52" fill="' + (bits[i] === "1" ? cream : paper) + '" stroke="' + ink + '"/>';
          body += text(x + 35, y + 32, bits[i], 18, ink);
        }
        body += text(130, 110, "A=0", 12, teal, "start") + text(130, 162, "A=1", 12, teal, "start");
        body += text(320, 210, "Gray code: 00, 01, 11, 10", 14, navy);
        return frame(640, 240, "Three-variable K-map", body);
      },
      sdlc: function () {
        var steps = ["Plan", "Analyze", "Design", "Build", "Test", "Maintain"];
        var body = "";
        for (var i = 0; i < steps.length; i++) {
          var angle = -Math.PI / 2 + i * (Math.PI * 2 / 6);
          var x = 320 + Math.cos(angle) * 150;
          var y = 130 + Math.sin(angle) * 78;
          body += '<circle cx="' + x + '" cy="' + y + '" r="28" fill="' + (i % 2 ? mint : sky) + '" stroke="' + ink + '" stroke-width="1.6"/>';
          body += text(x, y + 4, steps[i], 11, navy);
        }
        body += text(320, 134, "cycle", 13, amber);
        return frame(640, 250, "Software development life cycle", body);
      },
      waterfall: function () {
        var names = ["Requirements", "Design", "Build", "Test", "Release"];
        var body = "";
        for (var i = 0; i < names.length; i++) {
          body += round(40 + i * 36, 56 + i * 28, 210, 36, i === 4 ? mint : sky);
          body += text(145 + i * 36, 80 + i * 28, names[i], 13, navy);
        }
        body += text(470, 130, "Hard to step back", 14, rose, "start");
        body += text(470, 156, "Use when needs", 14, ink, "start", 500);
        body += text(470, 178, "are already clear", 14, ink, "start", 500);
        return frame(640, 250, "Waterfall moves one way", body);
      },
      agile: function () {
        return frame(640, 230, "Agile repeats short sprints",
          '<circle cx="230" cy="130" r="70" fill="none" stroke="' + teal + '" stroke-width="8" stroke-dasharray="40 14"/>' +
          text(230, 126, "sprint", 16, teal) +
          text(230, 148, "then review", 12, ink, "middle", 500) +
          round(390, 60, 210, 120, cream) +
          text(495, 100, "Plan a little", 14, navy) +
          text(495, 124, "Build a slice", 14, navy) +
          text(495, 148, "Ask the user", 14, teal)
        );
      },
      osi: function () {
        var layers = ["7 Application", "6 Presentation", "5 Session", "4 Transport", "3 Network", "2 Data link", "1 Physical"];
        var body = "";
        for (var i = 0; i < layers.length; i++) {
          var fill = i < 3 ? blush : i < 4 ? cream : sky;
          body += '<rect x="180" y="' + (48 + i * 26) + '" width="280" height="24" rx="6" fill="' + fill + '" stroke="' + ink + '"/>';
          body += text(320, 65 + i * 26, layers[i], 13, navy);
        }
        return frame(640, 260, "OSI has seven layers", body);
      },
      tcpip: function () {
        var layers = [["Application", blush], ["Transport", cream], ["Internet", mint], ["Network access", sky]];
        var body = "";
        for (var i = 0; i < layers.length; i++) {
          body += round(160, 52 + i * 42, 320, 36, layers[i][1]);
          body += text(320, 76 + i * 42, layers[i][0], 15, navy);
        }
        return frame(640, 250, "TCP/IP folds OSI into four layers", body);
      },
      pseudocode: function () {
        return frame(640, 230, "Pseudocode is an algorithm in plain steps",
          round(30, 56, 270, 140, sky) +
          text(165, 90, "Algorithm", 16, navy) +
          text(165, 118, "precise and finite", 13, ink, "middle", 500) +
          text(165, 142, "ends with a result", 13, ink, "middle", 500) +
          round(330, 56, 270, 140, cream) +
          text(465, 90, "Pseudocode", 16, amber) +
          text(465, 118, "1. read scores", 13, ink, "middle", 500) +
          text(465, 142, "2. add, then divide", 13, ink, "middle", 500)
        );
      },
      bubble: function () {
        var heights = [120, 70, 150, 48, 96];
        var body = "";
        for (var i = 0; i < heights.length; i++) {
          var h = heights[i];
          body += '<rect x="' + (70 + i * 70) + '" y="' + (180 - h) + '" width="46" height="' + h + '" rx="8" fill="' + (i < 2 ? blush : sky) + '" stroke="' + ink + '"/>';
        }
        body += '<path d="M93 50 Q140 20 163 70" fill="none" stroke="' + rose + '" stroke-width="2.5"/>';
        body += text(430, 110, "Swap neighbours", 15, rose, "start");
        body += text(430, 136, "until the list", 15, ink, "start", 500);
        body += text(430, 160, "is in order", 15, ink, "start", 500);
        return frame(640, 220, "Bubble sort swaps adjacent values", body);
      },
      selection: function () {
        return frame(640, 210, "Selection sort picks the smallest remaining",
          '<rect x="40" y="90" width="50" height="70" rx="8" fill="' + mint + '" stroke="' + ink + '"/>' +
          '<rect x="110" y="60" width="50" height="100" rx="8" fill="' + sky + '" stroke="' + ink + '"/>' +
          '<rect x="180" y="110" width="50" height="50" rx="8" fill="' + blush + '" stroke="' + rose + '" stroke-width="2.4"/>' +
          '<rect x="250" y="76" width="50" height="84" rx="8" fill="' + sky + '" stroke="' + ink + '"/>' +
          text(205, 190, "smallest", 12, rose) +
          text(420, 120, "Put it in the next slot.", 15, navy, "start") +
          text(420, 146, "Then search the rest.", 15, ink, "start", 500)
        );
      },
      "linear-search": function () {
        var body = "";
        var nums = ["4", "9", "2", "7", "5"];
        for (var i = 0; i < nums.length; i++) {
          body += round(30 + i * 78, 80, 64, 48, i === 3 ? mint : paper);
          body += text(62 + i * 78, 110, nums[i], 18, navy);
        }
        body += text(320, 170, "Check every cell until 7 is found", 14, teal);
        return frame(640, 210, "Linear search walks the list", body);
      },
      "binary-search": function () {
        var nums = ["2", "5", "8", "12", "16", "21", "30"];
        var body = text(320, 58, "Sorted list. Compare with the middle.", 13, ink);
        for (var i = 0; i < nums.length; i++) {
          body += round(24 + i * 86, 90, 74, 50, i === 3 ? cream : i < 3 ? "#f6f1e8" : paper);
          body += text(61 + i * 86, 122, nums[i], 18, i === 3 ? amber : navy);
        }
        body += text(320, 180, "12 is the middle. Too small? Look right.", 14, teal);
        return frame(640, 210, "Binary search halves the problem", body);
      },
      bigo: function () {
        return frame(640, 240, "Big O shows how work grows",
          '<path d="M60 190 H560 M60 190 V50" stroke="' + ink + '" stroke-width="1.5"/>' +
          '<path d="M60 170 H540" stroke="' + teal + '" stroke-width="3"/>' +
          text(500, 162, "O(1)", 12, teal, "start") +
          '<path d="M60 180 Q300 170 540 70" fill="none" stroke="' + navy + '" stroke-width="3"/>' +
          text(500, 78, "O(n)", 12, navy, "start") +
          '<path d="M60 186 Q240 180 400 80 Q480 30 540 40" fill="none" stroke="' + rose + '" stroke-width="3"/>' +
          text(430, 40, "O(n²)", 12, rose, "start") +
          text(80, 214, "bigger input →", 12, ink, "start", 500)
        );
      },
      stack: function () {
        return frame(640, 250, "Stack is LIFO. Last in, first out.",
          round(80, 150, 160, 36, sky) + text(160, 174, "first", 14, navy) +
          round(80, 108, 160, 36, sky) + text(160, 132, "second", 14, navy) +
          round(80, 66, 160, 36, cream) + text(160, 90, "TOP", 14, amber) +
          text(360, 100, "Push puts a plate on top.", 15, ink, "start") +
          text(360, 130, "Pop takes the top plate.", 15, teal, "start") +
          text(360, 170, "Undo and calls use stacks.", 14, ink, "start", 500)
        );
      },
      queue: function () {
        return frame(640, 210, "Queue is FIFO. First in, first out.",
          round(70, 80, 100, 54, mint) + text(120, 112, "front", 14, teal) +
          round(190, 80, 100, 54, sky) + text(240, 112, "next", 14, navy) +
          round(310, 80, 100, 54, cream) + text(360, 112, "back", 14, amber) +
          text(80, 170, "Dequeue leaves at the front. Enqueue joins at the back.", 14, ink, "start", 600)
        );
      },
      linked: function () {
        var body = "";
        var names = ["10", "20", "30", "null"];
        for (var i = 0; i < names.length; i++) {
          body += round(30 + i * 150, 80, 90, 50, i === 3 ? "#f3efe6" : mint);
          body += text(75 + i * 150, 112, names[i], 16, navy);
          if (i < 3) body += '<path d="M' + (120 + i * 150) + ' 105 H' + (175 + i * 150) + '" stroke="' + ink + '" stroke-width="2"/>';
        }
        body += text(320, 175, "Each node stores a value and the next address", 14, teal);
        return frame(640, 210, "Linked list follows pointers", body);
      },
      array: function () {
        var body = "";
        for (var i = 0; i < 6; i++) {
          body += '<rect x="' + (40 + i * 90) + '" y="90" width="80" height="54" fill="' + paper + '" stroke="' + ink + '"/>';
          body += text(80 + i * 90, 122, String(i * 3 + 2), 16, navy);
          body += text(80 + i * 90, 168, "[" + i + "]", 12, teal, "middle", 500);
        }
        return frame(640, 210, "Array cells sit side by side", body);
      },
      tree: function () {
        return frame(640, 240, "A tree has one root and no cycles",
          '<circle cx="320" cy="70" r="22" fill="' + cream + '" stroke="' + ink + '" stroke-width="1.6"/>' + text(320, 76, "8", 16, navy) +
          '<path d="M304 86 L220 130 M336 86 L420 130" stroke="' + ink + '" stroke-width="1.8"/>' +
          '<circle cx="200" cy="150" r="20" fill="' + sky + '" stroke="' + ink + '"/>' + text(200, 156, "3", 14, navy) +
          '<circle cx="440" cy="150" r="20" fill="' + mint + '" stroke="' + ink + '"/>' + text(440, 156, "12", 14, navy) +
          '<path d="M186 166 L140 200 M214 166 L250 200" stroke="' + ink + '" stroke-width="1.6"/>' +
          '<circle cx="130" cy="214" r="16" fill="' + paper + '" stroke="' + ink + '"/>' + text(130, 219, "1", 12) +
          '<circle cx="260" cy="214" r="16" fill="' + paper + '" stroke="' + ink + '"/>' + text(260, 219, "6", 12) +
          text(520, 214, "leaves", 12, teal, "start")
        );
      },
      "graph-ds": function () {
        return frame(640, 230, "A graph may contain cycles",
          '<circle cx="160" cy="90" r="22" fill="' + sky + '" stroke="' + ink + '"/>' + text(160, 96, "A") +
          '<circle cx="300" cy="70" r="22" fill="' + mint + '" stroke="' + ink + '"/>' + text(300, 76, "B") +
          '<circle cx="240" cy="170" r="22" fill="' + cream + '" stroke="' + ink + '"/>' + text(240, 176, "C") +
          '<path d="M182 90 H278 M176 108 L224 154 M284 90 L256 152" stroke="' + ink + '" stroke-width="1.8"/>' +
          text(430, 110, "Nodes and edges.", 15, navy, "start") +
          text(430, 138, "Roads and friends", 14, ink, "start", 500) +
          text(430, 160, "are graphs.", 14, ink, "start", 500)
        );
      },
      neural: function () {
        var layers = [3, 4, 2];
        var xs = [80, 250, 430];
        var body = "";
        var coords = [];
        for (var L = 0; L < layers.length; L++) {
          coords[L] = [];
          for (var n = 0; n < layers[L]; n++) {
            var y = 70 + n * (140 / (layers[L] - 1 || 1));
            if (layers[L] === 1) y = 140;
            coords[L].push([xs[L], y]);
          }
        }
        for (var a = 0; a < coords.length - 1; a++) {
          for (var i = 0; i < coords[a].length; i++) {
            for (var j = 0; j < coords[a + 1].length; j++) {
              body += '<line x1="' + coords[a][i][0] + '" y1="' + coords[a][i][1] + '" x2="' + coords[a + 1][j][0] + '" y2="' + coords[a + 1][j][1] + '" stroke="#c9bfb0" stroke-width="1.2"/>';
            }
          }
        }
        var fills = [sky, cream, mint];
        for (L = 0; L < coords.length; L++) {
          for (i = 0; i < coords[L].length; i++) {
            body += '<circle cx="' + coords[L][i][0] + '" cy="' + coords[L][i][1] + '" r="14" fill="' + fills[L] + '" stroke="' + ink + '"/>';
          }
        }
        body += text(80, 230, "input", 12, navy) + text(250, 230, "hidden", 12, amber) + text(430, 230, "output", 12, teal);
        body += text(520, 120, "weights", 13, ink, "start") + text(520, 142, "on each line", 13, ink, "start", 500);
        return frame(640, 260, "A neural net learns from examples", body);
      },
      "hci-senses": function () {
        var senses = [["Sight", sky], ["Touch", mint], ["Hearing", cream], ["Voice", blush], ["Space", "#efe7fb"]];
        var body = '<circle cx="320" cy="140" r="36" fill="' + paper + '" stroke="' + ink + '" stroke-width="1.8"/>' + text(320, 146, "user", 14, navy);
        for (var i = 0; i < senses.length; i++) {
          var angle = -Math.PI / 2 + i * (Math.PI * 2 / 5);
          var x = 320 + Math.cos(angle) * 150;
          var y = 140 + Math.sin(angle) * 78;
          body += '<rect x="' + (x - 48) + '" y="' + (y - 16) + '" width="96" height="32" rx="16" fill="' + senses[i][1] + '" stroke="' + ink + '"/>';
          body += text(x, y + 5, senses[i][0], 13, navy);
        }
        return frame(640, 250, "People and computers share senses", body);
      },
      "hci-domains": function () {
        var items = [["Health", mint], ["Banking", sky], ["Education", cream], ["Messages", blush]];
        var body = "";
        for (var i = 0; i < items.length; i++) {
          var x = 30 + (i % 4) * 150;
          body += round(x, 80, 136, 80, items[i][1]);
          body += text(x + 68, 126, items[i][0], 15, navy);
        }
        return frame(640, 210, "HCI shows up in everyday systems", body);
      },
      er: function () {
        return frame(640, 220, "Entity, attribute, relationship",
          round(30, 70, 140, 70, sky) + text(100, 112, "Student", 16, navy) +
          '<path d="M170 105 H230" stroke="' + ink + '" stroke-width="2"/>' +
          '<polygon points="250,70 330,105 250,140 170,105" fill="' + cream + '" stroke="' + ink + '" transform="translate(80,0)"/>' +
          text(330, 110, "borrows", 13, amber) +
          '<path d="M410 105 H450" stroke="' + ink + '" stroke-width="2"/>' +
          round(450, 70, 140, 70, mint) + text(520, 112, "Book", 16, teal) +
          text(100, 175, "name, roll no", 12, ink, "middle", 500)
        );
      },
      keys: function () {
        return frame(640, 220, "Primary key identifies. Foreign key connects.",
          round(24, 60, 280, 120, sky) +
          text(164, 96, "STUDENT", 14, navy) +
          text(164, 124, "roll_no  PK", 14, teal) +
          text(164, 150, "name", 14, ink, "middle", 500) +
          round(330, 60, 280, 120, cream) +
          text(470, 96, "BORROW", 14, amber) +
          text(470, 124, "roll_no  FK", 14, rose) +
          text(470, 150, "book_id", 14, ink, "middle", 500)
        );
      },
      variable: function () {
        return frame(640, 210, "A variable is a named container",
          round(40, 70, 250, 90, cream) +
          text(165, 108, "name", 13, amber) +
          text(165, 136, '"Ali"', 22, navy) +
          text(360, 100, "Start with a letter.", 15, ink, "start") +
          text(360, 126, "No spaces.", 15, ink, "start") +
          text(360, 152, "Do not use keywords.", 15, teal, "start")
        );
      },
      loop: function () {
        return frame(640, 210, "Loops repeat while the condition holds",
          '<circle cx="160" cy="120" r="58" fill="none" stroke="' + teal + '" stroke-width="8"/>' +
          text(160, 116, "again", 16, teal) +
          round(300, 55, 280, 110, sky) +
          text(440, 100, "for · count is known", 14, navy) +
          text(440, 128, "while · test each time", 14, teal)
        );
      },
      "selection-stmt": function () {
        return frame(640, 230, "Selection chooses a path",
          '<polygon points="200,50 300,100 200,150 100,100" fill="' + cream + '" stroke="' + ink + '" stroke-width="1.6"/>' +
          text(200, 105, "score ≥ 50?", 13, navy) +
          round(340, 60, 120, 40, mint) + text(400, 86, "pass", 14, teal) +
          round(340, 130, 120, 40, blush) + text(400, 156, "retry", 14, rose) +
          '<path d="M300 90 H340 M200 150 V150 H340" stroke="' + ink + '" stroke-width="1.5" fill="none"/>'
        );
      },
      bitwise: function () {
        return frame(640, 220, "Bitwise AND keeps shared 1s",
          text(200, 80, "1 0 1 1", 28, navy) +
          text(200, 120, "1 1 0 1", 28, teal) +
          '<path d="M80 136 H320" stroke="' + ink + '"/>' +
          text(200, 176, "1 0 0 1", 28, rose) +
          text(460, 120, "AND", 20, amber, "start")
        );
      },
      file: function () {
        return frame(640, 210, "Open, use, then close the file",
          round(40, 70, 150, 80, sky) + text(115, 116, "open", 16, navy) +
          round(230, 70, 150, 80, cream) + text(305, 116, "read / write", 15, amber) +
          round(420, 70, 150, 80, mint) + text(495, 116, "close", 16, teal) +
          '<path d="M190 110 H230 M380 110 H420" stroke="' + ink + '" stroke-width="2"/>'
        );
      },
      function: function () {
        return frame(640, 210, "A function names a repeated job",
          text(70, 120, "marks", 16, navy, "start") +
          '<path d="M140 112 H200" stroke="' + ink + '" stroke-width="2"/>' +
          round(200, 70, 200, 80, mint) + text(300, 104, "average()", 16, teal) + text(300, 128, "add, then divide", 12, ink, "middle", 500) +
          '<path d="M400 112 H460" stroke="' + ink + '" stroke-width="2"/>' +
          text(480, 120, "result", 16, navy, "start")
        );
      },
      pandas: function () {
        var body = "";
        var grid = [["name", "marks"], ["Ali", "80"], ["Sara", "91"]];
        for (var r = 0; r < 3; r++) {
          for (var c = 0; c < 2; c++) {
            body += '<rect x="' + (180 + c * 140) + '" y="' + (56 + r * 40) + '" width="140" height="40" fill="' + (r === 0 ? navy : paper) + '" stroke="' + ink + '"/>';
            body += text(250 + c * 140, 82 + r * 40, grid[r][c], 14, r === 0 ? "#fff" : ink);
          }
        }
        body += text(40, 110, "DataFrame", 16, teal, "start");
        body += text(40, 136, "a table in", 14, ink, "start", 500);
        body += text(40, 158, "Python", 14, ink, "start", 500);
        return frame(640, 220, "Pandas holds rows and columns", body);
      },
      missing: function () {
        var vals = ["12", "—", "18", "15"];
        var body = "";
        for (var i = 0; i < 4; i++) {
          body += round(40 + i * 140, 80, 110, 60, vals[i] === "—" ? blush : paper);
          body += text(95 + i * 140, 116, vals[i], 20, vals[i] === "—" ? rose : navy);
        }
        body += text(320, 180, "Drop the gap, or fill it with a fair value", 14, teal);
        return frame(640, 210, "Missing values need a decision", body);
      },
      spread: function () {
        var dots = [40, 70, 90, 110, 130, 150, 210, 240];
        var body = '<path d="M40 140 H560" stroke="' + ink + '"/>';
        for (var i = 0; i < dots.length; i++) {
          body += '<circle cx="' + (80 + dots[i]) + '" cy="140" r="7" fill="' + (i === 6 ? rose : teal) + '"/>';
        }
        body += '<path d="M250 80 V170" stroke="' + navy + '" stroke-width="2" stroke-dasharray="4 3"/>';
        body += text(250, 70, "mean", 12, navy);
        body += text(430, 70, "outlier", 12, rose);
        return frame(640, 210, "Spread shows distance from the centre", body);
      },
      flowchart: function () {
        return frame(640, 240, "Flowcharts use agreed shapes",
          '<ellipse cx="140" cy="70" rx="60" ry="22" fill="' + mint + '" stroke="' + ink + '"/>' + text(140, 75, "start") +
          round(70, 110, 140, 40, sky) + text(140, 136, "read n") +
          '<polygon points="140,170 210,205 140,240 70,205" fill="' + cream + '" stroke="' + ink + '"/>' +
          text(140, 210, "n > 0?", 12) +
          round(360, 170, 160, 44, blush) + text(440, 198, "handle error", 13, rose) +
          '<path d="M140 92 V110 M140 150 V170 M210 205 H360" stroke="' + ink + '" fill="none"/>'
        );
      },
      linegraph: function () {
        return frame(640, 220, "A line graph shows change over time",
          '<path d="M60 180 H560 M60 180 V40" stroke="' + ink + '"/>' +
          '<path d="M80 150 L180 140 L280 100 L380 110 L480 60" fill="none" stroke="' + teal + '" stroke-width="3"/>' +
          '<circle cx="480" cy="60" r="5" fill="' + rose + '"/>' +
          text(80, 200, "time →", 12, ink, "start", 500)
        );
      },
      pie: function () {
        return frame(640, 220, "A pie chart shows parts of a whole",
          '<path d="M220 120 L220 40 A80 80 0 0 1 290 150 Z" fill="' + sky + '" stroke="' + ink + '"/>' +
          '<path d="M220 120 L290 150 A80 80 0 0 1 150 160 Z" fill="' + mint + '" stroke="' + ink + '"/>' +
          '<path d="M220 120 L150 160 A80 80 0 0 1 220 40 Z" fill="' + cream + '" stroke="' + ink + '"/>' +
          text(430, 90, "Slice = share", 15, navy, "start") +
          text(430, 118, "of one whole", 15, ink, "start", 500)
        );
      },
      hist: function () {
        var hs = [40, 80, 130, 90, 50];
        var body = "";
        for (var i = 0; i < hs.length; i++) {
          body += '<rect x="' + (60 + i * 70) + '" y="' + (180 - hs[i]) + '" width="60" height="' + hs[i] + '" fill="' + sky + '" stroke="' + ink + '"/>';
        }
        body += text(460, 120, "Bars touch.", 15, navy, "start");
        body += text(460, 146, "They count ranges.", 14, ink, "start", 500);
        return frame(640, 220, "A histogram shows how values cluster", body);
      },
      scatter: function () {
        var pts = [[80, 160], [140, 140], [200, 150], [250, 110], [320, 100], [380, 80], [450, 70]];
        var body = '<path d="M50 180 H520 M50 180 V40" stroke="' + ink + '"/>';
        for (var i = 0; i < pts.length; i++) {
          body += '<circle cx="' + pts[i][0] + '" cy="' + pts[i][1] + '" r="6" fill="' + teal + '"/>';
        }
        body += '<path d="M70 170 L470 60" stroke="' + rose + '" stroke-width="1.6" stroke-dasharray="5 4"/>';
        body += text(360, 200, "Each dot is one pair", 13, navy);
        return frame(640, 230, "Scatter plots hint at a relationship", body);
      },
      box: function () {
        return frame(640, 200, "A box plot shows the middle 50%",
          '<path d="M40 100 H560" stroke="' + ink + '" stroke-width="2"/>' +
          '<path d="M80 80 V120 M520 80 V120" stroke="' + ink + '" stroke-width="2"/>' +
          '<rect x="180" y="70" width="220" height="60" fill="' + sky + '" stroke="' + ink + '"/>' +
          '<path d="M300 70 V130" stroke="' + rose + '" stroke-width="3"/>' +
          text(300, 165, "median", 13, rose) +
          text(120, 165, "min", 12, ink) +
          text(500, 165, "max", 12, ink)
        );
      },
      iot: function () {
        return frame(640, 230, "Things sense, send, and act",
          round(30, 80, 140, 70, mint) + text(100, 120, "sensor", 15, teal) +
          '<path d="M170 115 H230" stroke="' + ink + '" stroke-width="2"/>' +
          '<ellipse cx="310" cy="115" rx="70" ry="36" fill="' + sky + '" stroke="' + ink + '"/>' + text(310, 120, "cloud", 15, navy) +
          '<path d="M380 115 H430" stroke="' + ink + '" stroke-width="2"/>' +
          round(430, 80, 160, 70, cream) + text(510, 120, "action", 15, amber)
        );
      },
      security: function () {
        return frame(640, 220, "Protect the shared work",
          '<rect x="70" y="80" width="90" height="70" rx="8" fill="' + mint + '" stroke="' + ink + '"/>' +
          '<path d="M90 80 V64 a25 25 0 0 1 50 0 V80" fill="none" stroke="' + ink + '" stroke-width="3"/>' +
          text(115, 175, "lock", 13, teal) +
          round(250, 70, 150, 90, blush) + text(325, 110, "phish", 16, rose) + text(325, 134, "fake link", 12, ink, "middle", 500) +
          round(430, 70, 160, 90, cream) + text(510, 110, "update", 16, amber) + text(510, 134, "and back up", 12, ink, "middle", 500)
        );
      },
      equity: function () {
        return frame(640, 220, "Equal tools, and a ramp where needed",
          '<rect x="80" y="120" width="140" height="50" fill="' + sky + '" stroke="' + ink + '"/>' +
          text(150, 150, "same desk", 14, navy) +
          '<path d="M360 170 L500 90 H560 V170 Z" fill="' + mint + '" stroke="' + ink + '"/>' +
          text(470, 150, "ramp", 14, teal) +
          text(80, 70, "Access is the door. Equity is the ramp.", 15, ink, "start", 650)
        );
      },
      beachhead: function () {
        return frame(640, 210, "Win a small market, then expand",
          '<circle cx="160" cy="120" r="50" fill="' + cream + '" stroke="' + ink + '"/>' +
          text(160, 116, "first", 14, amber) + text(160, 136, "customers", 11, ink, "middle", 500) +
          '<path d="M220 120 H300" stroke="' + teal + '" stroke-width="3"/>' +
          '<circle cx="420" cy="120" r="80" fill="' + sky + '" stroke="' + ink + '"/>' +
          text(420, 124, "wider market", 14, navy)
        );
      },
      entrepreneur: function () {
        return frame(640, 210, "A problem can become a service",
          '<circle cx="120" cy="110" r="40" fill="' + cream + '" stroke="' + amber + '" stroke-width="3"/>' +
          text(120, 116, "idea", 14, amber) +
          '<path d="M170 110 H250" stroke="' + ink + '" stroke-width="2"/>' +
          round(260, 70, 140, 80, sky) + text(330, 116, "who hurts?", 14, navy) +
          '<path d="M400 110 H450" stroke="' + ink + '" stroke-width="2"/>' +
          round(450, 70, 140, 80, mint) + text(520, 116, "offer", 14, teal)
        );
      },
      prototype: function () {
        var words = ["sketch", "test", "learn", "improve"];
        var body = "";
        for (var i = 0; i < words.length; i++) {
          body += '<circle cx="' + (80 + i * 140) + '" cy="110" r="40" fill="' + (i % 2 ? mint : cream) + '" stroke="' + ink + '"/>';
          body += text(80 + i * 140, 115, words[i], 12, navy);
          if (i < 3) body += '<path d="M' + (122 + i * 140) + ' 110 H' + (138 + i * 140) + '" stroke="' + ink + '" stroke-width="2"/>';
        }
        return frame(640, 200, "A prototype is a cheap first try", body);
      },
      mvp: function () {
        return frame(640, 220, "MVP is the smallest real test",
          '<rect x="80" y="50" width="200" height="140" rx="12" fill="' + sky + '" stroke="' + ink + '"/>' +
          '<rect x="110" y="78" width="140" height="90" rx="10" fill="' + cream + '" stroke="' + ink + '"/>' +
          '<rect x="140" y="104" width="80" height="44" rx="8" fill="' + mint + '" stroke="' + teal + '" stroke-width="2"/>' +
          text(180, 132, "MVP", 14, teal) +
          text(360, 100, "One risky guess.", 16, navy, "start") +
          text(360, 128, "Real users.", 16, ink, "start", 500) +
          text(360, 156, "Nothing extra.", 16, teal, "start")
        );
      }
    };
  }

  global.SketchDiagrams = {
    render: function (id) {
      var all = builders();
      return all[id] ? all[id]() : "";
    }
  };
})(window);
