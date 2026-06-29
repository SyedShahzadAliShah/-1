import { useRef, useState } from 'react';
import type { Posture } from '../data/postures';
import { PostureIllustration } from './Illustrations';
import { PostureVideo } from './PostureVideo';
import { speakUrdu, stopSpeaking } from '../services/tts';
import { exportPosturePdf } from '../services/pdfExport';

interface PostureDetailProps {
  posture: Posture;
  onBack: () => void;
}

export function PostureDetail({ posture, onBack }: PostureDetailProps) {
  const [speaking, setSpeaking] = useState(false);
  const [exporting, setExporting] = useState(false);
  const svgRef = useRef<HTMLDivElement>(null);

  const fullText = `${posture.nameUrdu}. ${posture.description} فوائد: ${posture.benefits} مشورے: ${posture.tips}`;

  const handleSpeak = async () => {
    if (speaking) {
      await stopSpeaking();
      setSpeaking(false);
      return;
    }
    setSpeaking(true);
    await speakUrdu(fullText);
    setSpeaking(false);
  };

  const handleSpeakSection = async (text: string) => {
    await stopSpeaking();
    setSpeaking(true);
    await speakUrdu(text);
    setSpeaking(false);
  };

  const handleExportPdf = async () => {
    setExporting(true);
    try {
      const svg = svgRef.current?.querySelector('svg') ?? null;
      await exportPosturePdf(posture, svg);
    } finally {
      setExporting(false);
    }
  };

  return (
    <div className="posture-detail">
      <header className="detail-header">
        <button className="btn-back" onClick={onBack} type="button">
          ← واپس
        </button>
        <div className="detail-actions">
          <button className={`btn-icon ${speaking ? 'active' : ''}`} onClick={handleSpeak} type="button" title="مکمل پڑھیں">
            {speaking ? '⏹' : '🔊'}
          </button>
          <button className="btn-icon" onClick={handleExportPdf} disabled={exporting} type="button" title="PDF برآمد">
            {exporting ? '⏳' : '📄'}
          </button>
        </div>
      </header>

      <PostureVideo
        src={posture.videoUrl}
        title={`${posture.nameUrdu} — عملی ویڈیو`}
        captionUrdu={posture.videoCaptionUrdu}
      />

      <div className="detail-illustration detail-illustration-static" ref={svgRef}>
        <PostureIllustration type={posture.illustration} />
      </div>

      <div className="detail-content">
        <h1>{posture.nameUrdu}</h1>
        <p className="detail-en">{posture.nameEnglish}</p>
        <div className="detail-meta">
          <span className="badge category">{posture.categoryUrdu}</span>
          <span className={`badge difficulty ${posture.difficulty === 'آسان' ? 'easy' : posture.difficulty === 'درمیانہ' ? 'medium' : 'hard'}`}>
            {posture.difficulty}
          </span>
        </div>

        <section className="detail-section">
          <div className="section-header">
            <h2>تفصیل</h2>
            <button className="btn-speak-small" onClick={() => handleSpeakSection(posture.description)} type="button">
              🔊
            </button>
          </div>
          <p>{posture.description}</p>
        </section>

        <section className="detail-section">
          <div className="section-header">
            <h2>فوائد</h2>
            <button className="btn-speak-small" onClick={() => handleSpeakSection(posture.benefits)} type="button">
              🔊
            </button>
          </div>
          <p>{posture.benefits}</p>
        </section>

        <section className="detail-section">
          <div className="section-header">
            <h2>عملی مشورے</h2>
            <button className="btn-speak-small" onClick={() => handleSpeakSection(posture.tips)} type="button">
              🔊
            </button>
          </div>
          <p>{posture.tips}</p>
        </section>
      </div>
    </div>
  );
}
