<template>
  <div class="p-4 max-w-lg mx-auto">
    <h1 class="text-xl font-semibold text-center mb-4">Select Location</h1>

    <!-- Search Box -->
    <div class="relative">
      <input 
        v-model="searchQuery" 
        type="text" 
        placeholder="Search location..." 
        @input="fetchSuggestions"
        class="w-full p-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
      />
      
      <!-- Suggestions List -->
      <ul v-if="suggestions.length" class="absolute z-10 mt-1 w-full bg-white border rounded-md shadow-md">
        <li 
          v-for="(s, i) in suggestions" 
          :key="i" 
          @click="selectSuggestion(s)"
          class="p-2 hover:bg-gray-100 cursor-pointer text-sm"
        >
          {{ s.display_name }}
        </li>
      </ul>
    </div>

    <!-- Map Component -->
    <DMapComponent 
      :latitude="latitude" 
      :longitude="longitude" 
      @locationSelected="handleLocationSelected" 
      class="mt-4"
    />
  </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from 'axios';
import DMapComponent from '@/components/DriverComponents/DMapComponent.vue';

const searchQuery = ref('');
const suggestions = ref([]);
const latitude = ref(19.0356);
const longitude = ref(72.8421);

const fetchSuggestions = async () => {
  if (!searchQuery.value) {
    suggestions.value = [];
    return;
  }

  try {
    const { data } = await axios.get(
      `https://nominatim.openstreetmap.org/search?format=json&q=${encodeURIComponent(searchQuery.value)}&countrycodes=IN&bounded=1`
    );
    suggestions.value = data.slice(0, 5);
  } catch (error) {
    console.error('Error fetching suggestions:', error);
  }
};

const selectSuggestion = (s) => {
  searchQuery.value = s.display_name;
  latitude.value = parseFloat(s.lat);
  longitude.value = parseFloat(s.lon);
  suggestions.value = [];
};

const handleLocationSelected = ({ lat, lng, address }) => {
  latitude.value = lat;
  longitude.value = lng;
  searchQuery.value = address;
};
</script>
