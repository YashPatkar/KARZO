<template>
    <div class="flex items-center justify-center min-h-screen bg-gray-100">
      <div class="w-full max-w-md p-6 bg-white shadow-lg rounded-2xl">
        <h2 class="text-2xl font-semibold text-center text-gray-700">Verify Your Email</h2>
        <p class="text-center text-gray-600 mt-2">Enter the OTP sent to {{ email }}</p>
  
        <form @submit.prevent="verifyOtp" class="mt-6">
          <div>
            <label for="otp" class="block text-sm font-medium text-gray-600">OTP Code</label>
            <input
              v-model="otp"
              type="text"
              id="otp"
              placeholder="Enter 6-digit OTP"
              class="w-full mt-2 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-center tracking-widest"
              maxlength="6"
              :disabled="isLoading"
            />
          </div>
  
          <button
            type="submit"
            class="w-full mt-6 p-3 text-white bg-blue-600 hover:bg-blue-900 rounded-lg font-semibold transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed"
            :disabled="isLoading || otp.length !== 6"
          >
            {{ isLoading ? "Verifying..." : "Verify OTP" }}
          </button>
        </form>
  
        <p v-if="errorMessage" class="text-red-500 text-center mt-3">{{ errorMessage }}</p>
      </div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import { useRouter } from 'vue-router';
  import api from '@/api';
  
  const otp = ref('');
  const isLoading = ref(false);
  const errorMessage = ref('');
  const router = useRouter();
  const email = ref('');
  
  onMounted(() => {
    email.value = sessionStorage.getItem('driver_email') || '';
    if (!email.value) {
      router.push({ name: 'DRegisterView' });
    }
  });
  
  const verifyOtp = async () => {
    if (otp.value.length !== 6) return;
  
    isLoading.value = true;
    errorMessage.value = '';
  
    try {
      const response = await api.post(`/api/driver/${email.value}/check-verifications/`, { otp: otp.value });
  
      if (response.status === 200) {
        router.push({ name: 'DHomeView' });
      } else {
        errorMessage.value = 'Invalid OTP. Please try again.';
      }
    } catch (error) {
      errorMessage.value = 'Verification failed. Try again.';
    } finally {
      isLoading.value = false;
    }
  };
  </script>
  