<template>
  <PLayoutComponent>
    <PEventUploadComponent @submit-event="handleEventSubmit" />
  </PLayoutComponent>
</template>

<script setup>
import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue'
import PEventUploadComponent from '@/components/PassengerComponents/PEventUploadComponent.vue'
import api from '@/api'

const handleEventSubmit = async (data) => {
  try {
    console.log('Event Submitted:', data)
    const response = await api.post('/api/passenger/submit-event/', data)
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
