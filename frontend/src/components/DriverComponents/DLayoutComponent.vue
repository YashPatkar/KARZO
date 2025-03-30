<script setup>
import { ref, onMounted, computed } from 'vue';
import { useDriverStore } from '@/stores/driverStore';
import { useRouter } from 'vue-router';

const router = useRouter();
const drawer = ref(false);
const showDropdown = ref(false);

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};

const driverStore = useDriverStore();

onMounted(async () => {
  if (!driverStore.email) {
    console.error('Driver email is missing! Redirecting to DVerifyView...');
    router.push({ name: 'DVerifyView' });
    return;
  }
  await driverStore.fetchDriverData();
});

const driverName = computed(() => driverStore.driver.name || 'Driver');
const profilePhoto = computed(() => driverStore.driver.profile_photo_url || 'https://via.placeholder.com/150');

const items = ref([
  { title: 'Home', icon: 'fas fa-home', to: { name: 'DHomeView' } },
  { title: 'Dashboard', icon: 'fas fa-chart-line', to: { name: 'DHomeView' } },
  { title: 'Events', icon: 'fas fa-users', to: { name: 'DEventView' } },
  { title: 'Events Uploader', icon: 'fas fa-upload', to: { name: 'DEventUploadView' } }
]);
</script>

<template>
  <div class="flex h-screen w-screen">
    <!-- Sidebar -->
    <aside
      class="w-64 bg-white shadow-lg fixed h-full z-50 transition-transform duration-300 lg:translate-x-0"
      :class="{ 'transform -translate-x-full': !drawer, 'transform translate-x-0': drawer }"
    >
      <nav class="mt-10">
        <router-link
          v-for="(item, index) in items"
          :key="index"
          :to="item.to"
          class="flex items-center p-4 hover:bg-gray-100 rounded"
          @click="drawer = false"
        >
          <i :class="item.icon" class="w-6 h-6 mr-3 text-gray-700"></i>
          <span class="text-lg font-medium">{{ item.title }}</span>
        </router-link>
      </nav>
    </aside>

    <!-- Overlay for mobile -->
    <div
      v-if="drawer"
      class="fixed inset-0 bg-black opacity-50 z-40 lg:hidden"
      @click="toggleDrawer"
    ></div>

    <!-- Main content -->
    <div class="flex-1 flex flex-col ml-64 lg:ml-0">
      <!-- Header -->
      <header class="bg-white shadow-md flex items-center justify-between px-6 py-4 w-full fixed top-0 z-40">
        <button class="p-2 focus:outline-none lg:hidden" @click="toggleDrawer">
          <i class="fas fa-bars text-gray-700 text-xl"></i>
        </button>
        <h1 class="text-2xl font-semibold">KARZO</h1>
        <div class="relative">
          <button @click="showDropdown = !showDropdown" class="p-2 flex items-center focus:outline-none">
            <img :src="profilePhoto" class="w-10 h-10 rounded-full mr-2" />
            <span class="font-medium text-lg">{{ driverName }}</span>
          </button>
          <div
            v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded shadow-lg"
          >
            <div class="p-3 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fas fa-cog w-5 h-5 mr-2 text-gray-700"></i>
              <span>Settings</span>
            </div>
            <div class="p-3 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fas fa-sign-out-alt w-5 h-5 mr-2 text-gray-700"></i>
              <span>Logout</span>
            </div>
          </div>
        </div>
      </header>

      <!-- Main content area -->
      <main class="flex-1 p-6 bg-gray-200 mt-16 overflow-auto">
        <slot></slot>
      </main>
    </div>
  </div>
</template>

<style scoped>
/* Sidebar styles for mobile */
@media (max-width: 1024px) {
  aside {
    position: fixed;
    top: 0;
    left: 0;
    height: 100%;
  }
}
</style>
