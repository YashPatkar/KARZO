import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  // ----------------------------------------------Driver Routes------------------------------------------
  // Default Route ( Start Page)
  {
    path:'/home',
    name: 'Home',
    component: () => import('../pages/index.vue'),
  },
  // Driver Routes
  {
    path: '/Driver/',
    name: 'DriverHome',
    component: () => import('../pages/Driver/index.vue'),
  },
  {
    path: '/Driver/Features/event',
    name: 'DriverEvent',
    component: () => import('../pages/Driver/Features/event.vue'),
  },
  {
    path: '/Driver/Features/dashboard',
    name: 'DriverDashboard',
    component: () => import('../pages/Driver/Features/dashboard.vue'),
  },
  {
    path: '/Driver/Features/payment',
    name: 'DriverPayment',
    component: () => import('../pages/Driver/Features/payment.vue'),
  },
  {
    path: '/Driver/Features/eventUploader',
    name: 'DriverEventUploader',
    component: () => import('../pages/Driver/Features/eventUploader.vue'),
  },
  // Authentication Routes
  {
    path: '/',
    name: 'DriverSignup',
    component: () => import('../pages/Driver/Authentication/signup.vue'),
  },
  // ----------------------------------------------Passenger Routes------------------------------------------
  // Passenger Routes( Default Route )
  {
    path: '/Passenger/',
    name: 'PassengerHome',
    component: () => import('../pages/Passenger/index.vue'),
  }
];


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes
})

// Workaround for https://github.com/vitejs/vite/issues/11804
router.onError((err, to) => {
  if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
    if (!localStorage.getItem('vuetify:dynamic-reload')) {
      console.log('Reloading page to fix dynamic import error')
      localStorage.setItem('vuetify:dynamic-reload', 'true')
      location.assign(to.fullPath)
    } else {
      console.error('Dynamic import error, reloading page did not fix it', err)
    }
  } else {
    console.error(err)
  }
})

router.isReady().then(() => {
  localStorage.removeItem('vuetify:dynamic-reload')
})

export default router
