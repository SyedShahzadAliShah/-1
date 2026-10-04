package com.neduet.mt331lecture.data.mt331

/**
 * Inline SVG sketchnote diagrams (embedded beside MathJax in lecture beats).
 */
object Mt331BeatDiagrams {

    fun svgForBeat(beatId: String): String? = diagrams[beatId]

    private val diagrams = mapOf(
        "ch1_pop_sample" to populationSampleSvg(),
        "ch1_location" to histogramSvg(),
        "ch2_space" to vennSvg(),
        "ch2_rules" to vennUnionSvg(),
        "ch3_types" to pmfBarsSvg(),
        "ch6_normal" to normalCurveSvg(),
        "ch6_approx" to continuitySvg(),
        "ch8_clt" to cltSvg(),
        "ch9_one_mean" to ciSvg(),
        "ch10_framework" to hypothesisSvg(),
        "ch11_ls" to regressionSvg(),
        "ch13_table" to anovaSvg(),
        "ch16_charts" to controlChartSvg()
    )

    private fun populationSampleSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <rect x="16" y="24" width="200" height="92" rx="8" fill="none" stroke="#5B8DEF" stroke-width="2" stroke-dasharray="6 4"/>
  <text x="24" y="44" fill="#9AA8C7" font-size="12" font-family="sans-serif">Population N</text>
  <rect x="48" y="52" width="120" height="52" rx="6" fill="#5B8DEF33" stroke="#FFB347" stroke-width="2"/>
  <text x="58" y="82" fill="#F4F7FF" font-size="12" font-family="sans-serif">Sample n</text>
  <text x="230" y="78" fill="#7EE787" font-size="11" font-family="sans-serif">μ,σ² → x̄,s²</text>
</svg>""".trimIndent()

    private fun histogramSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <line x1="40" y1="110" x2="280" y2="110" stroke="#9AA8C7" stroke-width="1"/>
  <rect x="60" y="70" width="28" height="40" fill="#5B8DEF"/>
  <rect x="100" y="50" width="28" height="60" fill="#5B8DEF"/>
  <rect x="140" y="40" width="28" height="70" fill="#FFB347"/>
  <rect x="180" y="55" width="28" height="55" fill="#5B8DEF"/>
  <rect x="220" y="75" width="28" height="35" fill="#5B8DEF"/>
  <line x1="154" y1="20" x2="154" y2="115" stroke="#7EE787" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="158" y="28" fill="#7EE787" font-size="11" font-family="sans-serif">x̄</text>
</svg>""".trimIndent()

    private fun vennSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <rect x="20" y="20" width="280" height="100" rx="8" fill="none" stroke="#9AA8C7" stroke-width="1.5"/>
  <text x="28" y="38" fill="#9AA8C7" font-size="11" font-family="sans-serif">S</text>
  <circle cx="120" cy="72" r="42" fill="#5B8DEF22" stroke="#5B8DEF" stroke-width="2"/>
  <circle cx="200" cy="72" r="42" fill="#FFB34722" stroke="#FFB347" stroke-width="2"/>
  <text x="95" y="76" fill="#F4F7FF" font-size="14" font-family="sans-serif">A</text>
  <text x="210" y="76" fill="#F4F7FF" font-size="14" font-family="sans-serif">B</text>
</svg>""".trimIndent()

    private fun vennUnionSvg() = vennSvg()

    private fun pmfBarsSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <text x="16" y="24" fill="#9AA8C7" font-size="11" font-family="sans-serif">Discrete PMF</text>
  <line x1="40" y1="110" x2="280" y2="110" stroke="#9AA8C7"/>
  <rect x="70" y="80" width="20" height="30" fill="#7EE787"/>
  <rect x="110" y="55" width="20" height="55" fill="#7EE787"/>
  <rect x="150" y="40" width="20" height="70" fill="#7EE787"/>
  <rect x="190" y="65" width="20" height="45" fill="#7EE787"/>
  <text x="68" y="125" fill="#9AA8C7" font-size="10">0</text>
  <text x="108" y="125" fill="#9AA8C7" font-size="10">1</text>
  <text x="148" y="125" fill="#9AA8C7" font-size="10">2</text>
  <text x="188" y="125" fill="#9AA8C7" font-size="10">3</text>
</svg>""".trimIndent()

