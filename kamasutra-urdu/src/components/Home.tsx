import { useState } from 'react';
import { postures, categories } from '../data/postures';
import { PostureCard } from './PostureCard';
import { PostureDetail } from './PostureDetail';
import { exportAllPosturesPdf } from '../services/pdfExport';
import { getPostureSvgString, svgStringToElement } from '../data/svgStrings';

export function Home() {
  const [selectedId, setSelectedId] = useState<string | null>(null);
  const [activeCategory, setActiveCategory] = useState<string>('all');
  const [exporting, setExporting] = useState(false);

  const selected = postures.find((p) => p.id === selectedId);
  const filtered =
    activeCategory === 'all' ? postures : postures.filter((p) => p.category === activeCategory);

  const handleExportAll = async () => {
    setExporting(true);
    try {
      const getSvgForPosture = (id: string): SVGSVGElement | null => {
        const posture = postures.find((p) => p.id === id);
        if (!posture) return null;
        return svgStringToElement(getPostureSvgString(posture.illustration));
      };
      await exportAllPosturesPdf(postures, getSvgForPosture);
    } finally {
      setExporting(false);
    }
  };

  if (selected) {
    return <PostureDetail posture={selected} onBack={() => setSelectedId(null)} />;
  }

  return (
    <div className="home">
      <header className="app-header">
        <div>
          <h1>قربت کی تعلیم</h1>
          <p className="header-sub">عملی جوڑوں کے لیے — اردو میں</p>
        </div>
        <button className="btn-export-all" onClick={handleExportAll} disabled={exporting} type="button">
          {exporting ? 'برآمد...' : '📄 تمام PDF'}
        </button>
      </header>

      <div className="disclaimer">
        <p>
          قدیم کامسutra سے متاثر تعلیمی وضعیں — باہمی احترام، رضامندی اور حفاظت کے ساتھ عملی رہنمائی
        </p>
      </div>

      <div className="category-filter">
        <button
          className={`filter-btn ${activeCategory === 'all' ? 'active' : ''}`}
          onClick={() => setActiveCategory('all')}
          type="button"
        >
          تمام
        </button>
        {categories.map((cat) => (
          <button
            key={cat.id}
            className={`filter-btn ${activeCategory === cat.id ? 'active' : ''}`}
            onClick={() => setActiveCategory(cat.id)}
            type="button"
          >
            {cat.nameUrdu}
          </button>
        ))}
      </div>

      <div className="posture-grid">
        {filtered.map((posture) => (
          <PostureCard key={posture.id} posture={posture} onClick={() => setSelectedId(posture.id)} />
        ))}
      </div>

      <footer className="app-footer">
        <p>یہ مواد صرف تعلیمی مقاصد کے لیے ہے | 18+</p>
      </footer>
    </div>
  );
}
