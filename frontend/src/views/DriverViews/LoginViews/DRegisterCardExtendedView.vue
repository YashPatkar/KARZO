<template>
    <div class="min-h-screen bg-gray-100 p-8">
      <div v-if="currentStep === 1">
        <PersonalDetailsComponent
          @next="nextStep"
          @update:personalDetails="updatePersonalDetails"
        />
      </div>
      <div v-else-if="currentStep === 2">
        <VehicleRegistrationComponent
          @prev="prevStep"
          @submit="handleSubmit"
          @update:vehicleDetails="updateVehicleDetails"
        />
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import api from '@/api';

  import PersonalDetailsComponent from '@/components/DriverComponents/loginComponent/PersonalDetailsComponent.vue';
  import VehicleRegistrationComponent from '@/components/DriverComponents/loginComponent/VehicleRegistrationComponent.vue';
  
  const currentStep = ref(1);
  
  const personalDetails = ref({
    name: '',
    age: null,
    gender: 'male',
    birthdate: '',
    mobile: '',
    location: '',
    address: '',
    email: '',
    profilePhoto: null,
  });
  
  const vehicleDetails = ref({
    vehicleNumber: '',
    manufacturer: '',
    model: '',
    registrationDate: '',
  });
  
  const nextStep = () => {
    currentStep.value = 2;
  };
  
  const prevStep = () => {
    currentStep.value = 1;
  };
  
  const updatePersonalDetails = (details) => {
    personalDetails.value = { ...personalDetails.value, ...details };
  };
  
  const updateVehicleDetails = (details) => {
    vehicleDetails.value = { ...vehicleDetails.value, ...details };
  };
  
  const handleSubmit = async () => {
    try {
      // Save the image locally
      if (personalDetails.value.profilePhoto) {
        const email = personalDetails.value.email;
        const imageName = `${email}-image.${personalDetails.value.profilePhoto.name.split('.').pop()}`;
        const imagePath = `src/assets/Driver/pp/${imageName}`;
  
        // Convert the file to a base64 string
        const reader = new FileReader();
        reader.onload = (e) => {
          const base64Image = e.target.result;
          // Save the image to the specified path
          // Note: This is a simplified example. In a real app, you might need to handle file saving differently.
          const link = document.createElement('a');
          link.href = base64Image;
          link.download = imagePath;
          link.click();
        };
        reader.readAsDataURL(personalDetails.value.profilePhoto);
      }
  
      // Prepare data for the backend (excluding the image)
      const dataToSend = {
        ...personalDetails.value,
        ...vehicleDetails.value,
        profilePhoto: null, // Exclude the image from the backend payload
      };
  
      // Send data to the backend using Axios
      const response = await api.post('/api/driver/register', dataToSend);
      if(response.status === 200)
      {
          alert('Registration successful!');
      }
      else{
        alert('Registration Failed');
      }
    } catch (error) {
      console.error('Error submitting form:', error);
      alert('Registration failed. Please try again.');
    }
  };
  </script>