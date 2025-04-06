<script setup>
import { usePassengerStore } from '@/stores/passengerStore';
import { ref, defineAsyncComponent, onMounted, computed, nextTick, onBeforeUnmount } from 'vue';

const passengerStore = usePassengerStore();
onMounted(async () => {
  try {
    await passengerStore.fetchPassengerData();
  } catch (error) {
    console.error('Error in onMounted:', error);
  }
});

const passenger = computed(() => passengerStore.passenger);
const drawer = ref(false);
const showDropdown = ref(false);
const isFullScreen = ref(false);

// Full-Screen Toggle Function
const toggleFullScreen = () => {
  if (!isFullScreen.value) {
    document.documentElement.requestFullscreen?.();
  } else {
    document.exitFullscreen?.();
  }
};

// Listen for Full-Screen Changes
const handleFullScreenChange = () => {
  isFullScreen.value = !!document.fullscreenElement;
};

onMounted(() => {
  document.addEventListener('fullscreenchange', handleFullScreenChange);
});
onBeforeUnmount(() => {
  document.removeEventListener('fullscreenchange', handleFullScreenChange);
});

// Close Dropdown When Clicking Outside
const closeDropdown = (event) => {
  if (!event.target.closest('.dropdown-menu')) {
    showDropdown.value = false;
  }
};

onMounted(() => {
  document.addEventListener('click', closeDropdown);
});

onBeforeUnmount(() => {
  document.removeEventListener('click', closeDropdown);
});

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};

const items = ref([
  {
    title: 'Dashboard',
    icon: 'fa-solid fa-chart-line',
    to: { name: 'PDashboardView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PDashboardView.vue'))
  },
  {
    title: 'Events',
    icon: 'fa-solid fa-users',
    to: { name: 'PEventView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PEventView.vue'))
  },
  {
    title: 'Events Uploader',
    icon: 'fa-solid fa-briefcase',
    to: { name: 'PEventUploadView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PEventUploadView.vue'))
  },
  {
    title: 'History',
    icon: 'fa-solid fa-clock-rotate-left',
    to: { name: 'PHistoryView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PHistoryView.vue'))
  }
]);
</script>

<template>
  <div class="flex h-screen relative">
    <!-- Sidebar -->
    <aside
      class="w-64 bg-white z-40 transition-transform duration-300 lg:static lg:translate-x-0"
      :class="{
        'absolute inset-y-0 left-0 transform -translate-x-full': !drawer,
        'absolute inset-y-0 left-0 transform translate-x-0': drawer
      }"
    >
    <nav class="p-2 h-full">
        <header>
          <div class="flex items-center justify-between p-4 border-b">
            <h2 class="text-lg font-semibold">Karzo</h2>
          </div>
        </header>
        <router-link
          v-for="(item, index) in items"
          :key="index"
          :to="item.to"
            :class="['flex items-center p-3 hover:bg-gray-100 rounded active:bg-gray-50', { 'bg-gray-100': $route.name === item.to.name }]"
          @click="drawer = false"
        >
          <i :class="item.icon" class="w-5 h-5 mr-2 text-gray-700"></i>
          <span>{{ item.title }}</span>
        </router-link>
      </nav>
    </aside>

    <!-- Backdrop for mobile view -->
    <div
      v-if="drawer"
      class="fixed inset-0 bg-black opacity-50 z-30 lg:hidden"
      @click="toggleDrawer"
    ></div>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col">
      <!-- Navbar -->
      <header class="bg-white shadow-md flex items-center justify-between px-4 py-2">
        <button
          class="p-2 focus:outline-none lg:hidden"
          @click="toggleDrawer"
        >
          <i class="fa-solid fa-bars w-6 h-6 text-gray-700"></i>
        </button>
        <h1 class="text-lg font-semibold">
          {{ items.find(item => item.to.name === $route.name)?.title || $route.name }}
        </h1>
        <div class="relative flex items-center gap-2">
          <!-- Full-Screen Button -->
          <button @click="toggleFullScreen">
            <i :class="isFullScreen ? 'fa-solid fa-compress' : 'fa-solid fa-expand'"></i>
          </button>

          <!-- Dropdown Button -->
          <button @click="showDropdown = !showDropdown" class="p-2 focus:outline-none flex items-center gap-1 dropdown-menu">
            <img
              :src="passenger?.profile_photo || 'https://imgs.search.brave.com/TvEa5hDYoEHqMQXTiWO9VZK3Ow2GKxoSnIcxFb1IrBg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDcw/MTAwODQ4L3ZlY3Rv/ci9tYWxlLXByb2Zp/bGUtaWNvbi13aGl0/ZS1vbi10aGUtYmx1/ZS1iYWNrZ3JvdW5k/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz0yWjNBczdLZEhx/U0tCNlVEQnBTSWJN/a3dPZ1lRdGJoU1dy/RjFaSFg1MDVFPQ'"
              alt="Profile Photo"
              class="w-8 h-8 rounded-full"
            />
            {{ passenger.name }}
          </button>

          <!-- Dropdown Menu -->
          <div
            v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded shadow-lg dropdown-menu"
          >
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fa-solid fa-gear w-5 h-5 mr-2 text-gray-700"></i>
              <span>Settings</span>
            </div>
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fa-solid fa-right-from-bracket w-5 h-5 mr-2 text-gray-700"></i>
              <span>
                <button @click="sessionStorage.removeItem('passenger_email')" class="text-red-500">Logout</button>
              </span>
            
            </div>
          </div>
        </div>
      </header>

      <!-- Content -->
      <main class="flex-1 p-6 bg-gray-200">
        <slot></slot>
      </main>
    </div>
  </div>
</template>

<style scoped>
body {
  font-family: 'Inter', sans-serif;
}
</style>
