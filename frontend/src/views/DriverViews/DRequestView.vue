<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import { useRouter } from 'vue-router'
import api from '@/api'
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue'

const router = useRouter()
const eventRequests = ref([])
const driverEmail = sessionStorage.getItem('driver_email')
let interval = null
const isLoading = ref(false)
const error = ref(null)
const proposedPrices = ref({})

const fetchEventRequests = async (retry = false) => {
  isLoading.value = true
  error.value = null
  try {
    const response = await api.get(`/api/driver/event-requests/?email=${driverEmail}`)
    eventRequests.value = response.data
    eventRequests.value.forEach(event => {
      proposedPrices.value[event.id] = 30; // Initialize with minimum price
    });
    isLoading.value = false
  } catch (err) {
    console.error("Error fetching event requests:", err)
    error.value = err.message || 'Failed to fetch event requests.'
    isLoading.value = false
  }
}

const approveRequest = async (event) => {
  if (confirm(`Are you sure you want to approve this request?`)) {
    try {
      isLoading.value = true;
      
      // First make API call to approve the request and get full details
      console.log("Approving request for event:", event);
      const response = await api.post(`/api/driver/approve-request/`, {
        event_id: event.event_id,
        passenger_name: event.passenger_name,
        pickup_location: event.pickup_location,
        driver_email: driverEmail,
        proposed_price: proposedPrices.value[event.id]
      });
  
      // The backend should return the complete event details including coordinates
      const approvedEvent = response.data;
      
      // Validate we have the required coordinates
      if (!approvedEvent.pickup_lat || !approvedEvent.pickup_lng) {
        throw new Error('Missing coordinates in response');
      }

      // Store the approved event details
      sessionStorage.setItem('approved_event', JSON.stringify(approvedEvent));

      // Navigate to the map view with all required fields
      router.push({
        name: 'DMapView',
        query: {
          pickupLat: approvedEvent.pickup_lat,
          pickupLng: approvedEvent.pickup_lng,
          eventName: approvedEvent.event_name,
          passengerName: approvedEvent.passenger_name,
          // Include any other required fields from backend
          eventLat: approvedEvent.event_lat,  // if available
          eventLng: approvedEvent.event_lng   // if available
        }
      });

      // Remove from local list
      eventRequests.value = eventRequests.value.filter(req => req.id !== event.id);
      delete proposedPrices.value[event.id];
      
    } catch (error) {
      console.error("Error approving request:", error);
      alert(`Failed to approve request: ${error.message}`);
    } finally {
      isLoading.value = false;
    }
  }
};

const denyRequest = (id) => {
  if (confirm(`Are you sure you want to deny this request?`)) {
    console.log(`Denying request`);
    eventRequests.value = eventRequests.value.filter(req => req.id !== id);
    delete proposedPrices.value[id];
    alert(`Request denied.`);
  }
};

onMounted(() => {
  fetchEventRequests() // initial fetch
  interval = setInterval(fetchEventRequests, 30000) // poll every 30 seconds
})

onUnmounted(() => {
  clearInterval(interval)
})
</script>

