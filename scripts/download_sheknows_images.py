#!/usr/bin/env python3
"""Download SheKnows article images and replace ALL app illustrations (no stick figures)."""
from __future__ import annotations

import io
import os
import re
import shutil
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
USER_AGENT = "Mozilla/5.0 (compatible; IntimacyHandbook/4.2)"
TARGET_W = 960

SKIP_HEADINGS = {
    "Pin it!", "More Stories from Health & Wellness",
}

CATEGORY_HEADINGS = {
    "Classic Sex Positions": "cat_classic",
    "Non-Penetrative Sex Positions": "cat_non_penetrative",
    "Elevated Sex Positions": "cat_elevated",
    "Shower Sex Positions": "cat_shower",
    "Bondage Sex Positions": "cat_bondage",
    "Car Sex Positions": "cat_car",
    "Masturbation Sex Positions": "cat_solo",
    "Flat Sex Positions": "cat_flat",
    "Blindfolded Sex Positions": "cat_blindfold",
    "Cowboy Sex Positions": "cat_anal",
    "Beach-Inspired Sex Positions": "cat_beach",
    "Best Sex Positions For Vaginal Orgasm": "cat_orgasm",
    "Creative Sex Positions": "cat_creative",
}

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

LAP_DANCE_IDS = ["sk_lap_dance", "sk_lap_dance_creative"]

# Map legacy drawable names -> source (sk_* posture id or cat_* category id)
SUPPLEMENTAL_ALIASES: Dict[str, str] = {
    # Sex-ed insert cards
    "pic_edu_face_contact": "sk_cat",
    "pic_edu_consent_talk": "cat_non_penetrative",
    "pic_edu_hip_pillow": "sk_g_whiz",
    "pic_edu_rear_safety": "sk_doggy",
    "pic_edu_body_map": "cat_classic",
    "pic_edu_side_alignment": "sk_spooning",
    # Guide chapters
    "pic_chapter_consent": "cat_non_penetrative",
    "pic_chapter_connection": "sk_rocking_horse",
    "pic_chapter_comfort": "sk_butterfly",
    "pic_chapter_explore": "cat_creative",
    # Imagination exercises (closest SheKnows visuals)
    "pic_imagine_breath": "sk_yab_yum",
    "pic_imagine_candlelight": "sk_rocking_horse",
    "pic_imagine_embrace": "sk_spooning",
    "pic_imagine_ocean": "sk_under_blanket",
    "pic_imagine_starlight": "sk_under_blanket",
    "pic_imagine_morning": "sk_spooning",
}

# Legacy stick-figure assets no longer referenced — remove after refresh
OBSOLETE_STICK_FIGURES = [
    "pic_missionary", "pic_cowgirl", "pic_spooning", "pic_side_by_side",
    "pic_doggy", "pic_lotus", "pic_standing", "pic_edge_bed",
    "pic_reverse_cowgirl", "pic_butterfly", "pic_scissors", "pic_lazy_dog",
]


