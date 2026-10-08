import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import axios from 'axios';
import { orderService } from '../services/orderService';
import { cartService } from '../services/cartService';
import { Button } from '../components/Button';
import { Input } from '../components/Input';
import { authService } from '../services/authService';

export const CheckoutPage = () => {
  const navigate = useNavigate();
  const [loading, setLoading] = useState(false);
  const [priceNotice, setPriceNotice] = useState<string | null>(null);
  const [formData, setFormData] = useState({
    address: '',
    city: '',
    state: '',
    zipCode: '',
  });

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    
    if (!authService.isAuthenticated()) {
      navigate('/login');
      return;
    }

    try {
      setLoading(true);
      setPriceNotice(null);
      const order = await orderService.createOrder({
        address: formData.address,
        city: formData.city,
        state: formData.state,
        zipCode: formData.zipCode,
      });
      await cartService.clearCart();
      navigate(`/orders/${order.id}`);
    } catch (error) {
      console.error('Failed to create order:', error);
      if (axios.isAxiosError(error) && error.response?.status === 409) {
        const changedLines = error.response.data?.detail?.changedLines ?? [];
        const names = changedLines.map((line: { name: string }) => line.name).join(', ');
        setPriceNotice(`The price changed for ${names || 'one or more items'}. Review your cart before trying again.`);
      } else {
        setPriceNotice('Failed to place the order. Please check your address and try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="min-h-screen py-8"
    >
      <div className="max-w-2xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Checkout</h1>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <h2 className="text-xl font-semibold mb-4">Shipping Address</h2>
            <div className="space-y-4">
              <Input
                label="Address"
                value={formData.address}
                onChange={(e) => setFormData({ ...formData, address: e.target.value })}
                required
              />
              <div className="grid grid-cols-2 gap-4">
                <Input
                  label="City"
                  value={formData.city}
                  onChange={(e) => setFormData({ ...formData, city: e.target.value })}
                  required
                />
                <Input
                  label="State"
                  value={formData.state}
                  onChange={(e) => setFormData({ ...formData, state: e.target.value })}
                  required
                />
              </div>
              <Input
                label="Zip Code"
                value={formData.zipCode}
                onChange={(e) => setFormData({ ...formData, zipCode: e.target.value })}
                required
              />
            </div>
          </div>

          <p className="rounded-lg bg-amber-50 p-4 text-amber-900">
            This demonstration store does not collect card details. Payment methods will be configured before live orders are enabled.
          </p>
          {priceNotice && (
            <p role="alert" className="rounded-lg bg-red-50 p-4 text-red-800">
              {priceNotice}
            </p>
          )}

          <Button type="submit" disabled={loading} className="w-full">
            {loading ? 'Processing...' : 'Place Order'}
          </Button>
        </form>
      </div>
    </motion.div>
  );
};
