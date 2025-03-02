<template>
  <div class="p-6 bg-white rounded-lg shadow-md">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Bike Registration</h2>

    <div class="mb-6">
      <label for="vehicle_number" class="block text-sm font-medium text-gray-700 mb-2">Bike Number</label>
      <input
        type="text"
        id="vehicle_number"
        v-model="vehicleDetails.vehicle_number"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isVehicleNumberValid" class="text-sm text-red-500">Bike Number is required</span>
    </div>

    <div class="mb-6">
      <label for="vehicle_manufacturer" class="block text-sm font-medium text-gray-700 mb-2">Manufacturer</label>
      <input
        type="text"
        id="vehicle_manufacturer"
        v-model="vehicleDetails.vehicle_manufacturer"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isManufacturerValid" class="text-sm text-red-500">Manufacturer is required</span>
    </div>

    <div class="mb-6">
      <label for="vehicle_type" class="block text-sm font-medium text-gray-700 mb-2">Vehicle Type</label>
      <input
        type="text"
        id="vehicle_type"
        v-model="vehicleDetails.vehicle_type"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        readonly
      />
    </div>

    <div class="mb-6">
      <label for="vehicle_model" class="block text-sm font-medium text-gray-700 mb-2">Model</label>
      <input
        type="text"
        id="vehicle_model"
        v-model="vehicleDetails.vehicle_model"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isModelValid" class="text-sm text-red-500">Model is required</span>
    </div>

    <div class="mb-6">
      <label for="vehicle_color" class="block text-sm font-medium text-gray-700 mb-2">Color</label>
      <input
        type="text"
        id="vehicle_color"
        v-model="vehicleDetails.vehicle_color"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isColorValid" class="text-sm text-red-500">Color is required</span>
    </div>

    <div class="mb-6">
      <label for="vehicle_registration_date" class="block text-sm font-medium text-gray-700 mb-2">Registration Date</label>
      <input
        type="date"
        id="vehicle_registration_date"
        v-model="vehicleDetails.vehicle_registration_date"
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
  vehicle_number: '',
  vehicle_manufacturer: '',
  vehicle_type: 'bike', // Default to bike
  vehicle_model: '',
  vehicle_color: '',
  vehicle_registration_date: '',
});

const isVehicleNumberValid = computed(() => vehicleDetails.vehicle_number.trim() !== '');
const isManufacturerValid = computed(() => vehicleDetails.vehicle_manufacturer.trim() !== '');
const isModelValid = computed(() => vehicleDetails.vehicle_model.trim() !== '');
const isColorValid = computed(() => vehicleDetails.vehicle_color.trim() !== '');
const isRegistrationDateValid = computed(() => vehicleDetails.vehicle_registration_date !== '');

const isFormValid = computed(() => {
  return (
    isVehicleNumberValid.value &&
    isManufacturerValid.value &&
    isModelValid.value &&
    isColorValid.value &&
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