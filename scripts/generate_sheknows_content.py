#!/usr/bin/env python3
"""Generate SheKnows 69-position bilingual content, diagrams, and Kotlin repository."""
from __future__ import annotations

import importlib.util
import os
import sys
import types
from typing import Any, Dict, List

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(SCRIPT_DIR)
OUT_IMG = os.path.join(ROOT, "app/src/main/res/drawable-nodpi")
OUT_KT = os.path.join(ROOT, "app/src/main/java/com/couplesguide/postures/data/SheKnowsPostureRepository.kt")

SOURCE_BASE = (
    "https://www.sheknows.com/health-and-wellness/slideshow/"
    "5919/sex-positions-to-try-before-you-die/"
)

# Load illustration helpers from existing generator (register module for dataclasses)
_spec = importlib.util.spec_from_file_location(
    "gen_pics", os.path.join(SCRIPT_DIR, "generate_posture_pictures.py")
)
gen = types.ModuleType("gen_pics")
sys.modules["gen_pics"] = gen
_spec.loader.exec_module(gen)  # type: ignore

CATEGORIES = {
    "classic": ("Classic" , "کلاسک"),
    "non_penetrative": ("Non-Penetrative", "غیر داخلی"),
    "elevated": ("Elevated", "اونچی سطح"),
    "shower": ("Shower", "شاور"),
    "bondage": ("Bondage", "بندھن"),
    "car": ("Car", "گاڑی"),
    "solo": ("Solo / Masturbation", "اکیلے"),
    "flat": ("Flat", "سیدھے لیٹ کر"),
    "blindfold": ("Blindfolded", "آنکھوں پر پٹی"),
    "anal": ("Anal Variations", "پیچھے سے متبادل"),
    "beach": ("Beach-Inspired", "ساحل"),
    "orgasm": ("For Vaginal Orgasm", "اندام نہانی لطف"),
    "creative": ("Creative", "تخلیقی"),
}

DIFFICULTY = {
    "beginner": "BEGINNER",
    "intermediate": "INTERMEDIATE",
    "advanced": "ADVANCED",
}

# template -> draw function
def draw_template(draw, template: str):
    bed_y = 400
    if template == "missionary":
        gen.bed(draw, bed_y)
        gen.draw_figure_simple(draw, gen.lying_back(430, 390, 1.0), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.on_top(430, 330, 0.95), gen.SKIN_B)
        gen.tag(draw, 560, 345, "Face to face")
    elif template == "doggy":
        gen.bed(draw, 415)
        gen.draw_figure_simple(draw, gen.hands_knees(400, 360, 1.0), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.kneeling_behind(520, 330, 0.95), gen.SKIN_B)
        gen.tag(draw, 515, 320, "Rear entry")
    elif template == "spooning":
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.side_lying(500, 380, "left", 1.05), gen.SKIN_B)
        gen.draw_figure_simple(draw, gen.side_lying(420, 385, "left", 1.0), gen.SKIN_A)
        gen.tag(draw, 600, 300, "Spooning")
    elif template == "cowgirl":
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.lying_back(430, 400, 0.95), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.straddle(430, 290, 0.9), gen.SKIN_B)
        gen.tag(draw, 560, 250, "On top")
    elif template == "reverse_cowgirl":
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.lying_back(430, 400, 0.95), gen.SKIN_A)
        p = gen.straddle(430, 295, 0.9)
        p = gen.pose(**{**p.__dict__, "head": (p.head[0], p.head[1] + 8)})
        gen.draw_figure_simple(draw, p, gen.SKIN_B, show_pelvis=False)
        gen.tag(draw, 560, 250, "Facing away")
    elif template == "seated_face":
        draw.rounded_rectangle((120, 430, gen.W - 120, 500), radius=16, fill=gen.BED, outline=(190, 170, 160), width=2)
        gen.draw_figure_simple(draw, gen.seated(430, 400, 1.0), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.straddle(430, 320, 0.85), gen.SKIN_B)
        gen.tag(draw, 560, 300, "Seated embrace")
    elif template == "scissors":
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.side_lying(360, 380, "right", 1.0), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.side_lying(520, 385, "left", 1.0), gen.SKIN_B)
        gen.tag(draw, 600, 330, "Legs intertwined")
    elif template == "butterfly":
        gen.bed(draw, 400)
        gen.pillow(draw, (360, 375, 500, 395))
        p = gen.lying_back(400, 360, 0.95)
        p = gen.pose(**{**p.__dict__,
            "knee_l": (p.knee_l[0] - 15, p.knee_l[1] - 25),
            "knee_r": (p.knee_r[0] + 15, p.knee_r[1] - 25)})
        gen.draw_figure_simple(draw, p, gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.standing(540, 290, 0.85), gen.SKIN_B)
        gen.tag(draw, 560, 240, "Hips elevated")
    elif template == "standing":
        draw.rounded_rectangle((700, 120, 740, 480), radius=8, fill=(210, 200, 195))
        gen.draw_figure_simple(draw, gen.standing(500, 280, 1.0), gen.SKIN_B)
        gen.draw_figure_simple(draw, gen.lifted_legs(420, 310, 0.85), gen.SKIN_A)
        gen.tag(draw, 560, 200, "Standing")
    elif template == "edge_bed":
        gen.bed(draw, 400)
        gen.draw_figure_simple(draw, gen.lying_back(350, 385, 0.95), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.standing(540, 290, 0.9), gen.SKIN_B)
        gen.tag(draw, 495, 335, "At edge")
    elif template == "side_face":
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.side_lying(360, 380, "right", 1.0), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.side_lying(540, 380, "left", 1.0), gen.SKIN_B)
        gen.tag(draw, 420, 280, "Facing")
    elif template == "prone_stack":
        gen.bed(draw, 415)
        gen.pillow(draw, (350, 380, 490, 400))
        pa = gen.hands_knees(400, 390, 0.9)
        pa = gen.pose(**{**pa.__dict__, "head": (pa.head[0] + 20, pa.head[1] + 30)})
        gen.draw_figure_simple(draw, pa, gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.on_top(420, 350, 0.85), gen.SKIN_B)
        gen.tag(draw, 560, 310, "Flat")
    elif template == "counter":
        draw.rounded_rectangle((80, 360, gen.W - 80, 400), radius=8, fill=(200, 185, 175), outline=gen.SECONDARY, width=2)
        gen.draw_figure_simple(draw, gen.lying_back(400, 370, 0.85), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.standing(540, 280, 0.9), gen.SKIN_B)
        gen.tag(draw, 560, 250, "Counter height")
    elif template == "solo_kneel":
        draw.rounded_rectangle((120, 430, gen.W - 120, 500), radius=16, fill=gen.BED, outline=(190, 170, 160), width=2)
        gen.draw_figure_simple(draw, gen.seated(480, 360, 1.1), gen.SKIN_A, show_pelvis=False)
        gen.tag(draw, 600, 300, "Solo")
    elif template == "solo_lying":
        gen.bed(draw, 405)
        gen.pillow(draw, (400, 385, 520, 405))
        gen.draw_figure_simple(draw, gen.lying_prone(480, 390, 1.0), gen.SKIN_A)
        gen.tag(draw, 600, 320, "Solo")
    elif template == "hands_only":
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.lying_back(400, 390, 0.95), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.seated(560, 340, 0.85), gen.SKIN_B, show_pelvis=False)
        gen.tag(draw, 600, 300, "Manual focus")
    elif template == "oral_top":
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.lying_back(400, 400, 0.9), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.kneeling_behind(520, 360, 0.8), gen.SKIN_B)
        gen.tag(draw, 560, 320, "Oral focus")
    else:
        gen.bed(draw, 405)
        gen.draw_figure_simple(draw, gen.lying_back(400, 390, 0.95), gen.SKIN_A)
        gen.draw_figure_simple(draw, gen.on_top(400, 335, 0.85), gen.SKIN_B)


def gen_image(pic_id: str, title: str, template: str):
    img, draw = gen.new_canvas("SheKnows Sex Education")
    draw_template(draw, template)
    gen.partner_labels(draw)
    gen.title_label(draw, title[:48])
    gen.save(pic_id, img)


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace("\"", "\\\"")


def kotlin_string_list(items: List[str], indent: str = "                ") -> str:
    if not items:
        return "emptyList()"
    lines = ["listOf("]
    for item in items:
        lines.append(f'{indent}    "{esc(item)}",')
    lines.append(f"{indent})")
    return "\n".join(lines)


def kotlin_role(en_pos: str, ur_pos: str, en_guidance: List[str], ur_guidance: List[str]) -> str:
    return f"""PartnerRole(
                position = "{esc(en_pos)}",
                guidance = {kotlin_string_list(en_guidance, "                    ")}
            )""", f"""PartnerRole(
                position = "{esc(ur_pos)}",
                guidance = {kotlin_string_list(ur_guidance, "                    ")}
            )"""


