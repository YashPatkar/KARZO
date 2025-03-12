import { defineStore } from 'pinia';
import { ref } from 'vue';
import api from '@/api';
import { useRouter } from 'vue-router';

export const useDriverStore = defineStore('driver', () => {
  const driver = ref({});
  const email = ref(sessionStorage.getItem('driver_email') || null);
  const router = useRouter();

  const setEmail = (newEmail) => {
    email.value = newEmail;
    sessionStorage.setItem('driver_email', newEmail);
  };

  const fetchDriverData = async () => {
    if (!email.value) {
      console.error('Email is not set in store!');
      router.push({ name: 'DVerifyView' });
      return;
    }
    try {
      const response = await api.get(`/api/driver/${email.value}/driver-data/`);
      driver.value = response.data.driver; // Store the nested driver object directly
      console.log('Driver data fetched successfully:', driver.value);
    } catch (error) {
      console.error('Error fetching driver data:', error);
      if (error.response && error.response.status === 404) {
        router.push({ name: 'DVerifyView' });
      }
    }
  };

  return { driver, email, setEmail, fetchDriverData };
});
