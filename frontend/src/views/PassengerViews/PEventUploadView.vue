<template>
    <PLayoutComponent>
        <PEventUploadComponent @submit-event="handleEventSubmit" />
    </PLayoutComponent>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue';
  import PEventUploadComponent from '@/components/PassengerComponents/PEventUploadComponent.vue'
  import axios from 'axios'
  
  const eventData = ref(null)
  

  const handleEventSubmit = async (data) => {
    try {
      console.log('Event Submitted:', data)
      eventData.value = data
      const response = await axios.post('http://127.0.0.1:8000/api/event/', data)
      console.log('Response:', response.data)
    } catch (error) {
      console.error('Error submitting event:', error)
    }
  }
  </script>
  