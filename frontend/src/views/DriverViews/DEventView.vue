<template>
  <DLayoutComponent>
    <div class="container mx-auto px-4 py-6">
      <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Upcoming Events</h1>
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        <div 
          v-for="event in events" 
          :key="event.id" 
          class="bg-white shadow-lg rounded-lg overflow-hidden transition-transform transform hover:scale-105"
        >
          <div class="p-6">
            <h2 class="text-xl font-bold text-gray-900 mb-2">{{ event.name }}</h2>
            <p class="text-sm text-gray-600 mb-2">
              📅 {{ event.date }} | ⏰ {{ event.time }}
            </p>
            <p class="text-sm text-gray-600 mb-2">
              📍 <span class="font-medium">{{ event.location }}</span>
            </p>
            <p class="text-gray-700 text-sm whitespace-pre-wrap mb-4">
              {{ event.description }}
            </p>
            <div class="flex justify-between items-center text-sm text-gray-500">
              <span>👤 {{ event.driver_name }}</span>
              <span>📧 {{ event.driver_email }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </DLayoutComponent>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue';
import api from '@/api';

const events = ref([]);

// Fetch the events when the component is mounted
onMounted(async () => {
  try {
    const response = await api.get('/api/core/events/');
    events.value = response.data;
  } catch (error) {
    console.error('Error fetching events:', error);
  }
});
</script>

<style scoped>
/* Ensures a modern card layout */
.grid > div {
  background-color: #ffffff;
  border-radius: 12px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.grid > div:hover {
  transform: scale(1.03);
}
</style>
