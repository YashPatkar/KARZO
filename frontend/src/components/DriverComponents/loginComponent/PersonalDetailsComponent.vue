<template>
  <div class="p-6 bg-white rounded-lg shadow-md">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Personal Details</h2>

    <!-- Profile Photo Upload -->
    <div class="mb-6">
      <label class="block text-sm font-medium text-gray-700 mb-2">Profile Photo</label>
      <input 
        type="file" 
        accept="image/*" 
        @change="handleProfilePhotoUpload"
        class="p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isProfilePhotoValid" class="text-sm text-red-500">Profile Photo is required</span>
    </div>

    <!-- Name Field -->
    <div class="mb-6">
      <label for="name" class="block text-sm font-medium text-gray-700 mb-2">Name</label>
      <input
        type="text"
        id="name"
        v-model="personalDetails.name"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isNameValid" class="text-sm text-red-500">Name is required</span>
    </div>

    <!-- Other Fields -->
    <div v-for="(field, key) in fieldMappings" :key="key" class="mb-6">
      <label :for="key" class="block text-sm font-medium text-gray-700 mb-2">{{ field.label }}</label>
      <input
        v-if="field.type !== 'textarea' && field.type !== 'select'"
        :type="field.type"
        :id="key"
        v-model="personalDetails[key]"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <textarea
        v-else-if="field.type === 'textarea'"
        :id="key"
        v-model="personalDetails[key]"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      ></textarea>
      <select v-else :id="key" v-model="personalDetails[key]" class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200">
        <option v-for="option in field.options" :key="option" :value="option">{{ option }}</option>
      </select>
      <span v-if="!validations[key]" class="text-sm text-red-500">{{ field.error }}</span>
    </div>

    <!-- Email (Pre-filled & Disabled) -->
    <div class="mb-6">
      <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
      <input
        type="email"
        id="email"
        v-model="personalDetails.email"
        class="mt-1 p-3 border rounded-md w-full bg-gray-200 cursor-not-allowed"
        disabled
      />
    </div>

    <!-- Next Button -->
    <button @click="validateAndNext" class="bg-green-500 text-white px-6 py-3 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-200">
      Next
    </button>
  </div>
</template>

<script setup>
import { reactive, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import api from '@/api';

const route = useRoute();
const emit = defineEmits(['next', 'update:personalDetails', 'update:profilePhoto']);

const personalDetails = reactive({
  name: '',
  age: null,
  birth_date: '',
  gender: 'male',
  phone: '',
  location: '',
  pincode: '',
  address: '',
  email: ''
});

const fieldMappings = {
  age: { label: 'Age', type: 'number', error: 'Age is required' },
  birth_date: { label: 'Birth Date', type: 'date', error: 'Birth Date is required' },
  gender: { label: 'Gender', type: 'select', options: ['male', 'female', 'other'] },
  phone: { label: 'Phone Number', type: 'tel', error: 'Phone Number is required' },
  location: { label: 'Location', type: 'text', error: 'Location is required' },
  pincode: { label: 'Pincode', type: 'text', error: 'Pincode is required' },
  address: { label: 'Address', type: 'textarea', error: 'Address is required' },
};

const validations = computed(() => {
  return {
    age: personalDetails.age !== null && personalDetails.age > 0,
    birth_date: !!personalDetails.birth_date,
    phone: !!personalDetails.phone,
    location: !!personalDetails.location,
    pincode: !!personalDetails.pincode,
    address: !!personalDetails.address,
  };
});

onMounted(async () => {
  const token = route.query.token;
  if (!token) {
    console.error("No registration token found");
    return;
  }

  try {
    const response = await api.post("/api/driver/validate-token/", { token });
    personalDetails.email = response.data.email;
  } catch (err) {
    console.error("Token validation failed:", err);
  }
});

const isProfilePhotoValid = computed(() => true); // Remove this if not using profile photo validation here
const isNameValid = computed(() => personalDetails.name.trim() !== '');
const isFormValid = computed(() => 
  isNameValid.value && 
  Object.values(validations.value).every(Boolean)
);

const handleProfilePhotoUpload = (event) => {
  const file = event.target.files[0];
  if (file) {
    emit('update:profilePhoto', file);
  }
};

const validateAndNext = () => {
  if (isFormValid.value) {
    emit('update:personalDetails', personalDetails);
    emit('next');
  } else {
    alert('Please fill all required fields before proceeding.');
  }
};
</script>