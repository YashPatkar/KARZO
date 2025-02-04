<template>
    <v-card class="mx-auto my-4" max-width="400">
      <v-card-title>{{ name }}</v-card-title>
      <v-card-subtitle>
        {{ formatDate(date) }} at {{ time }}
      </v-card-subtitle>
      <v-card-text>
        <v-row align="center" class="mx-0">
          <v-icon class="mr-1">mdi-map-marker</v-icon>
          <span>{{ location }}</span>
        </v-row>
        <div class="mt-4">{{ description }}</div>
      </v-card-text>
    </v-card>
  </template>
  
  <script setup>

  // Define props using defineProps()
  const props = defineProps({
    name: {
      type: String,
      required: true,
    },
    date: {
      type: String,
      required: true,
    },
    time: {
      type: String,
      required: true,
    },
    location: {
      type: String,
      required: true,
    },
    description: {
      type: String,
      required: true,
    },
  });
  
  // Function to format the date
  const formatDate = (dateString) => {
    const options = { year: 'numeric', month: 'long', day: 'numeric' };
    return new Date(dateString).toLocaleDateString(undefined, options);
  };
  </script>
  