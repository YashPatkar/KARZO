import { defineStore } from 'pinia';
import { ref } from 'vue';
import api from '@/api';
import { useRouter } from 'vue-router';

export const usePassengerStore = defineStore('passenger', () => {
  const passenger = ref({}); // Store passenger data
  const router = useRouter();
  const email = ref(sessionStorage.getItem('passenger_email'));
 
  // Fetch passenger data from the API
  const fetchPassengerData = async () => {
    if (!email.value) {
      console.error('Email is not set in store!');
      router.push({ name: 'PVerifyView' }); // Redirect to verification view if email is not set
      return;
    }

    try {
      console.log('Fetching passenger data for email:', email.value);
      const response = await api.get('/api/passenger/check-user/', {
        params: { email: email.value }, // Send email as a query parameter
      });
      if (response.status === 200) {
        passenger.value = response.data; // Store the response data directly
        console.log('Passenger data fetched successfully:', passenger.value);
      }
    } catch (error) {
      console.error('Error fetching passenger data:', error);
      if (error.response && error.response.status === 404) {
        router.push({ name: 'PVerifyView' }); // Redirect to verification view if passenger is not found
      }
    }
  };

  return { passenger, email, fetchPassengerData };
});