import type { ExerciseAnimation } from '../types';
import { getRoutinePreviewAnimation } from '../data/fitnessAnimations';
import ExerciseFigure from './ExerciseFigure';
import './FitnessFigureEmbed.css';

interface Props {
  routineId: string;
  animation?: ExerciseAnimation;
  label?: string;
}

/** Compact embedded human figure preview for fitness cards */
export default function FitnessFigureEmbed({ routineId, animation, label }: Props) {
  const preview = animation ?? getRoutinePreviewAnimation(routineId);

  return (
    <div className="fitness-figure-embed" aria-hidden="true">
      <ExerciseFigure animation={preview} compact />
      {label && <span className="fitness-figure-label">{label}</span>}
    </div>
  );
}
