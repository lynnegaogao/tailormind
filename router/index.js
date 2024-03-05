import { createRouter, createWebHistory } from "vue-router";
import Forethought from '../src/Forethought.vue';
import Reflection from '../src/Reflection.vue';

const routes = [
    {
        path: '/',
        name: 'forethought',
        component: Forethought
    },
    {
        path: '/reflection',
        name: 'reflection',
        component: Reflection
    },


];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router;