<template>
    <v-card class="mx-auto my-4" max-width="450" style="height: 200px; overflow: hidden;">
      <v-card-title>{{ name }}</v-card-title>
      <v-card-subtitle>
        {{ formatDate(date) }} at {{ time }}
      </v-card-subtitle>
      <v-card-text>
        <v-row align="center" class="mx-0">
          <v-icon class="mr-1">mdi-map-marker</v-icon>
          <span>{{ location }}</span>
        </v-row>
        <div class="mt-4" style="height: 60px; overflow: hidden;">
          {{ description.substring(0, 200) }}{{ description.length > 200 ? '...' : '' }}
        </div>
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
  