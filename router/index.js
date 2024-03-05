import { createRouter, createWebHistory } from "vue-router";
import Forethought from '../src/Forethought.vue';
// import Performance from '../src/Performance.vue';

const routes = [
    {
        path: '/forethought',
        name: 'forethought',
        component: Forethought
    },
    // {
    //     path: '/performance',
    //     name: 'performance',
    //     component: Performance
    // },
  
];

const router = createRouter({
    history: createWebHistory(),
    routes: routes,
})

export default router;