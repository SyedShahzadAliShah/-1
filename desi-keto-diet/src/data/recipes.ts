import type { Recipe } from '../types';
import { featuredRecipes } from './recipesFeatured';
import { generatedRecipes } from './generatedRecipes';

const featuredTitles = new Set(featuredRecipes.map((r) => r.title.en.toLowerCase()));

/** 200 keto recipes: 10 hand-crafted featured + 190 generated across 8 cuisines */
export const recipes: Recipe[] = [
  ...featuredRecipes,
  ...generatedRecipes
    .filter((r) => !featuredTitles.has(r.title.en.toLowerCase()))
    .slice(0, 200 - featuredRecipes.length),
];

export const recipeCount = recipes.length;

export const recipesByCuisine = (cuisine: Recipe['cuisine']) =>
  recipes.filter((r) => r.cuisine === cuisine);
