import { createApp } from 'vue'
import './assets/tailwind.css';
import App from './App.vue'
import router from './router'
import { createPinia } from 'pinia';

const pinia = createPinia();

const app = createApp(App)
app.use(pinia) // Use Pinia
app.use(router) // Use Vue Router
app.mount('#app') // Mount the app to the #app element in index.html