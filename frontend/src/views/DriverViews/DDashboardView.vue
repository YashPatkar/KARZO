<template>
    <DLayoutComponent>
      <div class="container mx-auto px-4 py-6">
        <h1 class="text-2xl font-bold text-gray-800 mb-6 text-center">driver Dashboard</h1>
  
        <div class="bg-white shadow-lg rounded-lg p-6">
          <canvas ref="driverChart"></canvas>
        </div>
      </div>
    </DLayoutComponent>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import Chart from 'chart.js/auto';
  import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue';
  
  const driverChart = ref(null);
  let chartInstance = null;
  
  onMounted(() => {
    if (driverChart.value) {
      chartInstance = new Chart(driverChart.value, {
        type: 'bar',
        data: {
          labels: ['Rides Completed', 'Pending Rides', 'Cancelled Rides'],
          datasets: [{
            label: 'driver Ride Statistics',
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
  