import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { CartItem as CartItemType } from '../types';
import { cartService } from '../services/cartService';
import { CartItem } from '../components/CartItem';
import { LoadingSpinner } from '../components/LoadingSpinner';
import { Button } from '../components/Button';
import { authService } from '../services/authService';

export const CartPage = () => {
  const navigate = useNavigate();
  const [cartItems, setCartItems] = useState<CartItemType[]>([]);
  const [loading, setLoading] = useState(true);
  const [total, setTotal] = useState(0);

  useEffect(() => {
    if (!authService.isAuthenticated()) {
      navigate('/login');
      return;
    }
    loadCart();
  }, []);

  const loadCart = async () => {
    try {
      setLoading(true);
      const items = await cartService.getCart();
      setCartItems(items);

      // Calculate total
      const cartTotal = await cartService.getCartTotal();
      setTotal(cartTotal);
    } catch (error) {
      console.error('Failed to load cart:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleCheckout = () => {
    navigate('/checkout');
  };

  if (loading) {
    return (
      <div className="flex justify-center items-center h-screen">
        <LoadingSpinner size="lg" />
      </div>
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
        <p className="eyebrow mb-3">Your edit</p>
        <h1 className="display-lg mb-10 font-bold">Shopping cart</h1>

        {cartItems.length === 0 ? (
          <div className="text-center py-12">
            <p className="mb-4 text-lg text-meridian-muted">Your cart is empty</p>
            <Button onClick={() => navigate('/')}>Continue Shopping</Button>
          </div>
        ) : (
          <div className="space-y-4">
            <AnimatePresence>
              {cartItems.map((item) => (
                <CartItem
                  key={item.id}
                  item={item}
                  productName={item.productName}
                  productImage={item.productImage}
                  onUpdate={loadCart}
                />
              ))}
            </AnimatePresence>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="surface mt-8 p-6"
            >
              <div className="flex justify-between items-center mb-4">
                <span className="text-xl font-semibold">Total</span>
                <span className="text-2xl font-bold text-meridian-brand">
                  ${total.toFixed(2)}
                </span>
              </div>
              <Button onClick={handleCheckout} className="w-full">
                Proceed to Checkout
              </Button>
            </motion.div>
          </div>
        )}
      </div>
    </motion.div>
  );
};
