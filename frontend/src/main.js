import { createApp } from 'vue'
import { createVuetify } from 'vuetify';
import { createPinia } from 'pinia';
import App from './App.vue'
import router from './router'

import 'vuetify/styles';  // Vuetify's styles
import '@mdi/font/css/materialdesignicons.css'; // Optional: For Material Design Icons

const vuetify = createVuetify();  // Initialize Vuetify
const pinia = createPinia();  // Initialize Pinia
const app = createApp(App)


app.use(router) // Use Vue Router
app.use(vuetify)  // Use Vuetify
app.use(pinia)  // Use Pinia
app.mount('#app') // Mount the app to the #app element in index.html