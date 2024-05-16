

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import App from './App.vue'
import router from './router'

import {Vuex} from 'vuex'
// import 'bootstrap/dist/css/bootstrap.css'
// import 'bootstrap/dist/js/bootstrap'
//
import './assets/main.css'
import'./assets/css/bootstrap.css'
import'./assets/js/bootstrap.js'
// import './index.css'
// Optionally install the BootstrapVue icon components plugin


import axios from 'axios'
import VueAxios from 'vue-axios'
const app = createApp(App)
app.use(Vuex)
app.use(createPinia())
app.use(router)


app.mount('#app')
