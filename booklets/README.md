# Ultimate Teach Yourself Booklets

Self-study booklets for **Computer Science XI** and **XII** (Sindh curriculum),
built from the bilingual teacher's lecture notes.

## Download (after build)

- `booklets/output/CS-XI-Ultimate-Teach-Yourself-Booklet.pdf`
- `booklets/output/CS-XII-Ultimate-Teach-Yourself-Booklet.pdf`

## Build

```bash
python3 booklets/build.py        # both
python3 booklets/build.py xi     # Grade XI only
python3 booklets/build.py xii    # Grade XII only
```

Requires Google Chrome (`google-chrome`) and the Noto Naskh Arabic + Inter fonts.
Chapter HTML lives in `booklets/src/xi` and `booklets/src/xii`. Authoring rules: `booklets/AUTHORING.md`.
