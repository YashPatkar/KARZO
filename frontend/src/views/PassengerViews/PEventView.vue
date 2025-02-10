<template>
  <PLayoutComponent>  
    <div class="container mx-auto px-4 py-6">
      <h1 class="text-2xl font-bold mb-6">Event List</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="event in events" :key="event.id">
          <PEventCardComponent
            :name="event.name"
            :date="event.date"
            :time="event.time"
            :location="event.location"
            :description="event.description"
          >
          </PEventCardComponent>
        </div>
      </div>
    </div>
  </PLayoutComponent>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue';
import PEventCardComponent from '@/components/PassengerComponents/PEventCardComponent.vue';
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
