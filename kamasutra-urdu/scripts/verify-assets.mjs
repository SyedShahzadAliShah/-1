import { existsSync, readdirSync } from 'node:fs';
import { join } from 'node:path';

const dist = join(import.meta.dirname, '..', 'dist');
const videosDir = join(dist, 'videos');
const fontsDir = join(dist, 'fonts');

const requiredVideos = [
  'missionary.mp4', 'spooning.mp4', 'lotus.mp4', 'cowgirl.mp4',
  'side-by-side.mp4', 'standing.mp4', 'doggy.mp4', 'reverse-cowgirl.mp4',
  'butterfly.mp4', 'yab-yum.mp4', 'scissors.mp4', 'bridge.mp4',
];

let ok = true;

if (!existsSync(videosDir)) {
  console.error('MISSING: dist/videos/ — run npm run videos:generate');
  ok = false;
} else {
  const found = readdirSync(videosDir).filter((f) => f.endsWith('.mp4'));
  for (const name of requiredVideos) {
    if (!found.includes(name)) {
      console.error(`MISSING video: dist/videos/${name}`);
      ok = false;
    }
  }
  console.log(`Videos bundled: ${found.length}/${requiredVideos.length}`);
}

if (!existsSync(join(fontsDir, 'NotoSansArabic-Regular.ttf'))) {
  console.error('MISSING: dist/fonts/NotoSansArabic-Regular.ttf');
  ok = false;
} else {
  console.log('Urdu PDF font bundled');
}

if (!ok) process.exit(1);
console.log('Asset verification passed — all MP4s and font ready for APK');
