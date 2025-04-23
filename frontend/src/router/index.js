import { createRouter, createWebHistory } from 'vue-router'

const PassengerRoutes = [
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
  },
  {
    path: '/PDashboardView',
    name: 'PDashboardView',
    component: () => import('../views/PassengerViews/PDashboardView.vue')
  },
  {
    path: '/PHistoryView',
    name: 'PHistoryView',
    component: () => import('../views/PassengerViews/PHistoryView.vue')
  },
  {
    path: '/PProfileView',
    name: 'PProfileView',
    component: () => import('../views/PassengerViews/PProfileView.vue')
  },
  {
    path: '/PFeedbackView',
    name: 'PFeedbackView',
    component: () => import('../views/PassengerViews/PFeedbackView.vue')
  },
  {
    path: "/PRequestListView",
    name: "PRequestListView",
    component: () => import('../views/PassengerViews/PRequestListView.vue')
  }
]

const DriverRoutes = [
  {
    path: '/DRequestView',
    name: 'DRequestView',
    component: () => import('../views/DriverViews/DRequestView.vue')
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
  },
  {
    path: '/DDashboardView',
    name: 'DDashboardView',
    component: () => import('../views/DriverViews/DDashboardView.vue')
  },
  {
    path: '/DHistoryView',
    name: 'DHistoryView',
    component: () => import('../views/DriverViews/DHistoryView.vue')
  },
  {
    path: '/DProfileView',
    name: 'DProfileView',
    component: () => import('../views/DriverViews/DProfileView.vue')
  },
  {
    path: '/DFeedbackView',
    name: 'DFeedbackView',
    component: () => import('../views/DriverViews/DFeedbackView.vue')
  }
]

const CoreRoutes = [
  {
    path: '/',
    name: 'HomeView',
    component: () => import('../views/StartPageViews/startpage.vue')
  },
  { path: '/:pathMatch(.*)*',
    name: 'NotFound',
    component: () => import('../views/StartPageViews/NotFound.vue')}
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
