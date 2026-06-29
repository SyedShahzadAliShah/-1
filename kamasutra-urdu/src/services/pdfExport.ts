import jsPDF from 'jspdf';
import type { Posture } from '../data/postures';
import { getAssetUrl } from '../utils/assets';
import { savePdfDocument } from './pdfSave';
import { getPostureSvgString } from '../data/svgStrings';

let fontLoaded = false;

function arrayBufferToBase64(buffer: ArrayBuffer): string {
  const bytes = new Uint8Array(buffer);
  let binary = '';
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) {
    binary += String.fromCharCode(...bytes.subarray(i, i + chunk));
  }
  return btoa(binary);
}

async function ensureUrduFont(doc: jsPDF): Promise<void> {
  if (fontLoaded) {
    doc.setFont('NotoSansArabic', 'normal');
    return;
  }

  const response = await fetch(getAssetUrl('fonts/NotoSansArabic-Regular.ttf'));
  if (!response.ok) {
    throw new Error('Urdu font load failed');
  }

  const buffer = await response.arrayBuffer();
  const base64 = arrayBufferToBase64(buffer);
  doc.addFileToVFS('NotoSansArabic-Regular.ttf', base64);
  doc.addFont('NotoSansArabic-Regular.ttf', 'NotoSansArabic', 'normal');
  doc.setFont('NotoSansArabic', 'normal');
  fontLoaded = true;
}

function renderSvgToCanvas(svgElement: SVGSVGElement | null, illustration: string, width: number, height: number): Promise<string> {
  return new Promise((resolve, reject) => {
    let svgData: string;
    if (svgElement) {
      svgData = new XMLSerializer().serializeToString(svgElement);
    } else {
      svgData = getPostureSvgString(illustration);
    }

    if (!svgData.includes('xmlns')) {
      svgData = svgData.replace('<svg', '<svg xmlns="http://www.w3.org/2000/svg"');
    }

    const img = new Image();
    img.onload = () => {
      const canvas = document.createElement('canvas');
      canvas.width = width;
      canvas.height = height;
      const ctx = canvas.getContext('2d');
      if (!ctx) {
        reject(new Error('Canvas context unavailable'));
        return;
      }
      ctx.fillStyle = '#faf6f1';
      ctx.fillRect(0, 0, width, height);
      ctx.drawImage(img, 0, 0, width, height);
      resolve(canvas.toDataURL('image/png'));
    };
    img.onerror = () => reject(new Error('SVG render failed'));

    const encoded = btoa(unescape(encodeURIComponent(svgData)));
    img.src = `data:image/svg+xml;base64,${encoded}`;
  });
}

function wrapText(doc: jsPDF, text: string, x: number, y: number, maxWidth: number, lineHeight: number): number {
  const lines = doc.splitTextToSize(text, maxWidth) as string[];
  for (const line of lines) {
    doc.text(line, x, y, { align: 'right' });
    y += lineHeight;
  }
  return y;
}

function addPageHeader(doc: jsPDF, pageWidth: number, margin: number): void {
  doc.setFillColor(107, 45, 60);
  doc.rect(0, 0, pageWidth, 40, 'F');
  doc.setTextColor(255, 255, 255);
  doc.setFontSize(18);
  doc.text('قربت کی تعلیم — عملی رہنمائی', pageWidth - margin, 18, { align: 'right' });
  doc.setFontSize(10);
  doc.text('18+ Educational Material for Couples', pageWidth - margin, 28, { align: 'right' });
}

