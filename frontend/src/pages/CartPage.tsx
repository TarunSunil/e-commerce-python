import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useNavigate } from 'react-router-dom';
import { CartItem as CartItemType, Product } from '../types';
import { cartService } from '../services/cartService';
import { productService } from '../services/productService';
import { CartItem } from '../components/CartItem';
import { LoadingSpinner } from '../components/LoadingSpinner';
import { Button } from '../components/Button';
import { authService } from '../services/authService';

export const CartPage = () => {
  const navigate = useNavigate();
  const [cartItems, setCartItems] = useState<CartItemType[]>([]);
  const [products, setProducts] = useState<Record<string, Product>>({});
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

      // Load product details
      const productMap: Record<string, Product> = {};
      for (const item of items) {
        try {
          const product = await productService.getProductById(item.productId);
          productMap[item.productId] = product;
        } catch (error) {
          console.error(`Failed to load product ${item.productId}:`, error);
        }
      }
      setProducts(productMap);

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
      <div className="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <h1 className="text-3xl font-bold text-gray-900 mb-8">Shopping Cart</h1>

        {cartItems.length === 0 ? (
          <div className="text-center py-12">
            <p className="text-gray-500 text-lg mb-4">Your cart is empty</p>
            <Button onClick={() => navigate('/')}>Continue Shopping</Button>
          </div>
        ) : (
          <div className="space-y-4">
            <AnimatePresence>
              {cartItems.map((item) => (
                <CartItem
                  key={item.id}
                  item={item}
                  productName={products[item.productId]?.name}
                  productImage={products[item.productId]?.images?.[0]}
                  onUpdate={loadCart}
                />
              ))}
            </AnimatePresence>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="bg-white p-6 rounded-lg shadow-md mt-8"
            >
              <div className="flex justify-between items-center mb-4">
                <span className="text-xl font-semibold">Total:</span>
                <span className="text-2xl font-bold text-primary-600">
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


