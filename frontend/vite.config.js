import { resolve } from 'path'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  build: { //https://vitejs.dev/guide/build.html
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html'),
        staff: resolve(__dirname, 'staff/index.html')
      }
    }
  }
})
