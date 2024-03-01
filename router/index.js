import { createRouter,createWebHistory } from "vue-router";
//import Vue from 'vue';
//import Router from 'vue-router';

import Forethought from '../src/Forethought.vue'

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
    ]
})

export default router;