<template>
    <PLayoutComponent>
      <div class="container mx-auto px-4 py-6">
        <h1 class="text-2xl font-bold text-gray-800 mb-6 text-center">Passenger Dashboard</h1>
  
        <div class="bg-white shadow-lg rounded-lg p-6">
          <canvas ref="passengerChart"></canvas>
        </div>
      </div>
    </PLayoutComponent>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import Chart from 'chart.js/auto';
  import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue';
  
  const passengerChart = ref(null);
  let chartInstance = null;
  
  onMounted(() => {
    if (passengerChart.value) {
      chartInstance = new Chart(passengerChart.value, {
        type: 'bar',
        data: {
          labels: ['Rides Completed', 'Pending Rides', 'Cancelled Rides'],
          datasets: [{
            label: 'Passenger Ride Statistics',
            data: [0, 0, 0], // Initially set to 0
            backgroundColor: ['#4CAF50', '#FFC107', '#F44336']
          }]
        },
        options: {
          responsive: true,
          maintainAspectRatio: false
        }
      });
    }
  });
  </script>
  