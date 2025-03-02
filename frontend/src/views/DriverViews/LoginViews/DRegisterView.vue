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
          />
        </div>

        <button
          type="submit"
          class="w-full mt-6 p-3 text-white bg-blue-600 hover:bg-blue-700 rounded-lg font-semibold transition duration-300"
        >
          Send Sign-In Link
        </button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, provide } from 'vue';
import { useRouter } from 'vue-router';
import { sendSignInEmail } from '@/utils/firebase'; // Import updated function

const email = ref('');
const router = useRouter();

const sendLink = () => {
  sendSignInEmail(email.value).then(() => {
    // Provide the email to child components
    provide('email', email.value);
    // Redirect to the registration form
    router.push({ path: '/register-details' });
  });
};
</script>