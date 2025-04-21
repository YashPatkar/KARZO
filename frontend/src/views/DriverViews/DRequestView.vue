<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import api from '@/api'
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue'

const eventRequests = ref([])
const driverEmail = sessionStorage.getItem('driver_email')// Replace with actual login value
let interval = null

const fetchEventRequests = async () => {
  try {
    const response = await api.get(`/api/driver/event-requests/?email=${driverEmail}`)
    eventRequests.value = response.data
  } catch (error) {
    console.error("Error fetching event requests:", error)
  }
}

onMounted(() => {
  fetchEventRequests() // initial fetch
  interval = setInterval(fetchEventRequests, 5000) // poll every 5 seconds
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<template>
  <DLayoutComponent>
    <h2 class="text-lg font-bold mb-2">Pending Event Requests</h2>
    <div v-if="eventRequests.length === 0">
      No pending event requests.
    </div>
    <ul v-else class="space-y-2">
      <li v-for="event in eventRequests" :key="event.id" class="p-4 rounded shadow bg-white">
        <p><strong>Passenger:</strong> {{ event.passenger_name }}</p>
        <p><strong>Event:</strong> {{ event.event_name }}</p>
        <p><strong>Pickup Location:</strong> {{ event.pickup_location }}</p>
        <p><strong>Distance:</strong> {{ event.distance_km }} km</p>
      </li>
    </ul>
  </DLayoutComponent>
</template>
