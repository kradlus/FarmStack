import { createRouter, createWebHashHistory } from 'vue-router';
import LoginView from '../views/LoginView.vue';
import RegisterView from '../views/RegisterView.vue';
import DashboardView from '../views/DashboardView.vue';
import httpService from '../api/http'

const isAuthenticated = async (cookie:string) => {
    const response_status:number = await httpService.apiRoot(cookie).then((resp) => resp.status)
        .catch(error => error.response.status)
    console.log(response_status)
    return response_status !== undefined && response_status == 200 ? true:false;
}

const routes = [
    {
        path:'/login',
        component:LoginView
    },
    {
        path: '/register',
        component:RegisterView
    },
    {
        path:'/',
        component:DashboardView,
    }
]

const router = createRouter({
    history:createWebHashHistory(),
    routes
})

export default {
    router,
    isAuthenticated
}