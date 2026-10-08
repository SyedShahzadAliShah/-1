# BIEK Computer Science lecture notes

Original classroom lectures for Board of Intermediate Education Karachi Computer Science, Class XI and Class XII.

The chapter order is the Sindh Textbook Board scheme used with the New Sindh Curriculum of Computer Science 2024, which is aligned with the National Curriculum of Pakistan 2022–23. Each lecture has worked examples, short and long answers, a practical, MathJax equations, and SVG figures. Theory is treated as 75 marks and the practical as 25, matching the BIEK scheme of studies.

These notes are not an official BIEK or Sindh Textbook Board publication.

## Files

- `pdf/BIEK-CS-XI-Lectures.pdf`
- `pdf/BIEK-CS-XII-Lectures.pdf`
- `apk/BIEK-CS-Lectures-v1.0.0.apk`

Direct APK download:

https://github.com/SyedShahzadAliShah/-1/raw/cursor/biek-cs-lectures-d864/biek-cs-lectures/apk/BIEK-CS-Lectures-v1.0.0.apk

The app reads each concept aloud. If the phone has an Urdu voice, it speaks Urdu and keeps terms such as AND, Python, SDLC, and TCP in English. If not, it speaks the same lesson in Roman Urdu with those English terms, and the screen explains how to install an Urdu voice.

## Rebuild

```bash
pip install -r requirements.txt
python3 check_lectures.py
python3 build_lectures.py
```
