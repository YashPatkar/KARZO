import { defineStore } from 'pinia';
import { ref } from 'vue';
import api from '@/api';
import { useRouter } from 'vue-router';

export const useDriverStore = defineStore('driver', () => {
  const driver = ref({}); // Store driver data
  const router = useRouter();
  const email = ref(sessionStorage.getItem('driver_email'));
 
  // Fetch driver data from the API
  const fetchdriverData = async () => {
    if (!email.value) {
      console.error('Email is not set in store!');
      router.push({ name: 'DVerifyView' }); // Redirect to verification view if email is not set
      return;
    }

    try {
      console.log('Fetching driver data for email:', email.value);
      const response = await api.get('/api/driver/check-user/', {
        params: { email: email.value }, // Send email as a query parameter
      });
      if (response.status === 200) {
        driver.value = response.data; // Store the response data directly
        console.log('driver data fetched successfully:', driver.value);
      }
    } catch (error) {
      console.error('Error fetching driver data:', error);
      if (error.response && error.response.status === 404) {
        router.push({ name: 'DVerifyView' }); // Redirect to verification view if driver is not found
      }
    }
  };

  return { driver, email, fetchdriverData };
});