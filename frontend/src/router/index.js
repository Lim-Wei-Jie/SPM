import { createRouter, createWebHistory } from "vue-router";
// import components from the views folder to be used here

const routes = [
    /* 
    Each { } is for each page, e.g.,
    {
        path: "/", (URL name behind localhost:3000)
        name: "homepage", (give any name)
        component: HomePage (name of component in the views folder)
    }
    */
    {

    },

    {

    }
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes,
});

export default router;