# 69 SheKnows positions (curated from article)
POSITIONS: List[Dict[str, Any]] = [
    # Classic (9)
    {"id": "sk_cat", "cat": "classic", "diff": "intermediate", "tpl": "missionary",
     "en": "Modified Coital-Alignment Technique", "ur": "ترمیم شدہ CAT مشنری",
     "sum_en": "Face-to-face with upward grinding instead of thrusting.",
     "sum_ur": "آمنے سامنے، جھٹکوں کی بجائے اوپر نیچے رگڑ۔",
     "desc_en": "An upgraded missionary where the penetrating partner shifts weight forward so contact presses along the external vulva and clitoris while moving in circles rather than in and out.",
     "desc_ur": "بہتر مشنری جہاں اوپر والا وزن آگے رکھے تاکہ کلائٹورس اور بیرونی حصے پر دباؤ آئے اور گول حرکت کرے۔",
     "steps_en": ["Receiving partner lies on back.", "Penetrating partner enters from above.", "Shift weight forward — avoid deep thrusting.", "Move hips in slow circles.", "Receiver tilts hips and wraps legs as comfortable."],
     "steps_ur": ["سامنے والا پیٹ کے بل لیٹے۔", "دوسرا اوپر سے داخل ہو۔", "وزن آگے رکھیں — گہری جھٹکوں سے بچیں۔", "کولہے آہستہ گول گھمائیں۔", "لیٹا والا کولہے کا زاویہ بدلے۔"],
     "tips_en": ["Massages G-spot and clitoris together.", "Great for couples wanting more clitoral contact.", "Communicate about hip angle."],
     "tips_ur": ["جی سپاٹ اور کلائٹورس ساتھ محرک ہوتے ہیں۔", "زیادہ کلائٹورل رابطے کے لیے بہترین۔", "کولہے کے زاویے پر بات کریں۔"],
     "man_en": "On top, weight forward, circular hip motion", "man_ur": "اوپر، وزن آگے، گول حرکت",
     "woman_en": "On back, experiment with hip tilt and leg wrap", "woman_ur": "پیٹ کے بل، کولہے اور ٹانگیں ایڈجسٹ کریں"},
    {"id": "sk_doggy", "cat": "classic", "diff": "beginner", "tpl": "doggy",
     "en": "Doggy Style", "ur": "ڈوگی سٹائل",
     "sum_en": "Receiving partner on all fours; partner enters from behind.",
     "sum_ur": "سامنے والا چاروں پر، پیچھے سے داخلہ۔",
     "desc_en": "Classic rear-entry position. The receiving partner gets on all fours while the penetrating partner kneels or stands behind. Allows cat-cow pelvic movement and manual stimulation.",
     "desc_ur": "کلاسک پیچھے سے پوزیشن۔ سامنے والا ہاتھ گھٹنوں پر، دوسرا پیچھے سے۔ کولہے کی حرکت اور ہاتھ سے محرک ممکن۔",
     "steps_en": ["Receiver gets on hands and knees.", "Partner kneels or stands behind.", "Receiver cat-cows pelvis for pressure.", "Partner grips hips as both prefer.", "Adjust depth and pace together."],
     "steps_ur": ["سامنے والا ہاتھ گھٹنوں پر آئے۔", "ساتھی پیچھے گھٹنوں یا کھڑے ہو۔", "کولہے آگے پیچھے ہلائیں۔", "کولہے پکڑیں جیسا آرام ہو۔", "گہرائی اور رفتار ساتھ طے کریں۔"],
     "tips_en": ["Access to G-spot or A-spot by angle.", "Receiver can stimulate clitoris by hand.", "Try flat doggy or wheelbarrow variations."],
     "tips_ur": ["زاویے سے جی یا اے سپاٹ تک رسائی۔", "ہاتھ سے کلائٹورل محرک۔", "فلیٹ ڈوگی یا وہیل بیرو آزمائیں۔"],
     "man_en": "Behind receiver, kneeling or standing", "man_ur": "پیچھے، گھٹنوں یا کھڑے",
     "woman_en": "On all fours, control depth with hip shift", "woman_ur": "چاروں پر، کولہے سے گہرائی کنٹرول"},
    {"id": "sk_pushing_tush", "cat": "classic", "diff": "intermediate", "tpl": "missionary",
     "en": "Pushing Tush", "ur": "پشنگ ٹش",
     "sum_en": "Face-to-face missionary with anal entry.",
     "sum_ur": "آمنے سامنے مشنری، پیچھے سے داخلہ۔",
     "desc_en": "Missionary position with anal rather than vaginal entry. Use a pillow under hips and plenty of lubricant.",
     "desc_ur": "مشنری پوزیشن میں پیچھے سے داخلہ۔ کولہے کے نیچے تکیہ اور کافی لوبریکنٹ استعمال کریں۔",
     "steps_en": ["Assume missionary alignment.", "Place pillow under receiver's hips.", "Apply generous lubricant inside and out.", "Enter slowly watching facial cues.", "Receiver tilts hips to open anal canal."],
     "steps_ur": ["مشنری کی پوزیشن لیں۔", "کولہے کے نیچے تکیہ رکھیں۔", "اندر باہر لوبریکنٹ لگائیں۔", "آہستہ داخل ہوں، چہرے کے اشارے دیکھیں۔", "کولہے کا زاویہ کھولیں۔"],
     "tips_en": ["Lube is essential — anal canal is not self-lubricating.", "Face-to-face allows comfort reading.", "Consider vibrating plug for dual stimulation."],
     "tips_ur": ["لوبریکنٹ ضروری ہے۔", "آمنے سامنے آرام پڑھنا آسان ہے۔", "دگہری محرک کے لیے وائبریٹنگ پلگ آزمائیں۔"],
     "man_en": "On top, slow face-to-face anal entry", "man_ur": "اوپر، آہستہ آمنے سامنے",
     "woman_en": "On back with hip pillow, guide pace verbally", "woman_ur": "تکیے کے ساتھ پیٹ کے بل، رفتار بتائیں"},
    {"id": "sk_rocking_horse", "cat": "classic", "diff": "beginner", "tpl": "seated_face",
     "en": "Rocking Horse", "ur": "راکنگ ہارس",
     "sum_en": "Receiver sits between partner's legs; both rock together.",
     "sum_ur": "سامنے والا ساتھی کی ٹانگوں کے درمیان بیٹھے؛ دونوں ساتھ جھولیں۔",
     "desc_en": "Seated face-to-face with intimate eye contact. Receiver sits between penetrating partner's legs with legs nearly wrapped around them.",
     "desc_ur": "بیٹھ کر آمنے سامنے، آنکھوں کا رابطہ۔ سامنے والا ساتھی کی ٹانگوں کے بیچ بیٹھے۔",
     "steps_en": ["Penetrating partner sits with legs extended.", "Receiver sits between their legs.", "Wrap legs loosely around partner.", "Rock hips together to control depth.", "Hold each other close."],
     "steps_ur": ["ساتھی بیٹھے ٹانگیں پھیلائے۔", "سامنے والا درمیان میں بیٹھے۔", "ٹانگیں ہلکے لپیٹیں۔", "کولہے ساتھ جھولائیں۔", "قریب رہیں۔"],
     "tips_en": ["Excellent G-spot stimulation.", "Can be gentle or passionate.", "Control depth by rocking rhythm."],
     "tips_ur": ["جی سپاٹ محرک بہترین۔", "نرم یا پرجوش دونوں ہو سکتا ہے۔", "جھولنے کی تال سے گہرائی کنٹرول۔"],
     "man_en": "Seated base, supports receiver while rocking", "man_ur": "بیٹھے، سہارا دے کر جھولیں",
     "woman_en": "Sits on lap between legs, sets rocking pace", "woman_ur": "گود میں بیٹھ کر تال طے کریں"},
    {"id": "sk_seated_scissors", "cat": "classic", "diff": "intermediate", "tpl": "scissors",
     "en": "Seated Scissors", "ur": "بیٹھی قینچی",
     "sum_en": "Playful reverse-cowgirl variation on a bent leg.",
     "sum_ur": "موڑی ہوئی ٹانگ پر الٹ کاؤگرل جیسی تفریحی پوزیشن۔",
     "desc_en": "Penetrating partner lies back with one leg bent. Receiver straddles the bent leg and arranges legs comfortably on top.",
     "desc_ur": "نیچے والا پیٹ کے بل ایک ٹانگ موڑے۔ اوپر والا موڑی ٹانگ پر بیٹھے۔",
     "steps_en": ["Partner lies on back, one knee bent.", "Receiver straddles bent leg.", "Arrange top legs for comfort.", "Bounce, bump, or grind.", "Bottom partner relaxes and enjoys the view."],
     "steps_ur": ["نیچے والا پیٹ کے بل، ایک گھٹنا موڑے۔", "اوپر والا اس ٹانگ پر بیٹھے۔", "ٹانگیں آرام سے رکھیں۔", "اچھلیں یا رگڑیں۔", "نیچے والا آرام کرے۔"],
     "tips_en": ["Fun for both partners.", "Receiver controls most movement.", "Plenty of room to experiment."],
     "tips_ur": ["دونوں کے لیے مزیدار۔", "اوپر والا حرکت کنٹرول کرے۔", "تجربے کی گنجائش زیادہ۔"],
     "man_en": "Lies back with one leg bent as anchor", "man_ur": "پیٹ کے بل، ایک ٹانگ موڑی",
     "woman_en": "Straddles bent leg, controls bounce and grind", "woman_ur": "موڑی ٹانگ پر بیٹھ کر حرکت کریں"},
    {"id": "sk_spooning", "cat": "classic", "diff": "beginner", "tpl": "spooning",
     "en": "Spooning", "ur": "چمچے والی",
     "sum_en": "Side-by-side rear entry like cuddling spoons.",
     "sum_ur": "ساتھ لیٹ کر پیچھے سے، گلے ملنے جیسا۔",
     "desc_en": "Big spoon enters from behind while both lie on their sides. Ultra-intimate with free hands for touch and clitoral stimulation.",
     "desc_ur": "پیچھے والا سیدھے لیٹ کر پیچھے سے داخل ہو۔ ہاتھ آزاد چھونے کے لیے۔",
     "steps_en": ["Both lie on sides, same direction.", "Big spoon curls behind little spoon.", "Enter vaginally or anally from behind.", "Use free hands for touch.", "Move slowly — easy to snuggle after."],
     "steps_ur": ["دونوں ایک سمت سیدھے لیٹیں۔", "پیچھے والا آگے والے کے پیچھے۔", "آہستہ داخل ہوں۔", "ہاتھ سے محرک دیں۔", "بعد میں گلے مل سکتے ہیں۔"],
     "tips_en": ["Great for slow mornings.", "Remember to urinate after sex.", "Hands free for clitoral play."],
     "tips_ur": ["صبح کی آرام دہ قربت کے لیے بہترین۔", "بعد میں پیشاب کریں۔", "ہاتھ سے کلائٹورل لطف۔"],
     "man_en": "Big spoon behind, enters gently", "man_ur": "پیچھے سے آہستہ داخل ہوں",
     "woman_en": "Little spoon in front, guides with hips and hand", "woman_ur": "سامنے لیٹیں، کولہے اور ہاتھ سے رہنمائی"},
    {"id": "sk_scissoring", "cat": "classic", "diff": "beginner", "tpl": "scissors",
     "en": "Scissoring", "ur": "سیزرنگ",
     "sum_en": "Genital-to-genital grinding for any gender pairing.",
     "sum_ur": "کسی بھی جوڑے کے لیے رگڑ کر خارجی محرک۔",
     "desc_en": "Partners lie with heads opposite, straddling legs to grind pubic areas together. Focus is external stimulation, not penetration.",
     "desc_ur": "سر مخالف سمت، ٹانگیں ملاکر عضو ٹھانیوں کو رگڑیں۔ داخلہ نہیں، خارجی لطف۔",
     "steps_en": ["Lie with heads at opposite ends.", "Straddle each other's legs.", "Grind calves, knees, or genitals together.", "Or shimmy until genital contact.", "Find rhythm that feels good."],
     "steps_ur": ["سر مخالف سمت لیٹیں۔", "ٹانگیں ایک دوسرے پر رکھیں۔", "رانوں یا عضو ٹھانی رگڑیں۔", "جب رابطہ ہو تو تال بنائیں۔", "آرام دہ رفتار تلاش کریں۔"],
     "tips_en": ["Penetration isn't required for great sex.", "Lower STI risk without genital contact variant.", "Works across body types."],
     "tips_ur": ["داخلہ ضروری نہیں۔", "بغیر رابطے والے متبادل میں کم خطرہ۔", "ہر جسم کے لیے موزوں۔"],
     "man_en": "Grinds with partner at chosen angle", "man_ur": "ساتھی کے ساتھ زاویے پر رگڑیں",
     "woman_en": "Controls pressure and grinding rhythm", "woman_ur": "دباؤ اور رفتار کنٹرول کریں"},
    {"id": "sk_bend_over", "cat": "classic", "diff": "beginner", "tpl": "doggy",
     "en": "Bend Over, Baby", "ur": "جھک جاؤ بیبی",
     "sum_en": "90-degree bend for shallow penetration.",
     "sum_ur": "نوے ڈگری جھکاؤ، کم گہرائی۔",
     "desc_en": "Receiver bends at 90 degrees. Ideal when a smaller penis needs to feel fuller through angle and pelvic tilt.",
     "desc_ur": "سامنے والا نوے ڈگری جھکے۔ چھوٹے سائز کے لیے زاویہ بہتر بناتا ہے۔",
     "steps_en": ["Receiver bends forward at waist.", "Keep back relatively flat.", "Tilt pelvis to find hot spots.", "Partner enters from behind.", "Adjust angle together."],
     "steps_ur": ["کمر سے آگے جھکیں۔", "پیٹھ سیدھی رکھیں۔", "کولہے کا زاویہ بدلیں۔", "پیچھے سے داخل ہوں۔", "زاویہ ساتھ مل کر ٹھیک کریں۔"],
     "tips_en": ["Shallow penetration can feel intense.", "Great for targeted stimulation.", "Communicate about depth."],
     "tips_ur": ["کم گہرائی بھی شدید محسوس ہو سکتی ہے۔", "مخصوص محرک کے لیے اچھا۔", "گہرائی پر بات کریں۔"],
     "man_en": "Enters from behind at bent angle", "man_ur": "جھکے ہوئے پیچھے سے",
     "woman_en": "Bent at 90°, tilts pelvis for sensation", "woman_ur": "نوے ڈگری جھکیں، کولہے ہلائیں"},
    {"id": "sk_scissors_classic", "cat": "classic", "diff": "intermediate", "tpl": "side_face",
     "en": "Scissors (Side)", "ur": "قینچی (سیدھے)",
     "sum_en": "Side-lying facing each other for thicker anatomy.",
     "sum_ur": "آمنے سامنے سیدھے، موٹے سائز کے لیے۔",
     "desc_en": "Partners lie on sides facing each other with heads on opposite bed sides. Receiver straddles a leg for comfortable penetration.",
     "desc_ur": "دونوں سیدھے آمنے سامنے، سر بستر کے مخالف کناروں پر۔ ایک ٹانگ پر بیٹھ کر داخلہ۔",
     "steps_en": ["Lie on sides facing each other.", "Heads on opposite sides of bed.", "Receiver straddles partner's leg.", "Lift one leg to open for entry.", "Use friction and close contact."],
     "steps_ur": ["سیدھے آمنے سامنے لیٹیں۔", "سر مخالف سمت۔", "ساتھی کی ٹانگ پر بیٹھیں۔", "ایک ٹانگ اٹھا کر کھولیں۔", "رگڑ اور قربت استعمال کریں۔"],
     "tips_en": ["Good for thicker penis comfort.", "Creates friction and closeness.", "Fireworks from start to finish."],
     "tips_ur": ["موٹے سائز کے لیے آرام دہ۔", "رگڑ اور قربت بڑھتی ہے۔", "شروع سے لطف۔"],
     "man_en": "Lies on side, provides stable leg for straddle", "man_ur": "سیدھے لیٹیں، ٹانگ سہارا دے",
     "woman_en": "Straddles leg, controls angle of entry", "woman_ur": "ٹانگ پر بیٹھ کر زاویہ کنٹرول"},
]

