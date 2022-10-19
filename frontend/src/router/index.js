import { createRouter, createWebHistory } from "vue-router";
// import components from the views folder to be used here
import HomePage from "../views/HomePage.vue"
import LogIn from "../views/LogIn.vue"
import StaffPage from "../views/StaffPage.vue"
import ManagerPage from "../views/ManagerPage.vue"
import HrPage from "../views/HrPage.vue"
import JobRolePage from "../views/JobRolePage.vue"
import NewRolePage from "../views/NewRolePage.vue"
import EditJobRole from "../views/EditJobRole.vue"
import SearchJobRole from "../views/SearchRole.vue"
import createLJ from "../views/CreateLJ.vue"

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
        path: '/newRole',
        name: 'newRole',
        component: NewRolePage
    },

    {
        path: '/editRole',
        name: 'editRole',
        component: EditJobRole
    },

    {
        path: '/staff/searchRole',
        name: 'searchRole',
        component: SearchJobRole
    },

    {
        path: '/staff/create/:jobRoleName',
        name: 'createLJ',
        component: createLJ,
        props: true
    },


    // {
    //     path: '/newSkill',
    //     name: 'newSkill',
    //     component: NewSkillPage
    // },

    // {
    //     path: '/skill/:skillName',
    //     name: 'skill',
    //     component: SkillPage,
    //     props: true
    // },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;