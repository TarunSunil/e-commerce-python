import api from './api';
import { Order } from '../types';

export const orderService = {
  async createOrder(): Promise<Order> {
    const response = await api.post<Order>('/orders', {});
    return response.data;
  },

  async getUserOrders(userId: string): Promise<Order[]> {
    const response = await api.get<Order[]>(`/orders/${userId}`);
    return response.data;
  },

  async getOrderById(orderId: string): Promise<Order> {
    const response = await api.get<Order>(`/orders/order/${orderId}`);
    return response.data;
  },
};


