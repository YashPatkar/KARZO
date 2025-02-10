import { createApp } from 'vue'
import './assets/tailwind.css';
import App from './App.vue'
import router from './router'
  
const app = createApp(App)
app.use(router) // Use Vue Router
app.mount('#app') // Mount the app to the #app element in index.html