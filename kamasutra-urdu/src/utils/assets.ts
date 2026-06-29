import { Capacitor } from '@capacitor/core';

/**
 * Resolve bundled asset paths for web and Capacitor Android WebView.
 * Videos/fonts live under public/ → dist/ → android assets/public/
 */
export function getAssetUrl(relativePath: string): string {
  const clean = relativePath.replace(/^\//, '');

  if (Capacitor.isNativePlatform()) {
    const origin = window.location.origin.replace(/\/$/, '');
    return `${origin}/${clean}`;
  }

  const base = import.meta.env.BASE_URL ?? '/';
  return `${base}${clean}`.replace(/([^:]\/)\/+/g, '$1');
}

export const VIDEO_PATHS = [
  'videos/missionary.mp4',
  'videos/spooning.mp4',
  'videos/lotus.mp4',
  'videos/cowgirl.mp4',
  'videos/side-by-side.mp4',
  'videos/standing.mp4',
  'videos/doggy.mp4',
  'videos/reverse-cowgirl.mp4',
  'videos/butterfly.mp4',
  'videos/yab-yum.mp4',
  'videos/scissors.mp4',
  'videos/bridge.mp4',
] as const;
