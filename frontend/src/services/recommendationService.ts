import api from './api';
import { Product } from '../types';

export const recommendationService = {
  async getRecommendationsByProduct(productId: string, limit = 5): Promise<Product[]> {
    const response = await api.get<Product[]>(`/recommend/${productId}?limit=${limit}`);
    return response.data;
  },

  async getRecommendationsByUser(userId: string, limit = 5): Promise<Product[]> {
    const response = await api.get<Product[]>(`/recommend/user/${userId}?limit=${limit}`);
    return response.data;
  },
};


