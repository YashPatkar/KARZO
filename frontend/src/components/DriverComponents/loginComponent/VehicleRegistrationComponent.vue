<template>
    <div class="p-6 bg-white rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold mb-6 text-gray-800">Bike Registration</h2>
  
      <div class="mb-6">
        <label for="vehicleNumber" class="block text-sm font-medium text-gray-700 mb-2">Bike Number</label>
        <input
          type="text"
          id="vehicleNumber"
          v-model="vehicleDetails.vehicleNumber"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isVehicleNumberValid" class="text-sm text-red-500">Bike Number is required</span>
      </div>
  
      <div class="mb-6">
        <label for="manufacturer" class="block text-sm font-medium text-gray-700 mb-2">Manufacturer</label>
        <input
          type="text"
          id="manufacturer"
          v-model="vehicleDetails.manufacturer"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isManufacturerValid" class="text-sm text-red-500">Manufacturer is required</span>
      </div>
  
      <div class="mb-6">
        <label for="model" class="block text-sm font-medium text-gray-700 mb-2">Model</label>
        <input
          type="text"
          id="model"
          v-model="vehicleDetails.model"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isModelValid" class="text-sm text-red-500">Model is required</span>
      </div>
  
      <div class="mb-6">
        <label for="registrationDate" class="block text-sm font-medium text-gray-700 mb-2">Registration Date</label>
        <input
          type="date"
          id="registrationDate"
          v-model="vehicleDetails.registrationDate"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isRegistrationDateValid" class="text-sm text-red-500">Registration Date is required</span>
      </div>
  
      <div class="flex justify-between">
        <button @click="prev" class="bg-gray-500 text-white px-6 py-3 rounded-md hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-gray-200">Previous</button>
        <button @click="validateAndSubmit" class="bg-green-500 text-white px-6 py-3 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-200">Submit</button>
      </div>
    </div>
  </template>
  
  <script setup>
  import { reactive, computed } from 'vue';
  
  const emit = defineEmits(['prev', 'submit', 'update:vehicleDetails']);
  
  const vehicleDetails = reactive({
    vehicleNumber: '',
    manufacturer: '',
    model: '',
    registrationDate: '',
  });
  
  const isVehicleNumberValid = computed(() => vehicleDetails.vehicleNumber.trim() !== '');
  const isManufacturerValid = computed(() => vehicleDetails.manufacturer.trim() !== '');
  const isModelValid = computed(() => vehicleDetails.model.trim() !== '');
  const isRegistrationDateValid = computed(() => vehicleDetails.registrationDate !== '');
  
  const isFormValid = computed(() => {
    return (
      isVehicleNumberValid.value &&
      isManufacturerValid.value &&
      isModelValid.value &&
      isRegistrationDateValid.value
    );
  });
  
  const prev = () => {
    emit('prev');
  };
  
  const validateAndSubmit = () => {
    if (isFormValid.value) {
      emit('update:vehicleDetails', vehicleDetails);
      emit('submit');
    } else {
      alert('Please fill all the fields before submitting.');
    }
  };
  </script>