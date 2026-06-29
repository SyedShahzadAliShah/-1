export type Language = 'en' | 'ur';

export type AilmentCategory =
  | 'gastric'
  | 'gyne'
  | 'psyche'
  | 'cardiac'
  | 'diabetic'
  | 'thyroid'
  | 'joint'
  | 'liver'
  | 'kidney';

export type CuisineType =
  | 'pakistani'
  | 'bbq'
  | 'chinese'
  | 'continental'
  | 'mughlai'
  | 'punjabi'
  | 'sindhi'
  | 'balochi';

export type FitnessType =
  | 'aerobic'
  | 'yoga'
  | 'hiit'
  | 'walking'
  | 'strength'
  | 'stretching'
  | 'pilates';

export interface LocalizedText {
  en: string;
  ur: string;
}

export interface Recipe {
  id: string;
  title: LocalizedText;
  cuisine: CuisineType;
  ailments: AilmentCategory[];
  description: LocalizedText;
  ingredients: LocalizedText[];
  instructions: LocalizedText[];
  macros: { calories: number; protein: number; fat: number; carbs: number; fiber: number };
  prepTime: number;
  cookTime: number;
  servings: number;
  healingNotes: LocalizedText;
  tags: string[];
}

export interface AilmentGuide {
  id: AilmentCategory;
  title: LocalizedText;
  summary: LocalizedText;
  ketoApproach: LocalizedText;
  foodsToEat: LocalizedText[];
  foodsToAvoid: LocalizedText[];
  lifestyleTips: LocalizedText[];
  medicationAlternatives: LocalizedText;
}

export type ExerciseAnimation =
  | 'walk'
  | 'breathe'
  | 'squat'
  | 'pushup'
  | 'jumping-jack'
  | 'plank'
  | 'march'
  | 'butterfly'
  | 'cobra'
  | 'twist'
  | 'rest'
  | 'jog'
  | 'burpee'
  | 'mountain-climber'
  | 'high-knee'
  | 'neck-roll'
  | 'shoulder-roll'
  | 'knee-lift'
  | 'ankle-circle'
  | 'cat-cow'
  | 'goblet-squat'
  | 'row'
  | 'overhead-press'
  | 'deadlift'
  | 'hundred'
  | 'roll-up'
  | 'leg-stretch'
  | 'child-pose'
  | 'stretch';

export interface FitnessStepMeta {
  animation: ExerciseAnimation;
  durationSec: number;
}

export interface FitnessRoutine {
  id: string;
  type: FitnessType;
  title: LocalizedText;
  duration: number;
  difficulty: 'beginner' | 'intermediate' | 'advanced';
  description: LocalizedText;
  benefits: LocalizedText[];
  steps: LocalizedText[];
  ailments: AilmentCategory[];
  caloriesBurn: number;
}

export interface KnowledgeArticle {
  id: string;
  title: LocalizedText;
  category: string;
  content: LocalizedText;
  keyTakeaways: LocalizedText[];
}
