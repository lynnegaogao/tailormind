import { createRouter,createWebHistory } from "vue-router";
//import Vue from 'vue';
//import Router from 'vue-router';

import Forethought from '../src/Forethought.vue'
import Performance from '../src/Performance.vue';
import Reflection from '../src/Reflection.vue';

//Vue.use(Router);

const router = createRouter({
    history: createWebHistory(),
    routes: [
        // {
        //     path: '/HelloWorld',
        //     name: 'HelloWorld',
        //     component: () => import('@/components/HelloWorld.vue')
        // },
        {
            path: '/forethought',
            name: 'forethought',
            component: Forethought
        },
        {
            path: '/performance',
            name: 'performance',
            component: Performance
        },
        {
            path: '/reflection',
            name: 'reflection',
            component: Reflection
        },
    ]
})

export default router;