def fetch_html(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def scrape_article_images(html: str) -> Tuple[List[Tuple[str, str]], Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.find("article") or soup
    positions: List[Tuple[str, str]] = []
    categories: Dict[str, str] = {}
    current: str | None = None

    for el in article.find_all(["h2", "h3", "img"]):
        if el.name in ("h2", "h3"):
            t = el.get_text(strip=True)
            if not t or "optional screen" in t.lower():
                continue
            current = t
        elif el.name == "img" and current:
            src = el.get("src") or el.get("data-src") or ""
            if "sheknows.com/wp-content/uploads" not in src or "fav-icon" in src:
                continue
            base = src.split("?")[0]

            if current in CATEGORY_HEADINGS:
                categories[CATEGORY_HEADINGS[current]] = base
                current = None
                continue

            if current in SKIP_HEADINGS:
                current = None
                continue

            if re.search(
                r"Sex-Positions_|Sex-Positions\.|Bucket-List|FeatureImage",
                base,
            ):
                current = None
                continue

            positions.append((current, base))
            current = None

    return positions, categories


def hi_res_url(base_url: str) -> str:
    if base_url.lower().endswith((".jpg", ".jpeg")):
        return f"{base_url}?w={TARGET_W}"
    return base_url


def download_image(url: str) -> Image.Image:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = resp.read()
    return Image.open(io.BytesIO(data)).convert("RGB")


def save_named_image(img: Image.Image, name: str) -> str:
    os.makedirs(OUT, exist_ok=True)
    if img.width != TARGET_W:
        ratio = TARGET_W / img.width
        new_h = max(1, int(img.height * ratio))
        img = img.resize((TARGET_W, new_h), Image.Resampling.LANCZOS)
    if not name.endswith(".png"):
        name = f"{name}.png"
    path = os.path.join(OUT, name)
    img.save(path, "PNG", optimize=True)
    return path


def resolve_position_id(title: str, lap_counter: List[int]) -> str | None:
    if title == "Lap Dance":
        idx = lap_counter[0]
        lap_counter[0] += 1
        return LAP_DANCE_IDS[min(idx, len(LAP_DANCE_IDS) - 1)]
    return TITLE_TO_ID.get(title)


def copy_alias(alias_png: str, source_key: str) -> bool:
    src = os.path.join(OUT, f"pic_{source_key}.png")
    dst = os.path.join(OUT, alias_png if alias_png.endswith(".png") else f"{alias_png}.png")
    if not os.path.exists(src):
        print(f"  FAIL alias {alias_png}: missing pic_{source_key}.png", file=sys.stderr)
        return False
    shutil.copy2(src, dst)
    print(f"  OK {os.path.basename(dst)} <- pic_{source_key}.png")
    return True


def remove_obsolete() -> int:
    removed = 0
    for name in OBSOLETE_STICK_FIGURES:
        path = os.path.join(OUT, f"{name}.png")
        if os.path.exists(path):
            os.remove(path)
            print(f"  DEL {name}.png (obsolete stick figure)")
            removed += 1
    return removed


def main() -> int:
    print("Fetching SheKnows article...")
    html = fetch_html(ARTICLE_URL)
    positions, categories = scrape_article_images(html)
    print(f"Found {len(positions)} positions, {len(categories)} category images")

    lap_counter = [0]
    errors = 0

    print("\n[1/4] Position illustrations...")
    for title, base_url in positions:
        pid = resolve_position_id(title, lap_counter)
        if not pid:
            print(f"  SKIP (no id): {title}")
            errors += 1
            continue
        try:
            img = download_image(hi_res_url(base_url))
            path = save_named_image(img, f"pic_{pid}")
            print(f"  OK pic_{pid}.png <- {title}")
        except Exception as exc:
            print(f"  FAIL {title}: {exc}", file=sys.stderr)
            errors += 1

    print("\n[2/4] Category header images...")
    for cat_id, base_url in categories.items():
        try:
            img = download_image(hi_res_url(base_url))
            save_named_image(img, f"pic_{cat_id}")
            print(f"  OK pic_{cat_id}.png")
        except Exception as exc:
            print(f"  FAIL pic_{cat_id}: {exc}", file=sys.stderr)
            errors += 1

    print("\n[3/4] Cover + supplemental (edu, chapters, imagination)...")
    cover_url = (
        "https://www.sheknows.com/wp-content/uploads/2025/04/"
        "69-Sex-Positions-to-Put-on-Your-Bucket-List-Immediately.jpg?w=1024"
    )
    try:
        img = download_image(cover_url)
        save_named_image(img, "pic_guide_cover")
        print("  OK pic_guide_cover.png")
    except Exception as exc:
        print(f"  FAIL cover: {exc}", file=sys.stderr)
        errors += 1

    for alias, source in SUPPLEMENTAL_ALIASES.items():
        if not copy_alias(alias, source):
            errors += 1

    print("\n[4/4] Cleanup obsolete stick figures...")
    remove_obsolete()

    total = len([f for f in os.listdir(OUT) if f.endswith(".png")])
    print(f"\nDone — {total} PNG assets in drawable-nodpi")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
