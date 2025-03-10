<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md p-6 bg-white shadow-lg rounded-2xl">
      <h2 class="text-2xl font-semibold text-center text-gray-700">Register or Login</h2>

      <form @submit.prevent="sendEmail" class="mt-6">
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
          {{ isLoading ? "Sending..." : "Send Login Link" }}
        </button>
      </form>

      <p v-if="errorMessage" class="text-red-500 text-center mt-3">{{ errorMessage }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/api";
import { sendSignInEmail } from "@/utils/supabase";

const email = ref("");
const isLoading = ref(false);
const errorMessage = ref("");
const router = useRouter();

const sendEmail = async () => {
  if (!email.value) {
    errorMessage.value = "Please enter an email.";
    return;
  }

  isLoading.value = true;
  errorMessage.value = "";

  try {
    const response = await api.get(`http://127.0.0.1:8000/api/driver/${email.value}/check-verifications/`, {
      headers: { "Content-Type": "application/json" },
      withCredentials: true,
    });

    if (response.status === 200) {
      // ✅ If user exists, send OTP via Django and redirect
      sessionStorage.setItem("driver_email", email.value);
      router.push({ name: "DVerifyView" });
    } else if (response.status === 204) {
      // ✅ If user does not exist, send magic link via Supabase
      await sendSignInEmail(email.value);
      errorMessage.value = "A Verification link has been sent to your email.";
    } else {
      errorMessage.value = "Unexpected response. Please try again.";
    }
  } catch (error) {
    errorMessage.value = "An error occurred. Please check your email and try again.";
  } finally {
    isLoading.value = false;
  }
};
</script>
