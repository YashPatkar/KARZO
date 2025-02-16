<template>
  <PLayoutComponent>
    <div class="container mx-auto px-4 py-6">
      <h1 class="text-2xl font-bold mb-6">Event List</h1>
      <div class="columns-1 md:columns-2 lg:columns-3 gap-4 space-y-4">
        <div v-for="event in events" :key="event.id" class="break-inside-avoid bg-white rounded-lg shadow-md p-4">
          <h2 class="text-xl font-semibold mb-2">{{ event.name }}</h2>
          <p class="text-sm text-gray-500 mb-1">{{ event.date }} | {{ event.time }}</p>
          <p class="text-sm text-gray-500 mb-2">Location: {{ event.location }}</p>
          <p class="text-gray-700 whitespace-pre-wrap">{{ event.description }}</p>
        </div>
      </div>
    </div>
  </PLayoutComponent>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue';
import axios from 'axios';

const events = ref([]);

// Fetch the events when component is mounted
onMounted(async () => {
  try {
    const response = await axios.get('http://127.0.0.1:8000/api/event/');
    events.value = response.data;
  } catch (error) {
    console.error('Error fetching events:', error);
  }
});
</script>

<style scoped>
/* Add any additional styling if necessary */
</style>