<template>
  <DLayoutComponent>
    <div class="flex justify-between items-center mb-6">
      <h2 class="text-xl font-semibold text-gray-900 flex items-center">
        Event Request Inbox
        <span v-if="!isLoading && !error && eventRequests.length > 0"
          class="ml-3 inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-indigo-600 text-white">
          {{ eventRequests.length }}
        </span>
      </h2>
    </div>

    <div class="bg-white rounded-xl shadow-md border border-gray-200 p-6 min-h-[300px] flex flex-col"
      :aria-busy="isLoading" aria-live="polite">

      <div v-if="isLoading" class="flex-grow flex flex-col items-center justify-center text-center text-gray-500">
        <svg class="animate-spin h-8 w-8 text-indigo-600 mb-4" xmlns="http://www.w3.org/2000/svg" fill="none"
          viewBox="0 0 24 24">
          <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
          <path class="opacity-75" fill="currentColor"
            d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z">
          </path>
        </svg>
        <p class="text-lg font-medium">Loading Requests...</p>
        <p class="text-sm">Please wait a moment.</p>
      </div>

      <div v-else-if="error" class="flex-grow flex flex-col items-center justify-center text-center text-red-600">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-12 w-12 mb-3" fill="none" viewBox="0 0 24 24"
          stroke="currentColor" stroke-width="2">
          <path stroke-linecap="round" stroke-linejoin="round" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
        </svg>
        <p class="text-lg font-semibold mb-1">Oops! Something went wrong.</p>
        <p class="text-sm mb-4 max-w-md">{{ error }}</p>
        <button @click="fetchEventRequests(true)"
          class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-red-500 hover:bg-red-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
            stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round"
              d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
          </svg>
          Retry Loading
        </button>
      </div>

      <ul v-else-if="eventRequests.length > 0" class="space-y-4">
        <li v-for="event in eventRequests" :key="event.id"
          class="p-4 rounded-lg bg-gray-50 border border-gray-200 hover:border-indigo-300 hover:bg-indigo-50 transition-colors duration-150">
          <div class="flex flex-col sm:flex-row justify-between sm:items-center">
            <div class="flex-grow mb-3 sm:mb-0">
              <p class="flex items-center text-sm text-gray-600 mb-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2 text-gray-400" viewBox="0 0 20 20"
                  fill="currentColor">
                  <path fill-rule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
                    clip-rule="evenodd" />
                </svg>
                <strong>Passenger:</strong>&nbsp;<span class="text-gray-800">{{ event.passenger_name }}</span>
              </p>
              <p class="flex items-center text-sm text-gray-600 mb-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2 text-gray-400" viewBox="0 0 20 20"
                  fill="currentColor">
                  <path fill-rule="evenodd"
                    d="M6 2a1 1 0 00-1 1v1H4a2 2 0 00-2 2v10a2 2 0 002 2h12a2 2 0 002-2V6a2 2 0 00-2-2h-1V3a1 1 0 10-2 0v1H7V3a1 1 0 00-1-1zm0 5a1 1 0 000 2h8a1 1 0 100-2H6z"
                    clip-rule="evenodd" />
                </svg>
                <strong>Event:</strong>&nbsp;<span class="text-gray-800">{{ event.event_name }}</span>
              </p>
              <p class="flex items-center text-sm text-gray-600 mb-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2 text-gray-400" viewBox="0 0 20 20"
                  fill="currentColor">
                  <path fill-rule="evenodd"
                    d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z"
                    clip-rule="evenodd" />
                </svg>
                <strong>Pickup:</strong>&nbsp;<span class="text-gray-800">{{ event.pickup_location }}</span>
              </p>
              <p class="flex items-center text-sm text-gray-600 mb-1">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-2 text-gray-400" viewBox="0 0 20 20"
                  fill="currentColor">
                  <path
                    d="M8.433 7.418c.155-.103.346-.196.567-.267v1.698a2.5 2.5 0 00-.567-.267C8.07 8.488 8 8.735 8 9s.07 1.513.433 1.582c.155.103.346.196.567.267v1.698c-.22.071-.412.164-.567.267C8.07 11.513 8 11.265 8 11s.07-1.513.433-1.582zM10 12.75a2.5 2.5 0 100-5 2.5 2.5 0 000 5z" />
                  <path fill-rule="evenodd"
                    d="M12.545 11.957c.336-.1.643-.24.909-.418v-1.08a3.52 3.52 0 00-.909-.417V9c0-.365.07-.635.157-.815a.84.84 0 01.33-.342c.136-.09.3-.15.48-.193V6.05a4.507 4.507 0 00-.48-.193.883.883 0 01-.33-.342C12.57 5.335 12.5 5.065 12.5 4.7V3.001a7 7 0 00-7 0v1.698c0 .365.07.635.158.815.087.18.217.308.372.41.155.103.346.196.567.267v1.698a2.5 2.5 0 00-.567.267C5.07 8.488 5 8.735 5 9s.07 1.513.433 1.582c.155.103.346.196.567.267v1.698c-.22.071-.412.164-.567.267C5.07 11.513 5 11.265 5 11s.07-1.513.433-1.582a3.52 3.52 0 01-.433-.815v-1.19a4.507 4.507 0 00.48-.193c.155-.103.294-.233.372-.41.087-.18.158-.45.158-.815V4.5a.5.5 0 011 0v1.698a2.5 2.5 0 00.567-.267c.155-.103.294-.233.372-.41.087-.18.157-.45.157-.815V4.5a.5.5 0 011 0v1.698c0 .365.07.635.158.815.087.18.217.308.372.41.155.103.346.196.567.267v1.08c-.266.178-.573.317-.909-.417.336.1.643.24.909.418v1.08a3.52 3.52 0 00.909.417V11c0 .365-.07.635-.157.815a.84.84 0 01-.33-.342c-.136.09-.3.15-.48.193v1.598a4.507 4.507 0 00.48.193c.155.103.294.233.372.41.087.18.157.45.157.815v1.698a7 7 0 007 0v-1.698c0-.365-.07-.635-.158-.815a.883.883 0 01-.372-.41 4.507 4.507 0 00-.567-.267v-1.08c.266-.178.573-.317.909-.417z"
                    clip-rule="evenodd" />
                </svg>
                <strong>Distance:</strong>&nbsp;<span class="text-gray-800">{{ event.distance_km }} km</span>
              </p>
              <div class="flex items-center space-x-2 mt-2 sm:mt-0">
                <div class="relative rounded-md shadow-sm">
                  <div class="pointer-events-none absolute inset-y-0 left-0 flex items-center pl-3 text-gray-500">₹
                  </div>
                  <input type="number" :id="'price-' + event.id" v-model="proposedPrices[event.id]" min="30"
                    class="block w-full pl-7 pr-3 py-1.5 border border-gray-300 rounded-md text-gray-900 sm:text-sm focus:ring-indigo-500 focus:border-indigo-500"
                    placeholder="Your Price">
                </div>
                <button @click="approveRequest(event)" aria-label="Approve request"
                  class="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded shadow-sm text-white bg-green-500 hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-green-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd"
                      d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z"
                      clip-rule="evenodd" />
                  </svg>
                  Approve
                </button>
                <button @click="denyRequest(event.id)" aria-label="Deny request"
                  class="inline-flex items-center px-3 py-1.5 border border-gray-300 text-xs font-medium rounded shadow-sm text-gray-700 bg-white hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                  <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4 mr-1" viewBox="0 0 20 20" fill="currentColor">
                    <path fill-rule="evenodd"
                      d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.697a1 1 0 010-1.414z"
                      clip-rule="evenodd" />
                  </svg>
                  Deny
                </button>
              </div>
            </div>
          </div>
        </li>
      </ul>

      <div v-else class="flex-grow flex flex-col items-center justify-center text-center">
        <div class="mb-6">
          <svg class="inline-block h-24 w-24 text-green-500" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
            <path fill-rule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clip-rule="evenodd" />
          </svg>
        </div>
        <h3 class="text-2xl font-semibold text-gray-800 mb-2">
          Nice Work! No Pending Requests
        </h3>
        <p class="text-md text-gray-600 max-w-md mx-auto">
          Awesome job, the queue is currently empty! Any new event requests submitted will show up right here.
        </p>
        <div class="mt-8">
          <button @click="fetchEventRequests(true)"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 mr-2" fill="none" viewBox="0 0 24 24"
              stroke="currentColor" stroke-width="2">
              <path stroke-linecap="round" stroke-linejoin="round"
                d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
            </svg>
            Check for New Requests
          </button>
        </div>
      </div>
    </div>
  </DLayoutComponent>
</template>