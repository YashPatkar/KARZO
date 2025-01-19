<script setup>
import ApplicationLayoutComponent from '@/components/ApplicationComponent/applicationLayoutComponent.vue';
import EventCardComponent from '@/components/EventComponent/EventCardComponent.vue';

const EventData = [
  {
    EventName: 'Shivaji Park',
    State: 'Maharashtra',
    City: 'Mumbai',
    StartDate: '1-1-2025',
    EndDate: '26-1-2025',
    time: 'Event Time',
    location: 'Chhatrapati Shivaji Park',
    description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!'
  },
  {
    EventName: 'Vile Parle',
    State: 'Maharashtra',
    City: 'South Bombay',
    StartDate: '2-2-2025',
    EndDate: '11-2-2025',
    time: '10:20pm',
    location: 'Vile Parle East',
    description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus orem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!'
  },
  {
    EventName: 'Vile Parle',
    State: 'Maharashtra',
    City: 'South Bombay',
    StartDate: '3-2-2025',
    EndDate: '11-2-2025',
    time: '10:20pm',
    location: 'Vile Parle East',
    description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus orem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!'
  },
  {
    EventName: 'Vile Parle',
    State: 'Maharashtra',
    City: 'South Bombay',
    StartDate: '4-2-2025',
    EndDate: '11-2-2025',
    time: '10:20pm',
    location: 'Vile Parle East',
    description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus orem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!'
  },
  {
    EventName: 'Vile Parle',
    State: 'Maharashtra',
    City: 'South Bombay',
    StartDate: '5-2-2025',
    EndDate: '11-2-2025',
    time: '10:20pm',
    location: 'Vile Parle East',
    description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus orem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!'
  },
  {
    EventName: 'Vile Parle',
    State: 'Maharashtra',
    City: 'South Bombay',
    StartDate: '6-2-2025',
    EndDate: '11-2-2025',
    time: '10:20pm',
    location: 'Vile Parle East',
    description: 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus orem ipsum dolor sit amet consectetur adipisicing elit. Commodi, ratione debitis quis est labore voluptatibus!'
  },
]
</script>

<template>
  <ApplicationLayoutComponent breadcrumitem="Event">
      <EventCardComponent :event="EventData"/> <!-- Injected into the slot --> 
  </ApplicationLayoutComponent>
</template>
