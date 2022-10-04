import { createRouter, createWebHistory } from "vue-router";
// import components from the views folder to be used here
import HomePage from "../views/HomePage.vue"
import LogIn from "../views/LogIn.vue"
import StaffPage from "../views/StaffPage.vue"
import ManagerPage from "../views/ManagerPage.vue"
import HrPage from "../views/HrPage.vue"

const routes = [
    {
        path: '/',
        component: HomePage
    },

    {
        path: '/login',
        component: LogIn
    },

    {
        path: '/staff',
        component: StaffPage
    },

    {
        path: '/manager',
        component: ManagerPage
    },

    {
        path: '/hr',
        component: HrPage
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;