export async function exportPosturePdf(
  posture: Posture,
  svgElement: SVGSVGElement | null
): Promise<void> {
  const doc = new jsPDF({ orientation: 'portrait', unit: 'mm', format: 'a4' });
  await ensureUrduFont(doc);

  const pageWidth = doc.internal.pageSize.getWidth();
  const pageHeight = doc.internal.pageSize.getHeight();
  const margin = 20;
  const contentWidth = pageWidth - margin * 2;
  let y = 25;

  addPageHeader(doc, pageWidth, margin);

  y = 55;
  doc.setTextColor(60, 30, 40);
  doc.setFontSize(16);
  doc.text(posture.nameUrdu, pageWidth - margin, y, { align: 'right' });
  y += 8;
  doc.setFontSize(10);
  doc.setTextColor(120, 80, 90);
  doc.text(`${posture.nameEnglish} | ${posture.categoryUrdu} | ${posture.difficulty}`, pageWidth - margin, y, {
    align: 'right',
  });
  y += 12;

  try {
    const imgData = await renderSvgToCanvas(svgElement, posture.illustration, 400, 240);
    doc.addImage(imgData, 'PNG', margin + 20, y, contentWidth - 40, 50);
    y += 58;
  } catch {
    y += 5;
  }

  doc.setTextColor(40, 20, 30);
  doc.setFontSize(12);
  doc.text('تفصیل', pageWidth - margin, y, { align: 'right' });
  y += 7;
  doc.setFontSize(10);
  y = wrapText(doc, posture.description, pageWidth - margin, y, contentWidth, 5);

  y += 8;
  if (y > pageHeight - 60) {
    doc.addPage();
    y = 25;
  }
  doc.setFontSize(12);
  doc.text('فوائد', pageWidth - margin, y, { align: 'right' });
  y += 7;
  doc.setFontSize(10);
  y = wrapText(doc, posture.benefits, pageWidth - margin, y, contentWidth, 5);

  y += 8;
  if (y > pageHeight - 50) {
    doc.addPage();
    y = 25;
  }
  doc.setFontSize(12);
  doc.text('عملی مشورے', pageWidth - margin, y, { align: 'right' });
  y += 7;
  doc.setFontSize(10);
  y = wrapText(doc, posture.tips, pageWidth - margin, y, contentWidth, 5);

  y += 8;
  if (y > pageHeight - 40) {
    doc.addPage();
    y = 25;
  }
  doc.setFontSize(9);
  doc.setTextColor(100, 70, 80);
  doc.text('ویڈیو:', pageWidth - margin, y, { align: 'right' });
  y += 5;
  doc.setFontSize(8);
  wrapText(doc, posture.videoCaptionUrdu, pageWidth - margin, y, contentWidth, 4);

  const footerY = pageHeight - 15;
  doc.setFontSize(8);
  doc.setTextColor(150, 120, 130);
  doc.text(
    'یہ مواد صرف تعلیمی مقاصد کے لیے ہے۔ باہمی رضامندی، احترام اور حفاظت اولین ترجیح ہونی چاہیے۔',
    pageWidth / 2,
    footerY,
    { align: 'center' }
  );

  await savePdfDocument(doc, `qurbat-${posture.id}.pdf`);
}

export async function exportAllPosturesPdf(
  postures: Posture[],
  getSvgForPosture: (id: string) => SVGSVGElement | null
): Promise<void> {
  const doc = new jsPDF({ orientation: 'portrait', unit: 'mm', format: 'a4' });
  await ensureUrduFont(doc);

  const pageWidth = doc.internal.pageSize.getWidth();
  const pageHeight = doc.internal.pageSize.getHeight();
  const margin = 20;
  const contentWidth = pageWidth - margin * 2;

  doc.setFillColor(107, 45, 60);
  doc.rect(0, 0, pageWidth, 50, 'F');
  doc.setTextColor(255, 255, 255);
  doc.setFontSize(20);
  doc.text('قربت کی تعلیم', pageWidth - margin, 22, { align: 'right' });
  doc.setFontSize(11);
  doc.text('مکمل رہنمائی — کامسutra سے متاثر عملی وضعیں', pageWidth - margin, 35, { align: 'right' });
  doc.setFontSize(9);
  doc.text(`${postures.length} وضعیں | اردو | 18+`, pageWidth - margin, 44, { align: 'right' });

  for (let i = 0; i < postures.length; i++) {
    const posture = postures[i];
    doc.addPage();
    let y = 25;

    doc.setTextColor(60, 30, 40);
    doc.setFontSize(14);
    doc.text(`${i + 1}. ${posture.nameUrdu}`, pageWidth - margin, y, { align: 'right' });
    y += 7;
    doc.setFontSize(9);
    doc.setTextColor(120, 80, 90);
    doc.text(`${posture.nameEnglish} | ${posture.categoryUrdu}`, pageWidth - margin, y, { align: 'right' });
    y += 10;

    const svg = getSvgForPosture(posture.id);
    try {
      const imgData = await renderSvgToCanvas(svg, posture.illustration, 400, 240);
      doc.addImage(imgData, 'PNG', margin + 30, y, contentWidth - 60, 40);
      y += 48;
    } catch {
      /* skip illustration */
    }

    doc.setTextColor(40, 20, 30);
    doc.setFontSize(10);
    y = wrapText(doc, posture.description, pageWidth - margin, y, contentWidth, 4.5);

    if (y > pageHeight - 40) {
      doc.addPage();
      y = 25;
    }
    y += 5;
    doc.setFontSize(9);
    doc.setTextColor(80, 50, 60);
    doc.text('مشورہ:', pageWidth - margin, y, { align: 'right' });
    y += 5;
    wrapText(doc, posture.tips, pageWidth - margin, y, contentWidth, 4.5);
  }

  await savePdfDocument(doc, 'qurbat-ki-taleem-complete.pdf');
}