# Append remaining positions in batches via helper
def P(id_, cat, diff, tpl, en, ur, sum_en, sum_ur, desc_en, desc_ur,
      steps_en, steps_ur, tips_en, tips_ur,
      man_en="Active partner", man_ur="فعال ساتھی",
      woman_en="Receiving partner", woman_ur="وصول کنندہ",
      solo=False):
    return {
        "id": id_, "cat": cat, "diff": diff, "tpl": tpl,
        "en": en, "ur": ur, "sum_en": sum_en, "sum_ur": sum_ur,
        "desc_en": desc_en, "desc_ur": desc_ur,
        "steps_en": steps_en, "steps_ur": steps_ur,
        "tips_en": tips_en, "tips_ur": tips_ur,
        "man_en": man_en, "man_ur": man_ur,
        "woman_en": woman_en, "woman_ur": woman_ur,
        "solo": solo,
    }


POSITIONS.extend([
    # Non-penetrative (4)
    P("sk_uncloak", "non_penetrative", "beginner", "hands_only",
      "Uncloak the Clitoris", "کلائٹورس کو بے نقاب کریں",
      "Manual clitoral focus with communication.", "ہاتھ سے کلائٹورل محرک، بات چیت کے ساتھ۔",
      "Hands-only position focusing on glans clitoris stimulation with partner communication about touch style.",
      "ہاتھ سے کلائٹورس کی نوک کو محرک دینا، ساتھی سے پوچھ کر طریقہ طے کرنا۔",
      ["Ask what touch they prefer.", "Try tapping, pressing, or circling.", "Some need indirect touch through labia.", "Stay attuned to feedback.", "Build rhythm together."],
      ["پوچھیں کون سا چھونا پسند ہے۔", "تپ، دباؤ یا گول گھماؤ آزمائیں۔", "کچھ کو بالوں کے ذریعے نرم چھونا چاہیے۔", "ردعمل دیکھتے رہیں۔", "تال ساتھ بنائیں۔"],
      ["70% of women need clitoral stimulation.", "Encourages bedroom communication.", "No penetration required."],
      ["زیادہ تر خواتین کو کلائٹورل محرک چاہیے۔", "بات چیت بڑھاتی ہے۔", "داخلہ ضروری نہیں۔"]),
    P("sk_scepter", "non_penetrative", "intermediate", "hands_only",
      "Baring the Scepter", "بیرینگ دی سپیئرر",
      "DIY vibrating ring with fingers at penis base.", "انگلیوں سے عضو مخصوص کی جڑ پر حلقہ۔",
      "Partner forms thumb-forefinger ring at penis base and pulls slightly during intercourse for firmer erection.",
      "انگوٹھا اور شہادت سے جڑ پر حلقہ بنا کر ہلکا کھینچیں تاکہ سختی بڑھے۔",
      ["Form ring at penis base.", "Pull skin taut gently.", "Maintain during intercourse if possible.", "Communicate pressure level.", "Alternative to store-bought ring."],
      ["عضو کی جڑ پر حلقہ بنائیں۔", "جلد ہلکے کھینچیں۔", "ممکن ہو تو عمل کے دوران رکھیں۔", "دباؤ کے بارے میں بات کریں۔", "خریدی انگوٹی کا متبادل۔"],
      ["Slows blood flow for harder erection.", "No toy required.", "Rock-hard erection not mandatory for pleasure."],
      ["خون کے بہاؤ کو روک کر سختی بڑھاتا ہے۔", "کھلونے کی ضرورت نہیں۔", "مکمل سختی لطف کے لیے ضروری نہیں۔"]),
    P("sk_self_loving", "non_penetrative", "beginner", "solo_kneel",
      "Self-Loving (On Your Knees)", "خود محبت (گھٹنوں پر)",
      "Solo or partnered masturbation on pillow or thigh.", "تکیے یا ران پر اکیلے یا ساتھی کے ساتھ۔",
      "Straddle a firm pillow or partner's thigh and grind to preferred rhythm. Great for showing partner what you like.",
      "مضبوط تکیے یا ساتھی کی ران پر بیٹھ کر رفتار سے رگڑیں۔ ساتھی کو دکھانے کے لیے بہترین۔",
      ["Choose firm pillow or thigh.", "Straddle and set rhythm.", "Grind for desired friction.", "Share with partner if desired.", "No toys needed."],
      ["مضبوط تکیہ یا ران چنیں۔", "بیٹھ کر تال طے کریں۔", "رگڑ سے لطف لیں۔", "چاہیں تو ساتھی کو دکھائیں۔", "کھلونے ضروری نہیں۔"],
      ["Simple yet effective.", "Helps vulva owners get friction.", "Educational for couples."],
      ["سادہ مگر مؤثر۔", "خواتین کے لیے رگڑ بہترین۔", "جوڑوں کی تعلیم کے لیے۔"],
      solo=True),
    P("sk_queening", "non_penetrative", "intermediate", "oral_top",
      "Queening in Bondage", "کویننگ بندھن میں",
      "Oral receiving on top with optional restraint.", "اوپر بیٹھ کر زبانی لطف، اختیاری بندھن۔",
      "Receiver rests on or above partner's mouth for oral stimulation. Weight on knees and thighs — communicate pressure.",
      "وصول کنندہ ساتھی کے منہ پر یا اوپر بیٹھے۔ وزن گھٹنوں پر — دباؤ بتائیں۔",
      ["Receiver kneels over partner's face.", "Support weight on thighs.", "Set pace and pressure.", "Optional restraint for power play.", "Use safe words if binding."],
      ["وصول کنندہ منہ پر بیٹھے۔", "وزن رانوں پر رکھیں۔", "رفتار اور دباؤ طے کریں۔", "اختیاری بندھن۔", "بندھن ہو تو محفوظ لفظ استعمال کریں۔"],
      ["Power dynamic is enticing.", "Receiver controls pace.", "Restraint intensifies sensation."],
      ["اختیار کا عنصر پرکشش۔", "وصول کنندہ رفتار طے کرے۔", "بندھن سے شدت بڑھتی ہے۔"]),
    # Elevated (4)
    P("sk_countertop", "elevated", "beginner", "counter",
      "Countertop", "کاؤنٹر ٹاپ",
      "Sex on any hip-height flat surface.", "کولہے کی اونچائی کی کسی بھی سطح پر۔",
      "Receiver lies or sits on sturdy counter, desk, or table. Penetrating partner stands between legs.",
      "وصول کنندہ کاؤنٹر یا میز پر بیٹھے یا لیٹے۔ دوسرا درمیان میں کھڑا ہو۔",
      ["Find sturdy hip-height surface.", "Receiver lies or sits securely.", "Partner stands between legs.", "Hands free for nipple and clitoral touch.", "Works for penetration or oral."],
      ["مضبوط سطح تلاش کریں۔", "وصول کنندہ محفوظ بیٹھے یا لیٹیں۔", "ساتھی درمیان کھڑا ہو۔", "ہاتھ آزاد محرک کے لیے۔", "داخلہ یا زبانی دونوں۔"],
      ["Fulfills kitchen or office fantasies.", "Both hands free.", "Oral variation: giver kneels."],
      ["کچن یا دفتر کی فنتاسی۔", "دونوں کے ہاتھ آزاد۔", "زبانی: دینے والا گھٹنوں پر۔"]),
    P("sk_happy_scissors", "elevated", "intermediate", "counter",
      "Happy Scissors", "ہیپی سیزرز",
      "Receiver on surface with legs splayed upward.", "سطح پر لیٹے، ٹانگیں اوپر پھیلائیں۔",
      "Like Countertop but receiver splays legs and points toes to ceiling for open, erotic access.",
      "کاؤنٹر ٹاپ جیسا لیکن ٹانگیں کھول کر پاؤں چھت کی طرف۔",
      ["Receiver on hip-height surface.", "Splay legs wide, toes up.", "Partner stands and enters.", "Explore power dynamics.", "Access legs and feet erogenous zones."],
      ["کولہے کی اونچائی پر لیٹیں۔", "ٹانگیں چوڑی کھولیں۔", "ساتھی کھڑا داخل ہو۔", "اختیار کھیلیں۔", "ٹانگوں اور پاؤں کو چھوئیں۔"],
      ["Open-legged pose is erotic.", "Submission energy for some.", "Try toe play if curious."],
      ["کھلی ٹانگیں پرکشش۔", "کچھ کے لیے تسلیم کا عنصر۔", "پاؤں کا لطف آزمائیں۔"]),
    P("sk_butterfly", "elevated", "intermediate", "butterfly",
      "The Butterfly", "تتلی",
      "Heels on shoulders for deep penetration.", "ایڑیاں کندھوں پر، زیادہ گہرائی۔",
      "Receiver on elevated surface with heels over partner's shoulders. Standing partner uses athletic stance.",
      "وصول کنندہ اونچی سطح پر، ایڑیاں ساتھی کے کندھوں پر۔",
      ["Receiver lies on elevated bed or table.", "Place heels on partner's shoulders.", "Partner stands in athletic stance.", "Receiver's hands free for clitoral play.", "Adjust elevation for comfort."],
      ["اونچی سطح پر لیٹیں۔", "ایڑیاں کندھوں پر رکھیں۔", "ساتھی کھڑا مضبوط پوزیشن۔", "ہاتھ سے کلائٹورس۔", "اونچائی ایڈجسٹ کریں۔"],
      ["Great visual for standing partner.", "Allows cervical stimulation.", "Deeper is the motto."],
      ["کھڑے ساتھی کے لیے منظر۔", "گریوائیکل محرک۔", "زیادہ گہرائی کے لیے۔"]),
    P("sk_lap_dance", "elevated", "beginner", "cowgirl",
      "Lap Dance", "لیپ ڈانس",
      "Receiver straddles seated partner's lap.", "وصول کنندہ بیٹھے ساتھی کی گود میں۔",
      "Use armless chair or surface. Receiver straddles lap face-to-face or front-to-back and grinds.",
      "کرسی پر بیٹھے ساتھی کی گود میں آمنے سامنے یا پیٹھ کر کے۔",
      ["Partner sits on sturdy chair.", "Receiver straddles lap.", "Feet on floor for leverage.", "Rotate, bounce, grind.", "Deep penetration and eye contact."],
      ["ساتھی مضبوط کرسی پر بیٹھے۔", "گود میں بیٹھیں۔", "پاؤں فرش پر۔", "گھمائیں، اچھلیں، رگڑیں۔", "گہرائی اور آنکھوں کا رابطہ۔"],
      ["Accessible for different heights.", "Top partner does the work.", "Wheelchair-friendly option."],
      ["اونچائی کے فرق میں آسان۔", "اوپر والا محنت کرے۔", "وہیل چیئر کے لیے موزوں۔"]),
    # Shower (2)
    P("sk_shower_front", "shower", "intermediate", "standing",
      "Standing Up Full-Frontal", "شاور میں سامنے سے کھڑے",
      "Shower sex with one leg lifted on tub edge.", "شاور میں ایک ٹانگ اٹھا کر سامنے سے۔",
      "Penetrating partner keeps balance on wet floor. Receiver lifts one leg to wrap or rest on tub rim.",
      "گیلے فرش پر توازن رکھیں۔ وصول کنندہ ایک ٹانگ اٹھائے۔",
      ["Lock door for privacy.", "Use tub bench or wide rim.", "Receiver lifts one leg.", "Set pace together on wet surface.", "Move to dry area when water cools."],
      ["دروازہ بند کریں۔", "ٹب کے کنارے کا سہارا لیں۔", "ایک ٹانگ اٹھائیں۔", "مل کر رفتار طے کریں۔", "پانی ٹھنڈا ہو تو خشک جگہ جائیں۔"],
      ["Sleek and sensual with water.", "Both can set pace.", "Easy transition when water runs out."],
      ["پانی کے ساتھ پرکشش۔", "دونوں رفتار طے کر سکتے ہیں۔", "آسان منتقلی۔"]),
    P("sk_soap_grope", "shower", "intermediate", "doggy",
      "Soap'n'Grope", "صابن اور چھونا",
      "Shower rear entry against wall.", "دیوار سے ٹیک لگا کر شاور میں پیچھے سے۔",
      "Receiver braces on wall; penetrating partner enters from behind in shower.",
      "وصول کنندہ دیوار پکڑے؛ دوسرا پیچھے سے داخل ہو۔",
      ["Receiver braces on shower wall.", "Partner enters from behind.", "Explore with soapy hands.", "Watch footing on wet floor.", "Keep it playful and safe."],
      ["وصول کنندہ دیوار پکڑے۔", "پیچھے سے داخل ہوں۔", "صابن والے ہاتھوں سے چھوئیں۔", "پھسلن سے بچیں۔", "تفریحی اور محفوظ رہیں۔"],
      ["Hands-on shower exploration.", "Sexy angle from behind.", "Good clean fun."],
      ["شاور میں ہاتھوں سے کھوج۔", "پیچھے سے پرکشش زاویہ۔", "صاف ستھرا مزہ۔"]),
    # Bondage (3)
    P("sk_hands_ankles", "bondage", "advanced", "prone_stack",
      "Hands Behind Ankles", "ہاتھ ایڑیوں کے پیچھے",
      "Hogtie-style bondage with cuffs and flexibility.", "کف اور لچک کے ساتھ بندھن۔",
      "Receiver lies prone, bends legs up, cuffs wrists behind ankles. Requires safe words and aftercare.",
      "پیٹ کے بل، ٹانگیں موڑ کر کلائیوں کو ایڑیوں سے باندھیں۔ محفوظ الفاظ ضروری۔",
      ["Discuss comfort and safe words first.", "Receiver lies belly-down, legs bent.", "Cuff wrists behind ankles.", "Partner enters carefully.", "Plan cozy aftercare."],
      ["پہلے بات چیت اور محفوظ الفاظ۔", "پیٹ کے بل ٹانگیں موڑیں۔", "کلائیاں ایڑیوں کے پیچھے باندھیں۔", "احتیاط سے داخل ہوں۔", "بعد میں آرام دہ دیکھ بھال۔"],
      ["Vulnerability builds trust.", "Hip stretch increases stimulation.", "Use toys if maneuvering is hard."],
      ["نازک پن اعتماد بڑھاتا ہے۔", "کولہے کی کھلائی محرک بڑھاتی ہے۔", "مشکل ہو تو کھلونا استعمال کریں۔"]),
    P("sk_kinky_missionary", "bondage", "intermediate", "missionary",
      "The Kinky Missionary", "کنکی مشنری",
      "Missionary with under-bed or headboard restraints.", "بستر کی کفوں کے ساتھ مشنری۔",
      "Restrain partner to bed then approach standard missionary. Face-to-face adds safety for BDSM beginners.",
      "ساتھی کو بستر سے باندھ کر معمولی مشنری۔ آمنے سامنے ابتدائیوں کے لیے محفوظ۔",
      ["Set up mattress or headboard cuffs.", "Restrain willing partner comfortably.", "Approach missionary position.", "Use facial cues and words.", "Try blindfolds or sensation play."],
      ["کف لگائیں۔", "رضامندی سے باندھیں۔", "مشنری پوزیشن لیں۔", "چہرے اور الفاظ سے پڑھیں۔", "آنکھوں پر پٹی آزمائیں۔"],
      ["Face-to-face feels safer.", "Power play with blindfolds possible.", "Troubleshoot together first time."],
      ["آمنے سامنے محفوظ محسوس ہوتا ہے۔", "پٹی سے اختیار کھیل۔", "پہلی بار مل کر درست کریں۔"]),
    P("sk_standing_room", "bondage", "intermediate", "standing",
      "Standing Room Only", "کھڑے بندھن",
      "Standing sex with cuff restraint.", "کھڑے ہو کر کفوں کے ساتھ۔",
      "Standing position with cuffs. Usually receiver is cuffed with leg slung around partner's waist or thigh.",
      "کھڑے ہو کر کف۔ عام طور پر وصول کنندہ بندھا، ٹانگ کمر یا ران پر۔",
      ["Choose over-door or sturdy cuffs.", "Cuffed partner adjusts leg position.", "Uncuffed partner supports weight.", "Check restraints aren't too tight.", "Switch if cuffed partner tires."],
      ["مضبوط کف چنیں۔", "ٹانگ کی پوزیشن ایڈجسٹ کریں۔", "دوسرا ساتھی سہارا دے۔", "بندھن تنگ نہ ہو۔", "تھکیں تو بدلیں۔"],
      ["Feels like an erotic movie scene.", "Angle plus cuffs intensifies.", "Over-door cuffs work well."],
      ["فلمی منظر جیسا۔", "زاویہ اور کف شدت بڑھاتے ہیں۔", "دروازے کی کف بہترین۔"]),
    # Car (5)
    P("sk_backseat", "car", "beginner", "cowgirl",
      "Backseat Driver", "بیک سیٹ ڈرائیور",
      "Straddling in the car backseat.", "گاڑی کی پچھلی سیٹ پر اوپر بیٹھنا۔",
      "Hop in backseat; receiver assumes straddling position for kissing or penetration.",
      "پچھلی سیٹ میں اوپر بیٹھنے والی پوزیشن۔",
      ["Park in private driveway.", "Receiver straddles in backseat.", "Customize kissing or penetration.", "Mind headroom and seats.", "Keep activity private and legal."],
      ["نجی جگہ پارک کریں۔", "پچھلی سیٹ میں اوپر بیٹھیں۔", "بوسہ یا داخلہ طے کریں۔", "سر کی جگہ دیکھیں۔", "قانونی اور نجی رہیں۔"],
      ["Highly customizable.", "Public sex is illegal most places.", "Private driveway recommended."],
      ["بہت لچکدار۔", "عوامی جگہ غیر قانونی۔", "نجی ڈرائیو وے بہتر۔"]),
    P("sk_belt_bondage", "car", "intermediate", "hands_only",
      "Belt Bondage", "بیلٹ بندھن",
      "DIY seatbelt handcuffs in the car.", "سیٹ بیلٹ سے ہاتھ باندھنا۔",
      "Loop seatbelt in figure-eight around wrists for light restraint during car play.",
      "سیٹ بیلٹ سے کلائیوں پر آٹھ کی شکل میں ہلکا بندھن۔",
      ["Cuffed partner hands above head.", "Loop belt in figure-eight.", "Keep loose for quick release.", "Enjoy oral, hand, or penetrative sex.", "Return to front seat if needed."],
      ["ہاتھ اوپر رکھیں۔", "بیلٹ آٹھ کی شکل میں لپیٹیں۔", "ڈھیلا رکھیں۔", "زبانی، ہاتھ یا داخلہ۔", "ضرورت ہو تو اگلی سیٹ جائیں۔"],
      ["No bondage gear needed.", "Customizable once restrained.", "Loose belts allow quick exit."],
      ["سامان کی ضرورت نہیں۔", "باندھنے کے بعد لچک۔", "ڈھیلا بندھن فوری نکاس۔"]),
    P("sk_car_seated_rear", "car", "beginner", "seated_face",
      "Seated Rear Entry", "گاڑی میں بیٹھے پیچھے سے",
      "Stealthy driver-seat lap position.", "ڈرائیور سیٹ پر گود میں پیٹھ کر کے۔",
      "Shift driver seat back; receiver sits in lap facing forward for discreet car intimacy.",
      "ڈرائیور سیٹ پیچھے؛ وصول کنندہ آگے منہ کر کے گود میں۔",
      ["Turn car off, set emergency brake.", "Push driver seat fully back.", "Receiver sits in lap facing forward.", "Skirt or dress allows discretion.", "Lower risk than backseat climbing."],
      ["گاڑی بند، ہینڈ بریک۔", "سیٹ پیچھے کریں۔", "آگے منہ کر کے گود میں بیٹھیں۔", "اسکرٹ سے چھپاؤ۔", "پچھلی سیٹ سے آسان۔"],
      ["Less commitment than backseat.", "Can stay partially dressed.", "Ideal for quick private moments."],
      ["پچھلی سیٹ سے آسان۔", "جزوی لباس ممکن۔", "فوری نجی لمحات کے لیے۔"]),
    P("sk_yab_yum", "car", "beginner", "seated_face",
      "Yab-Yum", "یب یم",
      "Tantric seated face-to-face embrace.", "ٹینٹرک بیٹھے آمنے سامنے آغوش۔",
      "Insertive partner sits cross-legged; receiver sits in lap legs around back. Rock side-to-side slowly.",
      "نیچے والا پیر باندھ کر بیٹھے؛ اوپر والا گود میں ٹانگیں کمر کے گرد۔",
      ["Partner sits cross-legged on floor or seat.", "Receiver sits in lap facing them.", "Wrap legs around partner.", "Rock side-to-side slowly.", "Maintain eye contact and shared breath."],
      ["پیر باندھ کر بیٹھیں۔", "آمنے سامنے گود میں بیٹھیں۔", "ٹانگیں لپیٹیں۔", "آہستہ ساتھ جھولیں۔", "آنکھیں اور سانس ملائیں۔"],
      ["Popular Tantric position.", "Promotes deep romance.", "Try eye-gazing for intimacy."],
      ["مشہور ٹینٹرک پوزیشن۔", "گہری رومانویت۔", "آنکھوں میں دیکھیں۔"]),
    P("sk_trunk", "car", "intermediate", "doggy",
      "Trunk Space", "ٹرنک اسپیس",
      "Car-friendly doggy on lowered seats.", "سیٹیں جھکا کر گاڑی میں ڈوگی۔",
      "Lower front seat; receiver face-down on headrest while partner enters from behind. SUV back seats offer more room.",
      "اگلی سیٹ جھکائیں؛ وصول کنندہ سرے پر؛ پیچھے سے داخلہ۔",
      ["Lower front seat for space.", "Receiver face-down on headrest.", "Partner enters from behind.", "SUV: fold back seats for room.", "Skin contact feels intimate."],
      ["سیٹ جھکائیں۔", "منہ نیچے سرے پر۔", "پیچھے سے داخل ہوں۔", "SUV میں زیادہ جگہ۔", "جلد کا رابطہ قریبی۔"],
      ["More connected than standard doggy.", "Leverage for deep penetration.", "Hand play opportunities."],
      ["معمولی ڈوگی سے زیادہ رابطہ۔", "گہری داخلہ کے لیے۔", "ہاتھ سے لطف۔"]),
    # Solo (4)
    P("sk_over_hump", "solo", "beginner", "solo_lying",
      "Over the Hump", "اوور دی ہمپ",
      "Face-down solo grinding on pillow.", "پیٹ کے بل تکیے پر اکیلے رگڑنا۔",
      "Lie on stomach with pillow under pelvis and grind until pleasurable sensation peaks.",
      "پیٹ کے بل تکیہ کولہے کے نیچے رکھ کر رگڑیں۔",
      ["Lie on stomach.", "Place pillow under pelvis.", "Shimmy hips to find sensation.", "Grind until peak.", "Add hand or wand between legs."],
      ["پیٹ کے بل لیٹیں۔", "تکیہ کولہے کے نیچے۔", "کولہے ہلائیں۔", "لطف تک رگڑیں۔", "ہاتھ یا وائبریٹر شامل کریں۔"],
      ["Doggy-style variation for solo.", "Works on vacation without toys.", "Wand vibrators excel here."],
      ["اکیلے کے لیے ڈوگی جیسا۔", "سفر میں بغیر کھلونے۔", "وائبریٹر بہترین۔"],
      solo=True),
    P("sk_superstar", "solo", "beginner", "solo_kneel",
      "Superstar", "سپر اسٹار",
      "Kneeling upright solo masturbation.", "گھٹنوں پر سیدھے اکیلے لطف۔",
      "Kneel on soft surface, torso upright, knees open. Explore new angles for self-pleasure.",
      "نرم سطح پر گھٹنوں کے بل سیدھے، گھٹنے کھولیں۔",
      ["Kneel on soft surface.", "Keep torso upright.", "Open knees comfortably.", "Use wall for support if needed.", "Try mirror for body awareness."],
      ["نرم جگہ پر گھٹنوں پر۔", "سینہ سیدھا۔", "گھٹنے کھولیں۔", "دیوار سے سہارا۔", "آئینے میں دیکھیں۔"],
      ["Spices up solo routine.", "New orgasm angles possible.", "Mirror adds voyeur feeling."],
      ["اکیلے کے معمول میں تنوع۔", "نئے زاویے۔", "آئینہ اضافی لطف۔"],
      solo=True),
    P("sk_solo_snake", "solo", "beginner", "solo_lying",
      "The Solo Snake", "سولو سنیک",
      "Face-down grinding on palm vibrator.", "وائبریٹر پر پیٹ کے بل رگڑنا۔",
      "Lie on belly with vibrator under pelvis; body weight intensifies vibration.",
      "پیٹ کے بل وائبریٹر کولہے کے نیچے؛ وزن سے شدت بڑھے۔",
      ["Power on palm vibrator.", "Lie face-down on belly.", "Position toy under pelvis.", "Grind to preferred pressure.", "Adjust angle with hips."],
      ["وائبریٹر چالو کریں۔", "پیٹ کے بل لیٹیں۔", "کولہے کے نیچے رکھیں۔", "دباؤ سے رگڑیں۔", "کولہے سے زاویہ بدلیں۔"],
      ["Body weight intensifies vibe.", "Simple setup.", "Great for targeted external play."],
      ["جسم کا وزن وائبریشن بڑھاتا ہے۔", "آسان ترتیب۔", "خارجی لطف کے لیے۔"],
      solo=True),
    P("sk_opening_up", "solo", "beginner", "solo_kneel",
      "Opening Up", "اوپننگ اپ",
      "Chair-based solo with legs braced.", "کرسی پر ٹانگیں پھیلا کر اکیلے لطف۔",
      "Sit on chair, ankles wound around legs, open thighs and touch as desired.",
      "کرسی پر بیٹھیں، ٹانگیں کرسی کی لکڑیوں سے لپٹائیں۔",
      ["Sit on sturdy chair.", "Wrap ankles around chair legs.", "Open thighs wide.", "Touch and tease at your pace.", "Use leverage from braced legs."],
      ["مضبوط کرسی پر بیٹھیں۔", "ٹانگیں کرسی سے لپٹائیں۔", "رانیں کھولیں۔", "اپنی رفتار سے چھوئیں۔", "ٹانگوں کا سہارا لیں۔"],
      ["Leverage and support from chair.", "Keeps solo time interesting.", "Spine-tingling new sensations."],
      ["کرسی سے سہارا۔", "اکیلے کے وقت میں تنوع۔", "نئے احساسات۔"],
      solo=True),
    # Flat (4)
    P("sk_layer_cake", "flat", "beginner", "prone_stack",
      "Layer Cake", "لیئر کیک",
      "External grinding missionary stack.", "اوپر نیچے رگڑ، بغیر داخلہ۔",
      "One partner on back, other lies flat on top facing them. Press genitals together with rhythm and lube.",
      "ایک پیٹ کے بل، دوسرا اوپر آمنے سامنے۔ عضو ٹھانیاں ساتھ رگڑیں۔",
      ["Bottom partner lies on back.", "Top partner lies flat facing them.", "Press genitals together.", "Rock at pleasurable rhythm.", "Use lube for comfort."],
      ["نیچے والا پیٹ کے بل۔", "اوپر والا آمنے سامنے لیٹے۔", "عضو ٹھانیاں ملائیں۔", "تال سے رگڑیں۔", "لوبریکنٹ استعمال کریں۔"],
      ["Maximum clitoral stimulation.", "No penetration needed.", "Good during menstruation."],
      ["زیادہ کلائٹورل محرک۔", "داخلہ نہیں۔", "حیض میں موزوں۔"]),
    P("sk_reverse_slither", "flat", "intermediate", "prone_stack",
      "The Reverse Slither", "ریورس سلتھر",
      "Full skin contact rear entry while lying flat.", "سیدھے لیٹ کر مکمل جلد رابطے میں پیچھے سے۔",
      "Receiver lies on top prone; penetrating partner enters from behind for deep penetration plus intimacy.",
      "وصول کنندہ اوپر پیٹ کے بل؛ دوسرا پیچھے سے۔",
      ["Receiver lies on top facing away.", "Partner enters from behind.", "Maintain full body contact.", "Stimulate breasts and clitoris.", "Whisper near each other's heads."],
      ["وصول کنندہ اوپر پیٹ کے بل۔", "پیچھے سے داخل ہوں۔", "پورے جسم کا رابطہ۔", "سینے اور کلائٹورس۔", "کان کے پاس آہستہ بات۔"],
      ["Deep penetration plus intimacy.", "Breast and clit access.", "Great for dirty talk."],
      ["گہری داخلہ اور قربت۔", "سینے اور کلائٹورس تک رسائی۔", "آہستہ گندی بات۔"]),
    P("sk_stacked_snakes", "flat", "beginner", "prone_stack",
      "Stacked Snakes", "سٹیکڈ سنیکس",
      "Both prone with rear entry on top.", "دونوں پیٹ کے بل، اوپر سے پیچھے۔",
      "Penetrating partner on top enters receiver from behind while both lie totally prone.",
      "دونوں پیٹ کے بل؛ اوپر والا پیچھے سے داخل ہو۔",
      ["Both lie flat prone.", "Penetrating partner on top.", "Enter from behind.", "Receiver slips hand underneath.", "Low-effort combined grinding."],
      ["دونوں پیٹ کے بل۔", "اوپر والا دوسرے پر۔", "پیچھے سے داخلہ۔", "نیچے ہاتھ نیچے رکھے۔", "کم محنت والی رگڑ۔"],
      ["Combines penetration and grinding.", "Receiver can self-touch.", "Ultimate low-key pleasure."],
      ["داخلہ اور رگڑ ساتھ۔", "خود چھونے کی گنجائش۔", "آرام دہ لطف۔"]),
    P("sk_anal_spoon", "flat", "beginner", "spooning",
      "Anal Spoon", "اینل چمچہ",
      "Relaxed side-lying anal entry.", "سیدھے لیٹ کر آرام دہ پیچھے سے داخلہ۔",
      "Big spoon enters anally while snuggled side-by-side. Use plenty of lube and exhale to relax sphincter.",
      "چمچے والی پوزیشن میں پیچھے سے؛ کافی لوبریکنٹ۔",
      ["Lie side-by-side spooning.", "Apply generous anal lube.", "Enter slowly from behind.", "Receiver pulls knees to chest.", "Exhale to relax sphincter."],
      ["سیدھے چمچے کی طرح۔", "لوبریکنٹ لگائیں۔", "آہستہ داخل ہوں۔", "گھٹنے سینے کی طرف۔", "سانس چھوڑ کر آرام دیں۔"],
      ["Snuggliest anal option.", "Hands free for touch.", "Very relaxing."],
      ["سب سے آرام دہ پیچھے سے۔", "ہاتھ آزاد۔", "بہت پرسکون۔"]),
    # Blindfold (4)
    P("sk_splitting_bamboo", "blindfold", "intermediate", "missionary",
      "Splitting of Bamboo", "بانس کاٹنا",
      "Tantric missionary with one leg raised and blindfolds.", "ایک ٹانگ اٹھا کر مشنری، آنکھوں پر پٹی۔",
      "Receiver on back with one leg on partner's shoulder. Blindfolds heighten skin-on-skin sensation.",
      "پیٹ کے بل ایک ٹانگ کندھے پر؛ پٹی سے احساس بڑھے۔",
      ["Apply comfortable blindfolds.", "Receiver lies on back.", "One leg on partner's shoulder.", "Partner straddles other leg.", "Grind and enter at preferred pace."],
      ["آرام دہ پٹی لگائیں۔", "پیٹ کے بل لیٹیں۔", "ایک ٹانگ کندھے پر۔", "دوسری ٹانگ کے اوپر بیٹھیں۔", "اپنی رفتار سے۔"],
      ["Excellent penetration angle.", "Blindfolds intensify touch.", "Less flexibility needed than it looks."],
      ["بہترین زاویہ۔", "پٹی چھونے کو بڑھاتی ہے۔", "لچک کم لگتی ہے۔"]),
    P("sk_private_dancer", "blindfold", "beginner", "cowgirl",
      "The Private Dancer", "پرائیویٹ ڈانسر",
      "Blindfolded lap dance with receiver on top.", "پٹی بندھے ساتھی پر اوپر والا لیپ ڈانس۔",
      "Penetrating partner blindfolded; receiver slides onto lap and grinds with full control.",
      "نیچے والے کی آنکھوں پر پٹی؛ اوپر والا گود میں بیٹھ کر کنٹرول کرے۔",
      ["Blindfold bottom partner.", "Receiver slides onto lap.", "Grind and lean for sensation.", "Receiver has all power.", "Remove blindfold when ready."],
      ["نیچے والے کی پٹی باندھیں۔", "گود میں بیٹھیں۔", "رگڑیں اور جھکیں۔", "اوپر والا اختیار رکھے۔", "تیار ہوں تو پٹی کھولیں۔"],
      ["Frees awkward lap-dance feelings.", "Receiver controls everything.", "Very empowering."],
      ["لیپ ڈانس کی جھجک کم۔", "اوپر والا سب کنٹرول۔", "اختیار بڑھاتا ہے۔"]),
    P("sk_x_marks", "blindfold", "advanced", "missionary",
      "X Marks the Spot", "ایکس مارکس دی سپاٹ",
      "Spread-eagle bondage with optional penetration.", "ہاتھ پاؤں بندھے، اختیاری داخلہ۔",
      "Blindfold partner and restrain wrists/ankles to bed. Kiss, lick, touch — penetration optional.",
      "پٹی لگا کر بستر سے باندھیں۔ بوسہ، چھونا — داخلہ اختیاری۔",
      ["Discuss boundaries first.", "Blindfold willing partner.", "Restrain wrists and ankles comfortably.", "Explore with touch.", "Penetration optional."],
      ["حدود طے کریں۔", "پٹی لگائیں۔", "آرام سے باندھیں۔", "چھو کر کھوجیں۔", "داخلہ اختیاری۔"],
      ["Receiver can feel in control.", "Highly customizable scene.", "Fifty Shades energy."],
      ["وصول کنندہ اختیار محسوس کرے۔", "بہت لچکدار۔", "بندھن والا انداز۔"]),
    P("sk_rock_n_roll", "blindfold", "intermediate", "cowgirl",
      "Rock'n'Roll", "راک این رول",
      "Both blindfolded with receiver on top.", "دونوں کی آنکھوں پر پٹی، اوپر والا۔",
      "Receiver on top, heels planted for leverage. Both wear blindfolds before positioning.",
      "اوپر والا ایڑیاں بستر پر رکھے۔ پوزیشن سے پہلے دونوں کی پٹی۔",
      ["Get into position first.", "Both partners wear blindfolds.", "Receiver on top, heels down.", "Use leverage from heels.", "Let inhibitions fade."],
      ["پہلے پوزیشن لیں۔", "دونوں کی پٹی باندھیں۔", "اوپر والا ایڑیاں نیچے۔", "ایڑیوں سے سہارا۔", "جھجک چھوڑیں۔"],
      ["Dual blindfolds remove inhibition.", "Receiver controls angle.", "Trust exercise."],
      ["دونوں پٹی جھجک کم کرتی ہے۔", "اوپر والا زاویہ طے کرے۔", "اعتماد کی مشق۔"]),
    # Anal variations (6)
    P("sk_anal_cowgirl", "anal", "beginner", "cowgirl",
      "Cowgirl/Cowboy (Anal)", "کاؤگرل اینل",
      "Face-to-face anal with receiver on top.", "آمنے سامنے پیچھے سے، اوپر والا کنٹرول۔",
      "Same as cowgirl but anal entry. Receiver controls pace and depth — ideal for first-timers.",
      "کاؤگرل جیسا لیکن پیچھے سے۔ اوپر والا رفتار طے کرے۔",
      ["Apply anal lube generously.", "Receiver straddles facing partner.", "Lower slowly onto partner.", "Control depth and pace.", "Maintain eye contact."],
      ["لوبریکنٹ لگائیں۔", "آمنے سامنے اوپر بیٹھیں۔", "آہستہ نیچے بیٹھیں۔", "گہرائی کنٹرول کریں۔", "آنکھوں کا رابطہ۔"],
      ["Best anal position for beginners.", "Easy communication face-to-face.", "Receiver owns the rhythm."],
      ["ابتدائیوں کے لیے بہترین۔", "آمنے سامنے بات آسان۔", "اوپر والا تال طے کرے۔"]),
    P("sk_anal_doggy", "anal", "beginner", "doggy",
      "Doggy-Style (Anal)", "ڈوگی اینل",
      "Classic rear-entry anal with lots of lube.", "کلاسک پیچھے سے، کافی لوبریکنٹ۔",
      "Standard doggy adapted for anal. Stay relaxed and communicate depth verbally.",
      "معمولی ڈوگی پیچھے سے داخلہ کے لیے۔ آرام سے رہیں اور بات کریں۔",
      ["Generous lube on both partners.", "Receiver on hands and knees.", "Enter slowly from behind.", "Communicate depth verbally.", "Stay relaxed."],
      ["کافی لوبریکنٹ۔", "چاروں پر۔", "آہستہ پیچھے سے۔", "گہرائی بتائیں۔", "آرام رکھیں۔"],
      ["Feels good in all variations.", "Not face-to-face — talk more.", "Relaxation is key."],
      ["ہر متبادل میں اچھا۔", "منہ نہیں دکھتا — زیادہ بات کریں۔", "آرام کلید ہے۔"]),
    P("sk_anal_face", "anal", "intermediate", "seated_face",
      "Face to Face (Anal)", "آمنے سامنے اینل",
      "Straddling with anal or vaginal option.", "بیٹھ کر پیچھے یا اندام نہانی داخلہ۔",
      "One straddles the other for tons of eye contact. Can rub, penetrate vaginally, or try anal.",
      "ایک دوسرے پر بیٹھ کر آنکھوں کا رابطہ۔ رگڑ، اندام نہانی یا پیچھے سے۔",
      ["Partner sits or lies as base.", "Other straddles facing them.", "Apply lube if going anal.", "Set rhythm together.", "Kiss and touch freely."],
      ["نیچے والا بیٹھے یا لیٹے۔", "اوپر آمنے سامنے بیٹھیں۔", "پیچھے سے ہو تو لوبریکنٹ۔", "تال ساتھ طے کریں۔", "بوسہ اور چھونا۔"],
      ["Extra intimacy during act.", "Experiment with touch.", "Shared rhythm building."],
      ["عمل کے دوران قربت۔", "چھونے کے تجربے۔", "مشترکہ تال۔"]),
    P("sk_missionary_twist", "anal", "advanced", "butterfly",
      "Missionary With a Twist", "مشنری ٹوئسٹ اینل",
      "Anal missionary with knees by armpits.", "گھٹنے بغلوں تک، پیچھے سے مشنری۔",
      "Receiver's knees folded toward armpits with hips open. Requires lube and flexibility.",
      "گھٹنے بغلوں کی طرف، کولہے کھلے۔ لوبریکنٹ اور لچک چاہیے۔",
      ["Open hips wide.", "Fold knees toward armpits.", "Partner enters anally from front.", "Use pillows under hips.", "Go slowly."],
      ["کولہے کھولیں۔", "گھٹنے بغلوں کی طرف۔", "سامنے سے پیچھے داخلہ۔", "تکیہ کولہے کے نیچے۔", "آہستہ جائیں۔"],
      ["Worth the flexibility effort.", "Deep sensation.", "Keep lube nearby."],
      ["لچک کی محنت قابل ہے۔", "گہرا احساس۔", "لوبریکنٹ پاس رکھیں۔"]),
    P("sk_on_stomach", "anal", "beginner", "solo_lying",
      "On the Stomach (Anal)", "پیٹ کے بل اینل",
      "Prone anal for gentle deep penetration.", "پیٹ کے بل آہستہ گہری پیچھے سے۔",
      "Receiver relaxes on stomach with pillow under head. Partner enters gently from behind.",
      "سر کے نیچے تکیہ، پیٹ کے بل آرام۔ آہستہ پیچھے سے۔",
      ["Receiver lies on stomach.", "Pillow under head.", "Partner enters from behind.", "Keep movements gentle.", "Both stay relaxed."],
      ["پیٹ کے بل لیٹیں۔", "سر کے نیچے تکیہ۔", "پیچھے سے داخل ہوں۔", "نرم حرکت۔", "آرام رکھیں۔"],
      ["Great for anal beginners.", "Receiver fully relaxed.", "Comfortable and chill."],
      ["ابتدائیوں کے لیے۔", "وصول کنندہ آرام میں۔", "پرسکون۔"]),
    P("sk_spooning_twist", "anal", "beginner", "spooning",
      "Spooning With a Twist", "چمچہ ٹوئسٹ اینل",
      "Side-lying anal spooning.", "سیدھے چمچے میں پیچھے سے۔",
      "Classic spooning adapted for anal. Rock together to find angle and depth.",
      "چمچے والی پوزیشن پیچھے سے داخلہ کے لیے۔ ساتھ جھولیں۔",
      ["Lie back-to-front spooning.", "Apply anal lube.", "Enter slowly from behind.", "Rock hips together.", "Hands free for touch."],
      ["چمچے کی طرح لیٹیں۔", "لوبریکنٹ لگائیں۔", "آہستہ پیچھے سے۔", "کولہے ساتھ ہلائیں۔", "ہاتھ آزاد۔"],
      ["Comfort and intimacy help relax.", "Connected feeling.", "Free hands for stimulation."],
      ["آرام اور قربت مدد کرتی ہے۔", "جڑا ہوا احساس۔", "ہاتھ سے محرک۔"]),
    # Beach (10)
    P("sk_bbq_quickie", "beach", "intermediate", "doggy",
      "The BBQ Quickie", "بی بی کیو فوری",
      "Outdoor bench quickie (private only).", "باہر بینچ پر فوری (صرف نجی جگہ)۔",
      "Summer outdoor bend-over at secluded bench. Public sex is illegal — use private areas only.",
      "گرمیوں میں نجی بینچ پر جھکنا۔ عوامی جگہ غیر قانونی۔",
      ["Find truly private secluded area.", "Receiver bends over bench.", "Lift hem or adjust clothing.", "Partner enters from behind.", "Never at family gatherings."],
      ["مکمل نجی جگہ تلاش کریں۔", "بینچ پر جھکیں۔", "لباس ایڈجسٹ کریں۔", "پیچھے سے۔", "خاندانی تقریبات میں نہیں۔"],
      ["Summer heat adds thrill.", "Voyeur fantasy in private only.", "Avoid pool sex — irritation risk."],
      ["گرمی کا جوش۔", "صرف نجی میں فنتاسی۔", "پول سے بچیں۔"]),
    P("sk_lounging_lioness", "beach", "beginner", "prone_stack",
      "The Lounging Lioness", "آرام دہ شیرنی",
      "Receiver on top with legs closed on deck chair.", "ڈیک کرسی پر اوپر، ٹانگیں بند۔",
      "Penetrating partner on back; receiver lies on top legs closed for tighter sensation.",
      "نیچے والا پیٹ کے بل؛ اوپر والا ٹانگیں بند کر لیٹے۔",
      ["Partner lies on back on chair.", "Receiver lies on top.", "Keep legs together when ready.", "Increases pressure on pleasure zones.", "Less leg work than cowgirl."],
      ["نیچے والا کرسی پر پیٹ کے بل۔", "اوپر والا اوپر لیٹے۔", "ٹانگیں بند رکھیں۔", "دباؤ بڑھتا ہے۔", "کاؤگرل سے کم محنت۔"],
      ["Less leg work than cowgirl.", "Tighter sensation when legs close.", "Great on private deck chairs."],
      ["کاؤگرل سے کم محنت۔", "ٹانگیں بند کرنے سے تنگ احساس۔", "نجی ڈیک کرسی پر بہترین۔"]),
    P("sk_pouncing_panther", "beach", "beginner", "doggy",
      "Pouncing Panther", "چھلانگ مارتی پینتھر",
      "Poolside doggy on chair or towel.", "پول کے کنارے ڈوگی۔",
      "Doggy-style poolside on private chair or towel. Optional cool temperature play with ice pack.",
      "نجی کرسی یا تولیے پر ڈوگی۔ آئس پیک سے ٹھنڈک کا کھیل۔",
      ["Ensure complete privacy.", "Receiver on all fours on chair.", "Partner enters from behind.", "Optional ice pack under stomach.", "Vitamin D and pleasure."],
      ["مکمل نجی ہونے کا یقین۔", "چاروں پر کرسی پر۔", "پیچھے سے۔", "آئس پیک اختیاری۔", "دھوپ اور لطف۔"],
      ["Vitamin D plus pleasure.", "Ice pack for temperature play.", "Poolside private chair works best."],
      ["دھوپ اور لطف۔", "آئس پیک سے ٹھنڈک کا کھیل۔", "نجی پول کنارے کی کرسی بہترین۔"]),
    P("sk_teddy_bear", "beach", "intermediate", "seated_face",
      "The Teddy Bear", "ٹیڈی بیئر",
      "Kneeling proposal pose with straddle.", "گھٹنے پر گھٹنے، اوپر بیٹھنا۔",
      "One kneels proposal-style; receiver straddles one leg sliding down. Use mattress or yoga mat.",
      "ایک گھٹنے پر گھٹنے؛ دوسرا ٹانگ پر بیٹھ کر نیچے۔ بستر یا میٹ پر۔",
      ["Penetrating partner kneels on one knee.", "Receiver straddles that leg.", "Feet reach floor for leverage.", "Face-to-face kissing.", "Avoid carpet and hardwood."],
      ["ایک گھٹنے پر۔", "ٹانگ پر بیٹھیں۔", "پاؤں فرش پر سہارا۔", "آمنے سامنے بوسہ۔", "کارپٹ اور لکڑی سے بچیں۔"],
      ["Great leverage to bounce.", "Very intimate eye contact.", "Reserved for soft surfaces."],
      ["اچھالنے کا سہارا۔", "قریبی آنکھیں۔", "نرم سطح پر۔"]),
    P("sk_beach_doggy", "beach", "beginner", "doggy",
      "Beach-Safe Doggy-Style", "محفوظ ساحلی ڈوگی",
      "Doggy on towel avoiding sand.", "تولیے پر ڈوگی، ریت سے بچاؤ۔",
      "Lay towel, adjust swimsuits, enjoy doggy without sand in sensitive areas.",
      "تولیہ بچھائیں، سوئم سوٹ ایڈجسٹ، ریت سے بچیں۔",
      ["Lay large towel flat.", "Receiver on all fours on towel.", "Adjust swimwear aside.", "Partner kneels behind.", "Minimize sand contact."],
      ["بڑا تولیہ بچھائیں۔", "تولیے پر چاروں پر۔", "سوئم سوٹ ہٹائیں۔", "پیچھے گھٹنوں پر۔", "ریت سے بچیں۔"],
      ["Tailor-made for beach.", "Bodies not pressed in heat.", "Keeps sand away."],
      ["ساحل کے لیے۔", "گرمی میں جسم الگ۔", "ریت دور۔"]),
    P("sk_in_water", "beach", "intermediate", "standing",
      "In the Water", "پانی میں",
      "Standing water intimacy below surface.", "پانی میں کھڑے، نیچے نظر نہیں آتا۔",
      "Standing in safe clean water — looks like cuddling above surface. Choose safe water without currents.",
      "صاف پانی میں کھڑے — اوپر سے گلے ملنے جیسا۔ محفوظ پانی چنیں۔",
      ["Choose clean secluded water.", "Stand chest-deep together.", "Pull swimsuits aside.", "Maintain balance.", "No parasites or strong currents."],
      ["صاف نجی پانی۔", "سینے تک کھڑے۔", "سوئم سوٹ ہٹائیں۔", "توازن رکھیں۔", "طوفان یا کیڑوں سے بچیں۔"],
      ["Refreshing on hot days.", "Hidden below surface.", "Romantic in waves."],
      ["گرمی میں تروتازہ۔", "نیچے چھپا ہوا۔", "لہروں میں رومانوی۔"]),
    P("sk_beach_ball", "beach", "beginner", "doggy",
      "On a Beach Ball", "بیچ بال پر",
      "Receiver leans over inflatable ball.", "فلائیٹ بال پر جھکنا۔",
      "Beach ball supports receiver leaning forward while partner enters from behind. Playful and silly.",
      "بال سہارا دے؛ پیچھے سے داخلہ۔ تفریحی۔",
      ["Inflate sturdy beach ball.", "Receiver leans body over ball.", "Partner enters from behind.", "Works at home too.", "Reduces sand contact at beach."],
      ["بال پھلائیں۔", "بال پر جھکیں۔", "پیچھے سے۔", "گھر پر بھی۔", "ریت کم لگے۔"],
      ["Infuses play into practice.", "Unserious and fun.", "Elevates above sand."],
      ["کھیل کا عنصر۔", "ہلکی پھلکی مزہ۔", "ریت سے اوپر۔"]),
    P("sk_beach_reverse", "beach", "beginner", "reverse_cowgirl",
      "Reverse Cowgirl (Beach)", "الٹ کاؤگرل ساحل",
      "Beach reverse cowgirl on towel.", "تولیے پر الٹ کاؤگرل۔",
      "Receiver faces away on towel while partner reclines. Protects from sand with hot view.",
      "تولیے پر پیٹھ کر کے اوپر۔ ریت سے بچاؤ۔",
      ["Partner reclines on towel.", "Receiver straddles facing away.", "Ride and grind.", "Sand stays away from receiver.", "Partner enjoys the view."],
      ["تولیے پر لیٹیں۔", "پیٹھ کر کے اوپر بیٹھیں۔", "رگڑیں۔", "ریت دور۔", "منظر لطف۔"],
      ["Sand stays off receiver.", "Hot view for partner.", "Beach-friendly reverse cowgirl."],
      ["وصول کنندہ پر ریت نہیں۔", "ساتھی کے لیے منظر۔", "ساحل کے لیے الٹ کاؤگرل۔"]),
    P("sk_beach_standing", "beach", "beginner", "standing",
      "Standing Up (Beach)", "ساحل پر کھڑے",
      "Wind-protected standing beach sex.", "ہوا سے محفوظ کھڑے ساحلی لطف۔",
      "Find secluded wind-protected spot, lean on sturdy support, pull swimsuits aside.",
      "نجی جگہ، مضبوط سہارا، سوئم سوٹ ہٹائیں۔",
      ["Find secluded area.", "Lean on sturdy support.", "Pull swimwear aside.", "Maintain eye contact.", "Enjoy sun and waves."],
      ["نجی جگہ۔", "مضبوط سہارا۔", "سوئم سوٹ ہٹائیں۔", "آنکھوں کا رابطہ۔", "دھوپ اور لہریں۔"],
      ["Eye contact in sun feels intimate.", "Classic beach 101.", "Wind protection helps."],
      ["دھوپ میں آنکھیں قریبی۔", "ساحلی کلاسک۔", "ہوا سے بچاؤ مددگار۔"]),
    P("sk_under_blanket", "beach", "beginner", "spooning",
      "Under a Blanket", "کمبل تلے",
      "Discreet spooning under beach blanket.", "ساحلی کمبل میں چمچہ۔",
      "Simple spooning wrapped in blanket after beach clears. Subtle and intimate.",
      "ساحل خالی ہونے کے بعد کمبل میں چمچہ۔ چھپا اور قریبی۔",
      ["Wait until beach is mostly empty.", "Wrap in large blanket.", "Spoon together intimately.", "Move slowly and quietly.", "Stay aware of surroundings."],
      ["ساحل خالی ہو۔", "بڑے کمبل میں لپیٹیں۔", "چمچے کی طرح۔", "آہستہ حرکت۔", "ارد گرد دیکھتے رہیں۔"],
      ["Hotter because it's hidden.", "More subtle.", "Extra closeness."],
      ["چھپا ہونے سے پرکشش۔", "زیادہ باریک۔", "اضافی قربت۔"]),
    # Orgasm-focused (5)
    P("sk_closed_business", "orgasm", "beginner", "oral_top",
      "Closed for Business", "بند کاروبار",
      "Oral with receiver's legs closed.", "ٹانگیں بند، زبانی کلائٹورل محرک۔",
      "Receiver lies on back legs closed while partner performs oral — pressure where many want it.",
      "پیٹ کے بل ٹانگیں بند؛ ساتھی زبانی محرک دے۔",
      ["Receiver lies back legs together.", "Partner performs oral over closed legs.", "Build heat with pressure.", "Play with power dynamic.", "Communicate intensity."],
      ["پیٹ کے بل ٹانگیں ملائیں۔", "زبانی محرک دیں۔", "دباؤ سے گرمی بڑھائیں۔", "اختیار کھیلیں۔", "شدت بتائیں۔"],
      ["Intense orgasm potential.", "Power play dynamic.", "Targets clitoral pressure."],
      ["شدید لطف کا امکان۔", "اختیار کا کھیل۔", "کلائٹورل دباؤ۔"]),
    P("sk_high_heels", "orgasm", "intermediate", "doggy",
      "In High Heels", "اونچی ایڑیوں میں",
      "Standing bent-forward at counter or stairs.", "کاؤنٹر یا سیڑھی پر جھک کر کھڑے۔",
      "Receiver bends at counter or sink. Heels or stairs help height differences.",
      "کاؤنٹر پر جھکیں۔ ایڑی یا سیڑھی اونچائی کے فرق میں مدد۔",
      ["Receiver bends over sturdy surface.", "Use heels for height match.", "Stairs with banister work too.", "Partner enters from behind.", "Try bathroom mirror."],
      ["مضبوط سطح پر جھکیں۔", "ایڑی سے اونچائی ملائیں۔", "سیڑھی بھی چلے۔", "پیچھے سے۔", "آئینہ آزمائیں۔"],
      ["Animalistic standing energy.", "Mirror adds performer vibe.", "Mind height differences."],
      ["کھڑے جانوری جوش۔", "آئینہ پرفارمر والا۔", "اونچائی کا فرق دیکھیں۔"]),
    P("sk_drop_box", "orgasm", "intermediate", "edge_bed",
      "The Drop Box", "ڈراپ باکس",
      "Hips dangling off bed edge.", "کولہے بستر کے کنارے باہر۔",
      "Receiver lies at bed edge hips dangling. Partner bends knees to align. Hands free for clitoral stimulation.",
      "بستر کے کنارے کولہے باہر؛ ہاتھ سے کلائٹورس۔",
      ["Receiver lies at bed edge.", "Hips hang off slightly.", "Partner stands between legs.", "Wrap legs or rest on shoulders.", "Both hands free for clitoral play."],
      ["بستر کے کنارے لیٹیں۔", "کولہے باہر۔", "درمیان کھڑا ساتھی۔", "ٹانگیں لپیٹیں یا کندھوں پر۔", "ہاتھ سے کلائٹورس۔"],
      ["Simultaneous clitoral and vaginal stimulation.", "Great hip angle.", "Works for all anatomies."],
      ["کلائٹورل اور اندام نہانی ساتھ۔", "بہترین کولہے زاویہ۔", "ہر جسم کے لیے۔"]),
    P("sk_g_whiz", "orgasm", "beginner", "butterfly",
      "The G-Whiz", "جی وہز",
      "Lifted missionary with hip cushion.", "تکیے پر اونچے کولہے والی مشنری۔",
      "Receiver props hips on wedge or firm cushion for maximum G-zone stimulation.",
      "مثلثی تکیہ یا گدا سے جی سپاٹ محرک۔",
      ["Place wedge under receiver's hips.", "Receiver lies back comfortably.", "Partner enters from front.", "Adjust cushion height.", "Maximize depth for G-spot."],
      ["تکیہ کولہے کے نیچے۔", "آرام سے پیٹ کے بل۔", "سامنے سے داخلہ۔", "اونچائی ایڈجسٹ۔", "جی سپاٹ کے لیے گہرائی۔"],
      ["Named for G-zone focus.", "Helps shorter phallus depth.", "Shifts bellies out of way."],
      ["جی زون کے لیے۔", "چھوٹے سائز میں مدد۔", "پیٹ ہٹ جاتا ہے۔"]),
    P("sk_tilt_whirl", "orgasm", "intermediate", "seated_face",
      "The Tilt-a-Whirl", "ٹلٹ اے وہرل",
      "Face-to-face seated lean-back grind.", "بیٹھ کر آگے جھک کر رگڑنا۔",
      "Partner sits feet on floor; receiver sits lap face-to-face. Lean back holding arms and grind.",
      "نیچے والا پاؤں فرش پر؛ اوپر گود میں آمنے سامنے۔ پیچھے جھک کر رگڑیں۔",
      ["Partner sits feet on floor.", "Receiver sits lap facing.", "Hold each other's arms.", "Lean back together.", "Find rhythm and balance."],
      ["پاؤں فرش پر بیٹھیں۔", "گود میں آمنے سامنے۔", "بازو پکڑیں۔", "ساتھ پیچھے جھکیں۔", "تال اور توازن۔"],
      ["Trust exercise plus pleasure.", "Unique G-spot angle.", "Use wall for support if needed."],
      ["اعتماد اور لطف۔", "منفرد جی زاویہ۔", "دیوار سے سہارا۔"]),
    # Creative (9)
    P("sk_circus_freak", "creative", "advanced", "reverse_cowgirl",
      "The Circus Freak / Cowpoke", "سرکس فریک / کاوپوک",
      "Deep squat reverse ride with legs pulled in.", "گہری اسکواٹ الٹ سواری۔",
      "Penetrating partner lies back legs to chest. Receiver squats facing away lowering fully.",
      "نیچے والا ٹانگیں سینے کی طرف؛ اوپر الٹ بیٹھ کر نیچے۔",
      ["Partner lies back legs pulled to chest.", "Receiver faces away squatting.", "Lower until thighs touch.", "Bounce with leg muscles.", "Switch to reverse cowgirl if needed."],
      ["پیٹ کے بل ٹانگیں کھینچیں۔", "الٹ اسکواٹ میں بیٹھیں۔", "مکمل نیچے بیٹھیں۔", "رانوں سے اچھلیں۔", "ضرورت ہو تو الٹ کاؤگرل۔"],
      ["Rider controls internal hot spots.", "Needs flexibility or length.", "Easy fallback positions."],
      ["اندرونی محرک کنٹرول۔", "لچک یا لمبائی چاہیے۔", "آسان متبادل۔"]),
    P("sk_froggie", "creative", "intermediate", "doggy",
      "Froggie-Style", "فروگی سٹائل",
      "Receiver crouches like frog on hands and feet.", "مینڈک کی طرح ہاتھ اور پاؤں پر۔",
      "Receiver crouches in front balancing on feet and hands while partner kneels behind.",
      "سامنے والا مینڈک کی طرح جھکے؛ پیچھے والا گھٹنوں پر۔",
      ["Partner kneels behind.", "Receiver crouches frog-like.", "Balance on feet and hands.", "Lean forward or back for depth.", "Switch positions easily."],
      ["پیچھے گھٹنوں پر۔", "مینڈک جیسا جھکیں۔", "پاؤں اور ہاتھ پر توازن۔", "آگے پیچھے سے گہرائی۔", "آسانی سے بدلیں۔"],
      ["Strange at first then loved.", "Easy depth adjustment.", "Keeps fun going."],
      ["پہلے عجیب پھر پسند۔", "گہرائی آسان۔", "تفریح جاری۔"]),
    P("sk_lap_dance_creative", "creative", "beginner", "cowgirl",
      "Lap Dance (Creative)", "لیپ ڈانس تخلیقی",
      "Music-driven lap dance to penetration.", "موسیقی پر لیپ ڈانس سے داخلہ۔",
      "Partner sits while you move to music, tease, then slide down facing away for extra spice.",
      "ساتھی بیٹھے؛ موسیقی پر حرکت، چھوا، پھر پیٹھ کر کے نیچے۔",
      ["Turn on music.", "Partner sits on chair or bed.", "Dance and tease.", "Slide down for penetration.", "Facing away adds spice."],
      ["موسیقی چلائیں۔", "ساتھی بیٹھے۔", "ناچیں اور چھوئیں۔", "نیچے بیٹھ کر داخلہ۔", "پیٹھ کر کے تیز۔"],
      ["Fulfills lap dance fantasies.", "Receiver controls heat.", "Fast mutual turn-on."],
      ["لیپ ڈانس خواب۔", "اوپر والا گرمی طے کرے۔", "جلدی جوش۔"]),
    P("sk_yogi", "creative", "advanced", "doggy",
      "The Yogi", "یوگی",
      "Upside-down wheelbarrow yoga pose.", "الٹا وہیل بیرو یوگا۔",
      "Receiver mimics wheelbarrow pushing off floor arching back. Needs firm floor and strength.",
      "وہیل بیرو جیسا فرش سے دھکا؛ مضبوط فرش اور طاقت۔",
      ["Use firm floor surface.", "Receiver pushes off with arms and feet.", "Arch back for angle.", "Partner enters from behind.", "Practice balance first."],
      ["مضبوط فرش۔", "بازو اور پاؤں سے اٹھیں۔", "کمر آرچ کریں۔", "پیچھے سے۔", "پہلے توازن مشق۔"],
      ["Worth strength effort.", "Hot penetration angle.", "Hip movement adds stimulation."],
      ["طاقت قابل ہے۔", "پرکشش زاویہ۔", "کولہے کی حرکت۔"]),
    P("sk_inverted_missionary", "creative", "intermediate", "reverse_cowgirl",
      "Inverted Missionary", "الٹ مشنری",
      "Reverse cowgirl on top with drag control.", "اوپر الٹ کاؤگرل، گھسیٹنے کا کنٹرول۔",
      "Receiver on top facing away controlling penetration with forward and back lean.",
      "اوپر پیٹھ کر کے؛ آگے پیچھے جھک کر گہرائی۔",
      ["Partner lies on back.", "Receiver mounts facing away.", "Lean forward and back.", "Control penetration drag.", "Enjoy the view for partner."],
      ["نیچے پیٹ کے بل۔", "الٹ اوپر بیٹھیں۔", "آگے پیچھے جھکیں۔", "گہرائی کنٹرول۔", "منظر لطف۔"],
      ["Receiver fully in control.", "Delicious drag sensation.", "Reverse cowgirl upgrade."],
      ["اوپر والا مکمل کنٹرول۔", "گھسیٹنے کا لطف۔", "بہتر الٹ کاؤگرل۔"]),
    P("sk_cowpoke", "creative", "advanced", "reverse_cowgirl",
      "The Cowpoke", "کاؤپوک",
      "Squatting reverse ride legs-to-chest base.", "اسکواٹ الٹ سواری۔",
      "Same as Circus Freak — partner legs to chest, receiver squats and bounces controlling depth.",
      "نیچے والی ٹانگیں سینے کی طرف؛ اوپر اسکواٹ میں اچھال۔",
      ["Base partner pulls legs to chest.", "Receiver squats facing away.", "Lower fully onto partner.", "Bounce at preferred rhythm.", "Switch if flexibility lacking."],
      ["نیچے ٹانگیں کھینچیں۔", "الٹ اسکواٹ۔", "مکمل بیٹھیں۔", "اپنی تال سے اچھلیں۔", "لچک کم ہو تو بدلیں۔"],
      ["Stimulates G, A, and cervix.", "Best with flexibility.", "Easy switch to classic reverse."],
      ["جی، اے، گریوائیکس۔", "لچک کے ساتھ بہتر۔", "آسان متبادل۔"]),
    P("sk_field_goal", "creative", "intermediate", "edge_bed",
      "Field Goal", "فیلڈ گول",
      "Receiver hips on partner's lap field-goal style.", "کولہے ساتھی کی گود پر فیلڈ گول۔",
      "Receiver lies back hips on partner's lap in field goal position for unique penetration angle.",
      "پیٹ کے بل کولہے ساتھی کی گود پر، منفرد زاویہ۔",
      ["Partner sits with lap accessible.", "Receiver lies back hips on lap.", "Extend legs in field goal shape.", "Partner supports and thrusts.", "Optional touchdown arms."],
      ["ساتھی بیٹھے۔", "کولہے گود پر لیٹیں۔", "ٹانگیں فیلڈ گول۔", "ساتھی سہارا دے۔", "ہاتھ اختیاری۔"],
      ["Funny look, great angle.", "Needs core strength.", "Partner supports during thrusts."],
      ["عجیب منظر، اچھا زاویہ۔", "کور طاقت۔", "ساتھی سہارا۔"]),
    P("sk_fumble", "creative", "beginner", "side_face",
      "Fumble", "فمبل",
      "All-hands creative touching position.", "ہاتھوں سے تخلیقی چھونا۔",
      "Pull partner close with hands everywhere — between legs, belly, chest. Creativity and dirty talk welcome.",
      "قریب کھینچیں، ہاتھ ہر جگہ — رانوں، پیٹ، سینے۔ تخلیق اور بات۔",
      ["Lie facing each other.", "Touch wherever feels good.", "Between legs, down belly, chest.", "Pull partner close.", "Add dirty talk freely."],
      ["آمنے سامنے لیٹیں۔", "جہاں اچھا لگے چھوئیں۔", "رانوں، پیٹ، سینے۔", "قریب کھینچیں۔", "آہستہ گندی بات۔"],
      ["All about creativity.", "No single correct form.", "Communication is pleasure."],
      ["تخلیق پر مبنی۔", "ایک صحیح شکل نہیں۔", "بات چیت لطف ہے۔"]),
    P("sk_wide_receiver", "creative", "intermediate", "butterfly",
      "Wide Receiver", "وائڈ ریسیور",
      "Legs elevated spread wide for oral or penetration.", "ٹانگیں اونچی چوڑی — زبانی یا داخلہ۔",
      "Receiver on back legs elevated and spread. Partner kneels with room for oral, penetration, or manual — or all three.",
      "پیٹ کے بل ٹانگیں اونچی کھولیں۔ ساتھی گھٹنوں پر — زبانی، داخلہ، ہاتھ۔",
      ["Receiver lies back.", "Elevate and spread legs wide.", "Partner kneels before them.", "Oral, penetrative, or manual.", "Receiver directs with hands on head."],
      ["پیٹ کے بل۔", "ٹانگیں اونچی چوڑی۔", "ساتھی سامنے گھٹنوں پر۔", "زبانی، داخلہ یا ہاتھ۔", "سر رہنمائی کریں۔"],
      ["Sexy power dynamic.", "Receiver calls the plays.", "Room for combination play."],
      ["پرکشش اختیار۔", "وصول کنندہ حکم دے۔", "ملا جلا لطف۔"]),
])


