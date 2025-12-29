import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useCart } from '../context/CartContext';
import { ordersAPI } from '../services/api';
import './Checkout.css';

const Checkout = () => {
  const [shippingAddress, setShippingAddress] = useState('');
  const [loading, setLoading] = useState(false);
  const { cart, clearCart } = useCart();
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);

    try {
      await ordersAPI.create({ shipping_address: shippingAddress });
      await clearCart();
      alert('Order placed successfully!');
      navigate('/orders');
    } catch (error) {
      alert(error.response?.data?.detail || 'Error placing order');
    } finally {
      setLoading(false);
    }
  };

  if (cart.items.length === 0) {
    return (
      <div className="checkout-container">
        <h2>Checkout</h2>
        <p>Your cart is empty</p>
      </div>
    );
  }

  return (
    <div className="checkout-container">
      <h2>Checkout</h2>
      <div className="checkout-content">
        <div className="order-summary">
          <h3>Order Summary</h3>
          {cart.items.map((item) => (
            <div key={item.id} className="summary-item">
              <span>{item.product.name} x {item.quantity}</span>
              <span>${(item.product.price * item.quantity).toFixed(2)}</span>
            </div>
          ))}
          <div className="summary-total">
            <span>Total:</span>
            <span>${cart.total.toFixed(2)}</span>
          </div>
        </div>

        <form onSubmit={handleSubmit} className="checkout-form">
          <h3>Shipping Information</h3>
          <div className="form-group">
            <label>Shipping Address</label>
            <textarea
              value={shippingAddress}
              onChange={(e) => setShippingAddress(e.target.value)}
              required
              rows="4"
              placeholder="Enter your full shipping address"
            />
          </div>
          <button type="submit" disabled={loading} className="btn-place-order">
            {loading ? 'Placing Order...' : 'Place Order'}
          </button>
        </form>
      </div>
    </div>
  );
};

export default Checkout;
