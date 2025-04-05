<template>
  <div class="p-6 bg-white rounded-lg shadow-md max-w-2xl mx-auto">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Personal Details</h2>

    <!-- Profile Photo Upload -->
    <div class="mb-6">
      <label class="block text-sm font-medium text-gray-700 mb-2">Profile Photo</label>
      <input 
        type="file" 
        accept="image/*" 
        @change="handleProfilePhotoUpload"
        class="w-full border border-gray-300 rounded-lg p-2 focus:outline-none file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
      />
      <span v-if="!isProfilePhotoValid" class="text-sm text-red-500">Profile Photo is required</span>
    </div>

    <!-- Name Field -->
    <div class="mb-6">
      <label class="block text-sm font-medium text-gray-700 mb-2">Name</label>
      <input
        type="text"
        v-model="personalDetails.name"
        class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
      />
      <span v-if="!isNameValid" class="text-sm text-red-500">Name is required</span>
    </div>

    <!-- Other Fields -->
    <div v-for="(field, key) in fieldMappings" :key="key" class="mb-6">
      <label class="block text-sm font-medium text-gray-700 mb-2">{{ field.label }}</label>
      
      <template v-if="key !== 'location'">
        <input
          v-if="field.type !== 'textarea' && field.type !== 'select'"
          :type="field.type"
          v-model="personalDetails[key]"
          class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
        />
        <textarea
          v-else-if="field.type === 'textarea'"
          v-model="personalDetails[key]"
          class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
        ></textarea>
        <select v-else v-model="personalDetails[key]" class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none">
          <option v-for="option in field.options" :key="option" :value="option">{{ option }}</option>
        </select>
      </template>

      <!-- Special Location Field with Map Integration -->
      <div v-else class="relative">
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

      <span v-if="!validations[key]" class="text-sm text-red-500">{{ field.error }}</span>
    </div>

    <!-- Email (Pre-filled & Disabled) -->
    <div class="mb-6">
      <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
      <input
        type="email"
        v-model="personalDetails.email"
        class="w-full border border-gray-300 rounded-lg p-2 bg-gray-100 focus:outline-none"
        disabled
      />
    </div>

    <!-- Next Button -->
    <button 
      @click="validateAndNext" 
      class="w-full bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 rounded-lg transition duration-200"
    >
      Next
    </button>

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

<script setup>
import { reactive, computed, onMounted, ref, nextTick } from 'vue';
import { useRoute } from 'vue-router';
import api from '@/api';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { debounce } from 'lodash'


const route = useRoute();
const emit = defineEmits(['next', 'update:personalDetails', 'update:profilePhoto']);

// Location handling state
const locationQuery = ref('');
const locationSuggestions = ref([]);
const showMapModal = ref(false);
const map = ref(null);
const marker = ref(null);
const mapContainer = ref(null);
const selectedAddress = ref('');

const personalDetails = reactive({
  name: '',
  age: null,
  birth_date: '',
  gender: 'male',
  phone: '',
  location: '',
  pincode: '',
  address: '',
  email: ''
});

const fieldMappings = {
  age: { label: 'Age', type: 'number', error: 'Age is required' },
  birth_date: { label: 'Birth Date', type: 'date', error: 'Birth Date is required' },
  gender: { label: 'Gender', type: 'select', options: ['male', 'female', 'other'] },
  phone: { label: 'Phone Number', type: 'tel', error: 'Phone Number is required' },
  location: { label: 'Location', type: 'text', error: 'Location is required' },
  pincode: { label: 'Pincode', type: 'text', error: 'Pincode is required' },
  address: { label: 'Address', type: 'textarea', error: 'Address is required' },
};

// Location functions
const fetchLocationSuggestions = async () => {
  if (!locationQuery.value.trim()) {
    locationSuggestions.value = [];
    return;
  }

  try {
    const response = await fetch(
      `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(locationQuery.value)}&countrycodes=IN&limit=5`
    );
    const data = await response.json();
    locationSuggestions.value = data.map(place => ({
      display_name: place.display_name,
      lat: place.lat,
      lon: place.lon
    }));
  } catch (error) {
    console.error('Location search error:', error);
  }
};

const debounceFetchLocationSuggestions = debounce(fetchLocationSuggestions, 500);

const initMap = () => {
  if (!mapContainer.value) return;

  // Set initial view (India center by default)
  const initialView = personalDetails.latitude 
    ? [personalDetails.latitude, personalDetails.longitude]
    : [20.5937, 78.9629];
  const zoom = personalDetails.latitude ? 15 : 5;

  map.value = L.map(mapContainer.value).setView(initialView, zoom);

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map.value);

  // Add existing marker if coordinates exist
  if (personalDetails.latitude) {
    marker.value = L.marker(initialView).addTo(map.value);
  }

  // Handle map clicks
  map.value.on('click', async (e) => {
    const { lat, lng } = e.latlng;
    
    // Update marker
    if (marker.value) map.value.removeLayer(marker.value);
    marker.value = L.marker([lat, lng]).addTo(map.value);
    
    // Get address
    try {
      const response = await fetch(
        `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`
      );
      const data = await response.json();
      selectedAddress.value = data.display_name;
      personalDetails.latitude = lat;
      personalDetails.longitude = lng;
    } catch (error) {
      console.error('Geocoding error:', error);
      selectedAddress.value = 'Location selected';
    }
  });
};

const openMapModal = () => {
  showMapModal.value = true;
  nextTick(() => {
    initMap();
  });
};

const closeMapModal = () => {
  showMapModal.value = false;
  if (map.value) {
    map.value.remove();
    map.value = null;
  }
};

const selectLocation = (location) => {
  personalDetails.location = location.display_name;
  locationQuery.value = location.display_name;
  personalDetails.latitude = location.lat;
  personalDetails.longitude = location.lon;
  locationSuggestions.value = [];
};

const confirmLocation = () => {
  if (selectedAddress.value) {
    personalDetails.location = selectedAddress.value;
    locationQuery.value = selectedAddress.value;
  }
  closeMapModal();
};

const validations = computed(() => {
  return {
    age: personalDetails.age !== null && personalDetails.age > 0,
    birth_date: !!personalDetails.birth_date,
    phone: !!personalDetails.phone,
    location: !!personalDetails.location && !!personalDetails.latitude && !!personalDetails.longitude,
    pincode: !!personalDetails.pincode,
    address: !!personalDetails.address,
  };
});

onMounted(async () => {
  const token = route.query.token;
  if (!token) {
    console.error("No registration token found");
    return;
  }

  try {
    const response = await api.post("/api/driver/validate-token/", { token });
    personalDetails.email = response.data.email;
  } catch (err) {
    console.error("Token validation failed:", err);
  }
});

const isProfilePhotoValid = computed(() => true);
const isNameValid = computed(() => personalDetails.name.trim() !== '');
const isFormValid = computed(() => 
  isNameValid.value && 
  Object.values(validations.value).every(Boolean)
);

const handleProfilePhotoUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    emit('update:profilePhoto', file);
  }
};

const validateAndNext = () => {
  if (isFormValid.value) {
    emit('update:personalDetails', personalDetails);
    emit('next');
  } else {
    alert('Please fill all required fields before proceeding.');
  }
};
</script>