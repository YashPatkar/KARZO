<script setup>
import { ref, defineEmits } from 'vue'

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
    // Simulate API call
    loading.value = true
    setTimeout(() => {
        if (!eventForm.value.name || !eventForm.value.date || !eventForm.value.time || !eventForm.value.location || !eventForm.value.description) {
            alert('Please fill all the fields')
            loading.value = false
            return
        } else {
            // Emit event with form data
            emit('submit-event', { ...eventForm.value })
        }
        // Reset form
        eventForm.value = {
            name: '',
            date: '',
            time: '',
            location: '',
            description: ''
        }
        loading.value = false
    }, 1000)
}
</script>

<template>
    <v-container>
        <h1 class="text-h4 mb-4">Suggest New Event</h1>
        <v-card>
            <v-card-text>
                <v-form @submit.prevent="submitEvent">
                    <v-text-field v-model="eventForm.name" label="Event name" required></v-text-field>

                    <v-row>
                        <v-col cols="12" md="6">
                            <v-text-field v-model="eventForm.date" label="Date" type="date" required></v-text-field>
                        </v-col>
                        <v-col cols="12" md="6">
                            <v-text-field v-model="eventForm.time" label="Time" type="time" required></v-text-field>
                        </v-col>
                    </v-row>

                    <v-text-field v-model="eventForm.location" label="Location" required></v-text-field>
                    
                    <v-textarea v-model="eventForm.description" label="Event Description" required></v-textarea>

                    <v-btn :loading="loading" color="primary" type="submit" block>
                        Submit Event Suggestion
                    </v-btn>
                </v-form>
            </v-card-text>
        </v-card>
    </v-container>
</template>
