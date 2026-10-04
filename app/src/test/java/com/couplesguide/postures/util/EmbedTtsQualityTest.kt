package com.couplesguide.postures.util

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class EmbedTtsQualityTest {

    @Test
    fun rejectsBoilerplateTitlePage() {
        assertFalse(
            EmbedTtsQuality.isMeaningfulForTts(
                "TABLE OF CONTENTS 1. Computer Systems",
                LocaleHelper.LANG_EN
            )
        )
    }

    @Test
    fun acceptsRealLectureSnippet() {
        assertTrue(
            EmbedTtsQuality.isMeaningfulForTts(
                "Human-Computer Interaction defines the fundamental design of technology to serve people.",
                LocaleHelper.LANG_EN
            )
        )
    }
}
