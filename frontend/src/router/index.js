import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/index.vue'),
    },
    {
      path: '/Driver/home/',
      name: 'DriverHome',
      component: () => import('../views/Driver/home.vue')
    },
    {
      path: '/Driver/event/upload',
      name: 'DriverEventUpload',
      component: () => import('../views/Driver/eventUpload.vue')
    },
    {
      path: '/Driver/event/',
      name: 'DriverEvent',
      component: () => import('../views/Driver/events.vue')
    }
  ],
})

export default router
