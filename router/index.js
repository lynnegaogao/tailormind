import { createRouter,createWebHistory } from "vue-router";

const router = createRouter({
    history: createWebHistory(),
    routes: [
        // {
        //     path: '/HelloWorld',
        //     name: 'HelloWorld',
        //     component: () => import('@/components/HelloWorld.vue')
        // },
        {
            path: '/UploadFile',
            name: 'UploadFile',
            component: () => import('../src/components/UploadFile.vue')
        },
    ]
})

export default router;