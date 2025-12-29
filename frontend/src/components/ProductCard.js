import React from 'react';
import './ProductCard.css';

const ProductCard = ({ product, onAddToCart, onViewDetails }) => {
  return (
    <div className="product-card">
      <img src={product.image_url || 'https://via.placeholder.com/300'} alt={product.name} />
      <div className="product-info">
        <h3>{product.name}</h3>
        <p className="product-description">{product.description}</p>
        <div className="product-footer">
          <span className="price">${product.price.toFixed(2)}</span>
          <span className="stock">Stock: {product.stock}</span>
        </div>
        <div className="product-actions">
          <button onClick={() => onViewDetails(product.id)} className="btn-view">
            View Details
          </button>
          <button 
            onClick={() => onAddToCart(product.id)} 
            className="btn-add-cart"
            disabled={product.stock === 0}
          >
            {product.stock === 0 ? 'Out of Stock' : 'Add to Cart'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ProductCard;
