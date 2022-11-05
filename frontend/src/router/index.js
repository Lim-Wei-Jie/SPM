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
import CreateLJ from "../views/CreateLJ.vue"
import EditLJ from "../views/EditLJ.vue"
import ViewLJ from "../views/ViewLJ.vue"

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
        component: CreateLJ,
        props: true
    },

    {
        path: '/staff/edit/:ljpsID/:jobRoleID',
        name: 'editLJ',
        component: EditLJ,
        props: true
    },

    {
        path: '/staff/view/:ljpsID/:jobRoleID',
        name: 'viewLJ',
        component: ViewLJ,
        props: true
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;