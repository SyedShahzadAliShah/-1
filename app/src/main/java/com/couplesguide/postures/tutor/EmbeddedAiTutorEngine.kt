package com.couplesguide.postures.tutor

import android.content.Context
import com.couplesguide.postures.data.LectureNotesRepository
import kotlin.math.min

object EmbeddedAiTutorEngine {

    private val stopWordsEn = setOf(
        "a", "an", "the", "is", "are", "was", "were", "what", "how", "why", "when",
        "tell", "me", "about", "explain", "define", "in", "of", "for", "to", "and", "or"
    )

    fun reply(
        context: Context,
        userMessage: String,
        tutorContext: TutorContext,
        useUrdu: Boolean
    ): String {
        val query = userMessage.trim()
        if (query.isEmpty()) {
            return greeting(context, useUrdu)
        }

        val lower = query.lowercase()
        if (lower == "help" || lower == "?" || lower.contains("what can you")) {
            return helpText(useUrdu)
        }
        if (lower.startsWith("quiz")) {
            return quiz(context, query, tutorContext, useUrdu)
        }
        if (lower.contains("golden") || lower.contains("★") || lower.contains("star topic")) {
            return goldenTopics(context, tutorContext, useUrdu)
        }
        if (lower.contains("citation") || lower.contains("reference format") || lower.contains("bootcamp ref")) {
            return citationGuide(context, query, tutorContext, useUrdu)
        }

        val corpus = TutorCorpus.ensureLoaded(context)
        val tokens = tokenize(query)
        if (tokens.isEmpty()) {
            return if (useUrdu) {
                "براہِ کرم CS کے بارے میں کوئی سوال لکھیں (مثلاً logic gates، OSI model، bubble sort)۔"
            } else {
                "Please ask a CS question (e.g. logic gates, OSI model, bubble sort)."
            }
        }

        val ranked = corpus
            .map { passage -> passage to scorePassage(passage, tokens, tutorContext) }
            .filter { it.second > 0 }
            .sortedByDescending { it.second }
            .take(3)

        if (ranked.isEmpty()) {
            return noMatch(useUrdu, query)
        }

        return formatAnswer(context, ranked, useUrdu, query)
    }

    private fun greeting(context: Context, useUrdu: Boolean): String {
        return if (useUrdu) {
            "السلام علیکم! میں آپ کا embedded AI tutor ہوں — جوابات آپ کے bundled CS XI/XII لیکچر نوٹس سے آتے ہیں۔ ★ موضوعات پوچھیں یا \"quiz xi\" لکھیں۔"
        } else {
            "Hi! I'm your embedded AI tutor — answers are grounded in your bundled CS XI & XII lecture notes. Ask about any topic, try \"golden topics\", or \"quiz xii\"."
        }
    }

    private fun helpText(useUrdu: Boolean): String = if (useUrdu) {
        """
        🤖 Embedded AI Tutor
        • کسی بھی موضوع پر سوال پوچھیں (logic gates، HCI، Python loops)
        • golden topics — ★ امتحانی موضوعات
        • quiz xi / quiz xii — فوری کوئز
        • اختیاری: Settings میں Gemini API key سے گہرے جواب
        • ہر جواب میں 📚 Bootcamp حوالہ جات (جماعت، باب، PDF صفحہ، نصاب §)
        """.trimIndent()
    } else {
        """
        🤖 Embedded AI Tutor
        • Ask anything from the syllabus (logic gates, HCI, Python loops…)
        • golden topics — lists ★ exam-critical items
        • quiz xi / quiz xii — quick practice question
        • Optional: add a Gemini API key in the toolbar for richer answers (still grounded in your notes)
        • Every answer includes 📚 Bootcamp references (class, chapter, PDF page, syllabus §)
        """.trimIndent()
    }

