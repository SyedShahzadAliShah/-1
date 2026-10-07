# Computer Science — 30-Day Coaching Academy Edition

The **Bilingual Teacher’s Edition** for Sindh Computer Science XI and XII, rebuilt as a
30-day coaching-academy batch. One **90-minute class** a day. The coach runs the board;
students copy, drill, and take stamped homework home.

This is not a 40-minute school period and not a 3-hour self-study crash course.

## Direct download

- [CS XI 30-Day Coaching Academy Edition (269 pages)](https://raw.githubusercontent.com/SyedShahzadAliShah/-1/cursor/30-day-coaching-academy-9c8b/releases/CS-XI-30-Day-Coaching-Academy-Edition.pdf)
- [CS XII 30-Day Coaching Academy Edition (252 pages)](https://raw.githubusercontent.com/SyedShahzadAliShah/-1/cursor/30-day-coaching-academy-9c8b/releases/CS-XII-30-Day-Coaching-Academy-Edition.pdf)
- [XI + XII complete (521 pages)](https://raw.githubusercontent.com/SyedShahzadAliShah/-1/cursor/30-day-coaching-academy-9c8b/releases/CS-XI-and-XII-30-Day-Coaching-Academy-Edition-Complete.pdf)

## What is inside each book

- Cover, 30-day calendar, and a batch register for starter marks
- How to run a 90-minute academy class (starter · concept lock · board working · drill · error clinic · homework)
- **Days 1–23.** Every topic from the teacher’s notes as a board card. ★ Golden topics never skipped. Last day of each chapter is a 75-mark hall exam
- **Days 24–26.** ★ Golden blitz (no new non-Golden topic)
- **Day 27.** Oral recap at the board
- **Day 28.** Mock paper, 2 hours 30 minutes, academy hall conditions
- **Day 29.** Mark to the sealed key and fill the repair list
- **Day 30.** Repair clinic, then stop

Full-mark recipes use **Define · Explain · Example · Diagram · Working**. Urdu classroom lines sit on every teaching day.

Based on the New Sindh Curriculum (XI 2026, XII 2025–27). Topics marked ★ are high-yield for board exams.

## Rebuild

```bash
python3 booklets/build.py academy30
```

Requires Google Chrome, Inter + Noto Naskh Arabic fonts, and `pymupdf` (for the combined XI+XII file).

Chapter HTML lives in `booklets/src/xi` and `booklets/src/xii`. Authoring rules: `booklets/AUTHORING.md`.
