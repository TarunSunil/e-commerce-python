import axios from 'axios';

const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add token to requests if it exists
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Auth API
export const authAPI = {
  register: (userData) => api.post('/api/auth/register', userData),
  login: (credentials) => {
    const formData = new FormData();
    formData.append('username', credentials.username);
    formData.append('password', credentials.password);
    return api.post('/api/auth/login', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
    });
  },
  getMe: () => api.get('/api/auth/me'),
};

// Products API
export const productsAPI = {
  getAll: (params) => api.get('/api/products', { params }),
  getById: (id) => api.get(`/api/products/${id}`),
  create: (productData) => api.post('/api/products', productData),
  update: (id, productData) => api.put(`/api/products/${id}`, productData),
  delete: (id) => api.delete(`/api/products/${id}`),
};

// Categories API
export const categoriesAPI = {
  getAll: () => api.get('/api/categories'),
  getById: (id) => api.get(`/api/categories/${id}`),
  create: (categoryData) => api.post('/api/categories', categoryData),
  update: (id, categoryData) => api.put(`/api/categories/${id}`, categoryData),
  delete: (id) => api.delete(`/api/categories/${id}`),
};

// Cart API
export const cartAPI = {
  get: () => api.get('/api/cart'),
  addItem: (item) => api.post('/api/cart/items', item),
  updateItem: (id, quantity) => api.put(`/api/cart/items/${id}`, { quantity }),
  removeItem: (id) => api.delete(`/api/cart/items/${id}`),
  clear: () => api.delete('/api/cart'),
};

// Orders API
export const ordersAPI = {
  getAll: () => api.get('/api/orders'),
  getById: (id) => api.get(`/api/orders/${id}`),
  create: (orderData) => api.post('/api/orders', orderData),
  getAllAdmin: () => api.get('/api/orders/admin/all'),
  updateStatus: (id, status) => api.put(`/api/orders/${id}/status`, null, { params: { status } }),
};

export default api;
