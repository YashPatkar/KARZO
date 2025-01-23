<script setup>
import applicationLayoutComponent from '@/components/Driver/applicationLayoutComponent.vue';
import EventCard from '@/components/Driver/eventCardComponent.vue';
import { useEventStore } from '@/stores/Driver/eventStore';

const eventStore = useEventStore(); // Access the event store
console.log(eventStore.events); // Log the events

</script>

<template>
    <applicationLayoutComponent>
        <EventCard
            v-for="(eventObject, index) in eventStore.events"
            :key="index"
            :event="eventObject"
        />
    </applicationLayoutComponent>
</template>
