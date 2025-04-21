<script setup>
import { ref, computed, nextTick, watch } from 'vue'
import { usePassengerStore } from '@/stores/passengerStore'
import L from 'leaflet'
import 'leaflet/dist/leaflet.css'
import { getGroqChatCompletion } from "@/utils/EventDescription_groq"
import { debounce } from 'lodash'

const passengerStore = usePassengerStore()
const loading = ref(false)
const generatingDescription = ref(false)



// Compute dates
const today = new Date()
const formattedToday = computed(() => today.toISOString().split('T')[0])
const formattedMaxDate = computed(() => {
  const maxDate = new Date()
  maxDate.setFullYear(today.getFullYear() + 1)
  return maxDate.toISOString().split('T')[0]
})
console.log(passengerStore.passenger?.name, passengerStore.passenger?.email)
// Form data
const eventForm = ref({
    name: passengerStore.passenger?.name || '',
    email: passengerStore.passenger?.email || '',
    event_name: '',
    date: '',
    time: '',
    location: '',
    description: '',
    latitude: null,
    longitude: null,
    user_type: 'passenger',
})


// AI Description Generation
const generateEventDescription = async () => {
  if (!eventForm.value.event_name || !eventForm.value.date || !eventForm.value.time || !eventForm.value.location) {
    alert('Please enter event name, date, time, and location first.');
    return;
  }

  generatingDescription.value = true;
  try {
    eventForm.value.description = await getGroqChatCompletion(
      eventForm.value.event_name, 
      eventForm.value.location, 
      eventForm.value.date,
      eventForm.value.time
    );
  } catch (error) {
    console.error('AI request failed:', error);
    alert('Error generating description.');
  } finally {
    generatingDescription.value = false;
  }
};

// Location handling
const locationQuery = ref('')
const locationSuggestions = ref([])
const showMapModal = ref(false)
const map = ref(null)
const marker = ref(null)
const mapContainer = ref(null)
const selectedAddress = ref('')

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
      lat: place.lat,
      lon: place.lon
    }))
  } catch (error) {
    console.error('Location search error:', error)
  }
}

const debounceFetchLocationSuggestions = debounce(fetchLocationSuggestions, 500)

