import api from './api';
import { Order, ShippingAddress } from '../types';

export const orderService = {
  async createOrder(shippingAddress: ShippingAddress): Promise<Order> {
    const response = await api.post<Order>('/orders', { shippingAddress });
    return response.data;
  },

  async getUserOrders(userId: string): Promise<Order[]> {
    const response = await api.get<Order[]>(`/orders/user/${userId}`);
    return response.data;
  },

  async getOrderById(orderId: string): Promise<Order> {
    const response = await api.get<Order>(`/orders/order/${orderId}`);
    return response.data;
  },
};

