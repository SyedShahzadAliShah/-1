import { Capacitor } from '@capacitor/core';
import { Directory, Filesystem } from '@capacitor/filesystem';
import { Share } from '@capacitor/share';
import type { jsPDF } from 'jspdf';

function arrayBufferToBase64(buffer: ArrayBuffer): string {
  const bytes = new Uint8Array(buffer);
  let binary = '';
  const chunk = 0x8000;
  for (let i = 0; i < bytes.length; i += chunk) {
    binary += String.fromCharCode(...bytes.subarray(i, i + chunk));
  }
  return btoa(binary);
}

function downloadBlobWeb(blob: Blob, filename: string): void {
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = filename;
  anchor.style.display = 'none';
  document.body.appendChild(anchor);
  anchor.click();
  document.body.removeChild(anchor);
  setTimeout(() => URL.revokeObjectURL(url), 1000);
}

export async function savePdfDocument(doc: jsPDF, filename: string): Promise<void> {
  const safeName = filename.endsWith('.pdf') ? filename : `${filename}.pdf`;

  if (Capacitor.isNativePlatform()) {
    const pdfOutput = doc.output('arraybuffer');
    const base64 = arrayBufferToBase64(pdfOutput);

    await Filesystem.writeFile({
      path: safeName,
      data: base64,
      directory: Directory.Cache,
      recursive: true,
    });

    const { uri } = await Filesystem.getUri({
      path: safeName,
      directory: Directory.Cache,
    });

    await Share.share({
      title: safeName,
      url: uri,
      dialogTitle: 'PDF محفوظ کریں یا شیئر کریں',
    });
    return;
  }

  const blob = doc.output('blob');
  downloadBlobWeb(blob, safeName);
}