def generate_kotlin() -> str:
    cat_consts = []
    cat_labels = []
    for cid, (en, ur) in CATEGORIES.items():
        const = f"CAT_{cid.upper()}" if cid != "non_penetrative" else "CAT_NON_PENETRATIVE"
        if cid == "solo":
            const = "CAT_SOLO"
        elif cid == "blindfold":
            const = "CAT_BLINDFOLD"
        elif cid == "anal":
            const = "CAT_ANAL"
        elif cid == "orgasm":
            const = "CAT_ORGASM"
        cat_consts.append(f'    const val {const} = "{cid}"')
        cat_labels.append(f'        {const} to ("{esc(en)}" to "{esc(ur)}"),')

    posture_blocks = []
    for p in POSITIONS:
        pic = f"pic_{p['id']}"
        diff = DIFFICULTY[p["diff"]]
        cat_const = {
            "classic": "CAT_CLASSIC",
            "non_penetrative": "CAT_NON_PENETRATIVE",
            "elevated": "CAT_ELEVATED",
            "shower": "CAT_SHOWER",
            "bondage": "CAT_BONDAGE",
            "car": "CAT_CAR",
            "solo": "CAT_SOLO",
            "flat": "CAT_FLAT",
            "blindfold": "CAT_BLINDFOLD",
            "anal": "CAT_ANAL",
            "beach": "CAT_BEACH",
            "orgasm": "CAT_ORGASM",
            "creative": "CAT_CREATIVE",
        }[p["cat"]]
        en_cat, ur_cat = CATEGORIES[p["cat"]]

        roles_en = ""
        roles_ur = ""
        if not p.get("solo"):
            man_guidance_en = [
                f"Position: {p['man_en']}",
                p["tips_en"][0] if p["tips_en"] else "Communicate openly",
                p["steps_en"][0] if p["steps_en"] else "Move slowly",
            ]
            woman_guidance_en = [
                f"Position: {p['woman_en']}",
                p["tips_en"][1] if len(p["tips_en"]) > 1 else "Guide with hips and words",
                p["steps_en"][1] if len(p["steps_en"]) > 1 else "Adjust for comfort",
            ]
            man_guidance_ur = [
                f"پوزیشن: {p['man_ur']}",
                p["tips_ur"][0] if p["tips_ur"] else "کھل کر بات کریں",
                p["steps_ur"][0] if p["steps_ur"] else "آہستہ حرکت کریں",
            ]
            woman_guidance_ur = [
                f"پوزیشن: {p['woman_ur']}",
                p["tips_ur"][1] if len(p["tips_ur"]) > 1 else "کولہے اور الفاظ سے رہنمائی",
                p["steps_ur"][1] if len(p["steps_ur"]) > 1 else "آرام کے لیے ایڈجسٹ کریں",
            ]
            roles_en = f"""
                forMan = PartnerRole(
                    position = "{esc(p['man_en'])}",
                    guidance = {kotlin_string_list(man_guidance_en, "                        ")}
                ),
                forWoman = PartnerRole(
                    position = "{esc(p['woman_en'])}",
                    guidance = {kotlin_string_list(woman_guidance_en, "                        ")}
                ),"""
            roles_ur = f"""
                forMan = PartnerRole(
                    position = "{esc(p['man_ur'])}",
                    guidance = {kotlin_string_list(man_guidance_ur, "                        ")}
                ),
                forWoman = PartnerRole(
                    position = "{esc(p['woman_ur'])}",
                    guidance = {kotlin_string_list(woman_guidance_ur, "                        ")}
                ),"""

        posture_blocks.append(f"""        Posture(
            id = "{p['id']}",
            difficulty = Difficulty.{diff},
            illustrationRes = R.drawable.{pic},
            categoryId = {cat_const},
            sourceUrl = "{SOURCE_BASE}",
            isImagination = false,
            english = LocalizedContent(
                name = "{esc(p['en'])}",
                category = "{esc(en_cat)}",
                summary = "{esc(p['sum_en'])}",
                description = "{esc(p['desc_en'])}",
                steps = {kotlin_string_list(p['steps_en'])},
                tips = {kotlin_string_list(p['tips_en'])},{roles_en}
            ),
            urdu = LocalizedContent(
                name = "{esc(p['ur'])}",
                category = "{esc(ur_cat)}",
                summary = "{esc(p['sum_ur'])}",
                description = "{esc(p['desc_ur'])}",
                steps = {kotlin_string_list(p['steps_ur'])},
                tips = {kotlin_string_list(p['tips_ur'])},{roles_ur}
            )
        )""")

    all_cats = [
        "CAT_ALL", "CAT_CLASSIC", "CAT_NON_PENETRATIVE", "CAT_ELEVATED", "CAT_SHOWER",
        "CAT_BONDAGE", "CAT_CAR", "CAT_SOLO", "CAT_FLAT", "CAT_BLINDFOLD",
        "CAT_ANAL", "CAT_BEACH", "CAT_ORGASM", "CAT_CREATIVE", "CAT_IMAGINATION",
    ]

    return f"""package com.couplesguide.postures.data

import com.couplesguide.postures.R

/** Auto-generated from SheKnows 69-position slideshow. Do not edit by hand. */
object SheKnowsPostureRepository {{

    const val CAT_ALL = "all"
{chr(10).join(cat_consts)}
    const val CAT_IMAGINATION = "imagination"
    const val SOURCE_URL = "{SOURCE_BASE}"

    private val categoryLabels = mapOf(
        CAT_ALL to ("All" to "سب"),
{chr(10).join(cat_labels)}
        CAT_IMAGINATION to ("Imagination" to "تخیل")
    )

    fun getCategoryIds(): List<String> = listOf(
        {", ".join(all_cats)}
    )

    fun getCategoryLabel(categoryId: String, language: String): String {{
        val labels = categoryLabels[categoryId] ?: return categoryId
        return if (language == "ur") labels.second else labels.first
    }}

    fun getSheKnowsPostures(): List<Posture> = postures

    private val postures: List<Posture> = listOf(
{",".join(posture_blocks)}
    )
}}
"""


