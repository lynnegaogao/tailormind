import { createRouter, createWebHistory } from "vue-router";
import Forethought from '../src/Forethought.vue';
import Performance from '../src/Performance.vue';

const routes = [
    {
        path: '/performance',
        name: 'performance',
        component: Performance
    },
    {
        path: '/',
        name: 'forethought',
        component: Forethought
    },
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router;