package com.seccap.admissions.util

import android.content.Context
import com.seccap.admissions.R
import com.seccap.admissions.data.ApplicationDraft
import com.seccap.admissions.data.CollegeRepository
import com.seccap.admissions.data.FacultyRepository
import com.seccap.admissions.data.GuideRepository

object NarrationBuilder {

    fun welcome(@Suppress("UNUSED_PARAMETER") context: Context, language: String): String {
        return if (language == LocaleHelper.LANG_UR) {
            "SECCAP ایڈمیشنز میں خوش آمدید۔ یہ ایپ آپ کو سندھ کے سرکاری کالجوں میں داخلے کی درخواست تیار کرنے میں مدد کرتی ہے۔ " +
                "نئی درخواست شروع کریں، یا اپنی محفوظ شدہ درخواست جاری رکھیں۔"
        } else {
            "Welcome to SECCAP Admissions. This app helps you prepare your application for government college admissions in Sindh. " +
                "Start a new application or continue your saved draft."
        }
    }

    fun stepEducational(language: String): String {
        return if (language == LocaleHelper.LANG_UR) {
            "تعلیمی تفصیلات۔ اپنا میٹرک رول نمبر، نویں جماعت کا رول نمبر، بورڈ کا نام، " +
                "کل اور حاصل شدہ نمبر، اور سکول کا نام درج کریں۔"
        } else {
            "Educational details. Enter your Matric roll number, 9th class roll number, board name, " +
                "total and obtained marks, and school name."
        }
    }

    fun stepPersonal(language: String): String {
        return if (language == LocaleHelper.LANG_UR) {
            "ذاتی تفصیلات۔ اپنا پورا نام، والد کا نام، جنس، تاریخ پیدائش، B-Form نمبر، " +
                "فون نمبر، اور ڈومیسائل درج کریں۔"
        } else {
            "Personal details. Enter your full name, father's name, gender, date of birth, B-Form number, " +
                "phone number, and domicile."
        }
    }

    fun stepFaculty(language: String, draft: ApplicationDraft): String {
        val pct = String.format("%.1f", draft.percentage)
        return if (language == LocaleHelper.LANG_UR) {
            "گروپ کا انتخاب۔ آپ کے نمبر $pct فیصد ہیں۔ " +
                "اپنے نمبروں کے مطابق مناسب گروپ منتخب کریں جیسے پری میڈیکل، پری انجینئرنگ، یا کامرس۔"
        } else {
            "Faculty selection. Your marks are $pct percent. " +
                "Choose the appropriate faculty group based on your marks, such as Pre-Medical, Pre-Engineering, or Commerce."
        }
    }

    fun stepColleges(language: String): String {
        return if (language == LocaleHelper.LANG_UR) {
            "زون اور کالج کا انتخاب۔ پہلے اپنا زون منتخب کریں، پھر ترجیحی ترتیب میں زیادہ سے زیادہ پانچ کالج منتخب کریں۔"
        } else {
            "Zone and college selection. First select your zone, then choose up to five colleges in order of preference."
        }
    }

    fun stepDocuments(language: String): String {
        return if (language == LocaleHelper.LANG_UR) {
            "دستاویزات کی فہرست۔ اپنی مارک شیٹ، B-Form، تصاویر، کریکٹر سرٹیفکیٹ، اور ڈومیسائل تیار رکھیں۔ " +
                "تیار ہونے پر ہر دستاویز کو نشان زد کریں۔"
        } else {
            "Document checklist. Keep your mark sheet, B-Form, photographs, character certificate, and domicile ready. " +
                "Check off each document as you prepare it."
        }
    }

    fun stepReview(@Suppress("UNUSED_PARAMETER") context: Context, language: String, draft: ApplicationDraft): String {
        val faculty = FacultyRepository.findById(draft.facultyId)?.name?.get(language) ?: ""
        val zone = CollegeRepository.findZone(draft.zoneId)?.name?.get(language) ?: ""
        return if (language == LocaleHelper.LANG_UR) {
            "جائزہ۔ درخواست کی تفصیلات کا جائزہ لیں۔ طالب علم: ${draft.studentName}۔ " +
                "گروپ: $faculty۔ زون: $zone۔ کالج کی ترجیحات: ${draft.collegePreferences.size}۔ " +
                "مکمل ہونے پر PDF برآمد کریں۔"
        } else {
            "Review. Check your application details. Student: ${draft.studentName}. " +
                "Faculty: $faculty. Zone: $zone. College preferences: ${draft.collegePreferences.size}. " +
                "Export PDF when complete."
        }
    }

    fun fullGuide(language: String): String {
        val sections = GuideRepository.getSections()
        val sb = StringBuilder()
        if (language == LocaleHelper.LANG_UR) {
            sb.append("SECCAP داخلے کی مکمل رہنمائی۔\n")
        } else {
            sb.append("Complete SECCAP admission guide.\n")
        }
        for (section in sections) {
            sb.append(section.title.get(language)).append(". ")
            sb.append(section.body.get(language)).append(" ")
            for (step in section.steps) {
                sb.append(step.get(language)).append(". ")
            }
        }
        return sb.toString()
    }

    fun guideSection(language: String, sectionId: String): String {
        val section = GuideRepository.getSections().find { it.id == sectionId } ?: return ""
        val sb = StringBuilder()
        sb.append(section.title.get(language)).append(". ")
        sb.append(section.body.get(language))
        for (step in section.steps) {
            sb.append(" ").append(step.get(language))
        }
        return sb.toString()
    }
}
