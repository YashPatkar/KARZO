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
        class="w-full py-2 text-white font-semibold rounded-lg transition duration-200"
        :class="event.user_type === 'driver' ? 'bg-green-500 hover:bg-green-600' : 'bg-blue-500 hover:bg-blue-600'"
        @click="openApplyCard(event)"
      >
        {{ event.user_type === 'driver' ? 'Apply for Ride' : 'Book a Ride' }}
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
  {{ event.liked ? `Liked` : `Like` }}
</span>

        <span>Popularity: {{ event.like_count || 0 }}</span>
      </div>
    </div>
  </div>
</div>


<!-- Apply Ride Card -->
<div v-if="selectedEvent" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
  <div class="bg-white p-6 rounded-lg shadow-lg w-96">
    <h2 class="text-xl font-bold text-gray-800 mb-4">
      {{ selectedEvent.user_type === 'driver' ? 'Apply for Ride' : 'Book a Ride' }}
    </h2>
    <p class="text-gray-700 text-sm mb-2">
      Event: <span class="font-semibold">{{ selectedEvent.event_name }}</span>
    </p>
    <p class="text-gray-700 text-sm mb-2">
      Event Submitted by: <span class="font-semibold">{{ selectedEvent.user_type }}</span>
    </p>
    <p class="text-gray-700 text-sm mb-2">
      Date: <span class="font-semibold">{{ selectedEvent.date }}</span> at <span class="font-semibold">{{ selectedEvent.time }}</span>
    </p>

    <!-- Show Time Slot selection only for Drivers -->
    <div v-if="selectedEvent.user_type === 'driver'">
      <label class="block text-sm font-medium text-gray-700 mb-1">Select Time Slot:</label>
      <div class="flex gap-2">
        <select v-model="selectedFromTime" class="w-1/2 p-2 border border-gray-300 rounded-lg">
          <option disabled value="">From</option>
          <option v-for="time in availableTimes" :key="time" :value="time">{{ time }}</option>
        </select>

        <select v-model="selectedToTime" class="w-1/2 p-2 border border-gray-300 rounded-lg">
          <option disabled value="">To</option>
          <option v-for="time in availableTimes" :key="time" :value="time">{{ time }}</option>
        </select>
      </div>
    </div>

    <div class="flex justify-end gap-2 mt-4">
      <button @click="selectedEvent = null" class="px-4 py-2 text-gray-600 bg-gray-200 rounded-lg">Cancel</button>
      <button @click="applyForRide" class="px-4 py-2 text-white bg-green-500 hover:bg-green-600 rounded-lg">
        {{ selectedEvent.user_type === 'driver' ? 'Apply' : 'Book' }}
      </button>
    </div>
  </div>
</div>

      <!-- Success Popup -->
      <div v-if="showPopup" class="fixed bottom-5 right-5 bg-green-500 text-white px-4 py-2 rounded-lg shadow-lg">
        Applied for Ride Successfully! ✅
      </div>
    </div>
  </PLayoutComponent>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue';
import api from '@/api';

const events = ref([]);
const search = ref('');
const selectedEvent = ref(null);
const selectedFromTime = ref('');
const selectedToTime = ref('');
const showPopup = ref(false);

const availableTimes = ['10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM'];

onMounted(async () => {
  try {
    const response = await api.get('/api/core/events/');
    events.value = response.data;
  } catch (error) {
    console.error('Error fetching events:', error);
  }
});

const filteredEvents = computed(() => {
  return events.value.filter(event => 
    event.name.toLowerCase().includes(search.value.toLowerCase()) ||
    event.location.toLowerCase().includes(search.value.toLowerCase()) ||
    event.description.toLowerCase().includes(search.value.toLowerCase())
  );
});

const openApplyCard = (event) => {
  selectedEvent.value = event;
  selectedFromTime.value = '';
  selectedToTime.value = '';
};

// Handle like/unlike event
const toggleLike = async (event) => {
  try {
    const response = await api.post(`/api/core/events/${event.id}/like/`, {
      email: event.email, // Send the user's email
    });

    event.liked = response.data.liked;
    event.like_count = response.data.like_count;
  } catch (error) {
    console.error("Error toggling like:", error);
  }
};



const applyForRide = () => {
  if (!selectedFromTime.value || !selectedToTime.value) {
    alert('Please select both From and To time slots.');
    return;
  }

  // Simulate backend request (Replace with API call)
  setTimeout(() => {
    showPopup.value = true;
    selectedEvent.value = null;

    // Hide popup after 3 seconds
    setTimeout(() => {
      showPopup.value = false;
    }, 3000);
  }, 500);
};
</script>
