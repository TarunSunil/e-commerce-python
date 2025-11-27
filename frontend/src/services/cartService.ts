import api from './api';
import { CartItem } from '../types';

export const cartService = {
  async addToCart(productId: string, quantity: number): Promise<CartItem> {
    const response = await api.post<CartItem>('/cart', { productId, quantity });
    return response.data;
  },

  async getCart(): Promise<CartItem[]> {
    const response = await api.get<CartItem[]>('/cart');
    return response.data;
  },

  async getCartTotal(): Promise<number> {
    const response = await api.get<{ total: number }>('/cart/total');
    return response.data.total;
  },

  async removeFromCart(productId: string): Promise<void> {
    await api.delete(`/cart/${productId}`);
  },

  async clearCart(): Promise<void> {
    await api.delete('/cart');
  },
};


