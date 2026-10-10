import { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Product } from '../types';
import { productService } from '../services/productService';
import { cartService } from '../services/cartService';
import { recommendationService } from '../services/recommendationService';
import { LoadingSpinner } from '../components/LoadingSpinner';
import { Button } from '../components/Button';
import { ProductCard } from '../components/ProductCard';
import { authService } from '../services/authService';
import { useState as useImageState } from 'react';

export const ProductDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();
  const [product, setProduct] = useState<Product | null>(null);
  const [recommendations, setRecommendations] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [quantity, setQuantity] = useState(1);
  const [addingToCart, setAddingToCart] = useState(false);
  const [imageFailed, setImageFailed] = useImageState(false);

  useEffect(() => {
    if (id) {
      loadProduct();
      loadRecommendations();
    }
  }, [id]);

  const loadProduct = async () => {
    if (!id) return;
    try {
      setLoading(true);
      const data = await productService.getProductById(id);
      setProduct(data);
    } catch (error) {
      console.error('Failed to load product:', error);
    } finally {
      setLoading(false);
    }
  };

  const loadRecommendations = async () => {
    if (!id) return;
    try {
      const data = await recommendationService.getRecommendationsByProduct(id, 4);
      setRecommendations(data);
    } catch (error) {
      console.error('Failed to load recommendations:', error);
    }
  };

  const handleAddToCart = async () => {
    if (!authService.isAuthenticated()) {
      navigate('/login');
      return;
    }

    if (!product) return;

    try {
      setAddingToCart(true);
      await cartService.addToCart(product.id, quantity);
      alert('Product added to cart!');
    } catch (error) {
      console.error('Failed to add to cart:', error);
      alert('Failed to add product to cart');
    } finally {
      setAddingToCart(false);
    }
  };

  if (loading) {
    return (
      <div className="flex min-h-[70vh] items-center justify-center">
        <LoadingSpinner size="lg" />
      </div>
    );
  }

  if (!product) {
    return (
      <div className="container-meridian py-20 text-center">
        <p className="text-meridian-muted">Product not found</p>
      </div>
    );
  }

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      className="page-shell py-10 lg:py-20"
    >
      <div className="container-meridian">
        <div className="grid grid-cols-1 gap-10 lg:grid-cols-2 lg:gap-20">
          <motion.div
            initial={{ x: -50, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            className="surface overflow-hidden"
          >
            {product.images?.[0] && !imageFailed ? (
              <img
                src={product.images[0]}
                alt={product.name}
                onError={() => setImageFailed(true)}
                className="aspect-square w-full object-cover"
              />
            ) : (
              <div className="grid aspect-square place-items-center bg-gradient-to-br from-meridian-deep to-meridian-brand">
                <span className="font-display text-8xl font-bold text-meridian-highlight">{product.name.slice(0, 2).toUpperCase()}</span>
              </div>
            )}
          </motion.div>

          <motion.div
            initial={{ x: 50, opacity: 0 }}
            animate={{ x: 0, opacity: 1 }}
            className="flex flex-col justify-center"
          >
            <p className="eyebrow mb-5">The details</p>
            <h1 className="display-lg font-bold">{product.name}</h1>
            <p className="mt-6 text-3xl font-bold text-meridian-brand">
              ${product.price.toFixed(2)}
            </p>
            <p className="mt-6 max-w-xl text-lg leading-8 text-meridian-muted">{product.description}</p>

            {product.categories && product.categories.length > 0 && (
              <div className="flex flex-wrap gap-2">
                {product.categories.map((category) => (
                  <span
                    key={category}
                    className="rounded-full bg-meridian-highlight/40 px-3 py-1 text-sm font-semibold text-meridian-deep"
                  >
                    {category}
                  </span>
                ))}
              </div>
            )}

            <div className="mt-8 flex items-center gap-4">
              <span className="text-sm font-semibold text-meridian-muted">Quantity</span>
              <div className="flex items-center gap-2">
                <button
                  onClick={() => setQuantity(Math.max(1, quantity - 1))}
                  className="grid h-11 w-11 place-items-center rounded-full border border-meridian-ink/20 hover:border-meridian-brand"
                >
                  -
                </button>
                <span className="w-12 text-center font-bold">{quantity}</span>
                <button
                  onClick={() => setQuantity(quantity + 1)}
                  className="grid h-11 w-11 place-items-center rounded-full border border-meridian-ink/20 hover:border-meridian-brand"
                >
                  +
                </button>
              </div>
            </div>

            <div className="mt-5">
              <span className={`text-sm font-bold ${product.stock > 0 ? 'text-meridian-brand' : 'text-meridian-sale'}`}>
                {product.stock > 0 ? 'Available now' : 'Out of stock'}
              </span>
            </div>

            <Button
              onClick={handleAddToCart}
              disabled={product.stock === 0 || addingToCart}
              className="mt-8 w-full sm:w-auto"
            >
              {addingToCart ? 'Adding...' : 'Add to Cart'}
            </Button>
          </motion.div>
        </div>

        {recommendations.length > 0 && (
          <div>
            <h2 className="text-2xl font-bold text-gray-900 mb-6">You might also like</h2>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
              {recommendations.map((rec, index) => (
                <ProductCard key={rec.id} product={rec} index={index} />
              ))}
            </div>
          </div>
        )}
      </div>
    </motion.div>
  );
};

