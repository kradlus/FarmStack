import axios from 'axios';

const BASE_URL = "http://127.0.0.1:8000"

const getUser = async (search:string) => {
    return axios.get(`${BASE_URL}/search?user=${search}`, {
        headers:{
            "Authorization":`Bearer ${document.cookie.split("=")[1]}`
        }
    });
}

const apiRoot = async (cookie:string) => {
    const httpOptions = {
        headers:{
            "Authorization":`Bearer ${cookie}`
        }
    }
    return axios.get(`${BASE_URL}/`, httpOptions);
}

const userLogin = async (form_data:FormData) => {
    const httpOptions = {
        method:"POST",
        url:`${BASE_URL}/auth/login`,
        data:form_data,
        headers:{
            "Content-Type":"multipart/form-data"
        }
    }
    return axios(httpOptions)
}

const userRegistration = async (form_data:FormData) => {
    const httpOptions = {
        method:"POST",
        url:`${BASE_URL}/auth/register`,
        data:form_data,
        headers:{"Content-Type":"multipart/form-data"}
    }
    return axios(httpOptions);
}

export default {
    getUser,
    apiRoot,
    userLogin,
    userRegistration,
}