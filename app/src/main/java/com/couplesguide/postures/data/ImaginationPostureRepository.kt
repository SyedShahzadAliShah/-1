package com.couplesguide.postures.data

import com.couplesguide.postures.R

object ImaginationPostureRepository {

    fun getImaginationPostures(): List<Posture> = imaginationPostures

    private val imaginationPostures: List<Posture> = listOf(
        imagination(
            id = "imagine_breath",
            illustrationRes = R.drawable.pic_imagine_breath,
            enName = "Breath Together",
            urName = "ساتھ سانس لیں",
            enSummary = "Imagine your breathing slowly becoming one rhythm.",
            urSummary = "تصور کریں کہ آپ کی سانسیں آہستہ آہستہ ایک تال بن جائیں۔",
            enDesc = "This imagination exercise builds calm connection before physical intimacy. " +
                "Sit or lie facing each other. There is no goal beyond feeling present together.",
            urDesc = "یہ تخیلی مشق جسمانی قربت سے پہلے پرسکون تعلق بناتی ہے۔ " +
                "آمنے سامنے بیٹھیں یا لیٹیں۔ مقصد صرف موجودگی محسوس کرنا ہے۔",
            enSteps = listOf(
                "Close your eyes and place a hand on your partner's chest or hand.",
                "Imagine a warm golden light flowing between you with each breath.",
                "Inhale together for four counts — picture the light growing brighter.",
                "Exhale together for six counts — picture tension leaving your bodies.",
                "Repeat until your breathing naturally synchronizes."
            ),
            urSteps = listOf(
                "آنکھیں بند کریں اور ہاتھ ساتھی کے سینے یا ہاتھ پر رکھیں۔",
                "ہر سانس کے ساتھ گرم سنہری روشنی کا بہاؤ تصور کریں۔",
                "چار گنتی تک ساتھ سانس لیں — روشنی چمکتی محسوس کریں۔",
                "چھ گنتی تک ساتھ سانس چھوڑیں — تناؤ نکلتا محسوس کریں۔",
                "تب تک دہرائیں جب سانسیں خود ہم آہنگ ہو جائیں۔"
            ),
            enTips = listOf(
                "No need to force perfect timing — near-sync is enough.",
                "Whisper \"breathe with me\" if it helps you stay connected.",
                "Use this exercise to transition gently into touch."
            ),
            urTips = listOf(
                "مکمل وقت کی زبردستی نہیں — قریب قریب ہم آہنگی کافی ہے۔",
                "\"میرے ساتھ سانس لو\" آہستہ کہیں اگر مدد ملے۔",
                "نرم چھونے میں آنے کے لیے یہ مشق استعمال کریں۔"
            )
        ),
        imagination(
            id = "imagine_candlelight",
            illustrationRes = R.drawable.pic_imagine_candlelight,
            enName = "Candlelight Gaze",
            urName = "شمع کی روشنی میں نگاہیں",
            enSummary = "Imagine soft candlelight while holding gentle eye contact.",
            urSummary = "نرم شمع کی روشنی اور آہستہ آنکھوں کا رابطہ تصور کریں۔",
            enDesc = "Eye contact deepens emotional intimacy. This imagination posture uses " +
                "visualization to reduce self-consciousness and build trust.",
            urDesc = "آنکھوں کا رابطہ جذباتی قربت بڑھاتا ہے۔ یہ تخیلی مشق " +
                "خود آگاہی کم کر کے اعتماد بناتی ہے۔",
            enSteps = listOf(
                "Dim the lights or imagine a single candle between you.",
                "Sit knee to knee, spines relaxed, shoulders soft.",
                "Look into your partner's left eye — the \"soul eye\" — without staring harshly.",
                "When you blink or look away, return gently without judgment.",
                "After five minutes, share one word describing what you felt."
            ),
            urSteps = listOf(
                "روشنی مدھم کریں یا درمیان میں ایک شمع تصور کریں۔",
                "گھٹنے سے گھٹنا ملائے، آرام سے بیٹھیں۔",
                "ساتھی کی بائیں آنکھ میں دیکھیں — بغیر سخت گھورے۔",
                "جب نظر ہٹے تو نرمی سے واپس آئیں، بغیر تنقید کے۔",
                "پانچ منٹ بعد ایک لفظ میں احساس بتائیں۔"
            ),
            enTips = listOf(
                "Laughter is normal — smile and continue.",
                "Start with 60 seconds if five minutes feels long.",
                "Candlelight is symbolic; a phone's warm screen works too."
            ),
            urTips = listOf(
                "ہنسی معمول ہے — مسکرائیں اور جاری رکھیں۔",
                "پانچ منٹ لمبے لگیں تو ایک منٹ سے شروع کریں۔",
                "شمع علامتی ہے؛ فون کی گرم روشنی بھی چل سکتی ہے۔"
            )
        ),
        imagination(
            id = "imagine_slow_embrace",
            illustrationRes = R.drawable.pic_imagine_embrace,
            enName = "Slow Embrace",
            urName = "آہستہ آغوش",
            enSummary = "Picture a long, unhurried hug that gradually deepens closeness.",
            urSummary = "لمبا بے جلدی والا گلے ملنے کا تصور جو قربت بڑھائے۔",
            enDesc = "Physical posture begins in the mind. Visualizing a slow embrace " +
                "prepares the body to relax and welcome your partner.",
            urDesc = "جسمانی پوزیشن ذہن میں شروع ہوتی ہے۔ آہستہ آغوش کا تصور " +
                "جسم کو آرام اور ساتھی کا استقبال کرنے کے لیے تیار کرتا ہے۔",
            enSteps = listOf(
                "Stand or sit and imagine wrapping your arms fully around your partner.",
                "Picture pulling them closer by one inch every three breaths.",
                "Feel their heartbeat against yours — real or imagined.",
                "Imagine warmth spreading from your chest through your arms.",
                "Open your eyes and recreate the hug physically, matching the imagined pace."
            ),
            urSteps = listOf(
                "کھڑے یا بیٹھے ساتھی کے گرد بازو لپیٹنے کا تصور کریں۔",
                "ہر تین سانسوں میں ایک انچ قریب کھینچنے کا خیال کریں۔",
                "ان کے دل کی دھڑکن اپنے سینے پر محسوس کریں — حقیقی یا تصور میں۔",
                "سینے سے بازوؤں تک گرمی پھیلنے کا تصور کریں۔",
                "آنکھیں کھول کر یہی رفتار سے حقیقی آغوش دیں۔"
            ),
            enTips = listOf(
                "Keep shoulders dropped — tension blocks the exercise.",
                "Let the partner who feels safer initiate tighter contact.",
                "Pair with soft music if silence feels awkward."
            ),
            urTips = listOf(
                "کندھے ڈھیلے رکھیں — تناؤ رکاوٹ بنتا ہے۔",
                "جو محفوظ محسوس کرے وہ قریب آنے کی شروعات کرے۔",
                "خاموشی عجیب لگے تو نرم موسیقی چلائیں۔"
            )
        ),
        imagination(
            id = "imagine_ocean",
            illustrationRes = R.drawable.pic_imagine_ocean,
            enName = "Ocean Waves",
            urName = "سمندر کی لہریں",
            enSummary = "Imagine intimacy as gentle waves — rising, pausing, falling.",
            urSummary = "قربت کو نرم لہروں جیسا تصور کریں — اٹھنا، رکنا، اترنا۔",
            enDesc = "Rhythm reduces performance pressure. This educational imagination " +
                "posture teaches couples to think in waves rather than constant intensity.",
            urDesc = "تال کارکردگی کا دباؤ کم کرتی ہے۔ یہ تخیلی مشق جوڑوں کو " +
                "مسلسل شدت کی بجائے لہروں میں سوچنا سکھاتی ہے۔",
            enSteps = listOf(
                "Lie side by side and close your eyes.",
                "Imagine you are floating on calm water under a soft sky.",
                "Picture each wave as a rise of pleasure — not urgent, simply natural.",
                "Between waves, imagine still water — rest without stopping connection.",
                "Communicate: say \"wave\" when ready to increase, \"still\" to rest."
            ),
            urSteps = listOf(
                "ساتھ لیٹ کر آنکھیں بند کریں۔",
                "پرسکون پانی پر تیرتے نرم آسمان کے نیچے تصور کریں۔",
                "ہر لہر کو لطف کی چھوٹی سی لہر سمجھیں — بے جلدی، قدرتی۔",
                "لہروں کے درمیان ساکت پانی — رابطہ بغیر تھکن کے۔",
                "بتائیں: \"لہر\" جب بڑھنا ہو، \"ساکت\" جب آرام چاہیے۔"
            ),
            enTips = listOf(
                "Apply this mental model during physical intimacy later.",
                "There is no correct speed — your waves are unique.",
                "Combine with slow breathing from the Breath Together exercise."
            ),
            urTips = listOf(
                "بعد میں جسمانی قربت میں یہ ذہنی ماڈل استعمال کریں۔",
                "کوئی صحیح رفتار نہیں — آپ کی لہریں منفرد ہیں۔",
                "سانس والی مشق کے ساتھ ملا کر کریں۔"
            )
        ),
        imagination(
            id = "imagine_starlight",
            illustrationRes = R.drawable.pic_imagine_starlight,
            enName = "Starlit Embrace",
            urName = "ستاروں کی چادر میں",
            enSummary = "Imagine lying together under open stars, safe and unhurried.",
            urSummary = "کھلے ستاروں کے نیچے ساتھ لیٹنے کا محفوظ بے جلدی تصور۔",
            enDesc = "Setting a mental scene unlocks playfulness. This posture uses " +
                "romantic imagination to help couples feel less self-conscious.",
            urDesc = "ذہنی منظر کھلتاپن بڑھاتا ہے۔ یہ مشق رومانوی تخیل سے " +
                "جوڑوں کو کم جھجک محسوس کراتی ہے۔",
            enSteps = listOf(
                "Lie together and imagine a blanket of stars above you.",
                "Picture cool night air on skin contrasted with partner's warmth.",
                "Imagine whispering wishes only the stars can hear.",
                "Let hands explore slowly as if the world has paused for you both.",
                "Thank each other aloud for sharing the moment."
            ),
            urSteps = listOf(
                "ساتھ لیٹیں اور اوپر ستاروں کی چادر تصور کریں۔",
                "ٹھنڈی ہوا اور ساتھی کی گرمی کا فرق محسوس کریں۔",
                "ایسی خواہشیں سرگوشی میں کہیں جو صرف ستارے سنیں۔",
                "ہاتھ آہستہ دریافت کریں جیسے دنیا رک گئی ہو۔",
                "زور سے شکریہ کہیں اس لمحے کے لیے۔"
            ),
            enTips = listOf(
                "Play quiet night sounds if imagination is difficult.",
                "Works beautifully outdoors on a clear evening.",
                "Keep phones away to protect the imagined scene."
            ),
            urTips = listOf(
                "تصور مشکل ہو تو رات کی آہستہ آوازیں چلائیں۔",
                "صاف شام کھلے آسمان下 بہترین ہے۔",
                "فون دور رکھیں تاکہ منظر محفوظ رہے۔"
            )
        ),
        imagination(
            id = "imagine_morning",
            illustrationRes = R.drawable.pic_imagine_morning,
            enName = "Morning Light",
            urName = "صبح کی روشنی",
            enSummary = "Imagine lazy morning intimacy — soft light, no schedule.",
            urSummary = "سست صبح کی قربت — نرم روشنی، کوئی جلدی نہیں۔",
            enDesc = "Morning imagination reduces pressure to perform. It reframes intimacy " +
                "as a gentle awakening rather than a goal-oriented act.",
            urDesc = "صبح کا تصور کارکردگی کا دباؤ کم کرتا ہے۔ قربت کو " +
                "مقصد کی بجائے نرم بیداری سمجھنے میں مدد دیتا ہے۔",
            enSteps = listOf(
                "Imagine golden morning light through curtains.",
                "Picture waking with your partner's breath on your neck.",
                "Imagine stretching together like cats — slow, unhurried, playful.",
                "Visualize lazy kisses with nowhere to be.",
                "Carry this unhurried feeling into whatever you do next."
            ),
            urSteps = listOf(
                "پردوں سے سنہری صبح کی روشنی تصور کریں۔",
                "گردن پر ساتھی کی سانس سے جاگنے کا خیال کریں۔",
                "بلیوں کی طرح ساتھ ہلکا پھیلنا — آہستہ، بے جلدی، کھیل۔",
                "سست بوسے تصور کریں، کہیں جانے کی جلدی نہیں۔",
                "یہ بے جلدی احساس اگلے قدم میں لے جائیں۔"
            ),
            enTips = listOf(
                "Try on a real weekend morning without alarms.",
                "Warm beverages beforehand deepen the cozy feeling.",
                "Gentle touch only until you both feel fully awake."
            ),
            urTips = listOf(
                "حقیقی ویک اینڈ صبح بغیر الارم آزمائیں۔",
                "گرم مشروب پہلے آرام بڑھاتے ہیں۔",
                "پوری طرح جاگنے تک صرف نرم چھونا۔"
            )
        )
    )

    private fun imagination(
        id: String, illustrationRes: Int,
        enName: String, urName: String,
        enSummary: String, urSummary: String,
        enDesc: String, urDesc: String,
        enSteps: List<String>, urSteps: List<String>,
        enTips: List<String>, urTips: List<String>
    ) = Posture(
        id = id,
        difficulty = Difficulty.BEGINNER,
        illustrationRes = illustrationRes,
        categoryId = PostureRepository.CAT_IMAGINATION,
        isImagination = true,
        english = LocalizedContent(
            enName, "Imagination", enSummary, enDesc, enSteps, enTips
        ),
        urdu = LocalizedContent(
            urName, "تخیل", urSummary, urDesc, urSteps, urTips
        )
    )
}
