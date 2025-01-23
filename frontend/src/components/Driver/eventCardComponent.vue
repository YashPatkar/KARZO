<script setup>
defineProps({
  event: {
    type: Object,
    required: true
  }
})
</script>

<template>
  <v-row>
    <v-col cols="12" sm="4" md="4" v-for="(event, index) in eventStore.events" :key="index">
      <v-card class="mx-auto my-4" max-width="400">
        <v-card-title class="text-h5">{{ event.name }}</v-card-title>
        
        <v-card-text>
          <v-row dense>
            <v-col cols="12">
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-2">mdi-map-marker</v-icon>
                <span>{{ event.location }}</span>
              </div>
            </v-col>
            <v-col cols="12">
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-2">mdi-clock-outline</v-icon>
                <span>{{ event.time }}</span>
              </div>
            </v-col>
            <v-col cols="12">
              <div class="d-flex align-center mb-2">
                <v-icon class="mr-2">mdi-calendar</v-icon>
                <span>{{ event.date }}</span>
              </div>
            </v-col>
          </v-row>
          
          <v-divider class="my-2"></v-divider>
          
          <p class="mt-2">{{ event.description }}</p>
        </v-card-text>
      </v-card>
    </v-col>
  </v-row>
</template>
