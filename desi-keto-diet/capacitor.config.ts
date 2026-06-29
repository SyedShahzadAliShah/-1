import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.desiketo.diet',
  appName: 'Desi Keto Diet',
  webDir: 'dist',
  android: {
    allowMixedContent: true,
  },
  plugins: {
    TextToSpeech: {
      android: {
        lang: 'en-US',
      },
    },
  },
};

export default config;
