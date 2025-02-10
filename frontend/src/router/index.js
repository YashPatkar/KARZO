import { createRouter, createWebHistory } from 'vue-router'

const PassengerRoutes = [
  // {
  //   path: '/',
  //   name: 'HomeView',
  //   component: () => import('../views/HomeView.vue')
  // },
  {
    path: '/PHomeView',
    name: 'PHomeView',
    component: () => import('../views/PassengerViews/PHomeView.vue')
  },
  {
    path: '/PEventUploadView',
    name: 'PEventUploadView',
    component: () => import('../views/PassengerViews/PEventUploadView.vue')
  },
  {
    path: '/PEventView',
    name: 'PEventView',
    component: () => import('../views/PassengerViews/PEventView.vue')
  }
]

const DriverRoutes = [
  {
    path: '/driverHome',
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
