<script setup>
import applicationLayoutComponent from '@/components/applicationLayoutComponent.vue';
import { ref } from 'vue';

const items = ref([
    {
        title: 'Home',
        prependIcon: 'mdi-home',
        link: true,
    },
    {
        title: 'Dashboard',
        prependIcon: 'mdi-view-dashboard-outline',
        link: true,
    },
    {
        title: 'Events',
        prependIcon: 'mdi-account-group',
        link: true,
    },
    {
        title: 'Events Uploader',
        prependIcon: 'mdi-briefcase-outline',
        link: true,
    },
])

</script>

<template>
    <div>
        <h1>Driver Home</h1>
        <applicationLayoutComponent :items="items" />
    </div>
</template>