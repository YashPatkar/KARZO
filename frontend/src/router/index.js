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
    }
  ],
})

export default router
