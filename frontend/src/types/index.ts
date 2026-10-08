export interface User {
  id: string;
  name: string;
  email: string;
  roles: string[];
  preferences: string[];
}

export interface Product {
  id: string;
  name: string;
  description: string;
  categories: string[];
  price: number;
  images: string[];
  stock: number;
  attributes: Record<string, string>;
}

export interface CartItem {
  id: string;
  userId: string;
  productId: string;
  quantity: number;
  price: number;
  productName: string;
  productImage?: string;
  stock: number;
}

export interface Order {
  id: string;
  userId: string;
  items: OrderItem[];
  status: string;
  total: number;
  createdAt: string;
  shippingAddress: ShippingAddress;
}

export interface OrderItem {
  productId: string;
  qty: number;
  price: number;
  productName: string;
  unitPrice: number;
}

export interface ShippingAddress {
  address: string;
  city: string;
  state: string;
  zipCode: string;
}

export interface AuthResponse {
  token: string;
  userId: string;
  email: string;
  name: string;
  roles: string[];
}

export interface LoginRequest {
  email: string;
  password: string;
}

export interface RegisterRequest {
  name: string;
  email: string;
  password: string;
}

