# Chapter authoring spec — Ultimate Teach Yourself Booklet

Each chapter is one HTML **fragment** (no `<html>`, `<head>` or `<body>`) saved as
`booklets/src/<xi|xii>/ch<N>.html`. `build.py` wraps fragments with the cover, contents,
and the stylesheet `booklets/assets/booklet.css`. Use only the classes listed here.

## Audience and voice

- A Class XI/XII student in Sindh studying **alone**, without a teacher. The source is a
  teacher's slide deck; the booklet must *teach*: explain the why, define every term
  the first time it appears, and walk through examples step by step.
- Address the reader as "you". Short sentences. Simple English.
- Cover **every** topic and sub-topic in the chapter's source text, in the same order
  and with the same section numbers (e.g. `1.1.3`). Keep every fact, definition,
  table, example, and analogy from the source; expand them. Do not invent syllabus
  content that conflicts with the source; general, correct background is fine.
- Topics marked ★ / "GOLDEN TOPIC" in the source get `<span class="star">★ Golden</span>`
  in their `<h2>` and extra depth (an exam tip box and more practice).

## Urdu

- Write Urdu yourself in correct, natural Urdu (logical order, Unicode). The Urdu in the
  source text file is extracted in broken visual order — never copy it.
- Wrap Urdu in `<p class="ur">…</p>`, `<div class="box urdu">…</div>`, or `<td class="ur">`.
- English technical terms inside Urdu may be written in Latin script in parentheses, e.g.
  `ڈیٹا بیس (Database)`.

## Fragment skeleton (follow exactly)

```html
<section class="chapter" id="xi-ch1" data-num="1" data-title="Computer Systems">
  <div class="ch-opener">
    <div class="num">Chapter 1</div>
    <h1>Computer Systems</h1>
    <p>One or two sentences: what this chapter is about and why it matters.</p>
    <p class="ur">اردو میں ایک یا دو جملوں کا تعارف</p>
  </div>

  <h3>What you will learn</h3>
  <ul class="objectives">
    <li>Explain …</li>   <!-- 6–10 measurable objectives -->
  </ul>

  <div class="topic">
    <h2>1.1.3 Analog and Digital Signals <span class="star">★ Golden</span></h2>
    <div class="box learn"><p>Plain explanation…</p></div>
    <!-- free paragraphs, <ul>, <table>, <pre class="code">, figures allowed between boxes -->
    <div class="box example"><p>Step-by-step worked example…</p></div>
    <div class="box tip"><p>Memory trick / analogy / mnemonic…</p></div>
    <div class="box warn"><p>A mistake students often make, and the fix…</p></div>
    <div class="box urdu"><p class="ur">اس موضوع کا اردو خلاصہ (2–4 جملے)</p></div>
    <div class="box exam"><p>How this is asked in exams, what to write…</p></div>  <!-- Golden topics -->
    <div class="box check">
      <p><b>1.</b> Quick question?</p>
      <p><b>2.</b> Quick question?</p>
      <div class="ans">Answers: 1. … 2. …</div>
    </div>
  </div>
  <!-- …one .topic per source topic… -->

  <section class="review">
    <h2>Chapter 1 Review</h2>
    <h3>Chapter summary</h3>
    <ul class="summary"><li>…</li></ul>                       <!-- 10–16 bullets -->

    <h3>Key terms</h3>
    <table class="glossary">
      <tr><th>Term</th><th>Meaning</th><th>اردو</th></tr>
      <tr><td>Bit</td><td>A binary digit, 0 or 1.</td><td class="ur">بائنری ہندسہ</td></tr>
    </table>                                                  <!-- 15–30 terms -->

    <h3>Practice: multiple choice</h3>
    <ol class="mcq">                                          <!-- 15 MCQs -->
      <li>Question?
        <ol class="opts"><li>…</li><li>…</li><li>…</li><li>…</li></ol>
      </li>
    </ol>

    <h3>Practice: short questions</h3>
    <ol class="short"><li>…</li></ol>                         <!-- 10 -->

    <h3>Practice: long / problem questions</h3>
    <ol class="long"><li>…</li></ol>                          <!-- 4–6 -->

    <div class="answers">
      <h2>Answer key</h2>
      <h3>Multiple choice</h3>
      <ol class="inline"><li>b</li>…</ol>
      <h3>Short questions — model answers</h3>
      <ol><li>…</li></ol>
      <h3>Long questions — model answers</h3>
      <ol><li>…full worked solution / outline…</li></ol>
    </div>

    <h3>Self-assessment: I can…</h3>
    <ul class="checklist"><li>…</li></ul>                     <!-- 8–12 -->
  </section>
</section>
```

## Box classes

| Class | Label printed | Use for |
|---|---|---|
| `box learn` | Learn it | Core explanation of the topic |
| `box example` | Worked example | Step-by-step solved example (required wherever something can be computed, traced, coded, or applied) |
| `box tip` | Remember it | Memory tricks, mnemonics, analogies |
| `box warn` | Common mistake | Misconceptions and how to avoid them |
| `box urdu` | اردو میں سمجھیں | Urdu explanation (one per topic) |
| `box exam` | Exam tip | Golden topics: how it is examined |
| `box check` | Check yourself | 2–3 quick questions with `.ans` answers (one per topic) |

## Other building blocks

- Tables: plain `<table>` with `<th>` header row. `class="center"` centres cells (truth tables,
  K-maps). `<td class="hl">` highlights a cell.
- Code: `<pre class="code">` for Python/SQL; `<pre class="code output">` for program output.
  Escape `<`, `>` and `&` in code. Code must be correct, runnable Python 3, and outputs must be exact.
- Process chains: `<div class="flow"><span>Step</span><i>→</i><span>Step</span></div>`.
- Diagrams: `<figure class="diagram"><svg viewBox="…" width="…">…</svg><figcaption>…</figcaption></figure>`.
  Keep inline SVG simple and clean (rect, line, path, text; fonts `Inter`). Use for logic gate
  symbols, signal waves, trees/graphs, linked lists, stacks/queues, OSI layers, ER diagrams,
  etc. Width ≤ 640.
- Side-by-side: `<div class="two-col"><div>…</div><div>…</div></div>`.
- No external images, scripts, or fonts. No `<style>` blocks or inline `style` except in SVG.

## Quality bar

- Every computable claim must be correct: truth tables, K-map groupings, Boolean
  simplification, sort/search passes, trace tables, Big O, statistics (mean/median/mode/
  variance/std dev), Python outputs, SQL.
- Answer keys must match questions exactly; MCQ answers should be spread across a–d.
- HTML must be well formed.
