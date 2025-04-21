<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import api from "@/api";

const email = ref("");
const errorMessage = ref("");
const isLoading = ref(false);
const router = useRouter();

const handleRegister = async () => {
  isLoading.value = true;
  errorMessage.value = "";

  try {
    const response = await api.post("/api/driver/check-user/", { email: email.value });

    if (response.status === 200) {
      // ✅ User exists → Send OTP and redirect to OTP verification page
      sessionStorage.setItem("driver_email", email.value);
      console.log("Driver email:", email.value);
      router.push('/DVerifyView');
    } else if (response.status === 201) {
      // ✅ User does not exist → Send Registration Link
      alert("Registration link sended.");
      email.value = "";
    }
    else{
        errorMessage.value = "Failed to send registration link. Try again.";
    }
  } catch (err) {
    errorMessage.value = "An error occurred. Please try again.";
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="flex flex-col items-center justify-center min-h-screen bg-gray-50 px-4 py-12">
     

    <div class="w-full max-w-md p-8 space-y-6 bg-white shadow-xl rounded-xl">
      <div class="flex flex-row items-center mb-6 justify-center space-x-2">
        <RouterLink to="/" aria-label="Go to Homepage">
          <img
            src="https://placehold.co/60x60/6366f1/white?text=K&font=raleway"
            alt="Karzo Logo"
            class="h-10 w-10 rounded-xl shadow-sm"
          />
       </RouterLink>
        <h2 class="text-3xl font-bold text-center text-gray-900">
          Driver Portal
        </h2>
      </div>
      <p class="text-center text-sm text-gray-600">
        Enter your email to sign in or register as a Karzo driver.
      </p>

      <form @submit.prevent="handleRegister" class="space-y-5">
         <p v-if="errorMessage" class="text-red-600 text-sm text-center bg-red-50 p-3 rounded-md border border-red-200" role="alert">
           {{ errorMessage }}
        </p>

        <div>
          <label for="driver-email" class="block text-sm font-medium text-gray-700 mb-1">Email Address</label>
          <input
            id="driver-email"
            type="email"
            v-model="email"
            required
            autocomplete="email"
            class="w-full px-4 py-3 border border-gray-300 rounded-md shadow-sm focus:ring-indigo-500 focus:border-indigo-500 placeholder-gray-400 text-sm"
            placeholder="Enter your driver email"
            aria-label="Driver Email Address"
            aria-describedby="email-description"
          />
          <p id="email-description" class="mt-1 text-xs text-gray-500">
            We'll send a verification code or registration link to this email.
          </p>
        </div>

        <button
          type="submit"
          :disabled="isLoading"
          class="w-full flex justify-center py-3 px-4 border border-transparent rounded-md shadow-sm text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 disabled:opacity-50 transition duration-150 ease-in-out"
        >
          <svg v-if="isLoading" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
          </svg>
          {{ isLoading ? "Processing..." : "Continue" }}
        </button>
      </form>

       <p class="text-center text-xs text-gray-500 pt-4 border-t border-gray-200">
         Need help? Visit our
         <a href="#" class="underline hover:text-gray-700">Driver Support Center</a>.
      </p>
    </div>
  </div>
</template>