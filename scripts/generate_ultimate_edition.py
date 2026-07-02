#!/usr/bin/env python3
"""Generate UltimateEditionRepository.kt from structured move data."""
from __future__ import annotations

import os
import textwrap

OUT = "/workspace/app/src/main/java/com/couplesguide/postures/data/UltimateEditionRepository.kt"

SECTION = "Ultimate Edition"
SECTION_UR = "الٹیمیٹ ایڈیشن"

# (id, move_num, drawable, difficulty, en_name, ur_name, en_summary, ur_summary,
#  en_desc, ur_desc, en_steps, ur_steps, en_tips, ur_tips,
#  en_man_pos, ur_man_pos, en_man_guide, ur_man_guide,
#  en_woman_pos, ur_woman_pos, en_woman_guide, ur_woman_guide)

MOVES = [
    (
        "ultimate_cat", 1, "pic_missionary", "INTERMEDIATE",
        "Coital Alignment (CAT)", "ہم آہنگ داخلہ (CAT)",
        "Missionary variation focused on clitoral stimulation during intercourse.",
        "داخلہ کے دوران کلائیٹورل محرک پر توجہ دینے والی مشنری تبدیلی۔",
        "During missionary, body alignment often leaves the clitoris without direct stimulation. "
        "The Coital Alignment Technique (CAT) shifts your pelvis so the base of the penis and pubic "
        "bone contact her clitoris with each rocking motion. Research shows women using CAT report "
        "significantly more orgasms during intercourse.",
        "مشنری میں جسم کی سیدھ اکثر کلائیٹورس کو براہِ راست محرک نہیں دیتی۔ CAT میں کولہے کی "
        "پوزیشن بدل کر ہر ہلکی حرکت پر عضو تناسل کی جڑ اور عانہ کی ہڈی کلائیٹورس سے رابطہ کرتی ہے۔",
        [
            "Begin in missionary with her on her back and you on top.",
            "Shift your body slightly higher so your chest aligns nearer her shoulders.",
            "Instead of thrusting in and out, rock your pelvis slowly up and down.",
            "Keep the base of your penis and pubic bone pressed against her clitoris.",
            "Maintain eye contact and ask if the pressure and rhythm feel good.",
            "Try small circular hip motions for varied stimulation.",
        ],
        [
            "مشنری میں وہ پیٹ کے بل، آپ اوپر سے شروع کریں۔",
            "جسم تھوڑا اوپر کریں تاکہ سینہ اس کے کندھوں کے قریب آئے۔",
            "اندر باہر کی بجائے کولہے آہستہ اوپر نیچے ہلائیں۔",
            "عضو کی جڑ اور عانہ کی ہڈی کلائیٹورس سے دباؤ برقرار رکھیں۔",
            "آنکھوں سے رابطہ رکھیں اور پوچھیں کیا دباؤ اور تال اچھا لگ رہا ہے۔",
            "مختلف محرک کے لیے چھوٹے گول کولہے کے حرکات آزمائیں۔",
        ],
        [
            "Use a pillow under her hips for better angle.",
            "Slow rocking beats fast thrusting for clitoral contact.",
            "Combine with manual clitoral touch if she wants more.",
        ],
        [
            "بہتر زاویے کے لیے اس کے کولہوں کے نیچے تکیہ رکھیں۔",
            "کلائیٹورل رابطے کے لیے آہستہ جھولنا تیز جھٹکوں سے بہتر ہے۔",
            "اگر زیادہ چاہے تو ہاتھ سے کلائیٹورل چھونا ملا کر استعمال کریں۔",
        ],
        "On top in missionary, body shifted slightly higher than usual.",
        "مشنری میں اوپر، جسم معمول سے تھوڑا اوپر کی طرف۔",
        ["Rock pelvis rather than thrust", "Keep pubic contact steady", "Check in about pressure"],
        ["کولہے جھولیں، جھٹکے نہ ماریں", "عانہ کا رابطہ برقرار رکھیں", "دباؤ کے بارے میں پوچھیں"],
        "On her back, legs comfortably apart, receiving rocking motion.",
        "پیٹ کے بل، ٹانگیں آرام سے کھلی، جھولنے والی حرکت وصول کر رہی ہے۔",
        ["Guide his hips with your hands if needed", "Breathe deeply and relax", "Tell him what rhythm works"],
        ["ضرورت ہو تو کولہے ہاتھ سے رہنمائی کریں", "گہری سانس لیں اور آرام کریں", "بتائیں کون سی تال ٹھیک ہے"],
    ),
    (
        "ultimate_zen", 2, "pic_spooning", "BEGINNER",
        "Zen Hero", "زین ہیرو",
        "Calming rhythmic intimacy to help her unwind and feel grounded.",
        "اسے سکون اور زمین سے جڑا محسوس کرنے کے لیے پرسکون تال والی قربت۔",
        "When she carries stress from the day, slow rhythmic rocking penetration "
        "combined with steady breathing can be deeply calming. You become her anchor — "
        "present, patient, and grounding while pleasure builds naturally.",
        "جب وہ دن بھر کا تناؤ لیے ہو تو آہستہ تال والی جھولنے والی قربت اور "
        "مستقل سانسیں گہری سکون دیتی ہیں۔ آپ اس کا سہارا بنیں — موجود، صبر والا اور زمین سے جڑا۔",
        [
            "Draw a warm bath or sit together in comfortable warm water.",
            "Have her sit facing you or lie back against your chest.",
            "Enter slowly and establish a gentle rocking rhythm.",
            "Match your breathing — inhale and exhale together.",
            "Keep movements small, steady, and unhurried.",
            "Whisper reassurance: everything is okay, you are here together.",
        ],
        [
            "گرم غسل یا ساتھ آرام دہ گرم پانی میں بیٹھیں۔",
            "وہ آپ کی طرف منہ کر کے بیٹھے یا سینے سے ٹیک لگا کر لیٹے۔",
            "آہستہ داخل ہوں اور نرم جھولنے کی تال قائم کریں۔",
            "سانسیں ہم آہنگ کریں — ساتھ سانس لیں اور چھوڑیں۔",
            "حرکات چھوٹی، مستقل اور بغیر جلدی کے رکھیں۔",
            "تسلی دیں: سب ٹھیک ہے، آپ ساتھ ہیں۔",
        ],
        [
            "This is about presence, not performance.",
            "Dim lights and silence phones for full relaxation.",
            "Let her set the pace entirely.",
        ],
        [
            "یہ کارکردگی نہیں، موجودگی کے بارے میں ہے۔",
            "مکمل آرام کے لیے روشنی مدھم کریں اور فون خاموش کریں۔",
            "رفتار مکمل طور پر اس کے ہاتھ میں رہنے دیں۔",
        ],
        "Behind or beneath her, providing steady rocking motion.",
        "اس کے پیچھے یا نیچے، مستقل جھولنے والی حرکت۔",
        ["Breathe slowly and deeply", "Keep rhythm like ocean waves", "Stay present — no rushing"],
        ["آہستہ گہری سانس لیں", "سمندر کی لہروں جیسی تال رکھیں", "موجود رہیں — جلدی نہ کریں"],
        "Relaxed, supported, receiving slow rhythmic intimacy.",
        "آرام سے، سہارے میں، آہستہ تال والی قربت وصول کر رہی ہے۔",
        ["Close your eyes and melt into the rhythm", "Let stress leave with each exhale", "Communicate if anything feels off"],
        ["آنکھیں بند کریں اور تال میں ڈوب جائیں", "ہر سانس چھوڑنے پر تناؤ نکلے", "کچھ غلط لگے تو بتائیں"],
    ),
    (
        "ultimate_backyard", 3, "pic_standing", "ADVANCED",
        "Backyard Adventure", "صحن میں مہم",
        "Playful outdoor intimacy with bouncing movement for shared fun.",
        "مشترکہ لطف کے لیے اچھلنے والی حرکت کے ساتھ کھیلتی ہوئی بیرونی قربت۔",
        "Outdoor playfulness can unlock a sense of freedom and spontaneity. "
        "A trampoline or soft outdoor surface adds gentle bounce that creates unique "
        "rhythms and laughter. Privacy and safety come first — choose a secluded spot.",
        "بیرون کھیل پن آزادی اور بے ساختگی کا احساس کھول سکتا ہے۔ "
        "ٹرampoline یا نرم سطح ہلکی اچھال دیتی ہے جو منفرد تال اور ہنسی پیدا کرتی ہے۔",
        [
            "Ensure complete privacy — fence, timing, and consent.",
            "Use a trampoline or thick soft mat outdoors.",
            "Start clothed and playful before undressing.",
            "She lies or sits on the surface; you position above carefully.",
            "Use the bounce gently — let gravity assist small movements.",
            "Laugh together and pause if balance feels uncertain.",
        ],
        [
            "مکمل رازداری یقینی بنائیں — باڑ، وقت اور رضامندی۔",
            "بیرون ٹrampoline یا موٹی نرم چٹائی استعمال کریں۔",
            "برہنہ ہونے سے پہلے کپڑوں میں کھیل سے شروع کریں۔",
            "وہ سطح پر لیٹے یا بیٹھے؛ آپ احتیاط سے اوپر آئیں۔",
            "اچھال نرمی سے استعمال کریں — کشش ثقل چھوٹی حرکات میں مدد کرے۔",
            "ساتھ ہنسیں اور توازن مشکوک لگے تو رک جائیں۔",
        ],
        [
            "Have towels and water nearby.",
            "Avoid hard surfaces — safety over excitement.",
            "Check local laws regarding outdoor privacy.",
        ],
        [
            "تولیے اور پانی قریب رکھیں۔",
            "سخت سطحوں سے بچیں — جوش سے پہلے حفاظت۔",
            "بیرونی رازداری کے قوانین دیکھیں۔",
        ],
        "On top, using bounce for gentle rhythmic movement.",
        "اوپر، اچھال سے نرم تال والی حرکت۔",
        ["Hold her hips for stability", "Start very slowly", "Watch for signs of discomfort"],
        ["استحکام کے لیے کولہے تھامیں", "بہت آہستہ شروع کریں", "بے آرامی کے اشارے دیکھیں"],
        "On bouncing surface, relaxed and playful.",
        "اچھال والی سطح پر، آرام دہ اور کھیلتی ہوئی۔",
        ["Use arms for balance", "Enjoy the silliness", "Say stop anytime"],
        ["توازن کے لیے بازو استعمال کریں", "مذاق سے لطف اٹھائیں", "کسی بھی وقت رکنے کو کہیں"],
    ),
]

