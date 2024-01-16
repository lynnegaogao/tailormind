import { createApp } from 'vue'
import './style.css'
import App from './App.vue'
import router from '../router/index'
import axios from "axios";

// createApp(App).mount('#app')
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/";

const app = createApp(App)
app.use(router)
app.mount('#app')




