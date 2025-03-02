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
import { ref, inject } from 'vue';
import api from '@/api';

import PersonalDetailsComponent from '@/components/DriverComponents/loginComponent/PersonalDetailsComponent.vue';
import VehicleRegistrationComponent from '@/components/DriverComponents/loginComponent/VehicleRegistrationComponent.vue';

// Inject the email provided by DRegisterView.vue
const email = inject('email');

const currentStep = ref(1);

const personalDetails = ref({
  name: '',
  age: null,
  birth_date: '',
  gender: 'male',
  phone: '',
  location: '',
  pincode: '',
  address: '',
  email: email, // Use the injected email
});

const vehicleDetails = ref({
  vehicle_number: '',
  vehicle_manufacturer: '',
  vehicle_type: 'bike', // Default to bike
  vehicle_model: '',
  vehicle_color: '',
  vehicle_registration_date: '',
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
    // Prepare data for the backend
    const dataToSend = {
      driver: {
        email: personalDetails.value.email,
      },
      personal_details: {
        ...personalDetails.value,
      },
      vehicle_details: {
        ...vehicleDetails.value,
      },
    };

    // Send data to the backend using Axios
    const response = await api.post('/api/driver/register', dataToSend);
    if (response.status === 200) {
      alert('Registration successful!');
    } else {
      alert('Registration Failed');
    }
  } catch (error) {
    console.error('Error submitting form:', error);
    alert('Registration failed. Please try again.');
  }
};
</script>