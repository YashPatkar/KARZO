<template>
    <PLayoutComponent>  
        <v-container>
          <h1 class="text-h4 mb-4">Event List</h1>
          <v-row>
            <v-col v-for="event in events" :key="event.id" cols="12" md="6" lg="4">
              <PEventCardComponent
                :name="event.name"
                :date="event.date"
                :time="event.time"
                :location="event.location"
                :description="event.description"
              />
            </v-col>
          </v-row>
        </v-container>
    </PLayoutComponent>
</template>
  
  <script setup>
    import { ref } from 'vue';
    import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue';
    import PEventCardComponent from '@/components/PassengerComponents/PEventCardComponent.vue';
    import { onMounted } from 'vue';
    import axios from 'axios';

    const events = ref([]);

    onMounted(async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/event/');
            events.value = response.data;
        } catch (error) {
            console.error('Error fetching events:', error);
        }
    });

  </script>