// src/services/apiClients.js
import axios from 'axios';

// Axios instance for drivers
export const driverApiClient = axios.create({
  baseURL: 'http://localhost:8000/api/driver',
  headers: {
    'Content-Type': 'application/json',
  },
});

// Axios instance for passengers
export const passengerApiClient = axios.create({
  baseURL: 'http://localhost:8000/api/passenger',
  headers: {
    'Content-Type': 'application/json',
  },
});
