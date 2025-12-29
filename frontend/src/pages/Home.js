import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { productsAPI, categoriesAPI } from '../services/api';
import { useCart } from '../context/CartContext';
import { useAuth } from '../context/AuthContext';
import ProductCard from '../components/ProductCard';
import './Home.css';

const Home = () => {
  const [products, setProducts] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [loading, setLoading] = useState(true);
  const { addToCart } = useCart();
  const { isAuthenticated } = useAuth();
  const navigate = useNavigate();

  useEffect(() => {
    fetchData();
  }, [selectedCategory]);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [productsRes, categoriesRes] = await Promise.all([
        productsAPI.getAll({ category_id: selectedCategory }),
        categoriesAPI.getAll(),
      ]);
      setProducts(productsRes.data);
      setCategories(categoriesRes.data);
    } catch (error) {
      console.error('Error fetching data:', error);
    } finally {
      setLoading(false);
    }
  };

  const handleAddToCart = async (productId) => {
    if (!isAuthenticated) {
      alert('Please login to add items to cart');
      navigate('/login');
      return;
    }
    try {
      await addToCart(productId, 1);
      alert('Product added to cart!');
    } catch (error) {
      alert('Error adding product to cart');
    }
  };

  const handleViewDetails = (productId) => {
    navigate(`/products/${productId}`);
  };

  if (loading) {
    return <div className="loading">Loading...</div>;
  }

  return (
    <div className="home-container">
      <div className="hero-section">
        <h1>Welcome to Our E-Commerce Store</h1>
        <p>Find the best products at great prices</p>
      </div>

      <div className="categories-filter">
        <button
          className={!selectedCategory ? 'active' : ''}
          onClick={() => setSelectedCategory(null)}
        >
          All Products
        </button>
        {categories.map((category) => (
          <button
            key={category.id}
            className={selectedCategory === category.id ? 'active' : ''}
            onClick={() => setSelectedCategory(category.id)}
          >
            {category.name}
          </button>
        ))}
      </div>

      <div className="products-grid">
        {products.length === 0 ? (
          <p>No products found</p>
        ) : (
          products.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onAddToCart={handleAddToCart}
              onViewDetails={handleViewDetails}
            />
          ))
        )}
      </div>
    </div>
  );
};

export default Home;
