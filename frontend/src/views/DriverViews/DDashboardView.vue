<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue';
import Chart from 'chart.js/auto';
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue';

// --- Chart Refs ---
const eventImpressionsChartRef = ref(null);
const eventPerformanceChartRef = ref(null);
// (Removed refs for ride-specific charts)

// --- Chart Instances ---
let eventImpressionsChartInstance = null;
let eventPerformanceChartInstance = null;
// (Removed instances for ride-specific charts)

// --- Placeholder Data (Replace with actual API data) ---
const eventKpiData = ref({
  totalEventsSubmitted: 24,
  totalImpressions: 15780, // Views on submitted events
  totalLikes: 950,         // Likes received on submitted events
  avgLikesPerEvent: (950 / 18).toFixed(1), // Calculate average
});

// Placeholder data for top performing events submitted by this passenger
const topEventsData = ref([
  { id: 101, name: 'Weekend Bandra Cycle Meetup', dateSubmitted: 'Mar 15, 2025', impressions: 3200, likes: 250, status: 'Active' },
  { id: 102, name: 'Kala Ghoda Art Walk', dateSubmitted: 'Feb 01, 2025', impressions: 5100, likes: 380, status: 'Past' },
  { id: 103, name: 'Food Truck Rally - Powai Lake', dateSubmitted: 'Apr 01, 2025', impressions: 2500, likes: 150, status: 'Active' },
  { id: 104, name: 'Classic Car Show - BKC', dateSubmitted: 'Mar 20, 2025', impressions: 1850, likes: 85, status: 'Past' },
]);

// --- Chart Initialization Logic ---
const initializeEventCharts = () => {
  const ctxImpressions = eventImpressionsChartRef.value?.getContext('2d');
  const ctxPerformance = eventPerformanceChartRef.value?.getContext('2d');

  // Common Chart Options (reuse or adapt from previous example)
  const commonOptions = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'bottom', labels: { boxWidth: 12, padding: 15, font: { size: 11 } } },
      tooltip: { backgroundColor: 'rgba(0, 0, 0, 0.7)', titleFont: { size: 13 }, bodyFont: { size: 11 }, padding: 8, cornerRadius: 4 }
    },
    scales: {
      x: { grid: { display: false }, ticks: { font: { size: 10 } } },
      y: { grid: { color: '#e5e7eb', borderDash: [3, 3] }, ticks: { font: { size: 10 }, padding: 8 }, beginAtZero: true }
    }
  };

  // 1. Event Impressions Over Time (Area Chart)
  if (ctxImpressions) {
    eventImpressionsChartInstance = new Chart(ctxImpressions, {
      type: 'line', // Use 'line' with fill for area effect
      data: {
        labels: ['Nov \'24', 'Dec \'24', 'Jan \'25', 'Feb \'25', 'Mar \'25', 'Apr \'25'],
        datasets: [{
          label: 'Total Event Impressions',
          data: [1200, 1800, 2500, 4800, 3900, eventKpiData.value.totalImpressions - (1200+1800+2500+4800+3900)], // Example distribution
          borderColor: 'rgb(79, 70, 229)', // Indigo
          backgroundColor: 'rgba(79, 70, 229, 0.2)', // Lighter fill
          tension: 0.3,
          fill: true, // Make it an area chart
          pointBackgroundColor: 'rgb(79, 70, 229)',
          pointBorderWidth: 1,
          pointRadius: 3,
          pointHoverRadius: 5
        }]
      },
      options: {
        ...commonOptions,
        plugins: { ...commonOptions.plugins, legend: { display: false } } // Hide legend for single dataset
      }
    });
  }

  // 2. Event Performance Breakdown (Bar Chart - Top 3 Events)
  if (ctxPerformance) {
    // Get top 3 events based on impressions for the chart
    const top3Events = [...topEventsData.value].sort((a, b) => b.impressions - a.impressions).slice(0, 3);

    eventPerformanceChartInstance = new Chart(ctxPerformance, {
      type: 'bar',
      data: {
        labels: top3Events.map(event => event.name.substring(0, 15) + (event.name.length > 15 ? '...' : '')), // Shorten labels
        datasets: [
          {
            label: 'Impressions',
            data: top3Events.map(event => event.impressions),
            backgroundColor: 'rgba(79, 70, 229, 0.7)', // Indigo
            borderColor: 'rgb(79, 70, 229)',
            borderWidth: 1,
            borderRadius: 4,
            barThickness: 25,
            yAxisID: 'yImpressions', // Assign to left axis
          },
           {
            label: 'Likes',
            data: top3Events.map(event => event.likes),
            backgroundColor: 'rgba(16, 185, 129, 0.7)', // Emerald
            borderColor: 'rgb(16, 185, 129)',
            borderWidth: 1,
            borderRadius: 4,
             barThickness: 25,
             yAxisID: 'yLikes', // Assign to right axis
          }
        ]
      },
      options: {
        ...commonOptions,
        scales: {
           x: { ...commonOptions.scales.x }, // Keep common X axis settings
           yImpressions: { // Left Y Axis for Impressions
             ...commonOptions.scales.y,
             position: 'left',
             grid: { ...commonOptions.scales.y.grid, drawOnChartArea: true }, // Main grid lines
              title: { display: true, text: 'Impressions', font: { size: 10 } }
           },
           yLikes: { // Right Y Axis for Likes
              position: 'right',
              grid: { drawOnChartArea: false }, // No grid lines for this axis
              ticks: { font: { size: 10 }, padding: 8 },
              beginAtZero: true,
              title: { display: true, text: 'Likes', font: { size: 10 } }
           }
        },
         plugins: { ...commonOptions.plugins, legend: { display: true, position: 'top' } } // Show legend at top
      }
    });
  }
};

