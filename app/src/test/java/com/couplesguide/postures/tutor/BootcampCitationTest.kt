package com.couplesguide.postures.tutor

import org.junit.Assert.assertEquals
import org.junit.Test

class BootcampCitationTest {

    @Test
    fun extractSyllabusRef_findsTopicCode() {
        assertEquals("1.1.7", BootcampCitation.extractSyllabusRef("1.1.7 Basic Logic Gates"))
        assertEquals("2.4.1", BootcampCitation.extractSyllabusRef("Sorting 2.4.1 Bubble Sort"))
        assertEquals("3.2", BootcampCitation.extractSyllabusRef("Topic 3.2 OSI layers"))
    }

    @Test
    fun extractSyllabusRef_returnsNullWhenMissing() {
        assertEquals(null, BootcampCitation.extractSyllabusRef("Logic gates without code"))
    }
}