# Continue with remaining moves in compact form - I'll add all 30 in the generator output

def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def fmt_list(items: list[str], indent: str) -> str:
  lines = [f'{indent}"{esc(x)}",' for x in items]
  return "\n".join(lines)


def render_move(m: tuple) -> str:
    (id_, num, drawable, diff, en_name, ur_name, en_sum, ur_sum, en_desc, ur_desc,
     en_steps, ur_steps, en_tips, ur_tips,
     en_mp, ur_mp, en_mg, ur_mg, en_wp, ur_wp, en_wg, ur_wg) = m
    return f"""
        ultimateMove(
            id = "{id_}",
            moveNumber = {num},
            difficulty = Difficulty.{diff},
            illustrationRes = R.drawable.{drawable},
            enName = "{esc(en_name)}",
            urName = "{esc(ur_name)}",
            enSummary = "{esc(en_sum)}",
            urSummary = "{esc(ur_sum)}",
            enDesc = "{esc(en_desc)}",
            urDesc = "{esc(ur_desc)}",
            enSteps = listOf(
{fmt_list(en_steps, "                ")}
            ),
            urSteps = listOf(
{fmt_list(ur_steps, "                ")}
            ),
            enTips = listOf(
{fmt_list(en_tips, "                ")}
            ),
            urTips = listOf(
{fmt_list(ur_tips, "                ")}
            ),
            enManPos = "{esc(en_mp)}",
            urManPos = "{esc(ur_mp)}",
            enManGuide = listOf(
{fmt_list(en_mg, "                ")}
            ),
            urManGuide = listOf(
{fmt_list(ur_mg, "                ")}
            ),
            enWomanPos = "{esc(en_wp)}",
            urWomanPos = "{esc(ur_wp)}",
            enWomanGuide = listOf(
{fmt_list(en_wg, "                ")}
            ),
            urWomanGuide = listOf(
{fmt_list(ur_wg, "                ")}
            )
        ),"""


