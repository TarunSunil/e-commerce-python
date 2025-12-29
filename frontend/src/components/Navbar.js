import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { useCart } from '../context/CartContext';
import './Navbar.css';

const Navbar = () => {
  const { isAuthenticated, isAdmin, user, logout } = useAuth();
  const { cart } = useCart();

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          E-Commerce
        </Link>
        <ul className="navbar-menu">
          <li><Link to="/">Home</Link></li>
          <li><Link to="/products">Products</Link></li>
          {isAdmin && <li><Link to="/admin">Admin</Link></li>}
        </ul>
        <div className="navbar-actions">
          {isAuthenticated ? (
            <>
              <Link to="/cart" className="cart-link">
                Cart ({cart.items.length})
              </Link>
              <Link to="/orders">Orders</Link>
              <span>Welcome, {user?.username}</span>
              <button onClick={logout} className="btn-logout">Logout</button>
            </>
          ) : (
            <>
              <Link to="/login">Login</Link>
              <Link to="/register">Register</Link>
            </>
          )}
        </div>
      </div>
    </nav>
  );
};

export default Navbar;
