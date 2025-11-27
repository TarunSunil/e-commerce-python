import api from './api';
import { Product } from '../types';

export const productService = {
  async getAllProducts(page = 0, size = 20, category?: string, search?: string): Promise<Product[]> {
    const params = new URLSearchParams();
    params.append('page', page.toString());
    params.append('size', size.toString());
    if (category) params.append('category', category);
    if (search) params.append('q', search);
    
    const response = await api.get<Product[]>(`/products?${params.toString()}`);
    return response.data;
  },

  async getProductById(id: string): Promise<Product> {
    const response = await api.get<Product>(`/products/${id}`);
    return response.data;
  },

  async createProduct(product: Partial<Product>): Promise<Product> {
    const response = await api.post<Product>('/products', product);
    return response.data;
  },

  async updateProduct(id: string, product: Partial<Product>): Promise<Product> {
    const response = await api.put<Product>(`/products/${id}`, product);
    return response.data;
  },

  async deleteProduct(id: string): Promise<void> {
    await api.delete(`/products/${id}`);
  },
};


