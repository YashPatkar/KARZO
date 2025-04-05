<template>
  <PLayoutComponent>
    <div class="container mx-auto px-4 py-6">
      <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Upcoming Events</h1>

      <!-- Search Input -->
      <div class="flex justify-center mb-8">
        <input
          type="search"
          v-model="search"
          placeholder="🔍 Search events"
          class="w-[60%] p-2 px-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
      </div>

      <!-- No Events Message -->
      <div v-if="filteredEvents.length === 0" class="text-center text-gray-600">
        No events found.
      </div>

      <!-- Event Cards -->
      <div class="columns-1 sm:columns-2 lg:columns-3 gap-6">
        <div 
          v-for="event in filteredEvents" 
          :key="event.id" 
          class="bg-white shadow-lg rounded-lg overflow-hidden transition-transform transform hover:scale-105 mb-6"
        >
          <div class="p-6">
            <h2 class="text-xl font-bold text-gray-900 mb-2">{{ event.event_name }}</h2>
            <p class="text-sm text-gray-600 mb-2">
              📅 {{ event.date }} | ⏰ {{ event.time }}
            </p>
            <p class="text-sm text-gray-600 mb-2">
              📍 <span class="font-medium">{{ event.location }}</span>
            </p>
            <p class="text-gray-700 text-sm whitespace-pre-wrap mb-4">
              {{ event.description }}
            </p>
            <div class="flex justify-between items-center text-sm text-gray-500 mb-4">
              <span><i class="fa-solid fa-user"></i> {{ event.name }}</span>
              <span>📧 {{ event.email }}</span>
            </div>
            <button
              class="w-full py-2 bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-lg transition duration-200"
              @click="openBookingCard(event)"
            >
              Book a Ride
            </button>
            <div class="w-[85%] mx-auto h-[1px] opacity-20 bg-slate-800 rounded my-3"></div>
            <div class="flex justify-between items-center text-sm text-gray-500">
              <span 
                class="flex items-center gap-1 font-bold text-md cursor-pointer"
                :class="{ 'text-red-500': event.liked }"
                @click="toggleLike(event)"
              >
                <i 
                  class="fa-regular fa-heart text-xl" 
                  :class="{ 'fa-solid': event.liked, 'text-red-500': event.liked }"
                ></i> 
                {{ event.liked ? 'Liked' : 'Like' }}
              </span>
              <span>Popularity: {{ event.like_count || 0 }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Booking Ride Card -->
      <div v-if="selectedEvent" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50">
        <div class="bg-white rounded-lg w-full max-w-3xl max-h-[90vh] flex flex-col">
          <div class="p-4 border-b flex justify-between items-center">
            <h2 class="text-xl font-bold text-gray-800">Book a Ride</h2>
            <button @click="closeModal" class="text-gray-500 hover:text-gray-700">
              <i class="fas fa-times"></i>
            </button>
          </div>
          
          <div class="p-4 space-y-4 overflow-y-auto">
            <!-- Event Info -->
            <div class="bg-gray-50 p-3 rounded-lg">
              <p class="font-semibold text-gray-900">{{ selectedEvent.event_name }}</p>
              <p class="text-sm text-gray-600">
                📅 {{ selectedEvent.date }} | ⏰ {{ selectedEvent.time }}
              </p>
              <p class="text-sm text-gray-600">
                📍 {{ selectedEvent.location }}
              </p>
            </div>

            <!-- Location Selection -->
            <div>
              <h3 class="font-medium text-gray-800 mb-3">Pickup Location</h3>
              
              <!-- Address Input -->
              <div class="mb-4 relative">
                <label class="block text-sm font-medium text-gray-700 mb-1">Enter Address</label>
                <input
                  v-model="locationQuery"
                  @input="debounceFetchLocationSuggestions"
                  placeholder="Type your address"
                  class="w-full p-2 border border-gray-300 rounded-lg pr-20"
                >
                <div class="absolute right-2 top-8 flex gap-1">
                  <button
                    type="button"
                    @click="getCurrentLocation"
                    class="text-gray-500 hover:text-blue-500"
                    title="Get Current Location"
                    :disabled="gettingLocation"
                  >
                    <i v-if="!gettingLocation" class="fas fa-location-arrow"></i>
                    <i v-else class="fas fa-spinner fa-spin"></i>
                  </button>
                  <span class="text-gray-300">|</span>
                  <button
                    type="button"
                    @click="openMapModal"
                    class="text-gray-500 hover:text-blue-500"
                    title="Pick location on map"
                  >
                    <i class="fas fa-map-marker-alt"></i>
                  </button>
                </div>
                <ul v-if="locationSuggestions.length" class="mt-1 bg-white border border-gray-300 rounded-lg shadow-md z-10">
                  <li 
                    v-for="location in locationSuggestions" 
                    :key="location.display_name" 
                    @click="selectLocation(location)" 
                    class="p-2 cursor-pointer hover:bg-gray-100 border-b last:border-b-0"
                  >
                    {{ location.display_name }}
                  </li>
                </ul>
              </div>

              <!-- Map Container (shown when map modal is open) -->
              <div v-if="showMapModal" class="h-96 w-full relative border border-gray-300 rounded-lg overflow-hidden mb-4">
                <div ref="mapContainer" class="h-full w-full"></div>
                <div class="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2 z-10">
                  <i class="fas fa-map-marker-alt text-3xl text-red-500"></i>
                </div>
              </div>

              <!-- Selected Coordinates -->
              <div v-if="selectedLocation" class="mt-2 text-sm text-gray-600 p-2 bg-gray-100 rounded">
                <strong>Selected:</strong> {{ selectedLocation.display_name }}
                <div class="text-xs text-gray-500 mt-1">
                  Coordinates: {{ selectedLocation.lat.toFixed(6) }}, {{ selectedLocation.lon.toFixed(6) }}
                </div>
              </div>
            </div>

            <!-- Preferences -->
            <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Driver Preference</label>
                <select
                  v-model="driverPreference"
                  class="w-full p-2 border border-gray-300 rounded-lg"
                >
                  <option disabled value="">Select</option>
                  <option value="men">Men</option>
                  <option value="female">Female</option>
                  <option value="any">Any</option>
                </select>
              </div>

              <div>
                <label class="block text-sm font-medium text-gray-700 mb-1">Vehicle Type</label>
                <select
                  v-model="vehiclePreference"
                  class="w-full p-2 border border-gray-300 rounded-lg"
                >
                  <option disabled value="">Select</option>
                  <option value="sports_bike">Sports Bike</option>
                  <option value="electric_bike">Electric Bike</option>
                  <option value="scooty">Scooty</option>
                  <option value="regular_bike">Regular Bike</option>
                  <option value="bullet">Bullet</option>
                </select>
              </div>
            </div>
          </div>

          <div class="p-4 border-t flex justify-end space-x-2">
            <button 
              @click="closeModal" 
              class="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400"
            >
              Cancel
            </button>
            <button 
              @click="bookRide" 
              class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
              :disabled="!selectedLocation"
            >
              Confirm Booking
            </button>
          </div>
        </div>
      </div>

      <!-- Success Popup -->
      <div v-if="showPopup" class="fixed bottom-5 right-5 bg-green-500 text-white px-4 py-3 rounded-lg shadow-lg flex items-center animate-fade-in-up">
        <i class="fas fa-check-circle mr-2"></i>
        <span>Ride booked successfully!</span>
      </div>
    </div>
  </PLayoutComponent>
</template>

<script setup>
import { ref, computed, onMounted, nextTick } from 'vue'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue'
import api from '@/api'
import { debounce } from 'lodash'

// Map-related variables
const mapContainer = ref(null)
const map = ref(null)
const marker = ref(null)
const selectedLocation = ref(null)
const locationQuery = ref('')
const locationSuggestions = ref([])
const showMapModal = ref(false)
const gettingLocation = ref(false)

// Booking data
const events = ref([])
const search = ref('')
const selectedEvent = ref(null)
const driverPreference = ref('')
const vehiclePreference = ref('')
const showPopup = ref(false)

// Reverse geocode coordinates to address
const reverseGeocode = async (lat, lon) => {
  try {
    const response = await fetch(
      `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lon}`
    )
    const data = await response.json()
    return data.display_name || 'Current Location'
  } catch (error) {
    console.error('Reverse geocoding error:', error)
    return 'Current Location'
  }
}

// Get current location with address
const getCurrentLocation = async () => {
  if (!navigator.geolocation) {
    alert('Geolocation is not supported by your browser')
    return
  }

  gettingLocation.value = true
  try {
    const position = await new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject, {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 0
      })
    })

    const { latitude, longitude } = position.coords
    const address = await reverseGeocode(latitude, longitude)

    selectedLocation.value = {
      display_name: address,
      lat: latitude,
      lon: longitude
    }
    locationQuery.value = address

    // Update map if open
    if (map.value) {
      map.value.setView([latitude, longitude], 15)
      if (marker.value) map.value.removeLayer(marker.value)
      marker.value = L.marker([latitude, longitude]).addTo(map.value)
    }
  } catch (error) {
    console.error('Error getting location:', error)
    alert('Could not get your location. Please try again or enter manually.')
  } finally {
    gettingLocation.value = false
  }
}