def main():
    os.makedirs(OUT_IMG, exist_ok=True)
    os.makedirs(os.path.dirname(OUT_KT), exist_ok=True)

    # Download real SheKnows article images (replaces generated figure diagrams)
    print("Downloading SheKnows article images...")
    import subprocess
    result = subprocess.run(
        [sys.executable, os.path.join(SCRIPT_DIR, "download_sheknows_images.py")],
        check=False,
    )
    if result.returncode != 0:
        print("Warning: some SheKnows images failed; falling back to generated diagrams for missing ones.")
        for p in POSITIONS:
            pic_path = os.path.join(OUT_IMG, f"pic_{p['id']}.png")
            if not os.path.exists(pic_path):
                gen_image(f"pic_{p['id']}", p["en"], p["tpl"])

    # Edu cards, chapters, imagination (not in SheKnows article)
    print("Generating edu / imagination assets...")
    gen.gen_missionary()
    gen.gen_cowgirl()
    gen.gen_spooning()
    gen.gen_side_by_side()
    gen.gen_doggy()
    gen.gen_lotus()
    gen.gen_standing()
    gen.gen_edge_bed()
    gen.gen_reverse_cowgirl()
    gen.gen_butterfly()
    gen.gen_scissors()
    gen.gen_lazy_dog()
    gen.gen_edu_body_map()
    gen.gen_edu_face_contact()
    gen.gen_edu_hip_pillow()
    gen.gen_edu_consent_talk()
    gen.gen_edu_side_alignment()
    gen.gen_edu_rear_safety()
    gen.gen_chapter_consent()
    gen.gen_chapter_connection()
    gen.gen_chapter_comfort()
    gen.gen_chapter_explore()
    if not os.path.exists(os.path.join(OUT_IMG, "pic_guide_cover.png")):
        gen.gen_guide_cover()
    gen.gen_imagine_breath()
    gen.gen_imagine_candlelight()
    gen.gen_imagine_embrace()
    gen.gen_imagine_ocean()
    gen.gen_imagine_starlight()
    gen.gen_imagine_morning()

    kt = generate_kotlin()
    with open(OUT_KT, "w", encoding="utf-8") as f:
        f.write(kt)
    print(f"Wrote {OUT_KT}")
    print(f"Total SheKnows positions: {len(POSITIONS)}")


if __name__ == "__main__":
    main()
