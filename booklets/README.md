# Ultimate Teach Yourself Booklets

Self-study booklets for **Computer Science XI** and **XII** (Sindh curriculum),
built from the bilingual teacher's lecture notes.

## Download

- [CS XI booklet (PDF)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-booklets-44eb/releases/CS-XI-Ultimate-Teach-Yourself-Booklet.pdf)
- [CS XII booklet (PDF)](https://github.com/SyedShahzadAliShah/-1/raw/cursor/teach-yourself-booklets-44eb/releases/CS-XII-Ultimate-Teach-Yourself-Booklet.pdf)

Copies also live in `releases/` on this branch. Rebuild with:

## Build

```bash
python3 booklets/build.py        # both
python3 booklets/build.py xi     # Grade XI only
python3 booklets/build.py xii    # Grade XII only
```

Requires Google Chrome (`google-chrome`) and the Noto Naskh Arabic + Inter fonts.
Chapter HTML lives in `booklets/src/xi` and `booklets/src/xii`. Authoring rules: `booklets/AUTHORING.md`.
