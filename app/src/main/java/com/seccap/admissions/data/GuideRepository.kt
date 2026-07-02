package com.seccap.admissions.data

data class GuideSection(
    val id: String,
    val title: LocalizedText,
    val body: LocalizedText,
    val steps: List<LocalizedText>
)

data class RequiredDocument(
    val id: String,
    val name: LocalizedText,
    val description: LocalizedText
)

object GuideRepository {

    fun getSections(): List<GuideSection> = listOf(
        GuideSection(
            id = "overview",
            title = LocalizedText(
                "What is SECCAP?",
                "SECCAP کیا ہے؟"
            ),
            body = LocalizedText(
                "SECCAP (Sindh Electronic Centralized College Admission Program) is the Government of Sindh's official online system for 1st-year (Class XI) admissions to government colleges. This helper app lets you prepare your application offline, listen to step-by-step guidance, and export a printable PDF summary.",
                "SECCAP (سندھ الیکٹرانک سینٹرلائزڈ کالج ایڈمیشن پروگرام) حکومت سندھ کا سرکاری آن لائن نظام ہے جو سرکاری کالجوں میں فرسٹ ایئر (گیارہویں جماعت) داخلے کے لیے ہے۔ یہ ایپ آپ کو آف لائن درخواست تیار کرنے، قدم بہ قدم رہنمائی سننے اور قابلِ پرنٹ PDF خلاصہ برآمد کرنے میں مدد دیتی ہے۔"
            ),
            steps = emptyList()
        ),
        GuideSection(
            id = "eligibility",
            title = LocalizedText("Eligibility Requirements", "اہلیت کی شرائط"),
            body = LocalizedText(
                "You must have passed Matriculation (Science, General, or Commerce) from a recognized board in Sindh or equivalent. Your marks determine which faculty groups you can apply for. Domicile of Sindh is required for most government colleges.",
                "آپ کو سندھ بورڈ یا مساوی بورڈ سے میٹرک (سائنس، جنرل یا کامرس) پاس ہونا ضروری ہے۔ آپ کے نمبر بتاتے ہیں کہ آپ کس گروپ کے لیے درخواست دے سکتے ہیں۔ زیادہ تر سرکاری کالجوں کے لیے سندھ کا ڈومیسائل ضروری ہے۔"
            ),
            steps = listOf(
                LocalizedText("Matric pass certificate from recognized board", "تسلیم شدہ بورڈ سے میٹرک پاس سرٹیفکیٹ"),
                LocalizedText("Minimum marks as per faculty requirement", "گروپ کے مطابق کم از کم نمبر"),
                LocalizedText("Sindh domicile certificate", "سندھ کا ڈومیسائل سرٹیفکیٹ"),
                LocalizedText("Valid B-Form or CNIC", "درست B-Form یا CNIC")
            )
        ),
        GuideSection(
            id = "application_steps",
            title = LocalizedText("Application Steps", "درخواست کے مراحل"),
            body = LocalizedText(
                "Follow these steps to complete your SECCAP application. Use this app to prepare all details before entering them on the official portal at seccap.dgcs.gos.pk.",
                "اپنی SECCAP درخواست مکمل کرنے کے لیے یہ مراحل اپنائیں۔ سرکاری پورٹل seccap.dgcs.gos.pk پر درج کرنے سے پہلے اس ایپ میں تمام تفصیلات تیار کریں۔"
            ),
            steps = listOf(
                LocalizedText("Step 1: Enter educational details — Matric roll number, 9th roll number, board, marks, and school name.", "مرحلہ 1: تعلیمی تفصیلات — میٹرک رول نمبر، 9ویں کا رول نمبر، بورڈ، نمبر اور سکول کا نام۔"),
                LocalizedText("Step 2: Enter personal details — full name, father's name, B-Form, date of birth, phone, and domicile.", "مرحلہ 2: ذاتی تفصیلات — پورا نام، والد کا نام، B-Form، تاریخ پیدائش، فون اور ڈومیسائل۔"),
                LocalizedText("Step 3: Select faculty group — Pre-Medical, Pre-Engineering, Commerce, etc. based on your marks.", "مرحلہ 3: گروپ منتخب کریں — پری میڈیکل، پری انجینئرنگ، کامرس وغیرہ اپنے نمبروں کے مطابق۔"),
                LocalizedText("Step 4: Choose zone and up to 5 college preferences in order of priority.", "مرحلہ 4: زون اور ترجیحی ترتیب میں زیادہ سے زیادہ 5 کالج منتخب کریں۔"),
                LocalizedText("Step 5: Prepare required documents — marksheet, B-Form, photos, and character certificate.", "مرحلہ 5: ضروری دستاویزات تیار کریں — مارک شیٹ، B-Form، تصاویر اور کریکٹر سرٹیفکیٹ۔"),
                LocalizedText("Step 6: Review all details and export PDF summary for your records.", "مرحلہ 6: تمام تفصیلات کا جائزہ لیں اور اپنے ریکارڈ کے لیے PDF خلاصہ برآمد کریں۔")
            )
        ),
        GuideSection(
            id = "documents",
            title = LocalizedText("Required Documents", "ضروری دستاویزات"),
            body = LocalizedText(
                "Keep scanned copies or clear photos of all documents ready before applying on the official portal.",
                "سرکاری پورٹل پر درخواست دینے سے پہلے تمام دستاویزات کی اسکین یا واضح تصاویر تیار رکھیں۔"
            ),
            steps = emptyList()
        ),
        GuideSection(
            id = "tips",
            title = LocalizedText("Important Tips", "اہم تجاویز"),
            body = LocalizedText(
                "Double-check your roll numbers and marks before submission. Choose colleges within your zone and marks range. Keep your phone number active for SMS updates from SECCAP.",
                "جمع کرانے سے پہلے رول نمبر اور نمبر دوبارہ چیک کریں۔ اپنے زون اور نمبروں کی حد میں کالج منتخب کریں۔ SECCAP کی SMS اپڈیٹس کے لیے فون نمبر فعال رکھیں۔"
            ),
            steps = listOf(
                LocalizedText("Apply early — don't wait for the last day", "جلد درخواست دیں — آخری دن کا انتظار نہ کریں"),
                LocalizedText("Save your PDF summary and confirmation slip", "اپنا PDF خلاصہ اور تصدیقی سلپ محفوظ کریں"),
                LocalizedText("Visit the official portal for final submission", "حتمی جمع کرانے کے لیے سرکاری پورٹل پر جائیں"),
                LocalizedText("Contact your school for character certificate", "کریکٹر سرٹیفکیٹ کے لیے اپنے سکول سے رابطہ کریں")
            )
        )
    )

