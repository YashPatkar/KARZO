<script setup>
import { ref, defineAsyncComponent } from 'vue';
import { Home, LayoutDashboard, Users, Briefcase, Menu, Settings, LogOut } from 'lucide-vue-next';

const drawer = ref(false);  // Set default to false so it's hidden on mobile
const showDropdown = ref(false);

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};

const items = ref([
  {
    title: 'Home',
    icon: Home,
    to: { name: 'DHomeView' },
    component: defineAsyncComponent(() => import('@/views/DriverViews/DHomeView.vue'))
  },
  {
    title: 'Dashboard',
    icon: LayoutDashboard,
    to: { name: 'DHomeView' },
    component: defineAsyncComponent(() => import('@/views/DriverViews/DHomeView.vue'))
  },
  {
    title: 'Events',
    icon: Users,
    to: { name: 'DEventView' },
    component: defineAsyncComponent(() => import('@/views/DriverViews/DEventView.vue'))
  },
  {
    title: 'Events Uploader',
    icon: Briefcase,
    to: { name: 'DEventUploadView' },
    component: defineAsyncComponent(() => import('@/views/DriverViews/DEventUploadView.vue'))
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
        <h1 class="text-lg font-semibold">KARZO</h1>
        <div class="relative">
          <button @click="showDropdown = !showDropdown" class="p-2 focus:outline-none">
            <img
              src="https://cdn.vuetifyjs.com/images/john.png"
              class="w-8 h-8 rounded-full"
            />
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
