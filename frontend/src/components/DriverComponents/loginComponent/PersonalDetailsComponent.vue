<template>
  <div class="p-6 bg-white rounded-lg shadow-md">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Personal Details</h2>

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

    <!-- Age Field -->
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

    <!-- Birth Date Field -->
    <div class="mb-6">
      <label for="birth_date" class="block text-sm font-medium text-gray-700 mb-2">Birth Date</label>
      <input
        type="date"
        id="birth_date"
        v-model="personalDetails.birth_date"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isBirthdateValid" class="text-sm text-red-500">Birth Date is required</span>
    </div>

    <!-- Gender Field -->
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

    <!-- Phone Number Field -->
    <div class="mb-6">
      <label for="phone" class="block text-sm font-medium text-gray-700 mb-2">Phone Number</label>
      <input
        type="tel"
        id="phone"
        v-model="personalDetails.phone"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isPhoneValid" class="text-sm text-red-500">Phone Number is required</span>
    </div>

    <!-- Location Field -->
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

    <!-- Pincode Field -->
    <div class="mb-6">
      <label for="pincode" class="block text-sm font-medium text-gray-700 mb-2">Pincode</label>
      <input
        type="text"
        id="pincode"
        v-model="personalDetails.pincode"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <span v-if="!isPincodeValid" class="text-sm text-red-500">Pincode is required</span>
    </div>

    <!-- Address Field -->
    <div class="mb-6">
      <label for="address" class="block text-sm font-medium text-gray-700 mb-2">Address</label>
      <textarea
        id="address"
        v-model="personalDetails.address"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      ></textarea>
      <span v-if="!isAddressValid" class="text-sm text-red-500">Address is required</span>
    </div>

    <!-- Email Field -->
    <div class="mb-6">
      <label for="email" class="block text-sm font-medium text-gray-700 mb-2">Email</label>
      <input
        type="email"
        id="email"
        v-model="personalDetails.email"
        :disabled="!!email"
        class="mt-1 p-3 border rounded-md w-full focus:ring-2 focus:ring-green-200"
      />
      <!-- Make the field disabled if email is provided via inject -->
      <span v-if="!isEmailValid" class="text-sm text-red-500">Email is required</span>
    </div>

    <!-- Next Button -->
    <button
      @click="validateAndNext"
      class="bg-green-500 text-white px-6 py-3 rounded-md hover:bg-green-600 focus:outline-none focus:ring-2 focus:ring-green-200"
    >
      Next
    </button>
  </div>
</template>

<script setup>
import { reactive, computed, inject } from 'vue';

// Inject the email provided by DRegisterView.vue
const email = inject('email', null); // Default to null if email is not provided
console.log(email + ' is the email');
const emit = defineEmits(['next', 'update:personalDetails']);

// Reactive object for personal details
const personalDetails = reactive({
  name: '',
  age: null,
  birth_date: '',
  gender: 'male',
  phone: '',
  location: '',
  pincode: '',
  address: '',
  email: email || '', // Use the injected email if available, otherwise default to empty string
});

// Validation computed properties
const isNameValid = computed(() => personalDetails.name.trim() !== '');
const isAgeValid = computed(() => personalDetails.age !== null && personalDetails.age > 0);
const isBirthdateValid = computed(() => personalDetails.birth_date !== '');
const isPhoneValid = computed(() => personalDetails.phone.trim() !== '');
const isLocationValid = computed(() => personalDetails.location.trim() !== '');
const isPincodeValid = computed(() => personalDetails.pincode.trim() !== '');
const isAddressValid = computed(() => personalDetails.address.trim() !== '');
const isEmailValid = computed(() => personalDetails.email.trim() !== '');

// Check if the entire form is valid
const isFormValid = computed(() => {
  return (
    isNameValid.value &&
    isAgeValid.value &&
    isBirthdateValid.value &&
    isPhoneValid.value &&
    isLocationValid.value &&
    isPincodeValid.value &&
    isAddressValid.value &&
    isEmailValid.value
  );
});

// Validate and proceed to the next step
const validateAndNext = () => {
  if (isFormValid.value) {
    emit('update:personalDetails', personalDetails);
    emit('next');
  } else {
    alert('Please fill all the fields before proceeding.');
  }
};
</script>