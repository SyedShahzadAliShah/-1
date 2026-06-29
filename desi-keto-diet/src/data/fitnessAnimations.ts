import type { FitnessStepMeta } from '../types';

export const routineStepAnimations: Record<string, FitnessStepMeta[]> = {
  'morning-walk-urdu': [
    { animation: 'breathe', durationSec: 12 },
    { animation: 'walk', durationSec: 20 },
    { animation: 'walk', durationSec: 18 },
    { animation: 'stretch', durationSec: 15 },
  ],
  'pranayama-breathing': [
    { animation: 'breathe', durationSec: 15 },
    { animation: 'breathe', durationSec: 20 },
    { animation: 'breathe', durationSec: 18 },
    { animation: 'breathe', durationSec: 15 },
    { animation: 'rest', durationSec: 20 },
  ],
  'aerobic-dand-baithak': [
    { animation: 'march', durationSec: 12 },
    { animation: 'squat', durationSec: 20 },
    { animation: 'pushup', durationSec: 20 },
    { animation: 'jumping-jack', durationSec: 18 },
    { animation: 'plank', durationSec: 15 },
  ],
  'yoga-pcos': [
    { animation: 'butterfly', durationSec: 20 },
    { animation: 'cobra', durationSec: 18 },
    { animation: 'butterfly', durationSec: 20 },
    { animation: 'twist', durationSec: 18 },
    { animation: 'rest', durationSec: 20 },
  ],
  'hiit-fat-burn': [
    { animation: 'jog', durationSec: 12 },
    { animation: 'burpee', durationSec: 20 },
    { animation: 'mountain-climber', durationSec: 20 },
    { animation: 'high-knee', durationSec: 20 },
    { animation: 'walk', durationSec: 15 },
  ],
  'joint-mobility': [
    { animation: 'neck-roll', durationSec: 15 },
    { animation: 'shoulder-roll', durationSec: 15 },
    { animation: 'knee-lift', durationSec: 15 },
    { animation: 'ankle-circle', durationSec: 15 },
    { animation: 'cat-cow', durationSec: 18 },
  ],
  'strength-keto': [
    { animation: 'goblet-squat', durationSec: 20 },
    { animation: 'row', durationSec: 20 },
    { animation: 'overhead-press', durationSec: 20 },
    { animation: 'deadlift', durationSec: 20 },
    { animation: 'stretch', durationSec: 15 },
  ],
  'pilates-core': [
    { animation: 'hundred', durationSec: 20 },
    { animation: 'roll-up', durationSec: 18 },
    { animation: 'leg-stretch', durationSec: 18 },
    { animation: 'twist', durationSec: 15 },
    { animation: 'child-pose', durationSec: 18 },
  ],
};

export function getStepAnimations(routineId: string, stepCount: number): FitnessStepMeta[] {
  const mapped = routineStepAnimations[routineId];
  if (mapped && mapped.length === stepCount) return mapped;

  const fallbackDuration = 15;
  const defaults: FitnessStepMeta[] = Array.from({ length: stepCount }, () => ({
    animation: 'stretch',
    durationSec: fallbackDuration,
  }));
  return mapped?.length ? mapped : defaults;
}

/** Primary animation shown on fitness list/home card thumbnails */
export function getRoutinePreviewAnimation(routineId: string): FitnessStepMeta['animation'] {
  const steps = routineStepAnimations[routineId];
  if (!steps?.length) return 'stretch';
  const featured = steps.find((s) => s.animation !== 'breathe' && s.animation !== 'rest');
  return featured?.animation ?? steps[0].animation;
}
