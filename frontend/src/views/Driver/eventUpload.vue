<script setup>
import ApplicationLayoutComponent from '@/components/Driver/applicationLayoutComponent.vue';
import eventUploadComponent from '@/components/CommonComponents/eventUploadComponent.vue';
import { useEventStore } from '@/stores/Driver/eventStore';

const eventStore = useEventStore();
console.log(eventStore.events);
const handleData = (data) => {
    if (!data.name || !data.date || !data.time || !data.location || !data.description || !data.id) {
        alert('Please fill all the fields')
        return
    }
    else{
        // Send it to the backend and sent it to event page too
        // store it in the event store
        eventStore.addEvent(data);
        alert('Event submitted successfully!');
    }
}
</script>

<template>
    <ApplicationLayoutComponent>
        <eventUploadComponent @submit-event="handleData" />
    </ApplicationLayoutComponent>
</template>