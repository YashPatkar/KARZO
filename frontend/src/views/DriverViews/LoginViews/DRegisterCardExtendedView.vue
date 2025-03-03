<template>
  <div class="min-h-screen bg-gray-100 p-8">
    <div v-if="currentStep === 1">
      <PersonalDetailsComponent @next="nextStep" @update:personalDetails="updatePersonalDetails" />
    </div>
    <div v-else-if="currentStep === 2">
      <VehicleRegistrationComponent @prev="prevStep" @submit="handleSubmit"
        @update:vehicleDetails="updateVehicleDetails" />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router'; // Import Vue Router
import api from '@/api';
import { supabase } from "@/utils/supabase"; 

import PersonalDetailsComponent from '@/components/DriverComponents/loginComponent/PersonalDetailsComponent.vue';
import VehicleRegistrationComponent from '@/components/DriverComponents/loginComponent/VehicleRegistrationComponent.vue';

const router = useRouter(); // Initialize Vue Router
const currentStep = ref(1);
const storedEmail = ref('');

onMounted(() => {
  storedEmail.value = sessionStorage.getItem('userEmail') || '';
});

const personalDetails = ref({
  name: '',
  age: null,
  birth_date: '',
  gender: 'male',
  phone: '',
  location: '',
  pincode: '',
  address: '',
  email: '',
  profilePhoto: null, // Store the selected image file
});

const vehicleDetails = ref({
  vehicle_number: '',
  vehicle_manufacturer: '',
  vehicle_type: 'bike',
  vehicle_model: '',
  vehicle_color: '',
  vehicle_registration_date: '',
});

const nextStep = () => {
  currentStep.value = 2;
};

const prevStep = () => {
  currentStep.value = 1;
};

const updatePersonalDetails = (details) => {
  personalDetails.value = { ...personalDetails.value, ...details };
};

const updateVehicleDetails = (details) => {
  vehicleDetails.value = { ...vehicleDetails.value, ...details };
};

const uploadImageToImgBB = async (file, driverUUID) => {
  const formData = new FormData();
  formData.append('image', file);
  formData.append('name', `${driverUUID}_driver_image`);

  try {
    const apiKey = import.meta.env.VITE_IMGBB_API_KEY;
    if (!apiKey) {
      throw new Error('ImgBB API key is not set');
    }
    const response = await fetch(`https://api.imgbb.com/1/upload?key=${apiKey}`, {
      method: 'POST',
      body: formData,
    });
    const result = await response.json();
    if (result.success) {
      return result.data.url; // Return the image URL
    } else {
      throw new Error('Failed to upload image to ImgBB');
    }
  } catch (error) {
    console.error('Error uploading image to ImgBB:', error);
    throw error;
  }
};

const handleSubmit = async () => {
  try {
    if (personalDetails.value.email !== storedEmail.value) {
      alert('Email verification failed!');
      return;
    }

    const dataToSend = {
      driver: {
        email: personalDetails.value.email,
      },
      personal_details: {
        name: personalDetails.value.name,
        age: personalDetails.value.age,
        birth_date: personalDetails.value.birth_date,
        gender: personalDetails.value.gender,
        phone: personalDetails.value.phone,
        location: personalDetails.value.location,
        pincode: personalDetails.value.pincode,
        address: personalDetails.value.address,
      },
      vehicle_details: {
        vehicle_number: vehicleDetails.value.vehicle_number,
        vehicle_manufacturer: vehicleDetails.value.vehicle_manufacturer,
        vehicle_type: vehicleDetails.value.vehicle_type,
        vehicle_model: vehicleDetails.value.vehicle_model,
        vehicle_color: vehicleDetails.value.vehicle_color,
        vehicle_registration_date: vehicleDetails.value.vehicle_registration_date,
      },
    };

    const response = await api.post('/api/driver/register/', dataToSend);
    console.log('Driver registration response:', response);

    if (response.status === 201) {
      const driverUUID = response.data.driver_uuid;
      if (personalDetails.value.profilePhoto) {
        const imageUrl = await uploadImageToImgBB(personalDetails.value.profilePhoto, driverUUID);
        const updateResponse = await api.patch(`/api/driver/${driverUUID}/update-profile/`, {
          profile_photo_url: imageUrl,
        });
        if (updateResponse.status === 200) {
          await supabase
            .from("driver")
            .update({ registration_status: "COMPLETED" })
            .eq("email", storedEmail.value);
          router.push({ path: '/DHomeView' });
        } else {
          throw new Error('Failed to update driver profile with image URL');
        }
      } else {
        router.push({ path: '/DHomeView' });
      }
    } else {
      throw new Error('Failed to register driver');
    }
  } catch (error) {
    console.error('Error submitting form:', error);
    alert('Registration failed. Please try again.');
  }
};
</script>