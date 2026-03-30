import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000/api'
});

api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) config.headers.Authorization = `Token ${token}`;
  return config;
});

export const register = (payload) => api.post('/register', payload);
export const login = (payload) => api.post('/login', payload);
export const saveProfile = (payload) => api.post('/profile', payload);
export const getCareer = () => api.get('/career-recommendation');
export const getSkillGap = () => api.get('/skill-gap');
export const getCourses = () => api.get('/courses');
export const getJobs = () => api.get('/jobs');

export default api;
