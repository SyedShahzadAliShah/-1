import { useState, useEffect } from 'react';
import { AgeGate } from './components/AgeGate';
import { Home } from './components/Home';
import './App.css';

const AGE_KEY = 'qurbat_age_verified';

function App() {
  const [verified, setVerified] = useState(false);

  useEffect(() => {
    const stored = localStorage.getItem(AGE_KEY);
    if (stored === 'true') setVerified(true);
  }, []);

  const handleConfirm = () => {
    localStorage.setItem(AGE_KEY, 'true');
    setVerified(true);
  };

  if (!verified) {
    return <AgeGate onConfirm={handleConfirm} />;
  }

  return <Home />;
}

export default App;
