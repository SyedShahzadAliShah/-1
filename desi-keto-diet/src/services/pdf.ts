import jsPDF from 'jspdf';
import { Filesystem, Directory } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';
import { Capacitor } from '@capacitor/core';
import type { Recipe, AilmentGuide, FitnessRoutine, Language, LocalizedText } from '../types';

function getText(text: LocalizedText | string, lang: Language): string {
  if (typeof text === 'string') return text;
  return text[lang];
}

function addWrappedText(doc: jsPDF, text: string, x: number, y: number, maxWidth: number, lineHeight: number): number {
  const lines = doc.splitTextToSize(text, maxWidth);
  doc.text(lines, x, y);
  return y + lines.length * lineHeight;
}

export async function exportRecipePdf(recipe: Recipe, lang: Language): Promise<boolean> {
  const doc = new jsPDF();
  const margin = 20;
  const maxWidth = 170;
  let y = 20;

  doc.setFontSize(18);
  doc.text(getText(recipe.title, lang), margin, y);
  y += 12;

  doc.setFontSize(10);
  doc.setTextColor(100);
  doc.text(`Desi Keto Diet | ${lang === 'ur' ? 'دیسی کیٹو ڈائٹ' : 'Heal Through Food'}`, margin, y);
  y += 10;
  doc.setTextColor(0);

  doc.setFontSize(11);
  y = addWrappedText(doc, getText(recipe.description, lang), margin, y, maxWidth, 6);
  y += 8;

  const macroLabel = lang === 'ur' ? 'غذائی اجزاء' : 'Nutrition';
  doc.setFontSize(12);
  doc.text(`${macroLabel}:`, margin, y);
  y += 7;
  doc.setFontSize(10);
  doc.text(
    `${lang === 'ur' ? 'کیلوریز' : 'Calories'}: ${recipe.macros.calories} | ` +
    `${lang === 'ur' ? 'پروٹین' : 'Protein'}: ${recipe.macros.protein}g | ` +
    `${lang === 'ur' ? 'چکنائی' : 'Fat'}: ${recipe.macros.fat}g | ` +
    `${lang === 'ur' ? 'کاربس' : 'Carbs'}: ${recipe.macros.carbs}g`,
    margin, y
  );
  y += 12;

  const ingLabel = lang === 'ur' ? 'اجزاء' : 'Ingredients';
  doc.setFontSize(12);
  doc.text(`${ingLabel}:`, margin, y);
  y += 7;
  doc.setFontSize(10);
  recipe.ingredients.forEach((ing) => {
    y = addWrappedText(doc, `• ${getText(ing, lang)}`, margin, y, maxWidth, 5);
    y += 2;
  });
  y += 5;

  const stepsLabel = lang === 'ur' ? 'طریقہ' : 'Instructions';
  doc.setFontSize(12);
  doc.text(`${stepsLabel}:`, margin, y);
  y += 7;
  doc.setFontSize(10);
  recipe.instructions.forEach((step, i) => {
    if (y > 270) { doc.addPage(); y = 20; }
    y = addWrappedText(doc, `${i + 1}. ${getText(step, lang)}`, margin, y, maxWidth, 5);
    y += 3;
  });
  y += 5;

  if (y > 250) { doc.addPage(); y = 20; }
  const healLabel = lang === 'ur' ? 'شفا یابی نوٹس' : 'Healing Notes';
  doc.setFontSize(12);
  doc.text(`${healLabel}:`, margin, y);
  y += 7;
  doc.setFontSize(10);
  addWrappedText(doc, getText(recipe.healingNotes, lang), margin, y, maxWidth, 5);

  return savePdf(doc, `desi-keto-${recipe.id}.pdf`);
}

export async function exportHealthGuidePdf(guide: AilmentGuide, lang: Language): Promise<boolean> {
  const doc = new jsPDF();
  const margin = 20;
  const maxWidth = 170;
  let y = 20;

  doc.setFontSize(18);
  doc.text(getText(guide.title, lang), margin, y);
  y += 15;

  doc.setFontSize(10);
  y = addWrappedText(doc, getText(guide.summary, lang), margin, y, maxWidth, 6);
  y += 10;

  const sections = [
    { label: lang === 'ur' ? 'کیٹو طریقہ' : 'Keto Approach', text: guide.ketoApproach },
    { label: lang === 'ur' ? 'دوائیوں کے قدرتی متبادل' : 'Natural Alternatives', text: guide.medicationAlternatives },
  ];

  for (const section of sections) {
    if (y > 250) { doc.addPage(); y = 20; }
    doc.setFontSize(12);
    doc.text(`${section.label}:`, margin, y);
    y += 7;
    doc.setFontSize(10);
    y = addWrappedText(doc, getText(section.text, lang), margin, y, maxWidth, 5);
    y += 10;
  }

  const listSections = [
    { label: lang === 'ur' ? 'کھانے والے' : 'Foods to Eat', items: guide.foodsToEat },
    { label: lang === 'ur' ? 'بچنے والے' : 'Foods to Avoid', items: guide.foodsToAvoid },
    { label: lang === 'ur' ? 'طرز زندگی' : 'Lifestyle Tips', items: guide.lifestyleTips },
  ];

  for (const section of listSections) {
    if (y > 240) { doc.addPage(); y = 20; }
    doc.setFontSize(12);
    doc.text(`${section.label}:`, margin, y);
    y += 7;
    doc.setFontSize(10);
    section.items.forEach((item) => {
      if (y > 270) { doc.addPage(); y = 20; }
      y = addWrappedText(doc, `• ${getText(item, lang)}`, margin, y, maxWidth, 5);
      y += 2;
    });
    y += 5;
  }

  return savePdf(doc, `desi-keto-health-${guide.id}.pdf`);
}

export async function exportFitnessPdf(routine: FitnessRoutine, lang: Language): Promise<boolean> {
  const doc = new jsPDF();
  const margin = 20;
  const maxWidth = 170;
  let y = 20;

  doc.setFontSize(18);
  doc.text(getText(routine.title, lang), margin, y);
  y += 12;

  doc.setFontSize(10);
  y = addWrappedText(doc, getText(routine.description, lang), margin, y, maxWidth, 6);
  y += 10;

  const stepsLabel = lang === 'ur' ? 'اقدامات' : 'Steps';
  doc.setFontSize(12);
  doc.text(`${stepsLabel}:`, margin, y);
  y += 7;
  doc.setFontSize(10);
  routine.steps.forEach((step, i) => {
    y = addWrappedText(doc, `${i + 1}. ${getText(step, lang)}`, margin, y, maxWidth, 5);
    y += 3;
  });

  return savePdf(doc, `desi-keto-fitness-${routine.id}.pdf`);
}

async function savePdf(doc: jsPDF, filename: string): Promise<boolean> {
  try {
    const pdfBase64 = doc.output('datauristring').split(',')[1];

    if (Capacitor.isNativePlatform()) {
      const result = await Filesystem.writeFile({
        path: filename,
        data: pdfBase64,
        directory: Directory.Cache,
      });
      await Share.share({
        title: 'Desi Keto Diet PDF',
        url: result.uri,
      });
    } else {
      doc.save(filename);
    }
    return true;
  } catch {
    doc.save(filename);
    return true;
  }
}
