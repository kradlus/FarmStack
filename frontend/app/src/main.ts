import { createApp } from 'vue'
import router from './router'
import VueCookies from 'vue-cookies'
import App from './App.vue'

createApp(App).use(router.router).use(VueCookies).mount('#app')