    private fun quiz(
        context: Context,
        query: String,
        tutorContext: TutorContext,
        useUrdu: Boolean
    ): String {
        val classFilter = when {
            query.contains("xii") || query.contains("12") -> "xii"
            query.contains("xi") || query.contains("11") -> "xi"
            tutorContext.classId != null -> tutorContext.classId
            else -> null
        }
        val corpus = TutorCorpus.ensureLoaded(context)
        val pool = corpus.filter { passage ->
            passage.isGolden && (classFilter == null || passage.classId == classFilter)
        }.ifEmpty {
            corpus.filter { classFilter == null || it.classId == classFilter }
        }
        val pick = pool.randomOrNull() ?: return noMatch(useUrdu, "quiz")
        val snippet = excerpt(pick, useUrdu, 220)
        val cite = BootcampCitation.format(context, pick, 1, useUrdu)
        return if (useUrdu) {
            "📝 فوری کوئز:\n$snippet\n\n$cite\n\nاپنا جواب سوچیں، پھر \"explain\" لکھ کر وضاحت حاصل کریں۔"
        } else {
            "📝 Quick quiz:\n$snippet\n\n$cite\n\nThink of your answer, then type \"explain\" for a guided breakdown."
        }
    }

    private fun citationGuide(
        context: Context,
        query: String,
        tutorContext: TutorContext,
        useUrdu: Boolean
    ): String {
        val corpus = TutorCorpus.ensureLoaded(context)
        val tokens = tokenize(query).ifEmpty { listOf("logic", "gates") }
        val ranked = corpus
            .map { passage -> passage to scorePassage(passage, tokens, tutorContext) }
            .filter { it.second > 0 }
            .sortedByDescending { it.second }
            .take(2)
        val samples = if (ranked.isEmpty()) {
            corpus.filter { it.textEn.contains("logic", ignoreCase = true) }.take(2)
        } else {
            ranked.map { it.first }
        }
        val intro = if (useUrdu) {
            "Bootcamp میں ہر جواب کے ساتھ یہ لازمی حوالہ فارمیٹ استعمال کریں:"
        } else {
            "Required Bootcamp citation format (use on every answer and in your notes):"
        }
        val template = if (useUrdu) {
            "[n] سندھ CS جماعت … • باب … • PDF صفحات … • نصاب §… • cs_xi_lecture_notes.pdf"
        } else {
            "[n] Sindh CS Class … • Ch.… • Teacher PDF pp. … • Syllabus §… • cs_xi_lecture_notes.pdf"
        }
        val refs = BootcampCitation.referencesBlock(context, samples, useUrdu)
        return "$intro\n\n$template\n\n$refs"
    }

    private fun goldenTopics(
        context: Context,
        tutorContext: TutorContext,
        useUrdu: Boolean
    ): String {
        val corpus = TutorCorpus.ensureLoaded(context)
        val hits = corpus
            .filter { it.isGolden }
            .filter { tutorContext.classId == null || it.classId == tutorContext.classId }
            .take(8)
            .mapIndexed { i, passage ->
                val cite = BootcampCitation.format(context, passage, i + 1, useUrdu)
                "$cite\n${excerpt(passage, useUrdu, 100)}"
            }
        if (hits.isEmpty()) {
            return if (useUrdu) "★ والا مواد PDF صفحات میں تلاش کریں۔" else "Search your PDF pages for ★ markers in cinematic mode."
        }
        val header = if (useUrdu) "★ سنہری / امتحانی موضوعات (نوٹس سے):" else "★ Golden / high-yield topics from your notes:"
        return header + "\n\n" + hits.joinToString("\n\n") { "• $it" }
    }

