package com.neduet.mt331lecture.data.mt331

/**
 * LaTeX display strings for MathJax (Walpole / MT-331 cheat-sheet formulas).
 */
object Mt331LatexCatalog {

    private val byBeatId = mapOf(
        "ch1_pop_sample" to """N,\mu,\sigma^2 \qquad n,\bar{x},s^2""",
        "ch1_location" to """\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i,\quad \tilde{x},\quad \text{mode}""",
        "ch1_spread" to """s^2=\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1},\qquad s=\sqrt{s^2}""",
        "ch2_space" to """0\le P(A)\le 1,\qquad P(S)=1""",
        "ch2_rules" to """P(A\cup B)=P(A)+P(B)-P(A\cap B)""",
        "ch2_bayes" to """P(B_r|A)=\frac{P(B_r)P(A|B_r)}{\sum_i P(B_i)P(A|B_i)}""",
        "ch3_types" to """\sum_x f(x)=1,\qquad \int_{-\infty}^{\infty} f(x)\,dx=1""",
        "ch3_cdf" to """F(x)=P(X\le x)""",
        "ch4_mean_var" to """\mu=E(X),\qquad \sigma^2=V(X)=E(X^2)-[E(X)]^2""",
        "ch4_rules" to """\mathrm{Cov}(X,Y)=E(XY)-\mu_X\mu_Y""",
        "ch5_binomial" to """\mu=np,\qquad \sigma^2=npq""",
        "ch5_hyper_pois" to """P(X=x)=e^{-\lambda t}\frac{(\lambda t)^x}{x!}""",
        "ch6_normal" to """Z=\frac{X-\mu}{\sigma}""",
        "ch6_approx" to """Z=\frac{X\pm 0.5-np}{\sqrt{npq}}""",
        "ch6_exp" to """P(X>x)=e^{-x/\beta}""",
        "ch8_clt" to """Z=\frac{\bar{X}-\mu}{\sigma/\sqrt{n}}""",
        "ch8_t_f" to """t=\frac{\bar{X}-\mu}{s/\sqrt{n}},\quad v=n-1""",
        "ch9_one_mean" to """\bar{x}\pm z_{\alpha/2}\frac{\sigma}{\sqrt{n}}""",
        "ch9_prop_var" to """\hat{p}\pm z_{\alpha/2}\sqrt{\frac{\hat{p}\hat{q}}{n}}""",
        "ch10_framework" to """\alpha=P(\text{Type I}),\quad \beta=P(\text{Type II})""",
        "ch10_tests" to """t=\frac{\bar{d}-d_0}{s_d/\sqrt{n}}""",
        "ch11_ls" to """b_1=\frac{S_{xy}}{S_{xx}},\qquad b_0=\bar{y}-b_1\bar{x}""",
        "ch11_corr" to """-1\le r\le 1""",
        "ch13_table" to """F=\frac{MSA}{MSE}""",
        "ch16_charts" to """\bar{\bar{X}}\pm A_2\bar{R}""",
        "ch16_cap" to """C_p=\frac{USL-LSL}{6\sigma}"""
    )

    fun latexForBeat(beat: LectureBeat, language: String): String {
        val explicit = if (language == "ur") beat.latexUr else beat.latexEn
        if (explicit.isNotBlank()) return explicit
        return byBeatId[beat.id] ?: plainToLatex(if (language == "ur") beat.formulaUr else beat.formulaEn)
    }

    private fun plainToLatex(plain: String): String {
        if (plain.isBlank()) return ""
        return plain
            .replace("Σ", "\\sum")
            .replace("σ", "\\sigma")
            .replace("μ", "\\mu")
            .replace("≤", "\\le ")
            .replace("≥", "\\ge ")
            .replace("±", "\\pm ")
            .replace("√", "\\sqrt")
            .replace("̄", "") // combining macron — keep x̄ as \bar{x} manually in catalog
            .let { "\\displaystyle $it" }
    }
}
