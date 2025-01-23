<script setup>
import applicationLayoutComponent from '@/components/Driver/applicationLayoutComponent.vue';
import { useEventStore } from '@/stores/Driver/eventStore';

const eventStore = useEventStore(); // Access the event store
</script>

<template>
  <applicationLayoutComponent>
    <h1 class="text-h4 mb-4">Submitted Events</h1>

    <v-container>
      <v-card v-for="(event, index) in eventStore.events" :key="index" class="mb-4">
        <v-card-title>{{ event.title }}</v-card-title>
        <v-card-text>
          <p><strong>Date:</strong> {{ event.date }}</p>
          <p><strong>Time:</strong> {{ event.time }}</p>
          <p><strong>Location:</strong> {{ event.location }}</p>
          <p><strong>Description:</strong> {{ event.description }}</p>
        </v-card-text>
      </v-card>
    </v-container>
  </applicationLayoutComponent>
</template>
