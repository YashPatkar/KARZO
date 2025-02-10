<template>
  <DLayoutComponent>  
    <div class="container mx-auto px-4 py-6">
      <h1 class="text-2xl font-bold mb-6">Event List</h1>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div v-for="event in events" :key="event.id">
          <DEventCardComponent
            :name="event.name"
            :date="event.date"
            :time="event.time"
            :location="event.location"
            :description="event.description"
          >
              <!-- Slot content for assign/unassign button -->
            <button 
              @click="handleAssign(event.id)" 
              v-if="!event.isAssigned" 
              class="w-full mt-4 bg-blue-500 text-white py-2 px-4 rounded-lg hover:bg-blue-600 transition"
            >
              Assign
            </button>
            <button 
              @click="handleUnassign(event.id)" 
              v-if="event.isAssigned" 
              class="w-full mt-4 bg-red-500 text-white py-2 px-4 rounded-lg hover:bg-red-600 transition"
            >
              Unassign
            </button>
          </DEventCardComponent>
        </div>
      </div>
    </div>
  </DLayoutComponent>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue';
import DEventCardComponent from '@/components/DriverComponents/DEventCardComponent.vue';
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

// Handle Assign action (using fixed driver_id of 1)
const handleAssign = async (eventId) => {
  try {
    const driverId = 1;
    await axios.post(`http://127.0.0.1:8000/api/event/${eventId}/assign/${driverId}/`);
    const event = events.value.find(e => e.id === eventId);
    event.isAssigned = true;
  } catch (error) {
    console.error('Error assigning event:', error);
  }
};

// Handle Unassign action (using fixed driver_id of 1)
const handleUnassign = async (eventId) => {
  try {
    const driverId = 1;
    await axios.post(`http://127.0.0.1:8000/api/event/${eventId}/unassign/${driverId}/`);
    const event = events.value.find(e => e.id === eventId);
    event.isAssigned = false;
  } catch (error) {
    console.error('Error unassigning event:', error);
  }
};
</script>
