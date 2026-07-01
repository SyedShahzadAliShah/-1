#!/usr/bin/env python3
"""Download SheKnows article images and save as app posture drawables."""
from __future__ import annotations

import io
import os
import re
import sys
import urllib.request
from typing import Dict, List, Tuple

from bs4 import BeautifulSoup
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "app/src/main/res/drawable-nodpi")
ARTICLE_URL = (
    "https://www.sheknows.com/health-and-wellness/slideshow/"
    "5919/sex-positions-to-try-before-you-die/"
)
USER_AGENT = "Mozilla/5.0 (compatible; IntimacyHandbook/4.0)"
TARGET_W = 960

SKIP_HEADINGS = {
    "Classic Sex Positions", "Non-Penetrative Sex Positions", "Elevated Sex Positions",
    "Shower Sex Positions", "Bondage Sex Positions", "Car Sex Positions",
    "Masturbation Sex Positions", "Flat Sex Positions", "Blindfolded Sex Positions",
    "Cowboy Sex Positions", "Beach-Inspired Sex Positions",
    "Best Sex Positions For Vaginal Orgasm", "Creative Sex Positions",
    "Pin it!", "More Stories from Health & Wellness",
}

# Map article heading -> app posture id (manual fixes for duplicates / naming)
TITLE_TO_ID: Dict[str, str] = {
    "Modified Coital-Alignment Technique": "sk_cat",
    "Doggy Style": "sk_doggy",
    "Pushing Tush": "sk_pushing_tush",
    "Rocking Horse": "sk_rocking_horse",
    "Seated Scissors": "sk_seated_scissors",
    "Spooning": "sk_spooning",
    "Scissoring": "sk_scissoring",
    "Bend Over, Baby": "sk_bend_over",
    "Scissors": "sk_scissors_classic",
    "Uncloak the Clitoris": "sk_uncloak",
    "Baring the Scepter": "sk_scepter",
    "Self-Loving (On Your Knees)": "sk_self_loving",
    "Queening in Bondage": "sk_queening",
    "Countertop": "sk_countertop",
    "Happy Scissors": "sk_happy_scissors",
    "The Butterfly": "sk_butterfly",
    "Standing Up Full-Frontal": "sk_shower_front",
    "Soap'n'Grope": "sk_soap_grope",
    "Soap’n’Grope": "sk_soap_grope",
    "Hands Behind Ankles": "sk_hands_ankles",
    "The Kinky Missionary": "sk_kinky_missionary",
    "Standing Room Only": "sk_standing_room",
    "Backseat Driver": "sk_backseat",
    "Belt Bondage": "sk_belt_bondage",
    "Seated Rear Entry": "sk_car_seated_rear",
    "Yab-Yum": "sk_yab_yum",
    "Trunk Space": "sk_trunk",
    "Over the Hump": "sk_over_hump",
    "Superstar": "sk_superstar",
    "The Solo Snake": "sk_solo_snake",
    "Opening Up": "sk_opening_up",
    "Layer Cake": "sk_layer_cake",
    "The Reverse Slither": "sk_reverse_slither",
    "Stacked Snakes": "sk_stacked_snakes",
    "Anal Spoon": "sk_anal_spoon",
    "The Splitting of Bamboo": "sk_splitting_bamboo",
    "The Private Dancer": "sk_private_dancer",
    "X Marks the Spot": "sk_x_marks",
    "Rock 'n' Roll": "sk_rock_n_roll",
    "Rock ‘n’ Roll": "sk_rock_n_roll",
    "Cowgirl or Cowboy": "sk_anal_cowgirl",
    "Doggy-Style": "sk_anal_doggy",
    "Face to Face": "sk_anal_face",
    "Missionary With a Twist": "sk_missionary_twist",
    "On the Stomach": "sk_on_stomach",
    "Spooning With a Twist": "sk_spooning_twist",
    "The BBQ Quickie": "sk_bbq_quickie",
    "The Lounging Lioness": "sk_lounging_lioness",
    "The Pouncing Panther": "sk_pouncing_panther",
    "The Teddy Bear": "sk_teddy_bear",
    "Beach-Safe Doggy-Style": "sk_beach_doggy",
    "In the Water": "sk_in_water",
    "On a Beach Ball": "sk_beach_ball",
    "Reverse Cowgirl": "sk_beach_reverse",
    "Standing Up": "sk_beach_standing",
    "Under a Blanket": "sk_under_blanket",
    "Closed for Business": "sk_closed_business",
    "In High Heels": "sk_high_heels",
    "The Drop Box": "sk_drop_box",
    "The G-Whiz": "sk_g_whiz",
    "The Tilt-a-Whirl": "sk_tilt_whirl",
    "The Circus Freak": "sk_circus_freak",
    "Froggie-Style": "sk_froggie",
    "The Yogi": "sk_yogi",
    "Inverted Missionary": "sk_inverted_missionary",
    "The Cowpoke": "sk_cowpoke",
    "Field Goal": "sk_field_goal",
    "Fumble": "sk_fumble",
    "Wide Receiver": "sk_wide_receiver",
}

