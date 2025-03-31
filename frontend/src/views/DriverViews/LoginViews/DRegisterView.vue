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
      router.push('/DVerifyView');
    } else if (response.status === 201) {
      // ✅ User does not exist → Send Registration Link
      alert("Registration link sended.");
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
  <div class="flex items-center justify-center min-h-screen bg-gray-100">
    <div class="w-full max-w-md p-6 bg-white shadow-lg rounded-2xl">
      <h2 class="text-2xl font-semibold text-center text-gray-700">Driver Register/Login</h2>
      
      <p v-if="errorMessage" class="text-red-500 text-center mt-3">{{ errorMessage }}</p>

      <form @submit.prevent="handleRegister" class="mt-6">
        <div>
          <label class="block text-sm font-medium text-gray-600">Email Address</label>
          <input
            type="email"
            v-model="email"
            required
            class="w-full mt-2 p-3 border rounded-lg"
            placeholder="Enter your email"
          />
        </div>

        <button
          type="submit"
          class="w-full mt-6 p-3 text-white bg-blue-600 hover:bg-blue-900 rounded-lg font-semibold transition duration-300"
          :disabled="isLoading"
        >
          {{ isLoading ? "Processing..." : "Register" }}
        </button>
      </form>
    </div>
  </div>
</template>