// Map functions
const initMap = () => {
  if (!mapContainer.value) return

  // Set initial view (India center by default)
  const initialView = eventForm.value.latitude 
    ? [eventForm.value.latitude, eventForm.value.longitude]
    : [20.5937, 78.9629]
  const zoom = eventForm.value.latitude ? 15 : 5

  map.value = L.map(mapContainer.value).setView(initialView, zoom)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map.value)

  // Add existing marker if coordinates exist
  if (eventForm.value.latitude) {
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
      const response = await fetch(
        `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`
      )
      const data = await response.json()
      selectedAddress.value = data.display_name
      eventForm.value.latitude = lat
      eventForm.value.longitude = lng
    } catch (error) {
      console.error('Geocoding error:', error)
      selectedAddress.value = 'Location selected'
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

const selectLocation = (location) => {
  eventForm.value.location = location.display_name
  locationQuery.value = location.display_name
  eventForm.value.latitude = location.lat
  eventForm.value.longitude = location.lon
  locationSuggestions.value = []
}

const confirmLocation = () => {
  if (selectedAddress.value) {
    eventForm.value.location = selectedAddress.value
    locationQuery.value = selectedAddress.value
  }
  closeMapModal()
}

// Form submission
const emit = defineEmits(['submit-event'])

const submitEvent = () => {
    if (!eventForm.value.event_name || !eventForm.value.date || !eventForm.value.time || 
        !eventForm.value.location || !eventForm.value.description) {
        alert('Please fill all required fields')
        return
    }

    loading.value = true
    setTimeout(() => {
        emit('submit-event', { ...eventForm.value })
        eventForm.value = {
            name: passengerStore.passenger?.name || '',
            email: passengerStore.passenger?.email || '',
            event_name: '',
            date: '',
            time: '',
            location: '',
            description: '',
            latitude: null,
            longitude: null,
            user_type: 'passenger',
        }
        locationQuery.value = ''
        loading.value = false
    }, 500)
}

watch(
  () => passengerStore.passenger,
  (newVal) => {
    if (newVal) {
      eventForm.value.name = newVal.name
      eventForm.value.email = newVal.email
    }
  },
  { immediate: true } // trigger immediately on mount
)

</script>

<template>
  <div class="max-w-2xl mx-auto p-6">
    <h1 class="text-2xl font-bold mb-4 text-gray-800">Suggest New Event</h1>
    <div class="bg-white shadow-lg rounded-xl p-6">
      <form @submit.prevent="submitEvent" class="space-y-4">
        <!-- Event Name -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Event Name *</label>
          <input 
            v-model="eventForm.event_name"
            type="text"
            class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
            required
          />
        </div>

        <!-- Date and Time -->
        <div class="flex flex-col md:flex-row gap-4">
          <div class="w-full">
            <label class="block text-sm font-medium text-gray-700 mb-1">Date *</label>
            <input 
              v-model="eventForm.date"
              type="date"
              :min="formattedToday"
              :max="formattedMaxDate"
              class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
              required
            />
          </div>

          <div class="w-full">
            <label class="block text-sm font-medium text-gray-700 mb-1">Time *</label>
            <input 
              v-model="eventForm.time"
              type="time"
              class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
              required
            />
          </div>
        </div>

        <!-- Location Field -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Location (India) *</label>
          <div class="relative">
            <input 
              v-model="locationQuery"
              type="text"
              @input="debounceFetchLocationSuggestions"
              class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none pr-10"
              required
            />
            <button
              type="button"
              @click="openMapModal"
              class="absolute right-2 top-2 text-gray-500 hover:text-blue-500"
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

        <!-- Description -->
        <div>
          <label class="block text-sm font-medium text-gray-700 mb-1">Event Description *</label>
          <div class="relative">
            <textarea v-model="eventForm.description" rows="4"
              class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:outline-none pr-10"
              required></textarea>
            <button @click="generateEventDescription" type="button" title="Generate Description"
              class="absolute bottom-4 right-3 text-black border-[1px] border-black px-2 py-2 rounded-xl hover:bg-gray-700 hover:text-white hover:border-white transition duration-200 transform flex items-center"
              :disabled="generatingDescription || loading">
              <i class="fa-solid fa-wand-magic-sparkles"></i>
            </button>
          </div>
        </div>

        <!-- Submit Button -->
        <button 
          type="submit" 
          :disabled="loading"
          class="w-full bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 rounded-lg transition duration-200 flex items-center justify-center"
        >
          <svg v-if="loading" class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
          </svg>
          {{ loading ? 'Submitting...' : 'Submit Event Suggestion' }}
        </button>
      </form>
    </div>

    <!-- Map Modal -->
    <div v-if="showMapModal" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg w-full max-w-3xl max-h-[90vh] flex flex-col">
        <div class="p-4 border-b flex justify-between items-center">
          <h3 class="text-lg font-medium">Select Location</h3>
          <button @click="closeMapModal" class="text-gray-500 hover:text-gray-700">
            &times;
          </button>
        </div>
        <div class="p-4 flex-1 min-h-[400px]">
          <div ref="mapContainer" class="w-full h-full rounded-md" style="min-height: 400px;"></div>
        </div>
        <div class="p-4 border-t">
          <div v-if="selectedAddress" class="mb-3 p-2 bg-gray-100 rounded">
            <strong>Selected:</strong> {{ selectedAddress }}
          </div>
          <div class="flex justify-end space-x-2">
            <button @click="confirmLocation" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
              Confirm
            </button>
            <button @click="closeMapModal" class="px-4 py-2 bg-gray-300 rounded hover:bg-gray-400">
              Cancel
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>