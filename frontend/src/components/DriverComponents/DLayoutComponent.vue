<script setup>
import { useDriverStore } from "@/stores/driverStore";
import {
  ref,
  defineAsyncComponent,
  onMounted,
  computed,
  onBeforeUnmount,
} from "vue";

import api from "@/api";

const driverStore = useDriverStore();
onMounted(async () => {
  try {
    if (!sessionStorage.getItem("driver_email")) {
      nextTick(() => {
        window.location.href = "/";
      });
    }
    await driverStore.fetchdriverData();
    console.log("driver", driverStore.driver);
    const syncSuccess = await fetchWorkingStatus();
  
  // If server fetch fails, fallback to sessionStorage
  if (!syncSuccess) {
    const storedStatus = sessionStorage.getItem('driver_working_status');
    if (storedStatus !== null) {
      isWorking.value = storedStatus === 'true';
    }
  }
  } catch (error) {
    console.error("Error in onMounted:", error);
  }
});

const logout = () => {
  sessionStorage.removeItem("driver_email");
  window.location.href = "/";
};

const driver = computed(() => driverStore.driver);
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
  document.addEventListener("fullscreenchange", handleFullScreenChange);
});
onBeforeUnmount(() => {
  document.removeEventListener("fullscreenchange", handleFullScreenChange);
});

// Close Dropdown When Clicking Outside
const closeDropdown = (event) => {
  if (!event.target.closest(".dropdown-menu")) {
    showDropdown.value = false;
  }
};

onMounted(() => {
  document.addEventListener("click", closeDropdown);
});

onBeforeUnmount(() => {
  document.removeEventListener("click", closeDropdown);
});

const toggleDrawer = () => {
  drawer.value = !drawer.value;
};

const items = ref([
  {
    title: "Dashboard",
    icon: "fa-solid fa-chart-line",
    to: { name: "DDashboardView" },
    component: defineAsyncComponent(() =>
      import("@/views/DriverViews/DDashboardView.vue")
    ),
  },
  {
    title: "Events",
    icon: "fa-solid fa-users",
    to: { name: "DEventView" },
    component: defineAsyncComponent(() =>
      import("@/views/DriverViews/DEventView.vue")
    ),
  },
  {
    title: "Events Uploader",
    icon: "fa-solid fa-briefcase",
    to: { name: "DEventUploadView" },
    component: defineAsyncComponent(() =>
      import("@/views/DriverViews/DEventUploadView.vue")
    ),
  },
  {
    title: "Request",
    icon: "fa-solid fa-bell",
    to: { name: "DRequestView" },
    component: defineAsyncComponent(() =>
      import("@/views/DriverViews/DRequestView.vue")
    ),
  },

  {
    title: "History",
    icon: "fa-solid fa-clock-rotate-left",
    to: { name: "DHistoryView" },
    component: defineAsyncComponent(() =>
      import("@/views/DriverViews/DHistoryView.vue")
    ),
  },
  {
    title: "Feedback",
    icon: "fa-solid fa-comment",
    to: { name: "DFeedbackView" },
    component: defineAsyncComponent(() =>
      import("@/views/DriverViews/DFeedbackView.vue")
    ),
  }
]);

const isWorking = ref(
  sessionStorage.getItem('driver_working_status') === 'true' || false
);

// Enhanced status fetcher
const fetchWorkingStatus = async () => {
  try {
    const response = await api.get("/api/driver/toggle-working/", {
      params: { email: sessionStorage.getItem("driver_email") }
    });
    
    if (response.status === 200) {
      isWorking.value = response.data.working;
      sessionStorage.setItem('driver_working_status', response.data.working);
      return true;
    }
    return false;
  } catch (error) {
    console.error("Fetch status error:", error);
    return false;
  }
};

// Robust toggle function
const toggleWorking = async () => {
  const newStatus = !isWorking.value;
  const previousStatus = isWorking.value;
  
  // Optimistic UI update
  isWorking.value = newStatus;
  sessionStorage.setItem('driver_working_status', newStatus);
  
  try {
    const response = await api.post("/api/driver/toggle-working/", {
      email: sessionStorage.getItem("driver_email"),
      working: newStatus
    });
    
    if (response.status !== 200 || response.data.working !== newStatus) {
      throw new Error('Status mismatch');
    }
  } catch (error) {
    console.error("Update failed:", error);
    // Revert on failure
    isWorking.value = previousStatus;
    sessionStorage.setItem('driver_working_status', previousStatus);
    
    // Try to resync with server
    const syncSuccess = await fetchWorkingStatus();
    if (!syncSuccess) {
      alert("Failed to sync working status. Please refresh the page.");
    }
  }
};

</script>

