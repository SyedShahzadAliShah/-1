package com.couplesguide.postures.data

import com.couplesguide.postures.R

object PostureRepository {

    val categories: List<String> = listOf(
        "All",
        "Face to Face",
        "Side by Side",
        "Rear Entry",
        "Standing & Seated",
        "Variations"
    )

    private val postures: List<Posture> = listOf(
        Posture(
            id = "missionary",
            name = "Missionary",
            category = "Face to Face",
            summary = "Classic face-to-face position with one partner on top.",
            description = "One of the most common intimate positions. One partner lies on their back while the other lies on top, facing them. It allows eye contact, kissing, and easy communication.",
            steps = listOf(
                "One partner lies comfortably on their back with knees slightly bent.",
                "The other partner positions themselves on top, supporting their weight on hands or forearms.",
                "Adjust hip height and leg placement until both partners feel comfortable.",
                "Move slowly at first and check in with each other."
            ),
            tips = listOf(
                "Place a pillow under the lower back for better angle and comfort.",
                "Keep communication open — small adjustments make a big difference.",
                "Try varying depth and pace together."
            ),
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_missionary
        ),
        Posture(
            id = "cowgirl",
            name = "Cowgirl (Woman on Top)",
            category = "Face to Face",
            summary = "One partner straddles the other while facing them.",
            description = "The partner on top sits or kneels astride the other, facing them. This position gives the top partner control over movement, depth, and pace.",
            steps = listOf(
                "One partner lies on their back.",
                "The other partner kneels or sits astride their hips, facing them.",
                "The top partner can brace hands on the other's chest or thighs for balance.",
                "Rock hips gently or use leg strength to find a comfortable rhythm."
            ),
            tips = listOf(
                "The partner on top sets the pace — communicate what feels good.",
                "Lean forward for closeness or sit upright for a different angle.",
                "Use a wall or headboard for extra support if needed."
            ),
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_cowgirl
        ),
        Posture(
            id = "spooning",
            name = "Spooning",
            category = "Side by Side",
            summary = "Both partners lie on their sides, nestled together.",
            description = "Partners lie on their sides facing the same direction, like spoons in a drawer. It is gentle, intimate, and low-effort — ideal for relaxed or tired moments.",
            steps = listOf(
                "Both partners lie on their sides facing the same direction.",
                "The partner behind curls around the front partner, chest to back.",
                "The front partner may bend knees slightly for easier alignment.",
                "Move together slowly and stay attuned to each other's comfort."
            ),
            tips = listOf(
                "Place a pillow between knees for hip alignment.",
                "Great for morning intimacy or when you want something calm.",
                "The front partner can reach back or guide movement with their hand."
            ),
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_spooning
        ),
        Posture(
            id = "side_by_side",
            name = "Side by Side (Facing)",
            category = "Side by Side",
            summary = "Partners lie facing each other on their sides.",
            description = "Both partners lie on their sides facing one another. This creates closeness and equal participation while reducing physical strain.",
            steps = listOf(
                "Both partners lie on their sides, facing each other.",
                "Intertwine legs as comfort allows — top leg over partner's hip works well.",
                "Stay close with arms around each other for stability.",
                "Rock hips together gently to find a shared rhythm."
            ),
            tips = listOf(
                "Excellent for prolonged eye contact and whispered conversation.",
                "Adjust how tightly legs are intertwined to change sensation.",
                "Works well on a firm mattress or floor with padding."
            ),
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_side_by_side
        ),
        Posture(
            id = "doggy",
            name = "Rear Entry (Doggy Style)",
            category = "Rear Entry",
            summary = "One partner kneels while the other enters from behind.",
            description = "One partner is on hands and knees (or lying flat) while the other kneels or stands behind them. This allows deeper penetration and a different angle of stimulation.",
            steps = listOf(
                "One partner positions on hands and knees, or lies flat on their stomach.",
                "The other partner kneels or stands behind them at a comfortable height.",
                "The front partner can lower onto forearms or place a pillow under hips.",
                "Start slowly and adjust angle by changing knee width or hip height."
            ),
            tips = listOf(
                "A pillow under the hips can improve comfort and angle.",
                "The partner in front controls depth by shifting hips forward or back.",
                "Check in frequently — this position can be intense."
            ),
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_doggy
        ),
        Posture(
            id = "lotus",
            name = "Lotus",
            category = "Standing & Seated",
            summary = "Seated face-to-face with legs wrapped around each other.",
            description = "Both partners sit facing each other with legs intertwined. It emphasizes closeness, slow movement, and synchronized breathing.",
            steps = listOf(
                "One partner sits cross-legged or with legs extended.",
                "The other partner sits on their lap, facing them, wrapping legs around their waist.",
                "Wrap arms around each other for balance and closeness.",
                "Rock together slowly — small movements are often most pleasurable."
            ),
            tips = listOf(
                "Requires flexibility — use cushions for support under hips.",
                "Ideal for tantric or slow, mindful intimacy.",
                "Maintain eye contact to deepen emotional connection."
            ),
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.ill_lotus
        ),
        Posture(
            id = "standing",
            name = "Standing",
            category = "Standing & Seated",
            summary = "One partner lifts or supports the other while standing.",
            description = "Partners stand, often with one partner lifted or braced against a wall. Adds spontaneity but requires strength and stability.",
            steps = listOf(
                "One partner stands with back against a sturdy wall.",
                "The other partner faces them, with one or both legs wrapped around their waist.",
                "The standing partner supports their partner's weight with hands under thighs or hips.",
                "Move carefully — balance and communication are essential."
            ),
            tips = listOf(
                "Use a wall for support — never rely on balance alone.",
                "The lifted partner can help by gripping shoulders or the wall.",
                "Start with one foot on a low surface (chair) for an easier variation."
            ),
            difficulty = Difficulty.ADVANCED,
            illustrationRes = R.drawable.ill_standing
        ),
        Posture(
            id = "edge_of_bed",
            name = "Edge of Bed",
            category = "Variations",
            summary = "One partner sits or lies at the bed edge while the other stands.",
            description = "One partner sits or lies at the edge of the bed with legs draped over the side. The other partner stands between their legs. Comfortable and accessible.",
            steps = listOf(
                "One partner sits or lies back at the very edge of the bed.",
                "They place feet on the floor or rest calves on the standing partner's shoulders.",
                "The standing partner positions themselves between their partner's legs.",
                "Adjust bed height or use a sturdy surface for the best alignment."
            ),
            tips = listOf(
                "Works well when one partner has limited mobility.",
                "The lying partner can grip the bed edge for stability.",
                "Try different leg positions — bent, straight, or over shoulders."
            ),
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_edge_bed
        ),
        Posture(
            id = "reverse_cowgirl",
            name = "Reverse Cowgirl",
            category = "Variations",
            summary = "Top partner faces away while straddling the other.",
            description = "Similar to cowgirl, but the partner on top faces away from the other. Offers a different angle and allows the bottom partner to enjoy a new perspective.",
            steps = listOf(
                "One partner lies on their back.",
                "The other straddles them facing away (toward their feet).",
                "The top partner places hands on the bottom partner's thighs for balance.",
                "Lean forward or sit upright to change the sensation."
            ),
            tips = listOf(
                "The bottom partner should communicate if depth becomes uncomfortable.",
                "The top partner controls pace — go slowly at first.",
                "Combine with gentle hip circles for variety."
            ),
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_reverse_cowgirl
        ),
        Posture(
            id = "butterfly",
            name = "Butterfly",
            category = "Variations",
            summary = "Reclining partner's hips are elevated with legs open wide.",
            description = "One partner lies on their back near the edge of the bed with hips raised on a pillow. Their legs are open and drawn back. The other partner stands or kneels at the edge.",
            steps = listOf(
                "Place a firm pillow under the reclining partner's hips.",
                "They lie back and draw knees toward chest or rest legs on the standing partner's shoulders.",
                "The other partner stands or kneels at the bed edge.",
                "Adjust pillow height until the angle feels comfortable for both."
            ),
            tips = listOf(
                "Excellent for G-spot or prostate stimulation depending on anatomy.",
                "Use a wedge pillow for more stable elevation than a soft pillow.",
                "The reclining partner can hold their own legs for control."
            ),
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_butterfly
        ),
        Posture(
            id = "scissors",
            name = "Scissors",
            category = "Side by Side",
            summary = "Partners lie at an angle with legs intertwined.",
            description = "Partners lie on their sides at roughly a 90-degree angle to each other, with legs scissored together. Allows clitoral or mutual stimulation with less penetration depth.",
            steps = listOf(
                "Both partners lie on their sides facing each other at a slight angle.",
                "Intertwine legs so thighs and hips align comfortably.",
                "Each partner can use their hand or hip movement for stimulation.",
                "Adjust the angle of your bodies until contact feels natural."
            ),
            tips = listOf(
                "Works well for couples who want intimacy with less physical intensity.",
                "Add lubricant if needed for comfortable friction.",
                "Great for mutual pleasure and synchronized movement."
            ),
            difficulty = Difficulty.INTERMEDIATE,
            illustrationRes = R.drawable.ill_scissors
        ),
        Posture(
            id = "lazy_dog",
            name = "Lazy Dog",
            category = "Rear Entry",
            summary = "A relaxed rear-entry variation lying flat.",
            description = "A gentler version of rear entry where the receiving partner lies flat on their stomach rather than on hands and knees. Lower effort and very comfortable.",
            steps = listOf(
                "One partner lies flat on their stomach with a pillow under hips.",
                "The other partner lies on top or positions behind them.",
                "Keep weight distributed — the top partner should not bear down heavily.",
                "Use slow, grinding movements rather than deep thrusting."
            ),
            tips = listOf(
                "Ideal when one or both partners are tired.",
                "The bottom partner can adjust hip height with pillow thickness.",
                "Combine with gentle massage for a relaxing experience."
            ),
            difficulty = Difficulty.BEGINNER,
            illustrationRes = R.drawable.ill_lazy_dog
        )
    )

    fun getAllPostures(): List<Posture> = postures

    fun getPosturesByCategory(category: String): List<Posture> {
        if (category == "All") return postures
        return postures.filter { it.category == category }
    }

    fun getPostureById(id: String): Posture? = postures.find { it.id == id }
}
