import { createApp } from 'vue'
import './style.css'
import App from './Forethought.vue'
import router from '../router/index.js'
import axios from "axios";


// 按照教程引用
// import Antd from 'ant-design-vue';
// import 'ant-design-vue/dist/reset.css';

// createApp(App).mount('#app')
axios.defaults.withCredentials = true;
axios.defaults.baseURL = "http://localhost:8000/";

const app = createApp(App)
app.use(router)
// app.use(Antd)
app.mount('#app')