# Load extended moves from companion data file if exists, else append programmatically
REMAINING = [
    ("ultimate_alchemist", 4, "pic_standing", "ADVANCED", "The Alchemist", "الکیمسٹ",
     "Transform tension into passion through playful dominance and surrender.",
     "کھیلتی ہوئی غلبے اور سپردگی سے تناؤ کو جذبے میں بدلیں۔",
     "When emotions run high, channeling that energy into intentional intimacy can create "
     "powerful release. This move uses light restraint, commanding presence, and playful "
     "energy to help her let go. Consent and safewords are essential.",
     "جذبات تیز ہوں تو ان توانائی کو سوچ سمجھ کر قربت میں لانا طاقتور راحت دے سکتا ہے۔",
     ["Acknowledge her mood with humor and warmth, not criticism.",
      "Lift her arms gently above her head — a gesture of surrender.",
      "Kiss her deeply while maintaining confident, loving eye contact.",
      "Use soft ties or hold her wrists only if she has agreed beforehand.",
      "Penetrate with intention — match her energy, then guide it calmer.",
      "Afterward, cuddle and debrief — what felt good?"],
     ["مزاح اور گرمجوشی سے موڈ تسلیم کریں، تنقید نہیں۔",
      "بازو نرمی سے سر کے اوپر اٹھائیں — سپردگی کا اشارہ۔",
      "گہرا بوسہ دیں، اعتماد اور محبت بھری نظروں سے۔",
      "نرم پٹی یا کلائیاں صرف پہلے سے رضامندی ہو تو۔",
      "سوچ سمجھ کر داخل ہوں — توانائی ملائیں، پھر پرسکون رہنمائی کریں۔",
      "بعد میں گلے ملیں اور بات کریں — کیا اچھا لگا؟"],
     ["Establish a safeword before any restraint.", "Playfulness beats aggression.",
      "Never use this move to punish — only to connect."],
     ["کسی بھی بندھن سے پہلے محفوظ لفظ طے کریں۔", "جارحیت سے کھیل بھلا ہے۔",
      "سزا کے لیے نہیں — صرف جڑنے کے لیے استعمال کریں۔"],
     "Standing or kneeling, guiding with confident loving presence.",
     "کھڑے یا گھٹنوں کے بل، اعتماد اور محبت سے رہنمائی۔",
     ["Lead with warmth, not anger", "Watch her responses constantly", "Stop immediately if asked"],
     ["غصے سے نہیں، گرمجوشی سے قیادت کریں", "ردعمل مسلسل دیکھیں", "کہے تو فوراً رکیں"],
     "Arms raised or lightly restrained, surrendering to the moment.",
     "بازو اٹھے یا ہلکے بندھے، لمحے کے سپرد۔",
     ["You can stop or slow down anytime", "Let emotions release through sound and movement",
      "Trust that vulnerability is safe here"],
     ["کسی وقت رک یا سست کر سکتی ہیں", "آواز اور حرکت سے جذبات نکالیں",
      "یقین رکھیں کمزوری یہاں محفوظ ہے"],
    ),
]

print("Moves defined:", len(MOVES) + len(REMAINING))
