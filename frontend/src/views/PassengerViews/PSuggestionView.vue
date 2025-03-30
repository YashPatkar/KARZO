<script setup>
    import { ref } from 'vue'
    import PLayoutComponent from '@/components/PassengerComponents/PLayoutComponent.vue';
</script>

<template>
    <PLayoutComponent>

        <form action="">
            <input type="text" placeholder="Ask which events are in trending in your area" class="w-[90%] h-10 px-4 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500" />
        </form>
    </PLayoutComponent>
</template>