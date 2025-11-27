import { motion } from 'framer-motion';
import { CartItem as CartItemType } from '../types';
import { cartService } from '../services/cartService';

interface CartItemProps {
  item: CartItemType;
  productName?: string;
  productImage?: string;
  onUpdate?: () => void;
}

export const CartItem = ({ item, productName = 'Product', productImage, onUpdate }: CartItemProps) => {
  const handleRemove = async () => {
    await cartService.removeFromCart(item.productId);
    onUpdate?.();
  };

  const handleQuantityChange = async (newQuantity: number) => {
    if (newQuantity <= 0) {
      await handleRemove();
      return;
    }
    await cartService.removeFromCart(item.productId);
    await cartService.addToCart(item.productId, newQuantity);
    onUpdate?.();
  };

  return (
    <motion.div
      initial={{ opacity: 0, x: -20 }}
      animate={{ opacity: 1, x: 0 }}
      exit={{ opacity: 0, x: 20 }}
      className="flex items-center space-x-4 bg-white p-4 rounded-lg shadow-sm"
    >
      {productImage && (
        <img
          src={productImage}
          alt={productName}
          className="w-20 h-20 object-cover rounded"
        />
      )}
      <div className="flex-1">
        <h4 className="font-semibold text-gray-900">{productName}</h4>
        <p className="text-sm text-gray-600">${item.price.toFixed(2)} each</p>
      </div>
      <div className="flex items-center space-x-2">
        <button
          onClick={() => handleQuantityChange(item.quantity - 1)}
          className="w-8 h-8 rounded-full bg-gray-200 hover:bg-gray-300 flex items-center justify-center"
        >
          -
        </button>
        <span className="w-8 text-center">{item.quantity}</span>
        <button
          onClick={() => handleQuantityChange(item.quantity + 1)}
          className="w-8 h-8 rounded-full bg-gray-200 hover:bg-gray-300 flex items-center justify-center"
        >
          +
        </button>
      </div>
      <div className="text-right">
        <p className="font-semibold text-gray-900">
          ${(item.price * item.quantity).toFixed(2)}
        </p>
        <button
          onClick={handleRemove}
          className="text-sm text-red-600 hover:text-red-800 mt-1"
        >
          Remove
        </button>
      </div>
    </motion.div>
  );
};


