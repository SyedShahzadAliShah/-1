# Ultimate Teach Yourself Booklets & Lectures

Self-study materials for **Computer Science XI** and **XII** (Sindh curriculum),
built from the bilingual teacher's lecture notes.

## Download — lecture PDFs

Each topic is a printable **Teach Yourself lecture**. Each chapter also has a packed
lecture PDF with the review and answer key.

See [`releases/lectures/README.md`](../releases/lectures/README.md) for the full list.

Rebuild lectures:

```bash
python3 booklets/build.py lectures        # XI + XII lecture PDFs
python3 booklets/build.py lectures xi     # Grade XI only
```

## Download — full booklets

- [CS XI booklet (PDF)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-booklets-44eb/releases/CS-XI-Ultimate-Teach-Yourself-Booklet.pdf)
- [CS XII booklet (PDF)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-booklets-44eb/releases/CS-XII-Ultimate-Teach-Yourself-Booklet.pdf)

```bash
python3 booklets/build.py        # both booklets
python3 booklets/build.py xi     # Grade XI only
python3 booklets/build.py xii    # Grade XII only
python3 booklets/build.py all    # booklets + lectures
```

Requires Google Chrome (`google-chrome`) and the Noto Naskh Arabic + Inter fonts.
Chapter HTML lives in `booklets/src/xi` and `booklets/src/xii`. Authoring rules: `booklets/AUTHORING.md`.
