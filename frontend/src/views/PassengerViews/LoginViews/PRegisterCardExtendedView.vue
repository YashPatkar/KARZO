<script setup>
import { onMounted, reactive, ref, nextTick } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "@/api";
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { debounce } from 'lodash'

const route = useRoute();
const router = useRouter();
const token = ref(route.query.token);
const email = ref("");
const errorMessage = ref("");
const isTokenValid = ref(false);
const isLoading = ref(false);
const profilePhoto = ref(null);

// Location handling (from PEventUploadComponent)
const locationQuery = ref('')
const locationSuggestions = ref([])
const showMapModal = ref(false)
const map = ref(null)
const marker = ref(null)
const mapContainer = ref(null)
const selectedAddress = ref('')

const personalDetails = reactive({
  name: "",
  age: null,
  gender: "male",
  phone: "",
  address: "",
  latitude: null,
  longitude: null,
});

// Validate token on mount
onMounted(async () => {
  if (!token.value) {
    errorMessage.value = "Invalid link.";
    return;
  }

  try {
    const response = await api.post("/api/passenger/validate-token/", {
      token: token.value,
    });

    email.value = response.data.email;
    isTokenValid.value = true;
  } catch (err) {
    errorMessage.value = "Invalid or expired token.";
  }
});

// Location functions (from PEventUploadComponent)
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

const initMap = () => {
  if (!mapContainer.value) return

  // Set initial view (India center by default)
  const initialView = personalDetails.latitude 
    ? [personalDetails.latitude, personalDetails.longitude]
    : [20.5937, 78.9629]
  const zoom = personalDetails.latitude ? 15 : 5

  map.value = L.map(mapContainer.value).setView(initialView, zoom)

  L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a>'
  }).addTo(map.value)

  // Add existing marker if coordinates exist
  if (personalDetails.latitude) {
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
      personalDetails.latitude = lat
      personalDetails.longitude = lng
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
  personalDetails.address = location.display_name
  locationQuery.value = location.display_name
  personalDetails.latitude = location.lat
  personalDetails.longitude = location.lon
  locationSuggestions.value = []
}

const confirmLocation = () => {
  if (selectedAddress.value) {
    personalDetails.address = selectedAddress.value
    locationQuery.value = selectedAddress.value
  }
  closeMapModal()
}

// Handle file selection
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    profilePhoto.value = file;
  }
};

// Upload image to ImgBB
const uploadImageToImgBB = async () => {
  if (!profilePhoto.value) return null;

  const formData = new FormData();
  formData.append("image", profilePhoto.value);

  try {
    const response = await fetch(`https://api.imgbb.com/1/upload?key=${import.meta.env.VITE_IMGBB_API_KEY}`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    if (data.success) {
      return data.data.url;
    }
  } catch (error) {
    console.error("Error uploading image:", error);
  }

  return null;
};

const registerPassenger = async () => {
  if (!isTokenValid.value) {
    errorMessage.value = "Token validation failed. Cannot proceed.";
    return;
  }

  // Validation - now includes location coordinates
  if (!personalDetails.name || !personalDetails.age || !personalDetails.phone || 
      !personalDetails.address || !personalDetails.latitude || !personalDetails.longitude) {
    alert("Please fill in all required fields and select a valid location.");
    return;
  }

  isLoading.value = true;

  try {
    const profilePhotoUrl = await uploadImageToImgBB();

    if (!profilePhotoUrl) {
      alert("Failed to upload profile photo. Please try again.");
      isLoading.value = false;
      return;
    }

    const response = await api.post("/api/passenger/register/", {
      ...personalDetails,
      email: email.value,
      token: token.value,
      profile_photo: profilePhotoUrl,
    });

    if (response.status === 201) {
      sessionStorage.setItem("passenger_email", email.value);
      router.push("/PEventView");
    }
  } catch (error) {
    alert(error.response?.data?.message || "An error occurred. Try again.");
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="p-6 bg-white rounded-lg shadow-md max-w-2xl mx-auto">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Complete Registration</h2>

    <p v-if="errorMessage" class="text-red-500 text-center mb-4">{{ errorMessage }}</p>

    <form v-if="isTokenValid" @submit.prevent="registerPassenger" class="space-y-4">
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
        <input 
          type="text" 
          v-model="personalDetails.name" 
          class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none" 
          required 
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Age</label>
        <input 
          type="number" 
          v-model="personalDetails.age" 
          class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none" 
          required 
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Gender</label>
        <select 
          v-model="personalDetails.gender" 
          class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
        >
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
        <input 
          type="tel" 
          v-model="personalDetails.phone" 
          class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none" 
          required 
        />
      </div>

      <!-- Updated Location Field -->
      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Address *</label>
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

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
        <input 
          type="email" 
          :value="email" 
          disabled 
          class="w-full border border-gray-300 rounded-lg p-2 bg-gray-100 focus:outline-none" 
        />
      </div>

      <div>
        <label class="block text-sm font-medium text-gray-700 mb-1">Profile Photo</label>
        <input 
          type="file" 
          accept="image/*" 
          @change="handleFileChange" 
          class="w-full border border-gray-300 rounded-lg p-2 focus:outline-none file:mr-4 file:py-2 file:px-4 file:rounded-md file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100" 
        />
      </div>

      <button
        type="submit"
        class="w-full bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 rounded-lg transition duration-200 flex items-center justify-center"
        :disabled="isLoading"
      >
        <svg v-if="isLoading" class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
        </svg>
        {{ isLoading ? 'Registering...' : 'Register' }}
      </button>
    </form>

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