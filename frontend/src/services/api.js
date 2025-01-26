import axios from 'axios';

const API = axios.create({
  baseURL: 'http://127.0.0.1:5001', // URL backendu
});

export const addParagon = (data) => API.post('/paragony', data);
export const fetchParagony = () => API.get('/paragony');
export const fetchProducts = () => API.get('/produkty');