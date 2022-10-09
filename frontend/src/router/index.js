import { createRouter, createWebHistory } from "vue-router";
// import components from the views folder to be used here
import HomePage from "../views/HomePage.vue"
import LogIn from "../views/LogIn.vue"
import StaffPage from "../views/StaffPage.vue"
import ManagerPage from "../views/ManagerPage.vue"
import HrPage from "../views/HrPage.vue"
import JobRolePage from "../views/JobRolePage.vue"
import StaffCreateLearningJourney from "../views/StaffCreateLearningJourney.vue"

const routes = [
    {
        path: '/',
        name: 'home',
        component: HomePage
    },

    {
        path: '/login',
        name: 'login',
        component: LogIn
    },

    {
        path: '/staff',
        name: 'staff',
        component: StaffPage
    },

    {
        path: '/manager',
        name: 'manager',
        component: ManagerPage
    },

    {
        path: '/hr',
        name: 'hr',
        component: HrPage
    },

    {
        path: '/jobRole/:jobRoleName',
        name: 'jobRole',
        component: JobRolePage,
        props: true
    },

    {
        path: '/staff/create',
        name: 'staffCreateLearningJourney',
        component: StaffCreateLearningJourney
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;