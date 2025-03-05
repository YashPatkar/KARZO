<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md p-6 bg-white shadow-lg rounded-2xl">
      <h2 class="text-2xl font-semibold text-center text-gray-700">Register with Email</h2>

      <form @submit.prevent="sendLink" class="mt-6">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-600">Email Address</label>
          <input
            v-model="email"
            type="email"
            id="email"
            placeholder="Enter your email"
            class="w-full mt-2 p-3 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            :disabled="isLoading"
          />
        </div>

        <button
          type="submit"
          class="w-full mt-6 p-3 text-white bg-blue-600 hover:bg-blue-900 rounded-lg font-semibold transition duration-300 disabled:bg-gray-400 disabled:cursor-not-allowed"
          :disabled="isLoading"
        >
          {{ isLoading ? "Please Wait..." : "Send Sign-In Link" }}
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useRouter } from 'vue-router';
import { sendSignInEmail } from '@/utils/supabase';
import api from '@/api';

const email = ref('');
const isLoading = ref(false);
const router = useRouter();

const sendLink = async () => {
  isLoading.value = true;

  try {
    const response = await api.get(`/driver/${email.value}/check-verifications/`);

    if (response.status === 200) {
      // Redirect to verification page if the user is verified
      router.push({ name: 'DVerifyView'});
    } else if (response.status === 204) {
      // If user is not verified, send sign-in email
      await sendSignInEmail(email.value);
    } else {
      alert('An error occurred. Please try again.');
    }
  } catch (error) {
    console.error(error);
    alert('Failed to check verification status.');
  } finally {
    isLoading.value = false; // Ensure loading state is reset
  }
};
</script>