<template>
  <div class="flex h-screen relative">
    <!-- Sidebar -->
    <aside class="w-64 bg-white z-40 transition-transform duration-300 lg:static lg:translate-x-0" :class="{
      'absolute inset-y-0 left-0 transform -translate-x-full': !drawer,
      'absolute inset-y-0 left-0 transform translate-x-0': drawer,
    }">
      <nav class="p-2 h-full">
        <header>
          <div class="flex items-center justify-between p-4 border-b">
            <h2 class="text-lg font-semibold">Karzo</h2>
          </div>
        </header>
        <router-link v-for="(item, index) in items" :key="index" :to="item.to" :class="[
          'flex items-center p-3 hover:bg-gray-100 rounded active:bg-gray-100',
          {
            'bg-gray-100': $route.name === item.to.name,
            'pointer-events-none opacity-50': item.title === 'Request' && !isWorking,
          },
        ]" @click="drawer = false">
          <i :class="item.icon" class="w-5 h-5 mr-2 text-gray-700"></i>
          <span>{{ item.title }}</span>
        </router-link>

      </nav>
    </aside>

    <!-- Backdrop for mobile view -->
    <div v-if="drawer" class="fixed inset-0 bg-black opacity-50 z-30 lg:hidden" @click="toggleDrawer"></div>

    <!-- Main Content -->
    <div class="flex-1 flex flex-col">
      <!-- Navbar -->
      <header class="bg-white shadow-md flex items-center justify-between px-4 py-2">
        <button class="p-2 focus:outline-none lg:hidden" @click="toggleDrawer">
          <i class="fa-solid fa-bars w-6 h-6 text-gray-700"></i>
        </button>
        <h1 class="text-lg font-semibold">
          {{
            items.find((item) => item.to.name === $route.name)?.title ||
            $route.name
          }}
        </h1>
        <!-- toggle button -->
        <div class="hs-tooltip flex items-center gap-x-3">
    <label for="working-toggle" class="hs-tooltip-toggle relative inline-block w-11 h-6 cursor-pointer">
      <input 
        type="checkbox" 
        id="working-toggle" 
        class="peer sr-only" 
        :checked="isWorking"
        @change="toggleWorking" 
      />
      <span
        class="absolute inset-0 bg-gray-200 rounded-full transition-colors duration-200 ease-in-out peer-checked:bg-blue-600 dark:bg-neutral-700 dark:peer-checked:bg-blue-500 peer-disabled:opacity-50 peer-disabled:pointer-events-none"
      ></span>
      <span
        class="absolute top-1/2 start-0.5 -translate-y-1/2 size-5 bg-white rounded-full shadow-xs transition-transform duration-200 ease-in-out peer-checked:translate-x-full dark:bg-neutral-400 dark:peer-checked:bg-white"
      ></span>
    </label>
    <label for="working-toggle" class="text-sm text-gray-500 dark:text-neutral-400">
      {{ isWorking ? 'Available' : 'Unavailable' }}
    </label>
    <div
      class="hs-tooltip-content hs-tooltip-shown:opacity-100 hs-tooltip-shown:visible opacity-0 transition-opacity inline-block absolute invisible z-10 py-1 px-2 bg-gray-900 text-xs font-medium text-white rounded-md shadow-2xs dark:bg-neutral-700"
      role="tooltip"
    >
      {{ isWorking ? 'You will receive event requests' : 'You will NOT receive event requests' }}
    </div>
  </div>
        <div class="relative flex items-center gap-2">
          <!-- Full-Screen Button -->
          <button @click="toggleFullScreen">
            <i :class="isFullScreen ? 'fa-solid fa-compress' : 'fa-solid fa-expand'
              "></i>
          </button>

          <!-- Dropdown Button -->
          <button @click="showDropdown = !showDropdown"
            class="p-2 focus:outline-none flex items-center gap-1 dropdown-menu">
            <img :src="driver?.profile_photo ||
              'https://imgs.search.brave.com/TvEa5hDYoEHqMQXTiWO9VZK3Ow2GKxoSnIcxFb1IrBg/rs:fit:860:0:0:0/g:ce/aHR0cHM6Ly9tZWRp/YS5pc3RvY2twaG90/by5jb20vaWQvNDcw/MTAwODQ4L3ZlY3Rv/ci9tYWxlLXByb2Zp/bGUtaWNvbi13aGl0/ZS1vbi10aGUtYmx1/ZS1iYWNrZ3JvdW5k/LmpwZz9zPTYxMng2/MTImdz0wJms9MjAm/Yz0yWjNBczdLZEhx/U0tCNlVEQnBTSWJN/a3dPZ1lRdGJoU1dy/RjFaSFg1MDVFPQ'
              " alt="Profile Photo" class="w-8 h-8 rounded-full" />
            {{ driver.name }}
          </button>

          <!-- Dropdown Menu -->
          <div v-if="showDropdown"
            class="absolute right-0 mt-2 w-48 bg-white border border-gray-200 rounded shadow-lg dropdown-menu">
            <router-link :to="{ name: 'DProfileView' }" class="block">
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fa-solid fa-user w-5 h-5 mr-2 text-gray-700"></i>
              <span>
                Profile
              </span>
            </div>
          </router-link>
            <div class="p-2 hover:bg-gray-100 cursor-pointer flex items-center">
              <i class="fa-solid fa-right-from-bracket w-5 h-5 mr-2 text-gray-700"></i>
              <span>
                <a @click="logout" class="">Logout</a>
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
  font-family: "Inter", sans-serif;
}
</style>
