package com.couplesguide.postures.util

import org.junit.Assert.assertFalse
import org.junit.Assert.assertTrue
import org.junit.Test

class NaturalLanguageTtsPreparerTest {

    @Test
    fun english_fixesInvertedHciAndExpandsEg() {
        val out = NaturalLanguageTtsPreparer.prepareEnglish(
            ")HCI( Sensory Channels e.g. OSI model"
        )
        assertTrue(out.contains("human computer interaction"))
        assertTrue(out.contains("for example"))
        assertTrue(out.contains("O S I"))
        assertFalse(out.contains(")HCI("))
        assertFalse(out.contains("e.g."))
    }

    @Test
    fun urdu_prepareUsesUrduPunctuation() {
        val out = NaturalLanguageTtsPreparer.prepare("Test, question?", LocaleHelper.LANG_UR)
        assertTrue(out.contains("؟") || out.contains("،"))
    }
}
