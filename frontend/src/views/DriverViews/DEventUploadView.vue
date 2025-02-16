<template>
  <DLayoutComponent>
    <DEventUploadComponent @submit-event="handleEventSubmit" />
  </DLayoutComponent>
</template>

<script setup>
import { ref } from 'vue'
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue'
import DEventUploadComponent from '@/components/DriverComponents/DEventUploadComponent.vue'
import axios from 'axios'

const eventData = ref(null)

const handleEventSubmit = async (data) => {
  try {
    console.log('Event Submitted:', data)
    eventData.value = data
    const response = await axios.post('http://127.0.0.1:8000/api/event/', eventData.value)
    console.log('Response:', response.data)
  } catch (error) {
    console.error('Error submitting event:', error)
  }
}
</script>