// --- Lifecycle Hooks ---
onMounted(() => {
  // Fetch actual data from API here and update refs
  initializeEventCharts();
});

onBeforeUnmount(() => {
  // Destroy charts to prevent memory leaks
  eventImpressionsChartInstance?.destroy();
  eventPerformanceChartInstance?.destroy();
});

// --- Helper Functions ---
const formatNumber = (value) => {
  // Simple number formatter for large numbers (e.g., 15780 -> 15.8k)
  if (value >= 1000) {
    return (value / 1000).toFixed(1) + 'k';
  }
  return value.toString();
};

const getEventStatusClass = (status) => {
  switch (status?.toLowerCase()) {
    case 'active': return 'bg-green-100 text-green-800';
    case 'past': return 'bg-gray-100 text-gray-600';
    case 'pending': return 'bg-yellow-100 text-yellow-800';
    case 'rejected': return 'bg-red-100 text-red-800';
    default: return 'bg-gray-100 text-gray-800';
  }
};
</script>

<template>
  <DLayoutComponent>
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="mb-8 md:flex md:items-center md:justify-between">
        <div>
          <h1 class="text-3xl font-bold text-gray-900">Event Dashboard</h1>
          <p class="mt-1 text-sm text-gray-600">Track the performance of your submitted events.</p>
        </div>
        <div class="mt-4 md:mt-0">
          <button type="button" class="inline-flex items-center px-4 py-2 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
             <svg class="-ml-1 mr-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
            Submit New Event
          </button>
        </div>
      </div>

      <div class="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-3 mb-8">
        <div class="bg-white overflow-hidden shadow-lg rounded-xl border border-gray-100">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0 bg-blue-500 rounded-md p-3">
                 <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 012.25-2.25h13.5A2.25 2.25 0 0121 7.5v11.25m-18 0A2.25 2.25 0 005.25 21h13.5A2.25 2.25 0 0021 18.75m-18 0v-7.5A2.25 2.25 0 015.25 9h13.5A2.25 2.25 0 0121 11.25v7.5" /></svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 truncate">Events Submitted</dt>
                  <dd class="text-2xl font-bold text-gray-900">{{ eventKpiData.totalEventsSubmitted }}</dd>
                </dl>
              </div>
            </div>
          </div>
        </div>
        <div class="bg-white overflow-hidden shadow-lg rounded-xl border border-gray-100">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0 bg-indigo-500 rounded-md p-3">
                 <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M2.036 12.322a1.012 1.012 0 010-.639C3.423 7.51 7.36 4.5 12 4.5c4.638 0 8.573 3.007 9.963 7.178.07.207.07.431 0 .639C20.577 16.49 16.64 19.5 12 19.5c-4.638 0-8.573-3.007-9.963-7.178z" /><path stroke-linecap="round" stroke-linejoin="round" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" /></svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 truncate">Total Impressions</dt>
                  <dd class="text-2xl font-bold text-gray-900">{{ formatNumber(eventKpiData.totalImpressions) }}</dd>
                </dl>
              </div>
            </div>
          </div>
        </div>
        <div class="bg-white overflow-hidden shadow-lg rounded-xl border border-gray-100">
          <div class="p-5">
            <div class="flex items-center">
              <div class="flex-shrink-0 bg-rose-500 rounded-md p-3">
                 <svg class="h-6 w-6 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M21 8.25c0-2.485-2.099-4.5-4.688-4.5-1.935 0-3.597 1.126-4.312 2.733-.715-1.607-2.377-2.733-4.313-2.733C5.1 3.75 3 5.765 3 8.25c0 7.22 9 12 9 12s9-4.78 9-12z" /></svg>
              </div>
              <div class="ml-5 w-0 flex-1">
                <dl>
                  <dt class="text-sm font-medium text-gray-500 truncate">Avg. Likes / Event</dt>
                  <dd class="text-2xl font-bold text-gray-900">{{ eventKpiData.avgLikesPerEvent }}</dd>
                </dl>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 gap-6 lg:grid-cols-3">
        <div class="lg:col-span-2 bg-white shadow-lg rounded-xl p-6 border border-gray-100">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Event Impressions Trend</h3>
          <div class="h-80">
            <canvas ref="eventImpressionsChartRef"></canvas>
          </div>
        </div>

        <div class="lg:col-span-1 bg-white shadow-lg rounded-xl p-6 border border-gray-100 flex flex-col">
          <h3 class="text-lg font-semibold text-gray-900 mb-4">Top Events by Impressions</h3>
          <div class="flex-grow overflow-y-auto">
             <ul role="list" class="divide-y divide-gray-200">
                <li v-for="event in [...topEventsData].sort((a,b) => b.impressions - a.impressions)" :key="event.id" class="py-3 flex justify-between items-center">
                   <div class="flex-1 min-w-0">
                      <p class="text-sm font-medium text-gray-800 truncate">{{ event.name }}</p>
                      <p class="text-xs text-gray-500">Submitted: {{ event.dateSubmitted }}</p>
                   </div>
                   <div class="text-right ml-4">
                      <p class="text-sm font-semibold text-indigo-600">{{ formatNumber(event.impressions) }} <span class="text-xs text-gray-500 font-normal">views</span></p>
                      <p class="text-xs text-rose-600">{{ formatNumber(event.likes) }} <span class="text-xs text-gray-500 font-normal">likes</span></p>
                   </div>
                </li>
                 <li v-if="topEventsData.length === 0" class="py-4 text-center text-sm text-gray-500">
                    No event data available.
                 </li>
             </ul>
          </div>
           <div class="mt-4 text-right border-t border-gray-200 pt-3">
              <a href="#" class="text-sm font-medium text-indigo-600 hover:text-indigo-500">View All Events &rarr;</a>
           </div>
        </div>

        <div class="lg:col-span-3 bg-white shadow-lg rounded-xl p-6 border border-gray-100">
           <h3 class="text-lg font-semibold text-gray-900 mb-4">Performance of Top Events</h3>
           <div class="h-80">
             <canvas ref="eventPerformanceChartRef"></canvas>
           </div>
         </div>
      </div>
    </div>
  </DLayoutComponent>
</template>

<style scoped>
canvas {
  max-height: 100%;
}
</style>