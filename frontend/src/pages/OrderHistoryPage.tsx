import { useState, useEffect } from 'react';
import { motion } from 'framer-motion';
import { Order } from '../types';
import { orderService } from '../services/orderService';
import { LoadingSpinner } from '../components/LoadingSpinner';
import { authService } from '../services/authService';
import { useNavigate } from 'react-router-dom';

export const OrderHistoryPage = () => {
  const navigate = useNavigate();
  const [orders, setOrders] = useState<Order[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const user = authService.getCurrentUser();

  useEffect(() => {
    if (!authService.isAuthenticated() || !user) {
      navigate('/login');
      return;
    }
    loadOrders();
  }, []);

  const loadOrders = async () => {
    if (!user) return;
    try {
      setLoading(true);
      setError(null);
      const data = await orderService.getUserOrders(user.userId);
      setOrders(data);
    } catch (error) {
      console.error('Failed to load orders:', error);
      setError('We could not load your orders.');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  if (error) {
    return (
      <main className="mx-auto max-w-2xl px-4 py-12 text-center">
        <p role="alert" className="text-red-700">{error}</p>
        <button type="button" onClick={loadOrders} className="mt-4 rounded-lg bg-primary-600 px-4 py-2 text-white">
          Retry
        </button>
      </main>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="min-h-screen py-8"
    >
      <div className="container-meridian">
        <p className="eyebrow mb-3">Your account</p>
        <h1 className="display-lg mb-10 font-bold">Orders</h1>

        {orders.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg">No orders found</p>
          </div>
        ) : (
          <div className="space-y-4">
            {orders.map((order, index) => (
              <motion.div
                key={order.id}
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                className="surface p-6"
              >
                <div className="flex justify-between items-start mb-4">
                  <div>
                    <h3 className="font-display text-xl font-bold">Order #{order.id.slice(0, 8)}</h3>
                    <p className="text-sm text-meridian-muted">
                      {new Date(order.createdAt).toLocaleDateString()}
                    </p>
                  </div>
                  <div className="text-right">
                    <p className="text-lg font-semibold text-meridian-brand">
                      ${Number.isFinite(Number(order.total)) ? Number(order.total).toFixed(2) : '—'}
                    </p>
                    <span className={`text-sm px-2 py-1 rounded ${
                      'rounded-full bg-meridian-highlight/40 text-meridian-deep'
                    }`}>
                      {order.status}
                    </span>
                  </div>
                </div>
                <div className="border-t pt-4">
                  <p className="mb-2 text-sm text-meridian-muted">Items:</p>
                  <ul className="space-y-1">
                    {order.items.map((item, idx) => (
                      <li key={idx} className="text-sm">
                        {item.qty}x {item.productName || 'Product unavailable'} - ${
                          Number.isFinite(Number(item.unitPrice)) ? Number(item.unitPrice).toFixed(2) : '—'
                        } each
                      </li>
                    ))}
                  </ul>
                </div>
              </motion.div>
            ))}
          </div>
        )}
      </div>
    </motion.div>
  );
};
