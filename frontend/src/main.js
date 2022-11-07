import { createApp, watch } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from "./router";

import './style.css'

const pinia = createPinia()

// persist pinia store state
if (localStorage.getItem("state")) {
    pinia.state.value = JSON.parse(localStorage.getItem("state"))
}

watch (
    pinia.state,
    (state) => {
        localStorage.setItem("state", JSON.stringify(state))
    },
    { deep: true }
)

const app = createApp(App);

app.use(pinia).use(router).mount("#app");
