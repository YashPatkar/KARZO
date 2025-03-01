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
    path: '/DHomeView',
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
  },
  {
    path: '/',
    name: 'DRegisterView',
    component: () => import('../views/DriverViews/LoginViews/DRegisterView.vue')
  },
  {
    path: '/DRegisterCardExtendedView',
    name: 'DRegisterCardExtendedView',
    component: () => import('../views/DriverViews/LoginViews/DRegisterCardExtendedView.vue')
  },
  {
    path: '/DMapView',
    name: 'DMapView',
    component: () => import('../views/DriverViews/DMapView.vue')
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
