<script setup>
import { onMounted, reactive, ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import api from "@/api";
import PersonalDetailsComponent from "@/components/DriverComponents/loginComponent/PersonalDetailsComponent.vue";
import VehicleRegistrationComponent from "@/components/DriverComponents/loginComponent/VehicleRegistrationComponent.vue";

const route = useRoute();
const router = useRouter();
const token = ref(route.query.token);
const email = ref("");
const errorMessage = ref("");
const isTokenValid = ref(false);
const isLoading = ref(false);
const profilePhoto = ref(null);  // This will store the File object
const currentStep = ref(1);

const personalDetails = reactive({
  name: "",
  age: null,
  gender: "male",
  phone: "",
  address: "",
});

const vehicleDetails = reactive({
  vehicle_number: "",
  vehicle_manufacturer: "",
  vehicle_type: "bike",
  vehicle_model: "",
  vehicle_color: "",
  vehicle_registration_number: "",
  vehicle_registration_date: "",
});

onMounted(async () => {
  if (!token.value) {
    errorMessage.value = "Invalid link.";
    return;
  }

  try {
    const response = await api.post("/api/driver/validate-token/", {
      token: token.value,
    });

    email.value = response.data.email;
    isTokenValid.value = true;
  } catch (err) {
    errorMessage.value = "Invalid or expired token.";
  }
});

// Upload image to ImgBB - same as passenger
const uploadImageToImgBB = async () => {
  if (!profilePhoto.value) {
    console.error("No profile photo to upload");
    return null;
  }

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

const nextStep = () => {
  // Validate personal details before proceeding
  if (!personalDetails.name || !personalDetails.age || !personalDetails.phone || !personalDetails.address) {
    alert("Please fill all required personal details");
    return;
  }
  currentStep.value++;
};

const prevStep = () => {
  currentStep.value--;
};

const updatePersonalDetails = (updatedDetails) => {
  Object.assign(personalDetails, updatedDetails);
};

const updateVehicleDetails = (updatedDetails) => {
  Object.assign(vehicleDetails, updatedDetails);
};

// Handle profile photo update from child component
const updateProfilePhoto = (file) => {
  profilePhoto.value = file;
};

const handleSubmit = async () => {
  if (!isTokenValid.value) {
    errorMessage.value = "Token validation failed. Cannot proceed.";
    return;
  }

  // Validate vehicle details
  if (!vehicleDetails.vehicle_number || !vehicleDetails.vehicle_model) {
    alert("Please fill in all required vehicle details.");
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

    const response = await api.post("/api/driver/register/", {
      ...personalDetails,
      ...vehicleDetails,
      email: email.value,
      token: token.value,
      profile_photo: profilePhotoUrl,
    });

    if (response.status === 201) {
      sessionStorage.setItem("driver_email", email.value);
      router.push("/DEventView");
    }
  } catch (error) {
    alert(error.response?.data?.message || "An error occurred. Try again.");
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div v-if="currentStep === 1">
      <PersonalDetailsComponent 
        @next="nextStep" 
        @update:personalDetails="updatePersonalDetails"
        @update:profilePhoto="updateProfilePhoto"
      />
    </div>
    <div v-else-if="currentStep === 2">
      <VehicleRegistrationComponent 
        @prev="prevStep" 
        @submit="handleSubmit" 
        @update:vehicleDetails="updateVehicleDetails" 
      />
    </div>
  </div>
</template>