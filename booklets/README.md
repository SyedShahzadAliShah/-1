# Ultimate Teach Yourself Booklets & Lectures

Self-study materials for **Computer Science XI** and **XII** (Sindh curriculum),
built from the bilingual teacher's lecture notes.

## Student's Edition and Teacher's Edition

Separate all-in-one PDFs:

- [CS XI Student's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Students-Edition.pdf)
- [CS XII Student's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Students-Edition.pdf)
- [CS XI Teacher's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Teachers-Edition.pdf)
- [CS XII Teacher's Edition](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Teachers-Edition.pdf)
- [XI + XII Student's Edition complete](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Students-Edition-Complete.pdf)
- [XI + XII Teacher's Edition complete](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Teachers-Edition-Complete.pdf)

The **Student's Edition** hides Check yourself answers until the end of each chapter. The **Teacher's Edition** adds lesson timing, board cues, oral questions and Urdu classroom lines, with answers on the page.

```bash
python3 booklets/build.py editions
```

## Coaching Academy Edition

In-depth books for a 90-minute coaching batch: session calendar, full-mark recipes, extra drills with answers, and homework.

- [CS XI Coaching Academy Edition (297 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Coaching-Academy-Edition.pdf)
- [CS XII Coaching Academy Edition (298 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Coaching-Academy-Edition.pdf)
- [XI + XII Coaching Academy Edition complete (595 pages)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Coaching-Academy-Edition-Complete.pdf)

★ Golden topics take a full 90-minute class. Other topics pair into one class.

```bash
python3 booklets/build.py academy
```

## Download — lecture PDFs

Each topic is a printable **Teach Yourself lecture**. Each chapter also has a packed
lecture PDF with the review and answer key.

See [`releases/lectures/README.md`](../releases/lectures/README.md) for the full list.

Rebuild lectures:

```bash
python3 booklets/build.py lectures        # XI + XII lecture PDFs
python3 booklets/build.py lectures xi     # Grade XI only
```

## Download — full booklets (all-in-one)

- [CS XI All-in-One (PDF)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-Teach-Yourself-All-in-One.pdf)
- [CS XII All-in-One (PDF)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XII-Teach-Yourself-All-in-One.pdf)
- [XI + XII complete (PDF)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-lectures-pdf-339e/releases/CS-XI-and-XII-Teach-Yourself-Complete.pdf)

```bash
python3 booklets/build.py        # both booklets
python3 booklets/build.py xi     # Grade XI only
python3 booklets/build.py xii    # Grade XII only
python3 booklets/build.py all    # booklets + lectures + editions + academy
```

Requires Google Chrome (`google-chrome`) and the Noto Naskh Arabic + Inter fonts.
Chapter HTML lives in `booklets/src/xi` and `booklets/src/xii`. Authoring rules: `booklets/AUTHORING.md`.
