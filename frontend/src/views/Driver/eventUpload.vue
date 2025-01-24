<script setup>
import ApplicationLayoutComponent from '@/components/Driver/applicationLayoutComponent.vue';
import eventUploadComponent from '@/components/CommonComponents/eventUploadComponent.vue';
import { useEventStore } from '@/stores/Driver/eventStore';
import axios from 'axios';

console.log(eventStore.events);
const sendtodatabase = (data) => {
    axios.post('http://localhost:8000/api/events', data)
    .then((response) => {
        console.log(response);

    })
    .catch((error) => {
        console.log(error);
    });
}
const handleData = (data) => {
    if (!data.name || !data.date || !data.time || !data.location || !data.description || !data.id) {
        alert('Please fill all the fields')
        return
    }
    else{
        // Send it to the backend and sent it to event page too
        // store it in the event store
        sendtodatabase(data);
        alert('Event submitted successfully!');
    }
}
</script>

<template>
    <ApplicationLayoutComponent>
        <eventUploadComponent @submit-event="handleData" />
    </ApplicationLayoutComponent>
</template>