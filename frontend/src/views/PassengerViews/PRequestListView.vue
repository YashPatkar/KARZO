<script setup>
import { ref, onMounted } from 'vue'
import api from '@/api'
import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue'

const bookings = ref([])
const loading = ref(true)
const error = ref(null)
const email = sessionStorage.getItem('passenger_email')

const fetchBookings = async () => {
  try {
    const res = await api.get('/api/passenger/bookings/', { params: { email } })
    bookings.value = res.data.bookings
  } catch (err) {
    error.value = 'Failed to load bookings.'
  } finally {
    loading.value = false
  }
}

const cancelBooking = async (id) => {
  if (!confirm('Are you sure you want to cancel this booking?')) return
  try {
    await api.delete(`/api/passenger/bookings/${id}/`)
    bookings.value = bookings.value.filter(b => b.id !== id)
  } catch (err) {
    alert('Failed to cancel booking.')
  }
}

onMounted(fetchBookings)
</script>

<template>
  <PLayoutComponent>
    <div class="max-w-4xl mx-auto mt-10 space-y-6 px-4">
      <h2 class="text-3xl font-semibold text-center text-gray-800 mb-6">
        <i class="fa-solid fa-calendar-check text-blue-600 mr-2"></i>
        Your Event Bookings
      </h2>

      <div v-if="loading" class="text-center text-gray-600">
        <i class="fa-solid fa-spinner fa-spin mr-2"></i>Loading bookings...
      </div>

      <div v-if="error" class="text-red-600 text-center text-lg">{{ error }}</div>

      <div v-if="bookings.length === 0 && !loading && !error" class="text-gray-500 text-center">
        <i class="fa-regular fa-calendar-xmark text-2xl mb-2 block"></i>
        No bookings found.
      </div>

      <div v-for="booking in bookings" :key="booking.id" class="bg-white border border-gray-200 rounded-xl shadow-md p-5">
        <div class="flex items-center justify-between mb-2">
          <h3 class="text-xl font-medium text-gray-800">
            <i class="fa-solid fa-map-location-dot text-indigo-500 mr-2"></i>{{ booking.event_name }}
          </h3>
          <button
            @click="cancelBooking(booking.id)"
            class="text-red-600 hover:text-red-800 text-sm flex items-center"
          >
            <i class="fa-solid fa-ban mr-1"></i>Cancel
          </button>
        </div>
        <p class="text-gray-700 mb-1">
          <i class="fa-solid fa-location-dot mr-2 text-blue-500"></i>
          <strong>Pickup:</strong> {{ booking.pickup_location }}
        </p>
        <p class="text-gray-700 mb-1">
          <i class="fa-solid fa-user-tie mr-2 text-green-500"></i>
          <strong>Driver:</strong> {{ booking.driver_email || 'Not yet assigned' }}
        </p>
        <p class="text-gray-700">
          <i class="fa-solid fa-road mr-2 text-yellow-500"></i>
          <strong>Distance:</strong> {{ booking.distance_km }} km
        </p>
      </div>
    </div>
  </PLayoutComponent>
</template>

<style scoped>
button {
  transition: all 0.2s ease;
}
button:hover {
  transform: scale(1.02);
}
</style>
