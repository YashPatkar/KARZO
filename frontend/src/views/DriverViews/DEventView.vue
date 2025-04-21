<template>
  <DLayoutComponent>
    <div class="container mx-auto px-4 py-6">
      <h1 class="text-3xl font-bold text-gray-800 mb-6 text-center">Upcoming Events</h1>

      <!-- Search Input -->
      <div class="flex justify-center mb-8">
        <input
          type="search"
          v-model="search"
          placeholder="🔍 Search events"
          class="w-[60%] p-2 px-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-green-500"
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
              class="w-full py-2 bg-green-500 hover:bg-green-600 text-white font-semibold rounded-lg transition duration-200"
              @click="openApplicationCard(event)"
            >
              Apply for Ride
            </button>
            <div class="w-[85%] mx-auto h-[1px] opacity-20 bg-slate-800 rounded my-3"></div>
            <div class="flex justify-between items-center text-sm text-gray-500">
              <span 
                class="flex items-center gap-1 font-bold text-md cursor-pointer"
                :class="{ 'text-red-500': event.liked }"
                @click="toggleLike(event.id)"
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

      <!-- Application Card -->
      <div v-if="selectedEvent" class="fixed inset-0 flex items-center justify-center bg-black bg-opacity-50">
        <div class="bg-white p-6 rounded-lg shadow-lg w-96">
          <h2 class="text-xl font-bold text-gray-800 mb-4">
            Apply for Ride
          </h2>
          <p class="text-gray-700 text-sm mb-2">
            Event: <span class="font-semibold">{{ selectedEvent.event_name }}</span>
          </p>
          <p class="text-gray-700 text-sm mb-2">
            Date: <span class="font-semibold">{{ selectedEvent.date }}</span> at <span class="font-semibold">{{ selectedEvent.time }}</span>
          </p>

          <!-- Driver Application Fields -->
          <div>
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
            <button @click="closeModal" class="px-4 py-2 text-gray-600 bg-gray-200 rounded-lg">Cancel</button>
            <button @click="applyForRide" class="px-4 py-2 text-white bg-green-500 hover:bg-green-600 rounded-lg">
              Apply
            </button>
          </div>
        </div>
      </div>

      <!-- Success Popup -->
      <div v-if="showPopup" class="fixed bottom-5 right-5 bg-green-500 text-white px-4 py-2 rounded-lg shadow-lg">
        Application Submitted Successfully! ✅
      </div>
    </div>
  </DLayoutComponent>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue';
import api from '@/api';
import { useDriverStore } from '@/stores/driverStore.js';


const events = ref([]);
const search = ref('');
const selectedEvent = ref(null);
const selectedFromTime = ref('');
const selectedToTime = ref('');
const showPopup = ref(false);

const availableTimes = ['10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM', '3:00 PM', '4:00 PM', '5:00 PM'];



const filteredEvents = computed(() => {
  return events.value.filter(event => 
    event.name.toLowerCase().includes(search.value.toLowerCase()) ||
    event.location.toLowerCase().includes(search.value.toLowerCase()) ||
    event.description.toLowerCase().includes(search.value.toLowerCase())
  );
});

const openApplicationCard = (event) => {
  selectedEvent.value = event;
  selectedFromTime.value = '';
  selectedToTime.value = '';
};

const closeModal = () => {
  selectedEvent.value = null;
};

const getCurrentLocation = async () => {
  if (!navigator.geolocation) {
    alert('Geolocation is not supported by your browser');
    return null;
  }

  try {
    const position = await new Promise((resolve, reject) => {
      navigator.geolocation.getCurrentPosition(resolve, reject, {
        enableHighAccuracy: true,
        timeout: 10000,
        maximumAge: 0
      });
    });

    const { latitude, longitude } = position.coords;
    const address = await reverseGeocode(latitude, longitude);

    return {
      display_name: address,
      lat: latitude,
      lon: longitude
    };
  } catch (error) {
    console.error('Error getting location:', error);
    alert('Could not get your location. Please try again or enter manually.');
    return null;
  }
};


const applyForRide = async () => {
  console.log('Applying for ride with data:', {
    event_id: selectedEvent.value.id,
    from_time: selectedFromTime.value,
    to_time: selectedToTime.value,
  });
  if (!selectedFromTime.value || !selectedToTime.value || !selectedEvent.value) {
    alert('Please fill all required fields.');
    return;
  }
  const location = await getCurrentLocation();
  const driver_email = useDriverStore().fetchdriverData().email
  const bookingData = {
    event_id: selectedEvent.value.id,
    location: location,
    driver_email: driver_email,
    from_time: selectedFromTime.value,
    to_time: selectedToTime.value,
  };

  console.log('Booking data:', bookingData);

  // try {
  //   await api.post('/api/driver/book-ride/', bookingData);
  //   showPopup.value = true;
  //   selectedEvent.value = null;
  //   setTimeout(() => {
  //     showPopup.value = false;
  //   }, 3000);
  // } catch (error) {
  //   console.error('Error submitting application:', error);
  //   alert('Failed to submit application. Please try again.');
  // }
};
console.log('Driver email:', sessionStorage.getItem('driver_email'))
const toggleLike = async (eventId) => {
  try {
    const response = await api.post(`/api/core/events/${eventId}/like/`, {
      email: sessionStorage.getItem('driver_email'),
    });


    // Update local like count and UI
    const updatedEvent = events.value.find(event => event.id === eventId);
    if (updatedEvent) {
      updatedEvent.like_count = response.data.like_count;
      updatedEvent.liked = response.data.liked;
    }
  } catch (error) {
    console.error('Error toggling like:', error);
  }
};


onMounted(async () => {
  try {
    const response = await api.get('/api/core/events/')
    events.value = response.data
    console.log('Fetched events:', events.value)

    // Initial like count load
    await updateLikeCounts()

    // Set up polling for real-time like updates every 5 seconds
    setInterval(updateLikeCounts, 5000)
  } catch (error) {
    console.error('Error fetching events:', error)
  }
})

// Reusable function to update like counts for all events
const updateLikeCounts = async () => {
  for (const event of events.value) {
    try {
      const likeResponse = await api.get(`/api/core/events/${event.id}/like-count/`)
      event.like_count = likeResponse.data.like_count || 0
    } catch (likeError) {
      console.error(`Error fetching like count for event ${event.id}:`, likeError)
    }
  }
}


</script>
