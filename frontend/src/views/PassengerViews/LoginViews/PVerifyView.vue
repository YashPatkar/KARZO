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

      <!-- Resend OTP Button with Cooldown -->
      <button
        @click="resendOtp"
        class="w-full mt-3 p-3 text-white bg-gray-600 hover:bg-gray-800 rounded-lg font-semibold transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed"
        :disabled="isResending || cooldown > 0"
      >
        {{ cooldown > 0 ? `Resend OTP in ${cooldown}s` : "Resend OTP" }}
      </button>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import api from '@/api';

const otp = ref('');
const isLoading = ref(false);
const isResending = ref(false);
const errorMessage = ref('');
const router = useRouter();
const email = ref('');
const cooldown = ref(0);

onMounted(() => {
  email.value = sessionStorage.getItem('passenger_email') || '';
  if (!email.value) {
    router.push({ name: 'PRegisterView' });
  }
});

// OTP Verification
const verifyOtp = async () => {
  if (otp.value.length !== 6) return;

  isLoading.value = true;
  errorMessage.value = '';

  try {
    const response = await api.post(`/api/passenger/check-otp/`, { otp: otp.value, email: email.value });

    if (response.status === 200) {
      router.push({ name: 'PEventView' });
    } else {
      errorMessage.value = 'Invalid OTP. Please try again.';
    }
  } catch (error) {
    errorMessage.value = error.response?.data?.message || 'Verification failed. Try again.';
  } finally {
    isLoading.value = false;
  }
};

// Resend OTP with Cooldown
const resendOtp = async () => {
  if (cooldown.value > 0) return;

  isResending.value = true;
  errorMessage.value = '';

  try {
    const response = await api.post(`/api/passenger/resend-otp/${email.value}/`);

    if (response.status === 200) {
      alert('OTP has been resent. Please check your email.');
      startCooldown();
    } else {
      errorMessage.value = 'Failed to resend OTP. Please try again later.';
    }
  } catch (error) {
    errorMessage.value = 'Error resending OTP. Please try again.';
  } finally {
    isResending.value = false;
  }
};

// Start 30-second cooldown after resending OTP
const startCooldown = () => {
  cooldown.value = 30; // Set cooldown time in seconds
  const interval = setInterval(() => {
    cooldown.value--;
    if (cooldown.value === 0) clearInterval(interval);
  }, 1000);
};
</script>
