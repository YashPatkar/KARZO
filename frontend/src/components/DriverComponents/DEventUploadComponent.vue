<script setup>
import { ref } from 'vue'

const eventForm = ref({
    name: '',
    date: '',
    time: '',
    location: '',
    description: ''
})

const emit = defineEmits(['submit-event'])

const loading = ref(false)

const submitEvent = () => {
    loading.value = true
    setTimeout(() => {
        if (!eventForm.value.name || !eventForm.value.date || !eventForm.value.time || !eventForm.value.location || !eventForm.value.description) {
            alert('Please fill all the fields')
            loading.value = false
            return
        } else {
            emit('submit-event', { ...eventForm.value })
        }
        eventForm.value = {
            name: '',
            date: '',
            time: '',
            location: '',
            description: ''
        }
        loading.value = false
    }, 500)
}
</script>

<template>
    <div class="max-w-2xl mx-auto p-6">
        <h1 class="text-2xl font-bold mb-4 text-gray-800">Suggest New Event</h1>
        <div class="bg-white shadow-lg rounded-xl p-6">
            <form @submit.prevent="submitEvent" class="space-y-4">
                <!-- Event Name -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Event Name</label>
                    <input 
                        v-model="eventForm.name"
                        type="text"
                        class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
                        required
                    />
                </div>

                <!-- Date and Time -->
                <div class="flex flex-col md:flex-row gap-4">
                    <div class="w-full">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Date</label>
                        <input 
                            v-model="eventForm.date"
                            type="date"
                            class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
                            required
                        />
                    </div>

                    <div class="w-full">
                        <label class="block text-sm font-medium text-gray-700 mb-1">Time</label>
                        <input 
                            v-model="eventForm.time"
                            type="time"
                            class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
                            required
                        />
                    </div>
                </div>

                <!-- Location -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Location</label>
                    <input 
                        v-model="eventForm.location"
                        type="text"
                        class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
                        required
                    />
                </div>

                <!-- Description -->
                <div>
                    <label class="block text-sm font-medium text-gray-700 mb-1">Event Description</label>
                    <textarea 
                        v-model="eventForm.description"
                        rows="4"
                        class="w-full border border-gray-300 rounded-lg p-2 focus:ring-2 focus:ring-blue-500 focus:outline-none"
                        required
                    ></textarea>
                </div>

                <!-- Submit Button -->
                <button 
                    type="submit" 
                    :disabled="loading"
                    class="w-full bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 rounded-lg transition duration-200 flex items-center justify-center"
                >
                    <svg v-if="loading" class="animate-spin h-5 w-5 mr-2 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"></path>
                    </svg>
                    {{ loading ? 'Submitting...' : 'Submit Event Suggestion' }}
                </button>
            </form>
        </div>
    </div>
</template>

<style scoped>
/* Optional: Light gray background */
body {
    background-color: #f7fafc;
}
</style>
