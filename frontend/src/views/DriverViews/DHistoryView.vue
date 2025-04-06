<script setup>
import { ref } from 'vue'
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue';

const stats = ref({
  totalSubmissions: 24,
  totalBookings: 18,
  completedRides: 15,
  canceledBookings: 3,
  recentRides: [
    { id: 1, date: '2023-05-15', from: 'Airport', to: 'Downtown', status: 'completed', amount: 1200 },
    { id: 2, date: '2023-05-10', from: 'Home', to: 'Mall', status: 'completed', amount: 800 },
    { id: 3, date: '2023-05-05', from: 'Office', to: 'Restaurant', status: 'canceled', amount: 0 },
    { id: 4, date: '2023-04-28', from: 'Hotel', to: 'Convention Center', status: 'completed', amount: 950 },
  ]
});
</script>

<template>
  <DLayoutComponent>
    <div class="px-4 sm:px-6 lg:px-8 py-6 max-w-7xl mx-auto">
      <h1 class="text-xl sm:text-2xl font-bold text-gray-800 mb-1">Your Ride History</h1>
      <p class="text-sm sm:text-base text-gray-600 mb-6 sm:mb-8">Overview of your activities with Karzo</p>
      
      <!-- Stats Cards -->
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6 mb-8 sm:mb-10">
        <!-- Repeated Cards with same structure -->
        <div
          v-for="(value, key) in {
            'Total Submissions': stats.totalSubmissions,
            'Total Bookings': stats.totalBookings,
            'Completed Rides': stats.completedRides,
            'Canceled Bookings': stats.canceledBookings
          }"
          :key="key"
          class="bg-white rounded-lg shadow-sm p-4 sm:p-6 flex items-center"
        >
          <div
            class="p-2 sm:p-3 rounded-full mr-3 sm:mr-4"
            :class="{
              'bg-blue-100': key === 'Total Submissions',
              'bg-green-100': key === 'Total Bookings',
              'bg-purple-100': key === 'Completed Rides',
              'bg-red-100': key === 'Canceled Bookings'
            }"
          >
            <!-- Add icons dynamically if needed -->
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 sm:h-6 sm:w-6 text-current" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <div class="flex-1">
            <p class="text-xs sm:text-sm font-medium text-gray-500">{{ key }}</p>
            <p class="text-lg sm:text-2xl font-semibold text-gray-800 mt-1">{{ value }}</p>
          </div>
        </div>
      </div>
      
      <!-- Recent Rides Table -->
      <div class="mb-8 sm:mb-10">
        <h2 class="text-lg sm:text-xl font-semibold text-gray-800 mb-3 sm:mb-4">Recent Rides</h2>
        <div class="overflow-x-auto bg-white rounded-lg shadow-sm">
          <table class="min-w-full divide-y divide-gray-200 text-sm">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Date</th>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">From</th>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">To</th>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amount</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="ride in stats.recentRides" :key="ride.id" class="hover:bg-gray-50">
                <td class="px-4 py-3 whitespace-nowrap text-gray-800">{{ ride.date }}</td>
                <td class="px-4 py-3 whitespace-nowrap text-gray-800">{{ ride.from }}</td>
                <td class="px-4 py-3 whitespace-nowrap text-gray-800">{{ ride.to }}</td>
                <td class="px-4 py-3 whitespace-nowrap text-gray-800">
                  <span :class="[
                    'px-2 py-1 rounded-full text-xs font-medium',
                    ride.status === 'completed' ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                  ]">
                    {{ ride.status }}
                  </span>
                </td>
                <td class="px-4 py-3 whitespace-nowrap text-gray-800">
                  {{ ride.amount ? `₹${ride.amount}` : '-' }}
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </DLayoutComponent>
</template>
