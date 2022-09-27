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
        staff: resolve(__dirname, 'staff/index.html'),
        setLearningJourney: resolve(__dirname, 'setLearningJourney.html'),
        staff_create: resolve(__dirname, 'staff/create_lj.html'),
        staff_create_2: resolve(__dirname, 'staff/create_lj_2.html'),
        managerJobRole: resolve(__dirname, 'managerJobRole.html'),
        jobRoleDetails: resolve(__dirname, 'jobRoleDetails.html'),
      }
    }
  }
})
