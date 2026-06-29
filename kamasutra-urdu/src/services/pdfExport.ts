import jsPDF from 'jspdf';
import type { Posture } from '../data/postures';

function renderSvgToCanvas(svgElement: SVGSVGElement, width: number, height: number): Promise<string> {
  return new Promise((resolve, reject) => {
    const svgData = new XMLSerializer().serializeToString(svgElement);
    const svgBlob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
    const url = URL.createObjectURL(svgBlob);
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
      URL.revokeObjectURL(url);
      resolve(canvas.toDataURL('image/png'));
    };
    img.onerror = () => {
      URL.revokeObjectURL(url);
      reject(new Error('SVG render failed'));
    };
    img.src = url;
  });
}

function wrapText(doc: jsPDF, text: string, x: number, y: number, maxWidth: number, lineHeight: number): number {
  const lines = doc.splitTextToSize(text, maxWidth);
  doc.text(lines, x, y, { align: 'right' });
  return y + lines.length * lineHeight;
}

export async function exportPosturePdf(posture: Posture, svgElement: SVGSVGElement | null): Promise<void> {
  const doc = new jsPDF({ orientation: 'portrait', unit: 'mm', format: 'a4' });
  const pageWidth = doc.internal.pageSize.getWidth();
  const margin = 20;
  const contentWidth = pageWidth - margin * 2;
  let y = 25;

  doc.setFillColor(107, 45, 60);
  doc.rect(0, 0, pageWidth, 40, 'F');
  doc.setTextColor(255, 255, 255);
  doc.setFontSize(18);
  doc.text('قربت کی تعلیم — عملی رہنمائی', pageWidth - margin, 18, { align: 'right' });
  doc.setFontSize(10);
  doc.text('18+ Educational Material for Couples', pageWidth - margin, 28, { align: 'right' });

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

  if (svgElement) {
    try {
      const imgData = await renderSvgToCanvas(svgElement, 400, 240);
      doc.addImage(imgData, 'PNG', margin + 20, y, contentWidth - 40, 50);
      y += 58;
    } catch {
      y += 5;
    }
  }

  doc.setTextColor(40, 20, 30);
  doc.setFontSize(12);
  doc.text('تفصیل', pageWidth - margin, y, { align: 'right' });
  y += 7;
  doc.setFontSize(10);
  y = wrapText(doc, posture.description, pageWidth - margin, y, contentWidth, 5);

  y += 8;
  doc.setFontSize(12);
  doc.text('فوائد', pageWidth - margin, y, { align: 'right' });
  y += 7;
  doc.setFontSize(10);
  y = wrapText(doc, posture.benefits, pageWidth - margin, y, contentWidth, 5);

  y += 8;
  if (y > 240) {
    doc.addPage();
    y = 25;
  }
  doc.setFontSize(12);
  doc.text('عملی مشورے', pageWidth - margin, y, { align: 'right' });
  y += 7;
  doc.setFontSize(10);
  wrapText(doc, posture.tips, pageWidth - margin, y, contentWidth, 5);

  const footerY = doc.internal.pageSize.getHeight() - 15;
  doc.setFontSize(8);
  doc.setTextColor(150, 120, 130);
  doc.text(
    'یہ مواد صرف تعلیمی مقاصد کے لیے ہے۔ باہمی رضامندی، احترام اور حفاظت اولین ترجیح ہونی چاہیے۔',
    pageWidth / 2,
    footerY,
    { align: 'center' }
  );

  const filename = `qurbat-${posture.id}.pdf`;
  doc.save(filename);
}

export async function exportAllPosturesPdf(
  postures: Posture[],
  getSvgForPosture: (id: string) => SVGSVGElement | null
): Promise<void> {
  const doc = new jsPDF({ orientation: 'portrait', unit: 'mm', format: 'a4' });
  const pageWidth = doc.internal.pageSize.getWidth();
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
    if (svg) {
      try {
        const imgData = await renderSvgToCanvas(svg, 400, 240);
        doc.addImage(imgData, 'PNG', margin + 30, y, contentWidth - 60, 40);
        y += 48;
      } catch {
        /* skip illustration */
      }
    }

    doc.setTextColor(40, 20, 30);
    doc.setFontSize(10);
    y = wrapText(doc, posture.description, pageWidth - margin, y, contentWidth, 4.5);

    if (y > 250) {
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

  doc.save('qurbat-ki-taleem-complete.pdf');
}
