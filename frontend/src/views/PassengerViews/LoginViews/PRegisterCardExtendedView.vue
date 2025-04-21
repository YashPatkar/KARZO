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
  <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50 px-4 py-12">
    <div class="mb-6 flex flex-row items-center justify-center space-x-2">
       <RouterLink to="/" aria-label="Go to Homepage">
          <img
            src="https://placehold.co/60x60/6366f1/white?text=K&font=raleway" alt="Karzo Logo"
            class="h-12 w-12 rounded-lg shadow-sm"
          />
       </RouterLink>
       <h2 class="font-md text-medium">Karzo</h2>
    </div>

    <div class="w-full max-w-2xl p-8 space-y-6 bg-white shadow-xl rounded-xl">
      <h2 class="text-2xl md:text-3xl font-bold text-center text-gray-900">
        Complete Your Profile
      </h2>

      <p v-if="errorMessage" class="text-red-600 text-sm text-center bg-red-50 p-3 rounded-md border border-red-200" role="alert">
        {{ errorMessage }}
      </p>

      <div v-if="!isTokenValid && !errorMessage" class="text-center py-10">
           <p class="text-gray-500">Loading registration details...</p>
           </div>

      <form v-if="isTokenValid" @submit.prevent="registerPassenger" class="space-y-5">
         <div class="grid grid-cols-1 md:grid-cols-2 gap-x-6 gap-y-5">
            <div>
              <label for="name" class="block text-sm font-medium text-gray-700 mb-1">Full Name</label>
              <input
                id="name"
                type="text"
                v-model="personalDetails.name"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 placeholder-gray-400 text-sm"
                placeholder="Enter your full name"
              />
            </div>

            <div>
              <label for="phone" class="block text-sm font-medium text-gray-700 mb-1">Phone Number</label>
              <input
                id="phone"
                type="tel"
                v-model="personalDetails.phone"
                required
                pattern="[0-9]{10}" title="Please enter a 10-digit phone number"
                class="w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 placeholder-gray-400 text-sm"
                 placeholder="Enter 10-digit number"
              />
            </div>

             <div>
              <label for="age" class="block text-sm font-medium text-gray-700 mb-1">Age</label>
              <input
                id="age"
                type="number"
                v-model.number="personalDetails.age"
                required min="18" max="100"
                class="w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 placeholder-gray-400 text-sm"
                 placeholder="Enter your age"
              />
            </div>

            <div>
              <label for="gender" class="block text-sm font-medium text-gray-700 mb-1">Gender</label>
              <select
                id="gender"
                v-model="personalDetails.gender"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 text-sm bg-white"
              >
                <option value="male">Male</option>
                <option value="female">Female</option>
                <option value="other">Other</option>
                <option value="prefer_not_to_say">Prefer not to say</option>
              </select>
            </div>

            <div class="md:col-span-2">
               <label for="email" class="block text-sm font-medium text-gray-700 mb-1">Email</label>
               <input
                 id="email"
                 type="email"
                 :value="email"
                 disabled
                 class="w-full px-4 py-3 border border-gray-300 rounded-md bg-gray-100 text-gray-500 cursor-not-allowed text-sm"
               />
             </div>

            <div class="md:col-span-2 relative">
              <label for="location" class="block text-sm font-medium text-gray-700 mb-1">Address</label>
              <div class="relative">
                <input
                  id="location"
                  v-model="locationQuery"
                  type="text"
                  @input="debounceFetchLocationSuggestions"
                  class="w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 placeholder-gray-400 text-sm pr-10"
                  placeholder="Search address or use map"
                  autocomplete="off"
                />
                <button
                  type="button"
                  @click="openMapModal"
                  class="absolute inset-y-0 right-0 flex items-center pr-3 text-gray-400 hover:text-indigo-600"
                  title="Pick location on map"
                  aria-label="Pick location on map"
                >
                   <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-5 h-5">
                     <path stroke-linecap="round" stroke-linejoin="round" d="M15 10.5a3 3 0 11-6 0 3 3 0 016 0z" />
                     <path stroke-linecap="round" stroke-linejoin="round" d="M19.5 10.5c0 7.142-7.5 11.25-7.5 11.25S4.5 17.642 4.5 10.5a7.5 7.5 0 1115 0z" />
                   </svg>
                </button>
              </div>
              <ul v-if="locationSuggestions.length" class="absolute z-10 mt-1 w-full bg-white shadow-lg border border-gray-200 rounded-md max-h-60 overflow-auto">
                <li
                  v-for="location in locationSuggestions"
                  :key="location.place_id || location.display_name" @click="selectLocation(location)"
                  class="px-4 py-2 cursor-pointer hover:bg-indigo-50 text-sm"
                >
                  {{ location.display_name }}
                </li>
              </ul>
            </div>

            <div class="md:col-span-2">
               <label for="profile-photo" class="block text-sm font-medium text-gray-700 mb-1">Profile Photo (Optional)</label>
               <input
                  id="profile-photo"
                  type="file"
                  accept="image/png, image/jpeg, image/webp"
                  @change="handleFileChange"
                  class="block w-full text-sm text-gray-500 border border-gray-300 rounded-md cursor-pointer focus:outline-none shadow-sm
                         file:mr-4 file:py-3 file:px-4 file:rounded-l-md file:border-0
                         file:text-sm file:font-semibold file:bg-indigo-50 file:text-indigo-700
                         hover:file:bg-indigo-100"
               />
               </div>
         </div>

        <button
          type="submit"
          :disabled="isLoading"
          class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 transition duration-150 ease-in-out"
        >
          <svg v-if="isLoading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ isLoading ? 'Saving Profile...' : 'Complete Registration' }}
        </button>
      </form>
    </div>

    <div v-if="showMapModal" class="fixed inset-0 bg-gray-900 bg-opacity-75 flex items-center justify-center z-50 p-4" @click.self="closeMapModal"> {/* Allow closing by clicking backdrop */}
      <div class="bg-white rounded-xl w-full max-w-3xl max-h-[90vh] flex flex-col shadow-xl overflow-hidden">
        <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center">
          <h3 class="text-lg font-semibold text-gray-900">Select Location on Map</h3>
          <button @click="closeMapModal" class="text-gray-400 hover:text-gray-600" aria-label="Close map modal">
             <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="2" stroke="currentColor" class="w-6 h-6">
               <path stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12" />
             </svg>
          </button>
        </div>
        <div class="p-2 sm:p-4 flex-1 bg-gray-50 overflow-hidden"> {/* Added background */}
          <div ref="mapContainer" class="w-full h-full rounded-md border border-gray-200" style="min-height: 400px;">
            <div v-if="!mapInstance" class="flex items-center justify-center h-full text-gray-500">Loading map...</div>
          </div>
        </div>
        <div class="px-6 py-4 bg-gray-50 border-t border-gray-200">
          <div v-if="selectedAddress" class="mb-3 p-2 text-sm bg-blue-50 text-blue-800 border border-blue-200 rounded-md">
            <strong class="font-medium">Selected:</strong> {{ selectedAddress }}
          </div>
           <div v-else class="mb-3 text-sm text-gray-500">
             Click or drag the marker on the map to select your precise address.
           </div>
          <div class="flex justify-end space-x-3">
             <button @click="closeMapModal" type="button" class="px-4 py-2 text-sm font-medium rounded-md text-gray-700 bg-white border border-gray-300 shadow-sm hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
              Cancel
            </button>
            <button @click="confirmLocation" type="button" class="px-4 py-2 text-sm font-medium rounded-md text-white bg-indigo-600 border border-transparent shadow-sm hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500" :disabled="!selectedAddress || selectedAddress.includes('Fetching')">
              Confirm Location
            </button>
          </div>
        </div>
      </div>
    </div>

  </div>
</template>