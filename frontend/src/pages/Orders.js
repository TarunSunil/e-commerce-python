import React, { useState, useEffect } from 'react';
import { ordersAPI } from '../services/api';
import './Orders.css';

const Orders = () => {
  const [orders, setOrders] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchOrders();
  }, []);

  const fetchOrders = async () => {
    try {
      setLoading(true);
      const response = await ordersAPI.getAll();
      setOrders(response.data);
    } catch (error) {
      console.error('Error fetching orders:', error);
    } finally {
      setLoading(false);
    }
  };

  const getStatusClass = (status) => {
    switch (status) {
      case 'delivered':
        return 'status-delivered';
      case 'shipped':
        return 'status-shipped';
      case 'processing':
        return 'status-processing';
      case 'cancelled':
        return 'status-cancelled';
      default:
        return 'status-pending';
    }
  };

  if (loading) {
    return <div className="loading">Loading orders...</div>;
  }

  if (orders.length === 0) {
    return (
      <div className="orders-container">
        <h2>My Orders</h2>
        <p>You haven't placed any orders yet.</p>
      </div>
    );
  }

  return (
    <div className="orders-container">
      <h2>My Orders</h2>
      <div className="orders-list">
        {orders.map((order) => (
          <div key={order.id} className="order-card">
            <div className="order-header">
              <div>
                <h3>Order #{order.id}</h3>
                <p className="order-date">
                  {new Date(order.created_at).toLocaleDateString()}
                </p>
              </div>
              <span className={`order-status ${getStatusClass(order.status)}`}>
                {order.status.toUpperCase()}
              </span>
            </div>
            <div className="order-items">
              {order.order_items.map((item) => (
                <div key={item.id} className="order-item">
                  <span>{item.product?.name || 'Product'} x {item.quantity}</span>
                  <span>${(item.price * item.quantity).toFixed(2)}</span>
                </div>
              ))}
            </div>
            <div className="order-footer">
              <div>
                <strong>Shipping Address:</strong>
                <p>{order.shipping_address}</p>
              </div>
              <div className="order-total">
                <strong>Total: ${order.total_amount.toFixed(2)}</strong>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Orders;
