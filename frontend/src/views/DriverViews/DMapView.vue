<template>
  <DLayoutComponent>
    <div class="flex flex-col h-full">
      <div class="bg-white shadow-sm border-b border-gray-200 p-4">
        <div class="flex justify-between items-center">
          <h2 class="text-xl font-semibold text-gray-900">
            Navigation to Passenger
          </h2>
          <button @click="$router.go(-1)" class="text-gray-500 hover:text-gray-700">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <div class="mt-2">
          <p class="text-sm text-gray-600">
            <span class="font-medium">Passenger:</span> {{ passengerName }}
          </p>
          <p class="text-sm text-gray-600">
            <span class="font-medium">Event:</span> {{ eventName }}
          </p>
        </div>
      </div>
      
      <div class="flex-grow relative">
        <!-- Map Container -->
        <div id="map" class="absolute inset-0"></div>
        
        <!-- Loading Indicator -->
        <div v-if="isLoading" class="absolute inset-0 flex items-center justify-center bg-black bg-opacity-30 z-10">
          <div class="bg-white p-4 rounded-lg shadow-lg flex items-center">
            <svg class="animate-spin h-8 w-8 text-indigo-600 mr-3" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
              <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
              <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
            </svg>
            <span>Loading map...</span>
          </div>
        </div>
        
        <!-- Controls -->
        <div class="absolute bottom-4 left-4 right-4 flex justify-center space-x-4">
          <button @click="startNavigation" class="px-4 py-2 bg-indigo-600 text-white rounded-lg shadow hover:bg-indigo-700">
            Start Navigation
          </button>
          <button @click="cancelRide" class="px-4 py-2 bg-red-500 text-white rounded-lg shadow hover:bg-red-600">
            Cancel Ride
          </button>
        </div>
      </div>
    </div>
  </DLayoutComponent>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue'

const route = useRoute()
const router = useRouter()

const isLoading = ref(true)
const map = ref(null)
const eventName = ref(route.query.eventName || 'Event')
const passengerName = ref(route.query.passengerName || 'Passenger')
const pickupCoords = ref({
  lat: parseFloat(route.query.pickupLat),
  lng: parseFloat(route.query.pickupLng)
})

// Initialize the map when component mounts
onMounted(() => {
  loadOpenStreetMap()
})

// Clean up when component unmounts
onUnmounted(() => {
  if (map.value) {
    map.value.remove()
  }
})

const loadOpenStreetMap = () => {
  // Check if Leaflet is available
  if (typeof L === 'undefined') {
    // Dynamically load Leaflet CSS
    const link = document.createElement('link')
    link.rel = 'stylesheet'
    link.href = 'https://unpkg.com/leaflet@1.7.1/dist/leaflet.css'
    link.integrity = 'sha512-xodZBNTC5n17Xt2atTPuE1HxjVMSvLVW9ocqUKLsCC5CXdbqCmblAshOMAS6/keqq/sMZMZ19scR4PsZChSR7A=='
    link.crossOrigin = ''
    document.head.appendChild(link)
    
    // Dynamically load Leaflet JS
    const script = document.createElement('script')
    script.src = 'https://unpkg.com/leaflet@1.7.1/dist/leaflet.js'
    script.integrity = 'sha512-XQoYMqMTK8LvdxXYG3nZ448hOEQiglfqkJs1NOQV44cWnUrBc8PkAOcXy20w0vlaXaVUearIOBhiXZ5V3ynxwA=='
    script.crossOrigin = ''
    script.onload = initializeMap
    document.head.appendChild(script)
  } else {
    initializeMap()
  }
}

const initializeMap = () => {
  // Get driver's current location (in a real app, this would come from GPS)
  navigator.geolocation.getCurrentPosition(
    (position) => {
      const driverCoords = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      }
      
      // Initialize the map
      map.value = L.map('map').setView(driverCoords, 13)
      
      // Add OpenStreetMap tiles
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map.value)
      
      // Add markers
      const driverMarker = L.marker(driverCoords).addTo(map.value)
      driverMarker.bindPopup("Your Location").openPopup()
      
      const pickupMarker = L.marker(pickupCoords.value).addTo(map.value)
      pickupMarker.bindPopup("Passenger Pickup").openPopup()
      
      // Add routing
      L.Routing.control({
        waypoints: [
          L.latLng(driverCoords.lat, driverCoords.lng),
          L.latLng(pickupCoords.value.lat, pickupCoords.value.lng)
        ],
        routeWhileDragging: true,
        showAlternatives: true,
        fitSelectedRoutes: true,
        show: true,
        collapsible: true
      }).addTo(map.value)
      
      isLoading.value = false
    },
    (error) => {
      console.error("Error getting location:", error)
      // Fallback to pickup location if geolocation fails
      map.value = L.map('map').setView(pickupCoords.value, 13)
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      }).addTo(map.value)
      
      L.marker(pickupCoords.value).addTo(map.value)
        .bindPopup("Passenger Pickup")
        .openPopup()
      
      isLoading.value = false
    }
  )
}

const startNavigation = () => {
  alert('Navigation started! In a real app, this would connect to a navigation service.')
  // Here you would typically:
  // 1. Confirm the ride with the backend
  // 2. Start tracking the driver's location
  // 3. Provide turn-by-turn navigation
}

const cancelRide = () => {
  if (confirm('Are you sure you want to cancel this ride?')) {
    // Here you would typically notify the backend about the cancellation
    router.push({ name: 'DEventRequests' })
  }
}
</script>

<style>
#map {
  z-index: 0;
}
</style>