    private fun formatAnswer(
        context: Context,
        ranked: List<Pair<TutorPassage, Int>>,
        useUrdu: Boolean,
        query: String
    ): String {
        val top = ranked.first().first
        val intro = if (useUrdu) {
            "آپ کے bootcamp نوٹس سے:"
        } else {
            "From your bundled teacher lecture notes:"
        }
        val body = excerpt(top, useUrdu, 480)
        val refs = BootcampCitation.referencesBlock(
            context,
            ranked.map { it.first },
            useUrdu
        )
        val exam = if (top.isGolden) {
            if (useUrdu) "\n\n★ امتحان کی یاد دہانی — یہ موضوع teacher PDF میں ★ کے ساتھ نشان زد ہے۔"
            else "\n\n★ Exam tip — this topic is marked ★ in the teacher PDF."
        } else ""
        val more = if (ranked.size > 1) {
            val extra = ranked.drop(1).joinToString("\n\n") { (p, _) ->
                excerpt(p, useUrdu, 120)
            }
            if (useUrdu) "\n\nمتعلقہ اقتباسات:\n$extra" else "\n\nRelated excerpts:\n$extra"
        } else ""
        val cinematic = if (top.page != null) {
            if (useUrdu) "\n\nسینمائی لیکچر میں صفحہ ${top.page} کھولیں۔"
            else "\n\nOpen cinematic lecture around page ${top.page}."
        } else ""
        return "$intro\n\n$body\n\n$refs$exam$more$cinematic"
    }

    private fun noMatch(useUrdu: Boolean, query: String): String {
        return if (useUrdu) {
            "مجھے \"$query\" کے لیے مخصوص اقتباس نہیں ملا۔ \"golden topics\" یا \"quiz xi\" آزمائیں، یا لیکچر PDF میں تلاش کریں۔"
        } else {
            "I couldn't find a strong match for \"$query\" in the embedded notes. Try \"golden topics\", \"quiz xi\", or rephrase with a chapter keyword (e.g. K-map, OSI, bubble sort)."
        }
    }

    private fun tokenize(query: String): List<String> {
        return query.lowercase()
            .replace(Regex("[^a-z0-9★\\s]"), " ")
            .split(Regex("\\s+"))
            .filter { it.length > 1 && it !in stopWordsEn }
    }

    private fun scorePassage(
        passage: TutorPassage,
        tokens: List<String>,
        tutorContext: TutorContext
    ): Int {
        val hayEn = passage.textEn.lowercase()
        val hayUr = passage.textUr.lowercase()
        var score = 0
        for (token in tokens) {
            if (hayEn.contains(token)) score += 4
            if (hayUr.contains(token)) score += 2
        }
        if (passage.isGolden) score += 2
        if (tutorContext.chapterId != null && passage.chapterId == tutorContext.chapterId) score += 12
        if (tutorContext.classId != null && passage.classId == tutorContext.classId) score += 4
        if (tutorContext.page != null && passage.page == tutorContext.page) score += 15
        return score
    }

    private fun excerpt(passage: TutorPassage, useUrdu: Boolean, maxLen: Int): String {
        val raw = if (useUrdu) passage.textUr.ifBlank { passage.textEn } else passage.textEn
        val cleaned = raw.replace(Regex("\\s+"), " ").trim()
        if (cleaned.length <= maxLen) return cleaned
        val cut = cleaned.substring(0, min(maxLen, cleaned.length))
        val lastPeriod = cut.lastIndexOf('.')
        return if (lastPeriod > maxLen / 2) cut.substring(0, lastPeriod + 1) else "$cut…"
    }

    fun groundingExcerpt(context: Context, query: String, tutorContext: TutorContext): String {
        val tokens = tokenize(query)
        if (tokens.isEmpty()) return ""
        val corpus = TutorCorpus.ensureLoaded(context)
        val ranked = corpus
            .map { passage -> passage to scorePassage(passage, tokens, tutorContext) }
            .filter { it.second > 0 }
            .sortedByDescending { it.second }
            .take(4)
        return BootcampCitation.groundingWithCitations(
            context,
            ranked.map { (p, _) -> p to excerpt(p, false, 600) }
        )
    }

    fun chapterHint(context: Context, chapterId: String, useUrdu: Boolean): String {
        val chapter = LectureNotesRepository.getChapterById(context, chapterId) ?: return ""
        return if (useUrdu) {
            "اس باب پر بات کر رہے ہیں: ${chapter.urdu.title}. پوچھیں: \"★ topics\" یا کوئی سبق۔"
        } else {
            "Focused on: ${chapter.english.title}. Ask about ★ topics or any concept in this chapter."
        }
    }
}
