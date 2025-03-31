<template>
  <div class="p-6 bg-white rounded-lg shadow-md">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Bike Registration</h2>

    <div v-for="(field, key) in vehicleFields" :key="key" class="mb-6">
      <label :for="key" class="block text-sm font-medium text-gray-700 mb-2">{{ field.label }}</label>
      <input
        :type="field.type"
        :id="key"
        v-model="vehicleDetails[key]"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        :readonly="field.readonly"
      />
      <span v-if="!field.validator(vehicleDetails[key])" class="text-sm text-red-500">{{ field.errorMessage }}</span>
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
  vehicle_type: 'bike',
  vehicle_model: '',
  vehicle_color: '',
  vehicle_registration_number: '',
  vehicle_registration_date: ''
});

// Safe validator functions
const requiredTextValidator = (val) => val?.trim?.() !== '';
const requiredValidator = (val) => val !== null && val !== '';

const vehicleFields = {
  vehicle_number: { 
    label: 'Bike Number', 
    type: 'text', 
    errorMessage: 'Bike Number is required', 
    validator: requiredTextValidator 
  },
  vehicle_manufacturer: { 
    label: 'Manufacturer', 
    type: 'text', 
    errorMessage: 'Manufacturer is required', 
    validator: requiredTextValidator 
  },
  vehicle_type: { 
    label: 'Vehicle Type', 
    type: 'text', 
    readonly: true, 
    validator: () => true 
  },
  vehicle_model: { 
    label: 'Model', 
    type: 'text', 
    errorMessage: 'Model is required', 
    validator: requiredTextValidator 
  },
  vehicle_color: { 
    label: 'Color', 
    type: 'text', 
    errorMessage: 'Color is required', 
    validator: requiredTextValidator 
  },
  vehicle_registration_number: { 
    label: 'Registration Number', 
    type: 'text', 
    errorMessage: 'Registration Number is required', 
    validator: requiredTextValidator 
  },
  vehicle_registration_date: { 
    label: 'Registration Date', 
    type: 'date', 
    errorMessage: 'Registration Date is required', 
    validator: requiredValidator 
  }
};

const isFormValid = computed(() => {
  return Object.entries(vehicleFields).every(([key, field]) => {
    return field.validator(vehicleDetails[key]);
  });
});

const prev = () => {
  emit('prev');
};

const validateAndSubmit = () => {
  if (isFormValid.value) {
    emit('update:vehicleDetails', vehicleDetails);
    emit('submit');
  } else {
    alert('Please fill all the required fields before submitting.');
  }
};
</script>