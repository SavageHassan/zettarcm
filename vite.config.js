import { defineConfig } from 'vite'
import tailwindcss from '@tailwindcss/vite'
import { resolve } from 'path'

export default defineConfig({
  plugins: [
    tailwindcss(),
  ],
  build: {
    rollupOptions: {
      input: {
  main: resolve(__dirname, 'index.html'),
  company: resolve(__dirname, 'our-company/index.html'),
  nationwide: resolve(__dirname, 'nationwide-medical-billing/index.html'),
  privacy: resolve(__dirname, 'privacy-policy/index.html'),
  terms: resolve(__dirname, 'terms-and-conditions/index.html'),
  services: resolve(__dirname, 'medical-coding-services/index.html'), // Add this
      },
    },
  },
})