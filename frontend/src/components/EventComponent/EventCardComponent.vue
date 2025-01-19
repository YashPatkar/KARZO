<script setup>
import { ref, computed } from 'vue';
import { defineProps } from 'vue';

// Accept the event data as a prop
const props = defineProps({
    event: Array // Assuming the 'event' prop is an array of objects
});

// Search query for user input
const searchQuery = ref('');

// Compute filtered events dynamically
const filteredEvents = computed(() => {
    const query = searchQuery.value.toLowerCase().trim(); // Normalize input
    if (!query) return props.event; // Return all events if no query
    return props.event.filter(eventItem =>
        eventItem.EventName.toLowerCase().includes(query) ||
        eventItem.City.toLowerCase().includes(query) ||
        eventItem.StartDate.toLowerCase().includes(query) ||
        eventItem.EndDate.toLowerCase().includes(query) ||
        (eventItem.State?.toLowerCase().includes(query) ?? false)
    );
});
</script>

<template>
    <v-container align="center">
        <!-- Search Field -->
        <v-text-field v-model="searchQuery" label="Search Events" clearable width="80%"
            placeholder="Search by event name, city, or state" outlined dense class="mb-4" />
    </v-container>

    <!-- Display Filtered Events -->
    <v-row class="ma-4" align="center" justify="space-between">
        <v-col cols="12" sm="6" md="4" v-for="eventItem in filteredEvents" :key="eventItem.id">
            <v-card class="mx-auto uniform-card" :subtitle="`${eventItem.State} - ${eventItem.City}`">
                <template v-slot:title>
                    <span class="font-weight-bold">{{ eventItem.EventName }}</span>
                    <v-chip v-if="eventItem.StartDate && eventItem.EndDate" color="green" class="ml-2">
                        {{ eventItem.StartDate }} to {{ eventItem.EndDate }}
                    </v-chip>
                </template>
                <v-card-text class="bg-surface-light pt-4">
                    {{ eventItem.description }}
                </v-card-text>
            </v-card>
        </v-col>
    </v-row>

    <!-- No Events Message -->
    <v-container v-if="filteredEvents.length === 0">
        <v-alert type="info" outlined>
            No events found matching your search.
        </v-alert>
    </v-container>
</template>

<style scoped>
.uniform-card {
    border-radius: 20px;
    min-height: 250px;
    max-height: 250px;
    min-width: 350px;
    max-width: 350px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    transition: transform 0.3s, box-shadow 0.3s;
}

.uniform-card:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}
</style>
