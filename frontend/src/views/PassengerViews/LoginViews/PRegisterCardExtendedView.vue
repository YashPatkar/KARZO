<script setup>
import { onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "@/api";

const route = useRoute();
const router = useRouter();
const token = ref(route.query.token);
const email = ref("");
const errorMessage = ref("");
const isTokenValid = ref(false);
const isLoading = ref(false);
const profilePhoto = ref(null);

const personalDetails = reactive({
  name: "",
  age: null,
  gender: "male",
  phone: "",
  address: "",
});

// Validate token on mount
onMounted(async () => {
  if (!token.value) {
    errorMessage.value = "Invalid link.";
    return;
  }

  try {
    const response = await api.post("/api/passenger/validate-token/", {
      token: token.value,
    });

    email.value = response.data.email; // Prefill email
    isTokenValid.value = true;
  } catch (err) {
    errorMessage.value = "Invalid or expired token.";
  }
});

// Handle file selection
const handleFileChange = (event) => {
  const file = event.target.files[0];
  if (file) {
    profilePhoto.value = file;
  }
};

// Upload image to ImgBB
const uploadImageToImgBB = async () => {
  if (!profilePhoto.value) return null;

  const formData = new FormData();
  formData.append("image", profilePhoto.value);

  try {
    const response = await fetch(`https://api.imgbb.com/1/upload?key=${import.meta.env.VITE_IMGBB_API_KEY}`, {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    if (data.success) {
      return data.data.url;
    }
  } catch (error) {
    console.error("Error uploading image:", error);
  }

  return null;
};

const registerPassenger = async () => {
  if (!isTokenValid.value) {
    errorMessage.value = "Token validation failed. Cannot proceed.";
    return;
  }

  // Simple validation
  if (!personalDetails.name || !personalDetails.age || !personalDetails.phone || !personalDetails.address) {
    alert("Please fill in all required fields.");
    return;
  }

  isLoading.value = true;

  try {
    // Upload profile photo first
    const profilePhotoUrl = await uploadImageToImgBB();

    if (!profilePhotoUrl) {
      alert("Failed to upload profile photo. Please try again.");
      isLoading.value = false;
      return;
    }

    // Proceed with registration after successful image upload
    const response = await api.post("/api/passenger/register/", {
      ...personalDetails,
      email: email.value,
      token: token.value,
      profile_photo: profilePhotoUrl, // Send profile image URL to backend
    });

    if (response.status === 201) {
      sessionStorage.setItem("passenger_email", email.value);
      router.push("/PEventView"); // Redirect to the next step
    }
  } catch (error) {
    alert(error.response?.data?.message || "An error occurred. Try again.");
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="p-6 bg-white rounded-lg shadow-md">
    <h2 class="text-2xl font-semibold mb-6 text-gray-800">Complete Registration</h2>

    <p v-if="errorMessage" class="text-red-500 text-center mb-4">{{ errorMessage }}</p>

    <form v-if="isTokenValid" @submit.prevent="registerPassenger">
      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Full Name</label>
        <input type="text" v-model="personalDetails.name" class="p-3 border rounded-md w-full focus:ring-2 focus:ring-blue-200" required />
      </div>

      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Age</label>
        <input type="number" v-model="personalDetails.age" class="p-3 border rounded-md w-full focus:ring-2 focus:ring-blue-200" required />
      </div>

      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Gender</label>
        <select v-model="personalDetails.gender" class="p-3 border rounded-md w-full focus:ring-2 focus:ring-blue-200">
          <option value="male">Male</option>
          <option value="female">Female</option>
          <option value="other">Other</option>
        </select>
      </div>

      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Phone Number</label>
        <input type="tel" v-model="personalDetails.phone" class="p-3 border rounded-md w-full focus:ring-2 focus:ring-blue-200" required />
      </div>

      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Address</label>
        <textarea v-model="personalDetails.address" class="p-3 border rounded-md w-full focus:ring-2 focus:ring-blue-200" required></textarea>
      </div>

      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Email</label>
        <input type="email" :value="email" disabled class="p-3 border rounded-md w-full bg-gray-200" />
      </div>

      <div class="mb-6">
        <label class="block text-sm font-medium text-gray-700 mb-2">Profile Photo</label>
        <input type="file" accept="image/*" @change="handleFileChange" class="p-3 border rounded-md w-full focus:ring-2 focus:ring-blue-200" />
      </div>

      <button
        type="submit"
        class="w-full p-3 text-white bg-blue-600 hover:bg-blue-900 rounded-lg font-semibold transition duration-300"
        :disabled="isLoading"
      >
        {{ isLoading ? "Registering..." : "Register" }}
      </button>
    </form>
  </div>
</template>
