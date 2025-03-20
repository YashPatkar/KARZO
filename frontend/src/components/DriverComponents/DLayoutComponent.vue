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

// Get store instance
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
const profilePhoto = computed(() => driverStore.driver.profile_photo_url || 'https://imgs.search.brave.com/TvEa5hDYoEHqMQXTiWO9VZK3Ow2GKxoSnIcxFb1IrBg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDcw/MTAwODQ4L3ZlY3Rv/ci9tYWxlLXByb2Zp/bGUtaWNvbi13aGl0/ZS1vbi10aGUtYmx1/ZS1iYWNrZ3JvdW5k/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz0yWjNBczdLZEhx/U0tCNlVEQnBTSWJN/a3dPZ1lRdGJoU1dy/RjFaSFg1MDVFPQ');

// Computed properties for profile image and name

// Fetch driver data when the component is mounted

const items = ref([
  { title: 'Home', icon: 'fas fa-home', to: { name: 'DHomeView' } },
  { title: 'Dashboard', icon: 'fas fa-chart-line', to: { name: 'DHomeView' } },
  { title: 'Events', icon: 'fas fa-users', to: { name: 'DEventView' } },
  { title: 'Events Uploader', icon: 'fas fa-upload', to: { name: 'DEventUploadView' } }
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
          <i :class="item.icon" class="w-5 h-5 mr-2 text-gray-700"></i>
          <span>{{ item.title }}</span>
        </router-link>
      </nav>
    </aside>

    <!-- Overlay for mobile -->
    <div
      v-if="drawer"
      class="fixed inset-0 bg-black opacity-50 z-30 lg:hidden"
      @click="toggleDrawer"
    ></div>

    <!-- Main content -->
    <div class="flex-1 flex flex-col">
      <!-- Header -->
      <header class="bg-white shadow-md flex items-center justify-between px-4 py-2">
        <button class="p-2 focus:outline-none lg:hidden" @click="toggleDrawer">
          <i class="fas fa-bars text-gray-700 text-xl"></i>
        </button>
        <h1 class="text-lg font-semibold">KARZO</h1>
        <div class="relative">
          <!-- Profile dropdown -->
          <button @click="showDropdown = !showDropdown" class="p-2 focus:outline-none flex items-center">
            <img :src="profilePhoto" class="w-8 h-8 rounded-full mr-2" />
            <span class="font-medium">{{ driverName }}</span>
          </button>
          <div
            v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded shadow-lg"
          >
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fas fa-cog w-5 h-5 mr-2 text-gray-700"></i>
              <span>Settings</span>
            </div>
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fas fa-sign-out-alt w-5 h-5 mr-2 text-gray-700"></i>
              <span>Logout</span>
            </div>
          </div>
        </div>
      </header>

      <!-- Main content area -->
      <main class="flex-1 p-6 bg-gray-200">
        <slot></slot>
      </main>
    </div>
  </div>
</template>

<style scoped>
/* Add any custom styles here */
</style>