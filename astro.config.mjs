import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  site: 'https://implenia.ahrensoptimate.com',
  output: 'static',
  build: {
    assets: 'assets',
    inlineStylesheets: 'auto',
  },
  vite: {
    build: {
      cssMinify: true,
      minify: true,
    },
  },
});