// Initialize Map
const initMap = () => {
  if (!mapContainer.value) return

  // Set initial view (India center by default)
  const initialView = selectedLocation.value 
    ? [selectedLocation.value.lat, selectedLocation.value.lon]
    : [20.5937, 78.9629]
  const zoom = selectedLocation.value ? 15 : 5

  map.value = L.map(mapContainer.value).setView(initialView, zoom)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map.value)

  // Add existing marker if coordinates exist
  if (selectedLocation.value) {
    marker.value = L.marker(initialView).addTo(map.value)
  }

  // Handle map clicks
  map.value.on('click', async (e) => {
    const { lat, lng } = e.latlng
    
    // Update marker
    if (marker.value) map.value.removeLayer(marker.value)
    marker.value = L.marker([lat, lng]).addTo(map.value)
    
    // Get address
    try {
      const address = await reverseGeocode(lat, lng)
      selectedLocation.value = {
        display_name: address,
        lat: lat,
        lon: lng
      }
      locationQuery.value = address
    } catch (error) {
      console.error('Geocoding error:', error)
      selectedLocation.value = {
        display_name: 'Selected Location',
        lat: lat,
        lon: lng
      }
    }
  })
}

const openMapModal = () => {
  showMapModal.value = true
  nextTick(() => {
    initMap()
  })
}

