(function () {
  const ink = "#243e73";
  const gold = "#a67c2d";
  const teal = "#1f6f6a";
  const paper = "#fffdf8";
  const soft = "#e7edf8";

  function svg(w, h, body) {
    return `<svg viewBox="0 0 ${w} ${h}" role="img" xmlns="http://www.w3.org/2000/svg">${body}</svg>`;
  }

  function label(x, y, text, extra) {
    return `<text x="${x}" y="${y}" fill="${ink}" font-family="Roboto, sans-serif" font-size="14" text-anchor="middle" ${extra || ""}>${text}</text>`;
  }

  function gateShape(kind) {
    if (kind === "and" || kind === "nand") {
      return `<path d="M20 30 H70 V70 A30 30 0 0 1 70 130 H20 Z" fill="${paper}" stroke="${ink}" stroke-width="3"/>`;
    }
    if (kind === "not") {
      return `<path d="M24 36 L110 80 L24 124 Z" fill="${paper}" stroke="${ink}" stroke-width="3"/>`;
    }
    const extra = kind === "xor" || kind === "xnor"
      ? `<path d="M28 30 Q58 80 28 130" fill="none" stroke="${ink}" stroke-width="3"/>`
      : "";
    return `${extra}<path d="M20 30 Q70 30 90 80 Q70 130 20 130 Q50 80 20 30 Z" fill="${paper}" stroke="${ink}" stroke-width="3"/>`;
  }

  function gate(kind) {
    const title = {
      and: "AND", or: "OR", not: "NOT", nand: "NAND", nor: "NOR", xor: "XOR", xnor: "XNOR"
    }[kind] || "GATE";
    const bubbled = kind === "nand" || kind === "nor" || kind === "xnor" || kind === "not";
    const bodyRight = kind === "not" ? 110 : (kind === "and" || kind === "nand" ? 100 : 90);
    const bubbleX = bodyRight + 12;
    const lineStart = bubbled ? bubbleX + 8 : bodyRight;
    const lineEnd = lineStart + 36;
    const bubble = bubbled
      ? `<circle cx="${bubbleX}" cy="80" r="8" fill="${paper}" stroke="${ink}" stroke-width="3"/>`
      : "";
    const nameX = kind === "not" ? 58 : 78;
    return svg(280, 170, `
      ${gateShape(kind)}
      ${bubble}
      <line x1="0" y1="${kind === "not" ? 80 : 60}" x2="20" y2="${kind === "not" ? 80 : 60}" stroke="${ink}" stroke-width="3"/>
      ${kind === "not" ? "" : `<line x1="0" y1="100" x2="20" y2="100" stroke="${ink}" stroke-width="3"/>`}
      <line x1="${lineStart}" y1="80" x2="${lineEnd}" y2="80" stroke="${ink}" stroke-width="3"/>
      ${label(nameX, 84, title)}
      ${label(14, kind === "not" ? 72 : 52, "A")}
      ${kind === "not" ? "" : label(14, 118, "B")}
      ${label(lineEnd + 14, 76, "Y", 'text-anchor="start"')}
    `);
  }

  const diagrams = {
    stairs() {
      return svg(520, 180, `
        <rect x="16" y="16" width="230" height="148" rx="12" fill="${soft}"/>
        <rect x="274" y="16" width="230" height="148" rx="12" fill="#f8efd8"/>
        ${label(130, 40, "Discrete — stairs")}
        <path d="M40 140 H80 V110 H120 V80 H160 V50 H200" fill="none" stroke="${ink}" stroke-width="4"/>
        ${label(390, 40, "Continuous — ramp")}
        <path d="M300 140 L470 48" fill="none" stroke="${gold}" stroke-width="4"/>
      `);
    },
    waves() {
      let sine = "";
      for (let x = 0; x <= 200; x += 4) {
        const y = 70 - Math.sin((x / 200) * Math.PI * 4) * 28;
        sine += (x === 0 ? "M" : "L") + (40 + x) + " " + y + " ";
      }
      return svg(520, 180, `
        ${label(140, 24, "Analog — sine")}
        <path d="${sine}" fill="none" stroke="${teal}" stroke-width="3"/>
        <line x1="40" y1="70" x2="250" y2="70" stroke="${ink}" stroke-width="1"/>
        ${label(390, 24, "Digital — square")}
        <path d="M290 98 H340 V42 H390 V98 H440 V42 H490" fill="none" stroke="${ink}" stroke-width="3"/>
        ${label(470, 36, "HIGH 1", 'font-size="12"')}
        ${label(470, 116, "LOW 0", 'font-size="12"')}
      `);
    },
    gate(block) {
      return gate(block.gate || "and");
    },
    circuit() {
      return svg(560, 200, `
        ${label(40, 40, "A", 'text-anchor="start"')}
        ${label(40, 80, "B", 'text-anchor="start"')}
        ${label(40, 150, "C", 'text-anchor="start"')}
        <line x1="60" y1="36" x2="120" y2="36" stroke="${ink}" stroke-width="3"/>
        <line x1="60" y1="76" x2="120" y2="76" stroke="${ink}" stroke-width="3"/>
        <path d="M120 20 H170 V80 A28 28 0 0 1 170 136 H120 Z" fill="${paper}" stroke="${ink}" stroke-width="3"/>
        ${label(150, 84, "AND", 'font-size="13"')}
        <line x1="198" y1="78" x2="250" y2="78" stroke="${ink}" stroke-width="3"/>
        <line x1="60" y1="146" x2="250" y2="146" stroke="${ink}" stroke-width="3"/>
        <path d="M250 60 Q310 60 330 112 Q310 164 250 164 Q286 112 250 60 Z" fill="${paper}" stroke="${ink}" stroke-width="3"/>
        ${label(300, 118, "OR", 'font-size="13"')}
        <line x1="360" y1="112" x2="430" y2="112" stroke="${teal}" stroke-width="3"/>
        ${label(470, 116, "Y = A·B + C", 'text-anchor="start" font-size="13"')}
      `);
    },
    kmap2() {
      return svg(420, 200, `
        ${label(210, 24, "2-variable K-map")}
        <rect x="90" y="50" width="100" height="56" fill="#f8efd8" stroke="${ink}"/>
        <rect x="190" y="50" width="100" height="56" fill="${paper}" stroke="${ink}"/>
        <rect x="90" y="106" width="100" height="56" fill="${paper}" stroke="${ink}"/>
        <rect x="190" y="106" width="100" height="56" fill="#d9efe8" stroke="${ink}"/>
        ${label(140, 44, "B = 0", 'font-size="12"')}
        ${label(240, 44, "B = 1", 'font-size="12"')}
        ${label(70, 82, "A=0", 'font-size="12"')}
        ${label(70, 140, "A=1", 'font-size="12"')}
        ${label(140, 82, "A'B'")}
        ${label(240, 82, "A'B")}
        ${label(140, 140, "AB'")}
        ${label(240, 140, "AB")}
      `);
    },
    kmap3() {
      const cols = ["00", "01", "11", "10"];
      let cells = "";
      cols.forEach((c, i) => {
        cells += `<rect x="${80 + i * 78}" y="70" width="78" height="46" fill="${paper}" stroke="${ink}"/>`;
        cells += `<rect x="${80 + i * 78}" y="116" width="78" height="46" fill="${i === 0 || i === 3 ? "#d9efe8" : paper}" stroke="${ink}"/>`;
        cells += label(119 + i * 78, 58, c, 'font-size="12"');
        cells += label(119 + i * 78, 98, "m" + [0, 1, 3, 2][i], 'font-size="13"');
        cells += label(119 + i * 78, 144, "m" + [4, 5, 7, 6][i], 'font-size="13"');
      });
      return svg(460, 190, `
        ${label(230, 22, "3-variable K-map, Gray code columns")}
        ${label(40, 98, "A=0", 'font-size="12"')}
        ${label(40, 144, "A=1", 'font-size="12"')}
        ${cells}
      `);
    },
    logisim() {
      return svg(520, 180, `
        <rect x="16" y="20" width="120" height="140" rx="8" fill="${soft}" stroke="${ink}"/>
        ${label(76, 48, "Gates", 'font-size="13"')}
        ${label(76, 78, "Wiring", 'font-size="13"')}
        ${label(76, 108, "Poke", 'font-size="13"')}
        <rect x="150" y="20" width="250" height="140" rx="8" fill="${paper}" stroke="${ink}"/>
        ${label(275, 48, "Canvas")}
        <circle cx="210" cy="100" r="8" fill="#39d353"/>
        <line x1="218" y1="100" x2="300" y2="100" stroke="#39d353" stroke-width="4"/>
        ${label(430, 70, "1 bright green", 'font-size="12" text-anchor="start"')}
        ${label(430, 100, "0 dark green", 'font-size="12" text-anchor="start"')}
        ${label(430, 130, "blue unknown", 'font-size="12" text-anchor="start"')}
        ${label(430, 160, "red error", 'font-size="12" text-anchor="start"')}
      `);
    },
    waterfall() {
      const names = ["Requirements", "Design", "Code", "Test", "Deploy", "Maintain"];
      const boxes = names.map((name, i) => {
        const y = 16 + i * 26;
        return `<rect x="${20 + i * 18}" y="${y}" width="200" height="22" rx="6" fill="${i % 2 ? soft : "#f8efd8"}" stroke="${ink}"/>${label(120 + i * 18, y + 16, name, 'font-size="12"')}`;
      }).join("");
      return svg(420, 190, boxes + label(330, 40, "No easy", 'font-size="13"') + label(330, 60, "way back", 'font-size="13"'));
    },
    agile() {
      return svg(420, 180, `
        <circle cx="160" cy="90" r="62" fill="none" stroke="${teal}" stroke-width="8" stroke-dasharray="14 8"/>
        ${label(160, 86, "Sprint")}
        ${label(160, 106, "2–4 weeks", 'font-size="12"')}
        ${label(320, 50, "Plan", 'font-size="13"')}
        ${label(340, 90, "Build", 'font-size="13"')}
        ${label(330, 130, "Feedback", 'font-size="13"')}
      `);
    },
    osi() {
      const layers = [
        ["7 Application", "#243e73"],
        ["6 Presentation", "#31559a"],
        ["5 Session", "#3d6cb8"],
        ["4 Transport", "#1f6f6a"],
        ["3 Network", "#2e8a84"],
        ["2 Data Link", "#a67c2d"],
        ["1 Physical", "#c4a35a"]
      ];
      const body = layers.map((layer, i) => {
        const y = 8 + i * 24;
        return `<rect x="40" y="${y}" width="280" height="22" rx="6" fill="${layer[1]}"/><text x="180" y="${y + 16}" fill="white" font-size="13" text-anchor="middle" font-family="Roboto, sans-serif">${layer[0]}</text>`;
      }).join("");
      return svg(360, 190, body);
    },
    tcpip() {
      const rows = [
        ["Application", "OSI 7, 6, 5"],
        ["Transport", "OSI 4"],
        ["Internet", "OSI 3"],
        ["Network Access", "OSI 2, 1"]
      ];
      const body = rows.map((row, i) => {
        const y = 20 + i * 38;
        return `<rect x="20" y="${y}" width="160" height="30" rx="6" fill="${ink}"/><text x="100" y="${y + 20}" fill="white" font-size="13" text-anchor="middle" font-family="Roboto, sans-serif">${row[0]}</text><text x="200" y="${y + 20}" fill="${ink}" font-size="13" text-anchor="start" font-family="Roboto, sans-serif">${row[1]}</text>`;
      }).join("");
      return svg(420, 180, body);
    },
    bubble() {
      const rows = ["8 4 1 9 3", "4 8 1 9 3", "4 1 8 9 3", "4 1 8 3 9"];
      const body = rows.map((row, i) => label(200, 36 + i * 32, row, 'font-size="18" font-family="ui-monospace, monospace"')).join("");
      return svg(400, 160, `<rect width="400" height="160" fill="${soft}"/>${label(200, 20, "Pass 1, 9 sinks to the end", 'font-size="12"')}${body}`);
    },
    selection() {
      return svg(420, 150, `
        <rect width="420" height="150" fill="#f8efd8"/>
        ${label(210, 36, "Pick the smallest, park it at the front")}
        ${label(210, 78, "8  4  1  9  3", 'font-size="20"')}
        ${label(210, 112, "1  |  8  4  9  3", 'font-size="20"')}
      `);
    },
    binary() {
      return svg(520, 160, `
        ${label(260, 28, "Sorted list, find 3")}
        ${[1, 2, 3, 4, 5, 6, 7, 8].map((n, i) => {
          const x = 30 + i * 60;
          const fill = n === 4 ? "#f8efd8" : paper;
          return `<rect x="${x}" y="48" width="48" height="36" rx="6" fill="${fill}" stroke="${ink}"/>${label(x + 24, 72, n)}`;
        }).join("")}
        ${label(260, 120, "Mid value 4. 3 is smaller, go left.", 'font-size="13"')}
        ${label(260, 144, "Then mid 2, go right. Then 3 found.", 'font-size="13"')}
      `);
    },
    languages() {
      const rows = [
        ["Low", "01010101", soft],
        ["Mid", "MOV AX, BX", "#f8efd8"],
        ["High", 'print("Hello")', "#d9efe8"]
      ];
      return svg(460, 160, rows.map((row, i) => {
        const y = 18 + i * 46;
        return `<rect x="20" y="${y}" width="420" height="38" rx="8" fill="${row[2]}" stroke="${ink}"/>${label(80, y + 24, row[0])}${label(260, y + 24, row[1], 'font-family="ui-monospace, monospace"')}`;
      }).join(""));
    },
    flow() {
      return svg(240, 220, `
        <rect x="50" y="10" width="140" height="36" rx="18" fill="${ink}"/>
        <text x="120" y="34" fill="white" text-anchor="middle" font-size="14" font-family="Roboto, sans-serif">Start</text>
        <rect x="50" y="70" width="140" height="36" fill="${soft}" stroke="${ink}"/>
        ${label(120, 94, "Statement")}
        <rect x="50" y="130" width="140" height="36" fill="${soft}" stroke="${ink}"/>
        ${label(120, 154, "Statement")}
        <rect x="50" y="186" width="140" height="28" rx="14" fill="${teal}"/>
        <text x="120" y="206" fill="white" text-anchor="middle" font-size="14" font-family="Roboto, sans-serif">End</text>
        <path d="M120 46 V70 M120 106 V130 M120 166 V186" stroke="${ink}" stroke-width="2"/>
      `);
    },
    keys() {
      return svg(520, 170, `
        <rect x="16" y="30" width="150" height="110" rx="10" fill="${soft}" stroke="${ink}"/>
        ${label(90, 58, "Candidate keys")}
        ${label(90, 86, "EmpID")}
        ${label(90, 110, "License")}
        ${label(90, 134, "Passport")}
        <rect x="190" y="30" width="140" height="110" rx="10" fill="#d9efe8" stroke="${ink}"/>
        ${label(260, 70, "Primary")}
        ${label(260, 100, "EmpID")}
        <rect x="354" y="30" width="150" height="110" rx="10" fill="#f8efd8" stroke="${ink}"/>
        ${label(428, 70, "Alternate")}
        ${label(428, 100, "License, Passport", 'font-size="12"')}
      `);
    },
    er() {
      return svg(520, 180, `
        <rect x="20" y="60" width="120" height="48" fill="${soft}" stroke="${ink}"/>
        ${label(80, 90, "STUDENT")}
        <ellipse cx="250" cy="40" rx="54" ry="22" fill="${paper}" stroke="${ink}"/>
        ${label(250, 45, "Name")}
        <polygon points="250,70 310,100 250,130 190,100" fill="#f8efd8" stroke="${ink}"/>
        ${label(250, 104, "Enrolls")}
        <rect x="370" y="76" width="120" height="48" fill="${soft}" stroke="${ink}"/>
        ${label(430, 106, "COURSE")}
        <line x1="140" y1="84" x2="190" y2="96" stroke="${ink}" stroke-width="2"/>
        <line x1="310" y1="104" x2="370" y2="100" stroke="${ink}" stroke-width="2"/>
      `);
    },
    library() {
      return svg(540, 170, `
        <rect x="16" y="50" width="130" height="60" rx="6" fill="${soft}" stroke="${ink}"/>
        ${label(80, 76, "MEMBER")}
        ${label(80, 96, "1", 'font-size="12"')}
        <rect x="200" y="40" width="150" height="80" rx="6" fill="#f8efd8" stroke="${ink}"/>
        ${label(275, 68, "BorrowRecord")}
        ${label(275, 90, "M        M", 'font-size="12"')}
        <rect x="400" y="50" width="120" height="60" rx="6" fill="${soft}" stroke="${ink}"/>
        ${label(460, 76, "BOOK")}
        ${label(460, 96, "1", 'font-size="12"')}
        <line x1="146" y1="80" x2="200" y2="80" stroke="${ink}" stroke-width="2"/>
        <line x1="350" y1="80" x2="400" y2="80" stroke="${ink}" stroke-width="2"/>
      `);
    },
    integrity() {
      return svg(520, 160, `
        <rect x="20" y="30" width="180" height="100" rx="8" fill="${soft}" stroke="${ink}"/>
        ${label(110, 58, "Parent STUDENT")}
        ${label(110, 84, "101 Ali")}
        ${label(110, 108, "102 Sara")}
        <rect x="300" y="30" width="190" height="100" rx="8" fill="#f8efd8" stroke="${ink}"/>
        ${label(395, 58, "Child RESULT")}
        ${label(395, 84, "101 allowed")}
        ${label(395, 108, "999 rejected")}
        <path d="M200 80 H300" stroke="${teal}" stroke-width="3"/>
      `);
    },
    iot() {
      const bits = ["Sensor", "Wi-Fi", "Cloud", "AI", "Actuator"];
      return svg(540, 120, bits.map((bit, i) => {
        const x = 16 + i * 106;
        return `<rect x="${x}" y="36" width="96" height="48" rx="10" fill="${i === 3 ? "#d9efe8" : soft}" stroke="${ink}"/>${label(x + 48, 66, bit, 'font-size="13"')}`;
      }).join(""));
    },
    bars() {
      const vals = [2, 5, 8, 4];
      const names = ["0-1h", "1-3h", "3-5h", "5h+"];
      const body = vals.map((v, i) => {
        const x = 50 + i * 90;
        const h = v * 12;
        return `<rect x="${x}" y="${130 - h}" width="48" height="${h}" fill="${i === 2 ? teal : ink}"/>${label(x + 24, 148, names[i], 'font-size="12"')}`;
      }).join("");
      return svg(420, 170, body + label(210, 20, "Phone hours, class survey"));
    },
    pie() {
      return svg(280, 180, `
        <circle cx="100" cy="90" r="60" fill="${soft}" stroke="${ink}"/>
        <path d="M100 90 L100 30 A60 60 0 0 1 152 120 Z" fill="${teal}"/>
        ${label(210, 70, "Pass", 'text-anchor="start"')}
        ${label(210, 100, "Needs help", 'text-anchor="start"')}
      `);
    },
    sources() {
      return svg(360, 180, `
        <polygon points="180,20 300,150 60,150" fill="none" stroke="${ink}" stroke-width="3"/>
        <line x1="90" y1="110" x2="270" y2="110" stroke="${gold}"/>
        <line x1="120" y1="70" x2="240" y2="70" stroke="${gold}"/>
        ${label(180, 58, "Tertiary", 'font-size="12"')}
        ${label(180, 98, "Secondary", 'font-size="12"')}
        ${label(180, 140, "Primary", 'font-size="13"')}
      `);
    },
    inquiry() {
      const steps = ["Question", "Search", "Collect", "Analyze", "Create"];
      return svg(540, 110, steps.map((step, i) => {
        const x = 16 + i * 106;
        return `<circle cx="${x + 40}" cy="46" r="28" fill="${i === 0 ? ink : soft}" stroke="${ink}"/><text x="${x + 40}" y="50" fill="${i === 0 ? "white" : ink}" font-size="11" text-anchor="middle" font-family="Roboto, sans-serif">${step}</text>`;
      }).join(""));
    }
  };

  window.TYDiagrams = {
    draw(block) {
      const fn = diagrams[block.name];
      if (!fn) return "";
      return fn(block);
    }
  };
})();