    fun getRequiredDocuments(): List<RequiredDocument> = listOf(
        RequiredDocument(
            "marksheet",
            LocalizedText("Matric Mark Sheet", "میٹرک مارک شیٹ"),
            LocalizedText("Original or attested copy of Matric result", "میٹرک نتیجے کی اصل یا تصدیق شدہ کاپی")
        ),
        RequiredDocument(
            "bform",
            LocalizedText("B-Form / CNIC", "B-Form / CNIC"),
            LocalizedText("Computerized B-Form or CNIC of the student", "طالب علم کا کمپیوٹرائزڈ B-Form یا CNIC")
        ),
        RequiredDocument(
            "photo",
            LocalizedText("Passport-size Photographs", "پاسپورٹ سائز تصاویر"),
            LocalizedText("Recent color photos with blue/white background", "نیلی/سفید پس منظر کے ساتھ حالیہ رنگین تصاویر")
        ),
        RequiredDocument(
            "character",
            LocalizedText("Character Certificate", "کریکٹر سرٹیفکیٹ"),
            LocalizedText("Issued by your school head/principal", "آپ کے سکول کے سربراہ/پرنسپل کی طرف سے جاری")
        ),
        RequiredDocument(
            "domicile",
            LocalizedText("Domicile Certificate", "ڈومیسائل سرٹیفکیٹ"),
            LocalizedText("Sindh domicile from competent authority", "مجاز اتھارٹی سے سندھ کا ڈومیسائل")
        ),
        RequiredDocument(
            "father_cnic",
            LocalizedText("Father's CNIC Copy", "والد کے CNIC کی کاپی"),
            LocalizedText("Copy of father's computerized CNIC", "والد کے کمپیوٹرائزڈ CNIC کی کاپی")
        )
    )
}
