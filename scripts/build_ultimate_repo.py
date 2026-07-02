#!/usr/bin/env python3
"""Generate UltimateEditionRepository.kt with all 30 moves."""
from ultimate_moves_data import MOVE_META, CONTENT, CUSTOM, default_content

OUT = "/workspace/app/src/main/java/com/couplesguide/postures/data/UltimateEditionRepository.kt"


def esc(s: str) -> str:
    return s.replace("\\", "\\\\").replace('"', '\\"')


def fmt_list(items, indent="                "):
    return "\n".join(f'{indent}"{esc(x)}",' for x in items)


def get_content(move_id, en_name, num):
    c = dict(default_content(en_name, num))
    if move_id in CONTENT:
        c.update(CONTENT[move_id])
    if move_id in CUSTOM:
        c.update(CUSTOM[move_id])
    return c


def render_move(meta):
    move_id, num, drawable, diff, en_name, ur_name, en_sum, ur_sum = meta
    c = get_content(move_id, en_name, num)
    en_mp, en_mg = c["en_man"]
    ur_mp, ur_mg = c["ur_man"]
    en_wp, en_wg = c["en_woman"]
    ur_wp, ur_wg = c["ur_woman"]
    return f"""        ultimateMove(
            id = "{move_id}",
            moveNumber = {num},
            difficulty = Difficulty.{diff},
            illustrationRes = R.drawable.{drawable},
            enName = "Move {num}: {esc(en_name)}",
            urName = "حرکت {num}: {esc(ur_name)}",
            enSummary = "{esc(en_sum)}",
            urSummary = "{esc(ur_sum)}",
            enDesc = "{esc(c['en_desc'])}",
            urDesc = "{esc(c['ur_desc'])}",
            enSteps = listOf(
{fmt_list(c['en_steps'])}
            ),
            urSteps = listOf(
{fmt_list(c['ur_steps'])}
            ),
            enTips = listOf(
{fmt_list(c['en_tips'])}
            ),
            urTips = listOf(
{fmt_list(c['ur_tips'])}
            ),
            enManPos = "{esc(en_mp)}",
            urManPos = "{esc(ur_mp)}",
            enManGuide = listOf(
{fmt_list(en_mg)}
            ),
            urManGuide = listOf(
{fmt_list(ur_mg)}
            ),
            enWomanPos = "{esc(en_wp)}",
            urWomanPos = "{esc(ur_wp)}",
            enWomanGuide = listOf(
{fmt_list(en_wg)}
            ),
            urWomanGuide = listOf(
{fmt_list(ur_wg)}
            )
        ),"""


moves_kotlin = "\n".join(render_move(m) for m in MOVE_META)

HEADER = '''package com.couplesguide.postures.data

import com.couplesguide.postures.R

object UltimateEditionRepository {

    const val SECTION_ID = "ultimate_edition"

    private const val EN_CAT = "Ultimate Edition"
    private const val UR_CAT = "الٹیمیٹ ایڈیشن"

    fun getIntroChapter(): GuideChapter = introChapter

    fun getMoves(): List<Posture> = moves

    fun getMoveByNumber(number: Int): Posture? = moves.find { moveNumber(it) == number }

    fun getMoveById(id: String): Posture? = moves.find { it.id == id }

    fun moveNumber(posture: Posture): Int {
        val index = moves.indexOfFirst { it.id == posture.id }
        return if (index >= 0) index + 1 else 0
    }

    private val introChapter = GuideChapter(
        id = "ultimate_intro",
        illustrationRes = R.drawable.pic_ultimate_cover,
        english = ChapterContent(
            title = "How to Satisfy Your Wife — Ultimate Edition",
            summary = "The complete guide to confident, creative, connected lovemaking.",
            body = "This Ultimate Edition teaches you how to move and connect with your partner toward " +
                "complete mutual satisfaction. You will build confidence in your skills as a lover, " +
                "discover a new form of intimate communication, inspire sexual adventure and creativity, " +
                "and find freedom by stepping outside your comfort zone. Every technique emphasizes " +
                "consent, communication, and her pleasure as the foundation of great intimacy.",
            keyPoints = listOf(
                "30 proven techniques adapted for loving couples",
                "Man and woman roles for every move",
                "Bilingual English and Urdu guidance",
                "Educational illustrations — respectful and practical",
                "Consent and communication always come first"
            )
        ),
        urdu = ChapterContent(
            title = "بیوی کو کیسے خوش کریں — الٹیمیٹ ایڈیشن",
            summary = "اعتماد، تخلیق اور جڑے ہوئے پیار کی مکمل رہنمائی۔",
            body = "یہ الٹیمیٹ ایڈیشن سکھاتی ہے کہ ساتھی کے ساتھ کیسے جڑیں اور باہمی اطمینان حاصل کریں۔ " +
                "آپ کو محبت کرنے والے کی مہارت میں اعتماد ملے گا، قریبی بات چیت کی نئی شکل دریافت ہوگی، " +
                "جنسی مہم جوئی اور تخلیق پیدا ہوگی، اور آرام کے علاقے سے باہر نکلنے کی آزادی ملے گی۔ " +
                "ہر تکنیک رضامندی، بات چیت اور اس کے لطف کو بنیاد بناتی ہے۔",
            keyPoints = listOf(
                "محبت کرنے والے جوڑوں کے لیے 30 تکنیکیں",
                "ہر حرکت میں مرد اور عورت کے کردار",
                "انگریزی اور اردو رہنمائی",
                "تعلیمی تصویریں — باوقار اور عملی",
                "رضامندی اور بات چیت ہمیشہ پہلے"
            )
        )
    )

    private val moves = listOf(
'''

FOOTER = '''
    )

    private fun ultimateMove(
        id: String,
        moveNumber: Int,
        difficulty: Difficulty,
        illustrationRes: Int,
        enName: String,
        urName: String,
        enSummary: String,
        urSummary: String,
        enDesc: String,
        urDesc: String,
        enSteps: List<String>,
        urSteps: List<String>,
        enTips: List<String>,
        urTips: List<String>,
        enManPos: String,
        urManPos: String,
        enManGuide: List<String>,
        urManGuide: List<String>,
        enWomanPos: String,
        urWomanPos: String,
        enWomanGuide: List<String>,
        urWomanGuide: List<String>
    ): Posture = Posture(
        id = id,
        difficulty = difficulty,
        illustrationRes = illustrationRes,
        categoryId = SECTION_ID,
        english = LocalizedContent(
            name = enName,
            category = EN_CAT,
            summary = enSummary,
            description = enDesc,
            steps = enSteps,
            tips = enTips,
            forMan = PartnerRole(enManPos, enManGuide),
            forWoman = PartnerRole(enWomanPos, enWomanGuide)
        ),
        urdu = LocalizedContent(
            name = urName,
            category = UR_CAT,
            summary = urSummary,
            description = urDesc,
            steps = urSteps,
            tips = urTips,
            forMan = PartnerRole(urManPos, urManGuide),
            forWoman = PartnerRole(urWomanPos, urWomanGuide)
        )
    )
}
'''

import os
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", encoding="utf-8") as f:
    f.write(HEADER)
    f.write(moves_kotlin)
    f.write(FOOTER)
print(f"Wrote {OUT} ({len(MOVE_META)} moves)")
