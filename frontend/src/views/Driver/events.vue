<script setup>
import { ref, onMounted } from 'vue';
import applicationLayoutComponent from '@/components/Driver/applicationLayoutComponent.vue';
import EventCard from '@/components/Driver/eventCardComponent.vue';
import { driverApiClient } from '@/utils/apiClients';

const eventData = ref(null);
const error = ref(null);

onMounted(async () => {
    try {
        const response = await driverApiClient.post('/event/get-data/', data);
        eventData.value = response.data;
    } catch (err) {
        error.value = err;
    }
});
</script>

<template>
    <applicationLayoutComponent>
        <EventCard v-if="eventData" :data="eventData" />
        <div v-else-if="error">Error loading data: {{ error.message }}</div>
        <div v-else>Loading...</div>
    </applicationLayoutComponent>
</template>
