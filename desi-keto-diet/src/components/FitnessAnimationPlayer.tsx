import { useState, useEffect, useCallback, useRef } from 'react';
import { useTranslation } from 'react-i18next';
import type { FitnessRoutine } from '../types';
import { getStepAnimations } from '../data/fitnessAnimations';
import { useLang } from '../hooks/useLang';
import ExerciseFigure from './ExerciseFigure';
import './FitnessAnimationPlayer.css';

interface Props {
  routine: FitnessRoutine;
}

export default function FitnessAnimationPlayer({ routine }: Props) {
  const { t } = useTranslation();
  const lang = useLang();
  const stepMeta = getStepAnimations(routine.id, routine.steps.length);
  const [currentStep, setCurrentStep] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [timeLeft, setTimeLeft] = useState(stepMeta[0].durationSec);
  const stepMetaRef = useRef(stepMeta);
  stepMetaRef.current = stepMeta;

  const totalSteps = routine.steps.length;
  const meta = stepMeta[currentStep];
  const elapsed = meta.durationSec - timeLeft;
  const progress = Math.min(100, Math.max(0, (elapsed / meta.durationSec) * 100));

  const goToStep = useCallback((index: number) => {
    const clamped = Math.max(0, Math.min(index, totalSteps - 1));
    setCurrentStep(clamped);
    setTimeLeft(stepMetaRef.current[clamped].durationSec);
  }, [totalSteps]);

  const nextStep = useCallback(() => {
    goToStep(currentStep + 1);
  }, [currentStep, goToStep]);

  const prevStep = useCallback(() => {
    goToStep(currentStep - 1);
  }, [currentStep, goToStep]);

  // Countdown tick
  useEffect(() => {
    if (!playing) return;
    const id = setInterval(() => setTimeLeft((prev) => prev - 1), 1000);
    return () => clearInterval(id);
  }, [playing]);

  // Advance when timer hits zero
  useEffect(() => {
    if (!playing || timeLeft > 0) return;
    if (currentStep < totalSteps - 1) {
      goToStep(currentStep + 1);
    } else {
      setPlaying(false);
    }
  }, [playing, timeLeft, currentStep, totalSteps, goToStep]);

  const togglePlay = () => {
    if (playing) {
      setPlaying(false);
    } else {
      if (timeLeft <= 0) goToStep(currentStep);
      setPlaying(true);
    }
  };

  const restart = () => {
    setPlaying(false);
    goToStep(0);
  };

  return (
    <div className="fitness-player">
      <div className="player-header">
        <h3>{t('fitness.animatedRoutine')}</h3>
        <span className="step-counter">
          {t('fitness.stepOf', { current: currentStep + 1, total: totalSteps })}
        </span>
      </div>

      <ExerciseFigure key={`${routine.id}-${currentStep}-${meta.animation}`} animation={meta.animation} />

      <p className="human-figure-caption">{t('fitness.humanDemo')}</p>

      <div className="timer-bar">
        <div className="timer-fill" style={{ width: `${playing ? progress : 0}%` }} />
      </div>

      <div className="timer-display">
        <span className="timer-seconds">{Math.max(0, timeLeft)}s</span>
        <span className="timer-label">
          {playing ? t('fitness.keepGoing') : t('fitness.ready')}
        </span>
      </div>

      <div className="current-step-card">
        <span className="step-number">{currentStep + 1}</span>
        <p>{routine.steps[currentStep][lang]}</p>
      </div>

      <div className="player-controls">
        <button className="player-btn" onClick={prevStep} disabled={currentStep === 0} aria-label={t('fitness.prevStep')}>
          ⏮
        </button>
        <button className="player-btn player-btn-main" onClick={togglePlay} aria-label={playing ? t('fitness.pause') : t('fitness.play')}>
          {playing ? '⏸' : '▶️'}
        </button>
        <button className="player-btn" onClick={nextStep} disabled={currentStep === totalSteps - 1} aria-label={t('fitness.nextStep')}>
          ⏭
        </button>
        <button className="player-btn" onClick={restart} aria-label={t('fitness.restart')}>
          🔄
        </button>
      </div>

      <div className="step-dots">
        {routine.steps.map((_, i) => (
          <button
            key={i}
            className={`step-dot ${i === currentStep ? 'active' : ''} ${i < currentStep ? 'done' : ''}`}
            onClick={() => { setPlaying(false); goToStep(i); }}
            aria-label={`${t('fitness.stepOf', { current: i + 1, total: totalSteps })}`}
          />
        ))}
      </div>
    </div>
  );
}
