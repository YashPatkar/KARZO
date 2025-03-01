<template>
    <div class="p-6 bg-white rounded-lg shadow-md">
      <h2 class="text-2xl font-semibold mb-6 text-gray-800">Personal Details</h2>
  
      <div class="mb-6">
        <label for="profilePhoto" class="block text-sm font-medium text-gray-700 mb-2">Profile Photo</label>
        <input
          type="file"
          id="profilePhoto"
          accept="image/*"
          @change="handleProfilePhoto"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
      </div>
  
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
  
      <div class="mb-6">
        <label for="age" class="block text-sm font-medium text-gray-700 mb-2">Age</label>
        <input
          type="number"
          id="age"
          v-model="personalDetails.age"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isAgeValid" class="text-sm text-red-500">Age is required</span>
      </div>
  
      <div class="mb-6">
        <label for="gender" class="block text-sm font-medium text-gray-700 mb-2">Gender</label>
        <select
          id="gender"
          v-model="personalDetails.gender"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        >
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>
  
      <div class="mb-6">
        <label for="birthdate" class="block text-sm font-medium text-gray-700 mb-2">Birth Date</label>
        <input
          type="date"
          id="birthdate"
          v-model="personalDetails.birthdate"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isBirthdateValid" class="text-sm text-red-500">Birth Date is required</span>
      </div>
  
      <div class="mb-6">
        <label for="mobile" class="block text-sm font-medium text-gray-700 mb-2">Mobile Number</label>
        <input
          type="tel"
          id="mobile"
          v-model="personalDetails.mobile"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isMobileValid" class="text-sm text-red-500">Mobile Number is required</span>
      </div>
  
      <div class="mb-6">
        <label for="location" class="block text-sm font-medium text-gray-700 mb-2">Location</label>
        <input
          type="text"
          id="location"
          v-model="personalDetails.location"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isLocationValid" class="text-sm text-red-500">Location is required</span>
      </div>
  
      <div class="mb-6">
        <label for="address" class="block text-sm font-medium text-gray-700 mb-2">Address</label>
        <textarea
          id="address"
          v-model="personalDetails.address"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        ></textarea>
        <span v-if="!isAddressValid" class="text-sm text-red-500">Address is required</span>
      </div>
  
      <div class="mb-6">
        <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
        <input
          type="email"
          id="email"
          v-model="personalDetails.email"
          class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
        />
        <span v-if="!isEmailValid" class="text-sm text-red-500">Email is required</span>
      </div>
  
      <button @click="validateAndNext" class="bg-green-500 text-white px-6 py-3 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-200">Next</button>
    </div>
  </template>
  
  <script setup>
  import { reactive, computed } from 'vue';
  
  const emit = defineEmits(['next', 'update:personalDetails']);
  
  const personalDetails = reactive({
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
  
  const isNameValid = computed(() => personalDetails.name.trim() !== '');
  const isAgeValid = computed(() => personalDetails.age !== null && personalDetails.age > 0);
  const isBirthdateValid = computed(() => personalDetails.birthdate !== '');
  const isMobileValid = computed(() => personalDetails.mobile.trim() !== '');
  const isLocationValid = computed(() => personalDetails.location.trim() !== '');
  const isAddressValid = computed(() => personalDetails.address.trim() !== '');
  const isEmailValid = computed(() => personalDetails.email.trim() !== '');
  
  const isFormValid = computed(() => {
    return (
      isNameValid.value &&
      isAgeValid.value &&
      isBirthdateValid.value &&
      isMobileValid.value &&
      isLocationValid.value &&
      isAddressValid.value &&
      isEmailValid.value
    );
  });
  
  const handleProfilePhoto = (event) => {
    const file = event.target.files[0];
    if (file) {
      personalDetails.profilePhoto = file;
    }
  };
  
  const validateAndNext = () => {
    if (isFormValid.value) {
      emit('update:personalDetails', personalDetails);
      emit('next');
    } else {
      alert('Please fill all the fields before proceeding.');
    }
  };
  </script>