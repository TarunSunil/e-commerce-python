import { useEffect, useState } from 'react';
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
  const [checkingCart, setCheckingCart] = useState(true);
  const [priceNotice, setPriceNotice] = useState<string | null>(null);
  const [formData, setFormData] = useState({
    address: '',
    city: '',
    state: '',
    zipCode: '',
  });

  useEffect(() => {
    let active = true;
    cartService.getCart()
      .then((items) => {
        if (active && items.length === 0) {
          navigate('/cart', { replace: true });
        }
      })
      .catch((error) => {
        console.error('Failed to verify cart before checkout:', error);
      })
      .finally(() => {
        if (active) setCheckingCart(false);
      });

    return () => {
      active = false;
    };
  }, [navigate]);

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
        const detail = axios.isAxiosError(error) ? error.response?.data?.detail : null;
        const serverMessage = Array.isArray(detail)
          ? detail.map((item: { msg?: string }) => item.msg).filter(Boolean).join(', ')
          : typeof detail === 'object' && detail !== null && typeof detail.message === 'string'
            ? detail.message
            : typeof detail === 'string'
              ? detail
              : null;
        setPriceNotice(serverMessage || 'Failed to place the order. Please check your address and try again.');
      }
    } finally {
      setLoading(false);
    }
  };

  if (checkingCart) {
    return <div className="flex min-h-screen items-center justify-center">Checking your cart...</div>;
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="min-h-screen py-8"
    >
      <div className="container-meridian max-w-3xl">
        <p className="eyebrow mb-3">Almost yours</p>
        <h1 className="display-lg mb-10 font-bold">Checkout</h1>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="surface p-6 sm:p-8">
            <h2 className="mb-5 font-display text-2xl font-bold">Shipping address</h2>
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

          <p className="rounded-2xl border border-meridian-ink/10 bg-meridian-highlight/30 p-4 text-meridian-deep">
            This demonstration store does not collect card details. Payment methods will be configured before live orders are enabled.
          </p>
          {priceNotice && (
            <p role="alert" className="rounded-2xl border border-meridian-sale/40 bg-meridian-sale/10 p-4 text-meridian-sale">
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
