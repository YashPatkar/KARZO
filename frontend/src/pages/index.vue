<script setup>
    import { RouterLink, RouterView } from 'vue-router';
</script>

<template>
    <div>
        <h1>Driver Page</h1>
        <RouterLink :to="{name: 'DriverHome'}" tag="button">GOTO DriverPage</RouterLink>
    </div>
</template>