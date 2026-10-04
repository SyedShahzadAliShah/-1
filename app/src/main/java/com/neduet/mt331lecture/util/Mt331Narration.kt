package com.neduet.mt331lecture.util

import com.neduet.mt331lecture.data.mt331.LectureBeat
import com.neduet.mt331lecture.data.mt331.LectureChapter
import com.neduet.mt331lecture.data.mt331.Mt331LectureRepository

object Mt331Narration {

    fun buildOverviewNarration(language: String): String {
        val sb = StringBuilder()
        val intro = if (language == LocaleHelper.LANG_UR) {
            "ایم ٹی تین تین ایک احتمال و شماریات۔ این ای ڈی یونیورسٹی لیکچر نوٹس۔ "
        } else {
            "MT-331 Probability and Statistics. NED University lecture notes. "
        }
        sb.append(intro)
        for (chapter in Mt331LectureRepository.getChapters()) {
            val title = chapter.title(language)
            val tag = chapter.tagline(language)
            sb.append("Chapter ${chapter.chapterNumber}. $title. $tag. ")
        }
        return sb.toString()
    }

    fun buildChapterNarration(chapter: LectureChapter, language: String): String {
        val sb = StringBuilder("${chapter.title(language)}. ${chapter.tagline(language)}. ")
        for (beat in chapter.beats) {
            sb.append(buildBeatNarration(beat, language)).append(" ")
        }
        return sb.toString().trim()
    }

    fun buildBeatNarration(beat: LectureBeat, language: String): String {
        val title = if (language == LocaleHelper.LANG_UR) beat.titleUr else beat.titleEn
        val body = if (language == LocaleHelper.LANG_UR) beat.narrationUr else beat.narrationEn
        val formula = if (language == LocaleHelper.LANG_UR) beat.formulaUr else beat.formulaEn
        return buildString {
            append(title)
            append(". ")
            append(body)
            if (formula.isNotBlank()) {
                append(". Formula: ")
                append(formula)
            }
        }
    }

}
