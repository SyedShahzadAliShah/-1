/* Pack the booklet into A4 content sheets.
   A block that would spill past the bottom of the current page is scaled
   onto that page when the type stays readable. Taller blocks are split
   (tables by rows, lists by items, code by lines) so a few leftover lines
   never land alone on the next page. */
(function () {
  var SQUEEZE = 0.78;
  var MIN_SCALE = 0.72;

  function fit() {
    if (document.body.dataset.pagefit === "1") return;
    var meter = document.createElement("div");
    meter.className = "sheet";
    meter.style.cssText = "position:absolute;visibility:hidden;left:0;top:0;";
    document.body.appendChild(meter);
    var PAGE = meter.clientHeight;
    meter.remove();
    if (!PAGE || PAGE < 200) return;
    document.body.dataset.pagefit = "1";

    var FIT_LIMIT = PAGE;
    function chunkCap(partCount) {
      return partCount ? PAGE : FIT_LIMIT;
    }
    var probe = document.createElement("div");
    probe.className = "sheet-inner";
    probe.style.cssText = "position:absolute;visibility:hidden;left:0;top:0;width:180mm;";
    document.body.appendChild(probe);

    function detachProbe() {
      while (probe.firstChild) probe.removeChild(probe.firstChild);
    }

    function isHeading(el) {
      return /^H[1-4]$/.test(el.tagName);
    }

    function splitTable(table) {
      var rows = Array.prototype.slice.call(table.rows);
      if (rows.length < 2) return [table];
      var header = rows[0].querySelector("th") ? rows[0] : null;
      var data = header ? rows.slice(1) : rows.slice();
      detachProbe();
      var parts = [];
      var cur = table.cloneNode(false);
      cur.removeAttribute("id");
      if (header) cur.appendChild(header.cloneNode(true));
      probe.appendChild(cur);
      data.forEach(function (row) {
        cur.appendChild(row);
        if (probe.scrollHeight > chunkCap(parts.length) && cur.rows.length > (header ? 2 : 1)) {
          cur.removeChild(row);
          cur.remove();
          parts.push(cur);
          cur = table.cloneNode(false);
          cur.removeAttribute("id");
          if (header) cur.appendChild(header.cloneNode(true));
          probe.appendChild(cur);
          cur.appendChild(row);
        }
      });
      if (cur.rows.length > (header ? 1 : 0)) parts.push(cur);
      detachProbe();
      return parts.length ? parts : [table];
    }

    function splitPre(pre) {
      var lines = pre.innerText.replace(/\s+$/, "").split("\n");
      if (lines.length < 2) return [pre];
      detachProbe();
      var parts = [];
      var cur = pre.cloneNode(false);
      var buf = [];
      probe.appendChild(cur);
      lines.forEach(function (line) {
        buf.push(line);
        cur.textContent = buf.join("\n");
        if (probe.scrollHeight > chunkCap(parts.length) && buf.length > 1) {
          buf.pop();
          cur.textContent = buf.join("\n");
          cur.remove();
          parts.push(cur);
          cur = pre.cloneNode(false);
          probe.appendChild(cur);
          buf = [line];
          cur.textContent = line;
        }
      });
      if (buf.length) parts.push(cur);
      detachProbe();
      return parts.length ? parts : [pre];
    }

    function splitWords(el) {
      var words = el.textContent.split(/\s+/).filter(Boolean);
      if (words.length < 8) return [el];
      detachProbe();
      var parts = [];
      var cur = el.cloneNode(false);
      cur.removeAttribute("id");
      var buf = [];
      probe.appendChild(cur);
      words.forEach(function (word) {
        buf.push(word);
        cur.textContent = buf.join(" ");
        if (probe.scrollHeight > chunkCap(parts.length) && buf.length > 8) {
          buf.pop();
          cur.textContent = buf.join(" ");
          cur.remove();
          parts.push(cur);
          cur = el.cloneNode(false);
          cur.removeAttribute("id");
          probe.appendChild(cur);
          buf = [word];
          cur.textContent = word;
        }
      });
      if (buf.length) parts.push(cur);
      detachProbe();
      return parts.length ? parts : [el];
    }

    function splitList(list) {
      var items = Array.prototype.slice.call(list.children);
      if (items.length < 2) {
        if (items.length === 1) {
          var bits = splitElement(items[0]);
          if (bits.length < 2) return [list];
          return bits.map(function (bit, i) {
            var wrap = list.cloneNode(false);
            wrap.removeAttribute("id");
            if (i > 0) wrap.classList.add("split-continued");
            else if (list.tagName === "OL") wrap.start = list.start || 1;
            wrap.appendChild(bit);
            return wrap;
          });
        }
        return [list];
      }
      detachProbe();
      var parts = [];
      var number = list.start || 1;
      var cur = list.cloneNode(false);
      cur.removeAttribute("id");
      if (list.tagName === "OL") cur.start = number;
      probe.appendChild(cur);
      items.forEach(function (li) {
        cur.appendChild(li);
        if (probe.scrollHeight > chunkCap(parts.length) && cur.children.length > 1) {
          cur.removeChild(li);
          cur.remove();
          parts.push(cur);
          cur = list.cloneNode(false);
          cur.removeAttribute("id");
          if (list.tagName === "OL") cur.start = number;
          probe.appendChild(cur);
          cur.appendChild(li);
        }
        number += 1;
      });
      if (cur.children.length) parts.push(cur);
      detachProbe();
      var out = [];
      parts.forEach(function (part) {
        probe.appendChild(part);
        var tooTall = probe.scrollHeight > PAGE && part.children.length === 1;
        part.remove();
        if (!tooTall) {
          out.push(part);
          return;
        }
        var bits = splitElement(part.children[0]);
        if (bits.length < 2) {
          out.push(part);
          return;
        }
        bits.forEach(function (bit, i) {
          var wrap = list.cloneNode(false);
          wrap.removeAttribute("id");
          if (i > 0) wrap.classList.add("split-continued");
          else if (list.tagName === "OL") wrap.start = part.start || list.start || 1;
          wrap.appendChild(bit);
          out.push(wrap);
        });
      });
      return out.length ? out : [list];
    }

    function splitBox(box) {
      var kids = Array.prototype.slice.call(box.children);
      if (kids.length < 2) {
        if (kids.length === 1) {
          var innerBits = splitElement(kids[0]);
          if (innerBits.length < 2) return [box];
          return innerBits.map(function (bit, i) {
            var wrap = box.cloneNode(false);
            wrap.removeAttribute("id");
            if (i > 0) wrap.classList.add("box-continued");
            wrap.appendChild(bit);
            return wrap;
          });
        }
        return [box];
      }
      detachProbe();
      var parts = [];
      var cur = box.cloneNode(false);
      cur.removeAttribute("id");
      probe.appendChild(cur);
      kids.forEach(function (kid) {
        cur.appendChild(kid);
        if (probe.scrollHeight > chunkCap(parts.length) && cur.children.length > 1) {
          cur.removeChild(kid);
          cur.remove();
          parts.push(cur);
          cur = box.cloneNode(false);
          cur.removeAttribute("id");
          cur.classList.add("box-continued");
          probe.appendChild(cur);
          cur.appendChild(kid);
        }
      });
      if (cur.children.length) parts.push(cur);
      detachProbe();
      var out = [];
      parts.forEach(function (part) {
        probe.appendChild(part);
        var tooTall = probe.scrollHeight > PAGE;
        part.remove();
        if (!tooTall || part.children.length !== 1) {
          out.push(part);
          return;
        }
        var bits = splitElement(part.children[0]);
        if (bits.length < 2) {
          out.push(part);
          return;
        }
        bits.forEach(function (bit, i) {
          var wrap = box.cloneNode(false);
          wrap.removeAttribute("id");
          if (i > 0 || part.classList.contains("box-continued")) wrap.classList.add("box-continued");
          wrap.appendChild(bit);
          out.push(wrap);
        });
      });
      return out.length ? out : [box];
    }

    function splitElement(el) {
      if (!el || el.nodeType !== 1) return [el];
      if (el.matches("table")) return splitTable(el);
      if (el.matches("pre")) return splitPre(el);
      if (el.matches("ul,ol")) return splitList(el);
      if (el.classList.contains("box") || el.classList.contains("ch-opener")) return splitBox(el);
      if (el.classList.contains("two-col") || el.classList.contains("legend")) {
        var kids = Array.prototype.slice.call(el.children);
        return kids.length > 1 ? kids : [el];
      }
      if (el.matches("figure,svg,mjx-container")) return [el];
      probe.appendChild(el);
      var tall = probe.scrollHeight > FIT_LIMIT;
      el.remove();
      if (!tall) return [el];
      if (el.children.length > 1) {
        detachProbe();
        var parts = [];
        var cur = el.cloneNode(false);
        cur.removeAttribute("id");
        probe.appendChild(cur);
        Array.prototype.slice.call(el.childNodes).forEach(function (node) {
          if (node.nodeType === 3 && !node.textContent.trim()) return;
          cur.appendChild(node);
          if (probe.scrollHeight > chunkCap(parts.length) && cur.childNodes.length > 1) {
            cur.removeChild(node);
            cur.remove();
            parts.push(cur);
            cur = el.cloneNode(false);
            cur.removeAttribute("id");
            if (el.classList) cur.className = el.className;
            probe.appendChild(cur);
            cur.appendChild(node);
          }
        });
        if (cur.childNodes.length) parts.push(cur);
        detachProbe();
        if (parts.length > 1) return parts;
      }
      return splitWords(el);
    }

    var atoms = [];
    function walk(el) {
      Array.prototype.forEach.call(el.children, function (child) {
        if (child.classList.contains("cover") || child.id === "sheets") return;
        if (child.tagName === "SCRIPT") return;
        var atomic = child.matches(
          "h1,h2,h3,h4,p,table,pre,figure,ul,ol,blockquote,.box,.flow,.ch-opener,.legend,.two-col,.cheat-card,.cheat-head,.crash-head,.crash-seal,.pagebreak,mjx-container,.math,.note-block,.notes-head,.lesson-head,.answers-seal,.colophon,.imprint,.paced-lesson,.paced-chapter,.chapter-recap,.exam-head,.one-page-topic,.complete-lesson,.complete-chapter,.complete-part,.part-banner"
        );
        if (atomic) atoms.push(child);
        else if (child.children.length && child.matches("div,section,article")) walk(child);
        else atoms.push(child);
      });
    }
    walk(document.body);

    var host = document.createElement("div");
    host.id = "sheets";
    var cover = document.querySelector(".cover");
    if (cover) cover.after(host);
    else document.body.insertBefore(host, document.body.firstChild);

    var sheet = null;
    var inner = null;
    function openSheet() {
      sheet = document.createElement("div");
      sheet.className = "sheet";
      inner = document.createElement("div");
      inner.className = "sheet-inner";
      sheet.appendChild(inner);
      host.appendChild(sheet);
    }
    function seal() {
      if (!inner || !inner.childElementCount) return;
      openSheet();
    }
    openSheet();

    function splitTo(el, limit) {
      FIT_LIMIT = limit || PAGE;
      var parts = splitElement(el);
      FIT_LIMIT = PAGE;
      return parts;
    }

    var placeCalls = 0;
    function isOnePageBlock(el) {
      return el && el.matches && el.matches(".paced-lesson,.paced-chapter,.chapter-recap,.one-page-topic,.cheat-card,.note-block");
    }
    function placeGroup(nodes) {
      if (!nodes.length || ++placeCalls > 8000) return;
      if (nodes.length === 1 && isOnePageBlock(nodes[0])) {
        if (inner.childElementCount) seal();
        inner.appendChild(nodes[0]);
        seal();
        return;
      }
      nodes.forEach(function (n) { inner.appendChild(n); });
      var together = inner.scrollHeight;
      if (together <= PAGE) return;

      nodes.forEach(function (n) { n.remove(); });
      var used = inner.childElementCount ? inner.scrollHeight : 0;

      if (used > 0 && PAGE / together >= SQUEEZE) {
        nodes.forEach(function (n) { inner.appendChild(n); });
        seal();
        return;
      }
      if (used > 0) {
        var room = PAGE - used;
        if (room > 120 && nodes.length === 1 && !nodes[0].getAttribute("data-peeled")) {
          var peeled = splitTo(nodes[0], room);
          if (peeled.length > 1) {
            peeled[0].setAttribute("data-peeled", "1");
            placeGroup([peeled[0]]);
            peeled.slice(1).forEach(function (part) { placeGroup([part]); });
            return;
          }
        }
        seal();
        placeGroup(nodes);
        return;
      }
      if (PAGE / together >= MIN_SCALE) {
        nodes.forEach(function (n) { inner.appendChild(n); });
        seal();
        return;
      }
      if (nodes.length > 1) {
        var pieces = [];
        nodes.slice(1).forEach(function (n) {
          splitElement(n).forEach(function (part) { pieces.push(part); });
        });
        var unchanged = pieces.length === nodes.length - 1 &&
          pieces.every(function (part, i) { return part === nodes[i + 1]; });
        if (unchanged) {
          nodes.forEach(function (n) { inner.appendChild(n); });
          seal();
          return;
        }
        placeGroup([nodes[0], pieces[0]]);
        pieces.slice(1).forEach(function (part) { placeGroup([part]); });
        return;
      }
      var only = splitElement(nodes[0]);
      if (only.length < 2) {
        inner.appendChild(only[0]);
        seal();
        return;
      }
      only.forEach(function (part) { placeGroup([part]); });
    }

    for (var i = 0; i < atoms.length; i++) {
      var el = atoms[i];
      if (el.matches && el.matches(".crash-head,.crash-seal,.pagebreak,.notes-head,.answers-seal,.colophon,.paced-lesson,.paced-chapter,.chapter-recap,.exam-head,.exam-key,.one-page-topic,.cheat-card,.note-block,.complete-lesson,.complete-chapter,.complete-part,.part-banner")) {
        seal();
      }
      var nxt = atoms[i + 1];
      if (
        el.classList &&
        el.classList.contains("crash-head") &&
        nxt &&
        nxt.classList &&
        nxt.classList.contains("box")
      ) {
        i += 1;
        placeGroup([el, nxt]);
      } else if (isHeading(el) && nxt && !isHeading(nxt)) {
        i += 1;
        placeGroup([el, nxt]);
      } else {
        placeGroup([el]);
      }
    }
    if (inner && !inner.childElementCount && sheet) sheet.remove();

    Array.prototype.forEach.call(document.querySelectorAll(".sheet"), function (sh) {
      var box = sh.firstElementChild;
      if (!box || !box.childElementCount) {
        sh.remove();
        return;
      }
      var limit = sh.clientHeight || PAGE;
      var h = box.scrollHeight;
      if (h > limit + 1) {
        /* zoom changes layout size in Chrome, so the block stays inside this sheet
           instead of painting the leftover lines on the next page. */
        box.style.zoom = String((limit - 2) / h);
      }
    });

    var sheets = host.querySelectorAll(".sheet");
    if (sheets.length) {
      var last = sheets[sheets.length - 1];
      last.style.breakAfter = "auto";
      last.style.pageBreakAfter = "auto";
    }

    probe.remove();
    Array.prototype.slice.call(document.body.children).forEach(function (el) {
      if (el.classList.contains("cover") || el.id === "sheets" || el.tagName === "SCRIPT") return;
      el.remove();
    });
  }

  function start() {
    var fonts = (document.fonts && document.fonts.ready)
      ? document.fonts.ready
      : Promise.resolve();
    var math = Promise.resolve();
    if (window.MathJax && MathJax.startup && MathJax.startup.promise) {
      math = MathJax.startup.promise.then(function () {
        return MathJax.typesetPromise ? MathJax.typesetPromise() : null;
      });
    }
    Promise.all([fonts, math]).then(fit).catch(function () { fit(); });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", start);
  else start();
})();
