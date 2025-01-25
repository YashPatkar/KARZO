<script setup>
import ApplicationLayoutComponent from '@/components/Driver/applicationLayoutComponent.vue';
import eventUploadComponent from '@/components/CommonComponents/eventUploadComponent.vue';
import { driverApiClient } from '@/utils/apiClients';

const sendtodatabase = async (data) => {
    try{
        const response = await driverApiClient.post('/event/data-store/', data);
        console.log('Event Data send to the backend');
        alert('Event submitted successfully!');
    }
    catch (error){
        console.log(error);
        alert('Error in submitting the event');
    }
}
const handleData = (data) => {
    if(data.name && data.date && data.time && data.location && data.description && data.id){
        // Send it to the backend
        sendtodatabase(data);
    }
    else{
        alert('Error in submitting the event');
    }
}
</script>

<template>
    <ApplicationLayoutComponent>
        <eventUploadComponent @submit-event="handleData" />
    </ApplicationLayoutComponent>
</template>