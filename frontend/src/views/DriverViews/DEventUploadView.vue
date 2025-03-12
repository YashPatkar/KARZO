<template>
  <DLayoutComponent>
    <DEventUploadComponent @submit-event="handleEventSubmit" />
  </DLayoutComponent>
</template>

<script setup>
import DLayoutComponent from '@/components/DriverComponents/DLayoutComponent.vue'
import DEventUploadComponent from '@/components/DriverComponents/DEventUploadComponent.vue'
import api from '@/api'

const handleEventSubmit = async (data) => {
  try {
    console.log('Event Submitted:', data)
    const response = await api.post('/api/driver/submit-event/', data)
    if(response.status === 201) {
      alert('Event submitted successfully!')
    }
    else{
      alert('Failed to submit event')
    }
  } catch (error) {
    console.error('Error submitting event:', error)
  }
}
</script>
