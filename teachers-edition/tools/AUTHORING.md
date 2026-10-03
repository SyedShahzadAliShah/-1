# Authoring guide: page content for the bilingual Teacher's Edition

Source: `source/XI_8518.pdf` — "Computer Science XI, Bilingual Teacher's Edition" (127 pages).
Each page is authored as `content/pNNN.json` and drives the Android app: **English text on screen,
Urdu voice narration** (Urdu text is only used to synthesise audio, it is never displayed).

## Inputs per page N (3-digit, e.g. 009)

- `work/extract/pNNN.txt` — the page's English lines in reading-ish order with layout metadata:
  `[y=<top> x=<left> <B|R><fontsize>] text` (`B` bold, `R` regular, `M` monospace). Use `x`/`y` to
  rebuild tables (same `y` = same row, `x` = column), headings (large bold font) and list items.
  The English in this file is the ground truth and must be reproduced verbatim (same wording).
- `work/orig/pNNN.png` — the original page image (view it with the Read tool). It contains the
  Urdu translation that sits next to the English; use it as the source for the narration.

## Output `content/pNNN.json`

```json
{"page": 9, "blocks": [ ... ]}
```

Blocks, in reading order (top to bottom of the page, as the student would read):

| `t`       | fields                                   | meaning |
|-----------|------------------------------------------|---------|
| `title`   | `en`, `ur`                               | cover/chapter title lines (large type) |
| `h1`      | `en`, `ur`                               | main section heading (e.g. `1.1.7 Logic Gates`) |
| `h2`/`h3` | `en`, `ur`                               | sub headings (14pt / 12pt bold lines) |
| `badge`   | `en`, `ur`                               | the `GOLDEN TOPIC` star badge (`en` = `GOLDEN TOPIC`) |
| `p`       | `en`, `ur`                               | paragraph (join wrapped lines into one string) |
| `li`      | `en`, `ur`, optional `lead`              | one bullet / numbered item. `lead` = the bold lead-in prefix of `en` (e.g. `Reduces complexity:`) |
| `note`    | `label`, `en`, `ur`                      | call-out box (Analogy, Real-life Example, Tip, Remember...). `label` is the box heading |
| `table`   | `cols` [..], `rows` [{`cells` [..], `ur`}] | tables. One `ur` narration **per row** (header row needs none) |
| `code`    | `en` (newline separated), `ur`           | code / pseudo-code / monospace snippets |
| `figure`  | `en`, `ur`                               | a diagram. `en` = the English labels/captions that appear inside the diagram joined with ` | `; `ur` describes the diagram in words |

Rules:

1. **English is verbatim** from the extract (fix only line-wrap joins). Every English word of the
   page (except the `Page N` footer) must appear in exactly one block's `en`/`label`/`cols`/`cells`.
   Do not add English words that are not on the page. Keep symbols such as `·`, `+`, `'`, `→`.
2. `ur` is spoken by a neural Urdu TTS voice. Write it in **Urdu script only** (no Latin letters,
   no markdown, no emoji, no brackets/slashes). Digits are fine (`0`, `1`, `2026`).
   - Base it on the Urdu translation printed on the page image when present (clean it up: the page
     image is the source). If a block has no Urdu counterpart on the page, translate the English
     faithfully into natural, classroom-level Urdu yourself.
   - Transliterate technical English words in Urdu script the way Urdu teachers say them
     (ڈیجیٹل، بائنری، لاجک گیٹ، الگورتھم، ڈیٹا بیس...). Spell acronyms letter by letter
     (`CPU` -> سی پی یو, `OSI` -> او ایس آئی, `AND` -> اینڈ, `OR` -> آر, `NOT` -> ناٹ).
   - Speak formulas and symbols in words: `Y = A · B` -> "وائی برابر اے ضرب بی",
     `A + B` -> "اے جمع بی" (or "اے آر بی" in a Boolean context), `A'` -> "اے ناٹ".
     Letters: A اے، B بی، C سی، D ڈی، X ایکس، Y وائی، Z زیڈ.
   - End sentences with `۔` so the voice pauses. A table row's `ur` should read naturally as one
     or two sentences that convey the whole row (e.g. "قابلِ بھروسہ: شور اور مداخلت سے کم متاثر ہوتا ہے۔").
   - Keep each `ur` under about 600 characters; split long paragraphs into several `p` blocks only if
     the English also splits naturally.
   - `badge`: say "یہ ایک سنہری موضوع ہے، امتحان کے لیے انتہائی اہم۔"
3. Every block (and every table row) needs a non-empty `ur`. Page footer text (`Page N`) is not content.
4. Tables: one `table` block per visual table; `cols` from the header row. If a table has an empty
   corner or Urdu-only column, keep only the English columns.
5. Pure decorative/empty lines are skipped. Diagrams made of vector shapes are not in the extract
   except for their text labels - group those labels into a `figure` block placed where the diagram is.
6. Write valid UTF-8 JSON (use the Write tool, not shell heredocs with escapes).

## Validate

```
python3 tools/validate_content.py 9 10 11     # selected pages
python3 tools/validate_content.py             # all pages
```

The validator checks the schema, that the English matches the extract (missing / invented words),
and that `ur` is mostly Urdu script. Fix every reported problem and re-run until the pages pass.
