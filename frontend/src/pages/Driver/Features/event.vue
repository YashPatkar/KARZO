<script setup>
import ApplicationLayoutComponent from '@/components/ApplicationComponent/applicationLayoutComponent.vue';
import EventCardComponent from '@/components/EventComponent/EventCardComponent.vue';
</script>

<template>
  <ApplicationLayoutComponent breadcrumitem="Event">
    <EventCardComponent /> <!-- Injected into the slot --> 
  </ApplicationLayoutComponent>
</template>
