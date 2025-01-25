import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5000', // URL backendu
});

export const addParagon = (data) => API.post('/paragony', data);
export const fetchProducts = () => API.get('/produkty');