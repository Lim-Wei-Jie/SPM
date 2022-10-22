import { defineStore } from 'pinia'

// ref()s become state properties
// computed()s become getters
// function()s become actions

export const useStore = defineStore('main', () => {
    const name = ref()
})

export default store