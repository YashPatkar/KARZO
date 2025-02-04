import { createRouter, createWebHistory } from 'vue-router'

const PassengerRoutes = [

]

const DriverRoutes = [
  {
    path: '/',
    name: 'DHomeView',
    component: () => import('../views/DriverViews/DHomeView.vue')
  },
  {
    path: '/DEventUploadView',
    name: 'DEventUploadView',
    component: () => import('../views/DriverViews/DEventUploadView.vue')
  },
  {
    path: '/DEventView',
    name: 'DEventView',
    component: () => import('../views/DriverViews/DEventView.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...DriverRoutes,
    ...PassengerRoutes,
  ],
})
export default router