    private fun normalCurveSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <path d="M40,110 C80,110 100,30 160,30 C220,30 240,110 280,110" fill="#5B8DEF33" stroke="#5B8DEF" stroke-width="2.5"/>
  <line x1="160" y1="30" x2="160" y2="110" stroke="#FFB347" stroke-width="1.5" stroke-dasharray="4 3"/>
  <text x="152" y="125" fill="#FFB347" font-size="11" font-family="sans-serif">μ</text>
  <text x="200" y="50" fill="#9AA8C7" font-size="10" font-family="sans-serif">68%</text>
</svg>""".trimIndent()

    private fun continuitySvg() = normalCurveSvg()

    private fun cltSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <path d="M30,95 Q60,40 90,95 T150,95" fill="none" stroke="#9AA8C7" stroke-width="1.5"/>
  <text x="24" y="88" fill="#9AA8C7" font-size="9">pop.</text>
  <path d="M170,110 C200,110 215,35 250,35 C285,35 295,110 305,110" fill="#5B8DEF33" stroke="#5B8DEF" stroke-width="2"/>
  <text x="168" y="28" fill="#7EE787" font-size="10" font-family="sans-serif">x̄ ~ Normal</text>
</svg>""".trimIndent()

    private fun ciSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <line x1="60" y1="70" x2="260" y2="70" stroke="#5B8DEF" stroke-width="3"/>
  <line x1="60" y1="55" x2="60" y2="85" stroke="#FFB347" stroke-width="2"/>
  <line x1="260" y1="55" x2="260" y2="85" stroke="#FFB347" stroke-width="2"/>
  <circle cx="160" cy="70" r="6" fill="#7EE787"/>
  <text x="150" y="105" fill="#7EE787" font-size="11" font-family="sans-serif">x̄</text>
  <text x="100" y="40" fill="#9AA8C7" font-size="10" font-family="sans-serif">CI</text>
</svg>""".trimIndent()

    private fun hypothesisSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <text x="24" y="36" fill="#F4F7FF" font-size="12" font-family="sans-serif">H₀ vs H₁</text>
  <rect x="24" y="48" width="120" height="36" rx="6" fill="#5B8DEF33" stroke="#5B8DEF"/>
  <text x="40" y="72" fill="#F4F7FF" font-size="12">H₀</text>
  <rect x="176" y="48" width="120" height="36" rx="6" fill="#FFB34733" stroke="#FFB347"/>
  <text x="192" y="72" fill="#F4F7FF" font-size="12">H₁</text>
  <text x="24" y="110" fill="#9AA8C7" font-size="10">α Type I · β Type II</text>
</svg>""".trimIndent()

    private fun regressionSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <line x1="50" y1="110" x2="270" y2="110" stroke="#9AA8C7"/>
  <line x1="50" y1="110" x2="50" y2="30" stroke="#9AA8C7"/>
  <line x1="60" y1="100" x2="250" y2="45" stroke="#5B8DEF" stroke-width="2.5"/>
  <circle cx="90" cy="78" r="4" fill="#FFB347"/>
  <circle cx="140" cy="62" r="4" fill="#FFB347"/>
  <circle cx="190" cy="58" r="4" fill="#FFB347"/>
  <circle cx="230" cy="48" r="4" fill="#FFB347"/>
</svg>""".trimIndent()

    private fun anovaSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <text x="20" y="28" fill="#9AA8C7" font-size="10" font-family="sans-serif">Between | Within</text>
  <rect x="40" y="50" width="50" height="60" fill="#5B8DEF"/>
  <rect x="110" y="65" width="50" height="45" fill="#5B8DEF88"/>
  <rect x="180" y="72" width="50" height="38" fill="#5B8DEF88"/>
  <rect x="250" y="40" width="40" height="70" fill="#FFB34755" stroke="#FFB347"/>
</svg>""".trimIndent()

    private fun controlChartSvg() = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 140" role="img">
  <rect width="320" height="140" rx="12" fill="#0d1220"/>
  <line x1="40" y1="35" x2="280" y2="35" stroke="#FF6B6B" stroke-dasharray="5 3"/>
  <line x1="40" y1="70" x2="280" y2="70" stroke="#7EE787"/>
  <line x1="40" y1="105" x2="280" y2="105" stroke="#FF6B6B" stroke-dasharray="5 3"/>
  <polyline points="50,68 90,72 130,65 170,74 210,67 250,71 270,69" fill="none" stroke="#5B8DEF" stroke-width="2"/>
  <text x="40" y="28" fill="#9AA8C7" font-size="9">UCL</text>
  <text x="40" y="118" fill="#9AA8C7" font-size="9">LCL</text>
</svg>""".trimIndent()
}
