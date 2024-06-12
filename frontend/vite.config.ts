import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  base: '/pokedoku2/',
  plugins: [vue()],
  build: {
    target: "ES2022"
  }
})
