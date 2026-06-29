import { useState } from 'react';

interface AgeGateProps {
  onConfirm: () => void;
}

export function AgeGate({ onConfirm }: AgeGateProps) {
  const [checked, setChecked] = useState(false);

  return (
    <div className="age-gate">
      <div className="age-gate-card">
        <div className="age-gate-icon">🔞</div>
        <h1>قربت کی تعلیم</h1>
        <p className="subtitle">Intimacy Education for Couples</p>
        <div className="age-notice">
          <p>
            یہ ایپ صرف بالغ جوڑوں (۱۸ سال سے زیادہ) کے لیے تعلیمی مواد فراہم کرتی ہے۔ اس میں قدیم
            کامسutra سے متاثر عملی وضعوں کی رہنمائی، اردو میں وضاحت، آواز (TTS) اور PDF برآمد کی
            سہولت شامل ہے۔
          </p>
          <p>
            یہ مواد صحت مند اور محفوظ قربت کی تعلیم کے لیے ہے۔ باہمی رضامندی اور احترام لازمی ہے۔
          </p>
        </div>
        <label className="age-checkbox">
          <input
            type="checkbox"
            checked={checked}
            onChange={(e) => setChecked(e.target.checked)}
          />
          <span>میں ۱۸ سال یا اس سے زیادہ عمر کا/کی ہوں اور یہ مواد دیکھنے کی رضامندی دیتا/دیتی ہوں</span>
        </label>
        <button className="btn-primary" disabled={!checked} onClick={onConfirm}>
          ایپ میں داخل ہوں
        </button>
      </div>
    </div>
  );
}
