<template>
    <div class="card max-w-md mx-auto p-5">
        <div class="form-card flex flex-col border-2 border-black p-5 rounded-md">
            <h1 class="text-2xl mx-auto mb-5">{{ showOtpForm ? "Enter OTP" : "Register" }}</h1>

            <form v-if="!showOtpForm" @submit.prevent="register" class="flex flex-col gap-3">
                <!-- Email Input -->
                <input 
                    type="email" 
                    placeholder="emailid@gmail.com" 
                    v-model.trim="driverlogin.email" 
                    required
                    :disabled="isLoading"
                />
                <span v-if="errors.email" class="text-red-500">{{ errors.email }}</span>

                <!-- Submit Button -->
                <button 
                    type="submit" 
                    class="text-md font-medium bg-blue-500 text-gray-100 hover:text-white hover:bg-blue-900 flex justify-center items-center gap-2 p-1"
                    :disabled="isLoading"
                >
                    <span v-if="isLoading" class="loader"></span>
                    <span v-else>Register</span>
                </button>
            </form>

            <!-- OTP Form -->
            <form v-else @submit.prevent="verifyOtp" class="flex flex-col gap-3">
                <input 
                    type="text" 
                    v-model="emailOtp" 
                    placeholder="Enter Email OTP" 
                    required
                    :disabled="isVerifying"
                />
                <button 
                    type="submit" 
                    class="p-1 text-md font-medium bg-green-500 text-gray-100 hover:text-white hover:bg-green-900 flex justify-center items-center gap-2"
                    :disabled="isVerifying"
                >
                    <span v-if="isVerifying" class="loader"></span>
                    <span v-else>Verify OTP</span>
                </button>
            </form>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import axios from "axios";

const driverlogin = ref({ email: '' });
const emailOtp = ref('');
const errors = ref({ email: '' });

const isLoading = ref(false);
const isVerifying = ref(false);
const showOtpForm = ref(false);

const emit = defineEmits(['register']);

const register = async () => {
    errors.value.email = '';
    isLoading.value = true;  // Start loading

    if (!driverlogin.value.email.endsWith('@gmail.com')) {
        errors.value.email = 'Only Gmail accounts are allowed.';
        isLoading.value = false;
        return;
    }

    try {
        // Send request to backend to register driver
        const response = await axios.post("http://127.0.0.1:8000/api/driver/driver-register/", {
            email: driverlogin.value.email

        });

        if (response.status === 200) {
            showOtpForm.value = true;  // Show OTP form
            emit('register', { email: driverlogin.value.email });
        }
    } catch (error) {
        errors.value.email = error.response?.data?.error || "Registration failed.";
        console.error("Error:", error);
    } finally {
        isLoading.value = false;  // Stop loading
    }
};

const verifyOtp = async () => {
    isVerifying.value = true;

    try {
        const response = await axios.post("http://127.0.0.1:8000/api/driver/register-verify-otp/", {
            email: driverlogin.value.email,
            email_otp: emailOtp.value  // Match backend
        });

        if (response.status === 200) {
            alert("OTP Verified Successfully! Redirecting...");
            // Redirect user to the dashboard or profile page
            // window.location.href = "/driver-dashboard";  
        } else {
            alert("Invalid OTP. Please try again.");
        }
    } catch (error) {
        alert("OTP Verification Failed.");
        console.error("Error:", error);
    } finally {
        isVerifying.value = false;
    }
};


</script>

<style scoped>
input {
    padding: 10px;
    border: 1px solid #000;
    border-radius: 5px;
    width: 100%;
}

.text-red-500 {
    color: red;
    font-size: 12px;
}

/* Loader Animation */
.loader {
    border: 3px solid #fff;
    border-top: 3px solid transparent;
    border-radius: 50%;
    width: 16px;
    height: 16px;
    animation: spin 0.8s linear infinite;
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
</style>
