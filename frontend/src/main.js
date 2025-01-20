import { createApp } from 'vue'
import { createVuetify } from 'vuetify'; // Import Vuetify
import App from './App.vue'
import router from './router'

import 'vuetify/styles';  // Import Vuetify's styles
import '@mdi/font/css/materialdesignicons.css'; // Optional: For Material Design Icons

const vuetify = createVuetify();  // Initialize Vuetify

const app = createApp(App)

app.use(router)
app.use(vuetify)  // Use Vuetify
app.mount('#app')