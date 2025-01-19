<script setup>
import { ref } from 'vue';

const username = ref('');
const email = ref('');

const submitForm = () => {
    // Handle form submission
    console.log('Username:', username.value);
    console.log('Email:', email.value);
};
</script>

<template>
    <v-container>
        <v-form @submit.prevent="submitForm">
            <v-text-field v-model="username" label="Username" required prepend-inner-icon="mdi-account"></v-text-field>
            <v-text-field v-model="email" label="Email" type="email" required prepend-inner-icon="mdi-email"></v-text-field>
            <v-text-field v-model="password" label="Password" type="password" required prepend-inner-icon="mdi-lock"></v-text-field>
            <v-btn type="submit" color="primary">Submit</v-btn>
        </v-form>
    </v-container>
</template>