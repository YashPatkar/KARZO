<template>
    <DLayoutComponent>
        <DEventUploadComponent @submit-event="handleEventSubmit" />
    </DLayoutComponent>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue';
  import DEventUploadComponent from '@/components/DriverComponents/DEventUploadComponent.vue'
  
  const eventData = ref(null)
  
  const handleEventSubmit = (data) => {
    // Handle the event data here
    console.log('Event Submitted:', data)
    eventData.value = data
  }
  </script>
  