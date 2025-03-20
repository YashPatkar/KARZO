<script setup>
import { Home, LayoutDashboard, Users, Briefcase, Menu, Settings, LogOut } from 'lucide-vue-next';
import { usePassengerStore } from '@/stores/passengerStore';
import { ref, defineAsyncComponent, onMounted, computed } from 'vue';

const passengerStore = usePassengerStore();

onMounted(async () => {
  try {
    await passengerStore.fetchPassengerData();
  } catch (error) {
    console.error('Error in onMounted:', error);
  }
});

const passenger = computed(() => passengerStore.passenger);

const drawer = ref(false);  // Set default to false so it's hidden on mobile
const showDropdown = ref(false);

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};

const items = ref([
  {
    title: 'Home',
    icon: Home,
    to: { name: 'PHomeView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PHomeView.vue'))
  },
  {
    title: 'Dashboard',
    icon: LayoutDashboard,
    to: { name: 'PHomeView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PHomeView.vue'))
  },
  {
    title: 'Events',
    icon: Users,
    to: { name: 'PEventView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PEventView.vue'))
  },
  {
    title: 'Events Uploader',
    icon: Briefcase,
    to: { name: 'PEventUploadView' },
    component: defineAsyncComponent(() => import('@/views/PassengerViews/PEventUploadView.vue'))
  }
]);
</script>

<template>
  <div class="flex h-screen relative">
    <!-- Sidebar -->
    <aside
      class="w-64 bg-white shadow-md z-40 transition-transform duration-300 lg:static lg:translate-x-0"
      :class="{
        'absolute inset-y-0 left-0 transform -translate-x-full': !drawer,
        'absolute inset-y-0 left-0 transform translate-x-0': drawer
      }"
    >
      <nav class="mt-10">
        <router-link
          v-for="(item, index) in items"
          :key="index"
          :to="item.to"
          class="flex items-center p-2 hover:bg-gray-100 rounded"
          @click="drawer = false"
        >
          <component :is="item.icon" class="w-5 h-5 mr-2 text-gray-700" />
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
          <Menu class="w-6 h-6 text-gray-700" />
        </button>
        <h1 class="text-lg font-semibold">Karzo</h1>
        <div class="relative flex items-center gap-2">
            <button @click="toggleFullScreen">
            <i :class="isFullScreen ? 'fa-solid fa-compress' : 'fa-solid fa-expand'"></i>
            </button>
          <button @click="showDropdown = !showDropdown" class="p-2 focus:outline-none flex items-center gap-1">
            <img
              src="https://imgs.search.brave.com/TvEa5hDYoEHqMQXTiWO9VZK3Ow2GKxoSnIcxFb1IrBg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDcw/MTAwODQ4L3ZlY3Rv/ci9tYWxlLXByb2Zp/bGUtaWNvbi13aGl0/ZS1vbi10aGUtYmx1/ZS1iYWNrZ3JvdW5k/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz0yWjNBczdLZEhx/U0tCNlVEQnBTSWJN/a3dPZ1lRdGJoU1dy/RjFaSFg1MDVFPQ"
              class="w-8 h-8 rounded-full"
            />
            {{ passenger.name }}
          </button>
          <div
            v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded shadow-lg"
          >
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <Settings class="w-5 h-5 mr-2 text-gray-700" />
              <span>Settings</span>
            </div>
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <LogOut class="w-5 h-5 mr-2 text-gray-700" />
              <span>Logout</span>
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
