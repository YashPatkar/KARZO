<script setup>
import ApplicationLayoutComponent from '@/components/Driver/applicationLayoutComponent.vue';
import eventUploadComponent from '@/components/CommonComponents/eventUploadComponent.vue';
import { useEventStore } from '@/stores/Driver/eventStore';

const eventStore = useEventStore();

const handleData = (data) => {
    if (!data.title || !data.date || !data.time || !data.location || !data.description) {
        alert('Please fill all the fields')
        return
    }
    else{
        // Send it to the backend and sent it to event page too
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