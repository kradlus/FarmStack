import axios from 'axios';

const BASE_URL = "http://127.0.0.1:8000"

const getUser = async (search:string) => {
    return axios.get(`${BASE_URL}/search?user=${search}`);
}

export default {
    getUser,
}