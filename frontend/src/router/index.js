import PVerifyView from '@/views/PassengerViews/LoginViews/PVerifyView.vue'
import { createRouter, createWebHistory } from 'vue-router'

const PassengerRoutes = [
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
  },
  {
    path: '/PRegisterView',
    name: 'PRegisterView',
    component: () => import('../views/PassengerViews/LoginViews/PRegisterView.vue')
  },
  {
    path: '/PRegisterCardExtendedView',
    name: 'PRegisterCardExtendedView',
    component: () => import('../views/PassengerViews/LoginViews/PRegisterCardExtendedView.vue')
  },
  {
    path: '/PVerifyView',
    name: 'PVerifyView',
    component: () => import('../views/PassengerViews/LoginViews/PVerifyView.vue')
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
    path: '/DRegisterView',
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
  },
  {
    path: '/DVerifyView',
    name: 'DVerifyView',
    component: () => import('../views/DriverViews/LoginViews/DVerifyView.vue')
  }
]

const CoreRoutes = [
  {
    path: '/',
    name: 'HomeView',
    component: () => import('../views/StartPageViews/startpage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...DriverRoutes,
    ...PassengerRoutes,
    ...CoreRoutes,
  ],
})
export default router