# Two "Lap Dance" entries in article — first elevated, second creative
LAP_DANCE_IDS = ["sk_lap_dance", "sk_lap_dance_creative"]


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def scrape_title_images(html: str) -> List[Tuple[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup
    pairs: List[Tuple[str, str]] = []
    current: str | None = None
    lap_idx = 0

    for el in article.find_all(["h2", "h3", "img"]):
        if el.name in ("h2", "h3"):
            t = el.get_text(strip=True)
            if not t or t in SKIP_HEADINGS or "optional screen" in t.lower():
                continue
            current = t
        elif el.name == "img" and current:
            src = el.get("src") or el.get("data-src") or ""
            if "sheknows.com/wp-content/uploads" not in src or "fav-icon" in src:
                continue
            base = src.split("?")[0]
            if re.search(
                r"Sex-Positions_|Sex-Positions\.|Bucket-List|FeatureImage|Non-Penetrative|Elevated-Sex|Shower-Sex|Flat-Sex|Masturbation-Sex",
                base,
            ):
                continue
            pairs.append((current, base))
            current = None

    return pairs


def hi_res_url(base_url: str) -> str:
    if base_url.lower().endswith((".jpg", ".jpeg")):
        return f"{base_url}?w={TARGET_W}"
    return base_url


def download_image(url: str) -> Image.Image:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    img = Image.open(io.BytesIO(data))
    return img.convert("RGB")


def save_posture_image(img: Image.Image, posture_id: str) -> str:
    os.makedirs(OUT, exist_ok=True)
    # Scale to consistent width, keep aspect ratio
    if img.width != TARGET_W:
        ratio = TARGET_W / img.width
        new_h = max(1, int(img.height * ratio))
        img = img.resize((TARGET_W, new_h), Image.Resampling.LANCZOS)
    path = os.path.join(OUT, f"pic_{posture_id}.png")
    img.save(path, "PNG", optimize=True)
    return path


def resolve_id(title: str, lap_counter: List[int]) -> str | None:
    if title == "Lap Dance":
        idx = lap_counter[0]
        lap_counter[0] += 1
        if idx < len(LAP_DANCE_IDS):
            return LAP_DANCE_IDS[idx]
        return LAP_DANCE_IDS[-1]
    return TITLE_TO_ID.get(title)


def main() -> int:
    print("Fetching SheKnows article...")
    html = fetch_html(ARTICLE_URL)
    pairs = scrape_title_images(html)
    print(f"Found {len(pairs)} position images in article")

    lap_counter = [0]
    saved = 0
    missing: List[str] = []

    for title, base_url in pairs:
        pid = resolve_id(title, lap_counter)
        if not pid:
            missing.append(title)
            print(f"  SKIP (no id): {title}")
            continue
        url = hi_res_url(base_url)
        try:
            img = download_image(url)
            path = save_posture_image(img, pid)
            print(f"  OK pic_{pid}.png <- {title} ({os.path.getsize(path)//1024}KB)")
            saved += 1
        except Exception as exc:
            print(f"  FAIL {title}: {exc}", file=sys.stderr)
            missing.append(title)

    # Cover image from article hero
    cover_url = "https://www.sheknows.com/wp-content/uploads/2025/04/69-Sex-Positions-to-Put-on-Your-Bucket-List-Immediately.jpg?w=1024"
    try:
        img = download_image(cover_url)
        path = save_posture_image(img, "guide_cover")
        # also keep pic_guide_cover name used by app
        img.save(os.path.join(OUT, "pic_guide_cover.png"), "PNG", optimize=True)
        print(f"  OK pic_guide_cover.png ({os.path.getsize(path)//1024}KB)")
        saved += 1
    except Exception as exc:
        print(f"  FAIL cover: {exc}", file=sys.stderr)

    print(f"\nSaved {saved} images to {OUT}")
    if missing:
        print(f"Missing/unmapped ({len(missing)}): {missing}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
