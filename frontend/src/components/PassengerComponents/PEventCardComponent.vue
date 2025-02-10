<template>
  <div class="max-w-sm mx-auto my-4 bg-white shadow-lg rounded-lg overflow-hidden h-52">
    <div class="px-4 py-2">
      <h2 class="text-xl font-semibold text-gray-800">{{ name }}</h2>
      <p class="text-sm text-gray-600">
        {{ formatDate(date) }} at {{ time }}
      </p>
    </div>
    
    <div class="px-4 py-2">
      <div class="flex items-center text-gray-700">
        <MapPin class="w-5 h-5 mr-2" />
        <span>{{ location }}</span>
      </div>

      <div class="mt-4 text-gray-600 h-16 overflow-hidden">
        {{ description.substring(0, 200) }}{{ description.length > 200 ? '...' : '' }}
      </div>
    </div>
  </div>
</template>

<script setup>
import { MapPin } from 'lucide-vue-next';  // Updated import for Vue 3

// Define props using defineProps()
const props = defineProps({
  name: {
    type: String,
    required: true,
  },
  date: {
    type: String,
    required: true,
  },
  time: {
    type: String,
    required: true,
  },
  location: {
    type: String,
    required: true,
  },
  description: {
    type: String,
    required: true,
  },
});

// Function to format the date
const formatDate = (dateString) => {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString(undefined, options);
};
</script>

<style>
/* Removed MDI import since we're using Lucide now */
</style>
