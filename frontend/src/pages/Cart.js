import React from 'react';
import { useNavigate } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import './Cart.css';

const Cart = () => {
  const { cart, updateCartItem, removeFromCart, loading } = useCart();
  const navigate = useNavigate();

  const handleUpdateQuantity = async (itemId, newQuantity) => {
    if (newQuantity < 1) return;
    try {
      await updateCartItem(itemId, newQuantity);
    } catch (error) {
      alert('Error updating cart item');
    }
  };

  const handleRemoveItem = async (itemId) => {
    try {
      await removeFromCart(itemId);
    } catch (error) {
      alert('Error removing item from cart');
    }
  };

  const handleCheckout = () => {
    navigate('/checkout');
  };

  if (loading) {
    return <div className="loading">Loading cart...</div>;
  }

  if (cart.items.length === 0) {
    return (
      <div className="cart-container">
        <h2>Shopping Cart</h2>
        <div className="empty-cart">
          <p>Your cart is empty</p>
          <button onClick={() => navigate('/products')} className="btn-shop">
            Continue Shopping
          </button>
        </div>
      </div>
    );
  }

  return (
    <div className="cart-container">
      <h2>Shopping Cart</h2>
      <div className="cart-items">
        {cart.items.map((item) => (
          <div key={item.id} className="cart-item">
            <img src={item.product.image_url || 'https://via.placeholder.com/100'} alt={item.product.name} />
            <div className="item-details">
              <h3>{item.product.name}</h3>
              <p className="item-price">${item.product.price.toFixed(2)}</p>
            </div>
            <div className="item-quantity">
              <button onClick={() => handleUpdateQuantity(item.id, item.quantity - 1)}>-</button>
              <span>{item.quantity}</span>
              <button onClick={() => handleUpdateQuantity(item.id, item.quantity + 1)}>+</button>
            </div>
            <div className="item-total">
              ${(item.product.price * item.quantity).toFixed(2)}
            </div>
            <button onClick={() => handleRemoveItem(item.id)} className="btn-remove">
              Remove
            </button>
          </div>
        ))}
      </div>
      <div className="cart-summary">
        <div className="summary-row">
          <span>Subtotal:</span>
          <span>${cart.total.toFixed(2)}</span>
        </div>
        <div className="summary-row total">
          <span>Total:</span>
          <span>${cart.total.toFixed(2)}</span>
        </div>
        <button onClick={handleCheckout} className="btn-checkout">
          Proceed to Checkout
        </button>
      </div>
    </div>
  );
};

export default Cart;