const closeMapModal = () => {
  showMapModal.value = false
  if (map.value) {
    map.value.remove()
    map.value = null
  }
}

// Fetch location suggestions
const fetchLocationSuggestions = async () => {
  if (!locationQuery.value.trim()) {
    locationSuggestions.value = []
    return
  }

  try {
    const response = await fetch(
      `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(locationQuery.value)}&countrycodes=IN&limit=5`
    )
    const data = await response.json()
    locationSuggestions.value = data.map(place => ({
      display_name: place.display_name,
      lat: parseFloat(place.lat),
      lon: parseFloat(place.lon)
    }))
  } catch (error) {
    console.error('Location search error:', error)
  }
}

const debounceFetchLocationSuggestions = debounce(fetchLocationSuggestions, 500)

const selectLocation = (location) => {
  selectedLocation.value = location
  locationQuery.value = location.display_name
  locationSuggestions.value = []
  if (showMapModal.value) {
    closeMapModal()
  }
}

// Booking functions
const openBookingCard = (event) => {
  selectedEvent.value = event
  resetBookingForm()
}

const closeModal = () => {
  selectedEvent.value = null
  showMapModal.value = false
  if (map.value) {
    map.value.remove()
    map.value = null
  }
}

const resetBookingForm = () => {
  driverPreference.value = ''
  vehiclePreference.value = ''
  locationQuery.value = ''
  selectedLocation.value = null
  locationSuggestions.value = []
}

const bookRide = async () => {
  if (!driverPreference.value || !vehiclePreference.value || !selectedLocation.value) {
    alert('Please select all required fields')
    return
  }

  const bookingData = {
    event_id: selectedEvent.value.id,
    driver_preference: driverPreference.value,
    vehicle_preference: vehiclePreference.value,
    pickup_location: selectedLocation.value.display_name,
    latitude: selectedLocation.value.lat,
    longitude: selectedLocation.value.lon
  }

  try {
    console.log('Booking data:', bookingData)
    const response = await api.post('/api/passenger/book-event/', bookingData)
    if(response.status === 201) {
      alert('Event submitted successfully!')
      selectedEvent.value = null
    }
    else{
      alert('Failed to submit event')
      selectedEvent.value = null
    }
  } catch (error) {
    console.error('Booking failed:', error)
    alert('Failed to book ride. Please try again.')
  }
}

// Event listing functions
const filteredEvents = computed(() => {
  if (!search.value) return events.value
  return events.value.filter(event => 
    event.event_name.toLowerCase().includes(search.value.toLowerCase()) ||
    event.location.toLowerCase().includes(search.value.toLowerCase()) ||
    event.description.toLowerCase().includes(search.value.toLowerCase())
  )
})

const toggleLike = async (event) => {
  try {
    const response = await api.post(`/api/core/events/${event.id}/like/`, {
      email: event.email,
    })

    event.liked = response.data.liked
    event.like_count = response.data.like_count
  } catch (error) {
    console.error("Error toggling like:", error)
  }
}

// Lifecycle
onMounted(async () => {
  try {
    const response = await api.get('/api/core/events/')
    events.value = response.data
  } catch (error) {
    console.error('Error fetching events:', error)
  }
})
</script>

<style scoped>
.animate-fade-in-up {
  animation: fadeInUp 0.3s ease-out;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.fa-spinner {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(360deg);
  }
}
</style>