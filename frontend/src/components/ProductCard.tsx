import React from 'react';
import { Product } from '../types';
import { useNavigate } from 'react-router-dom';

interface ProductCardProps {
  product: Product;
  index?: number;
}

export const ProductCard = ({ product, index = 0 }: ProductCardProps) => {
  const navigate = useNavigate();
  const [imageFailed, setImageFailed] = React.useState(false);
  const initials = product.name.split(/\s+/).map((part) => part[0]).join('').slice(0, 2).toUpperCase();

  return (
    <article
      style={{ animationDelay: `${index * 60}ms` }}
      className="surface product-card cursor-pointer overflow-hidden animate-rise"
      onClick={() => navigate(`/products/${product.id}`)}
    >
      <div className="relative aspect-[4/3] overflow-hidden bg-meridian-deep">
        {product.images?.[0] && !imageFailed ? (
          <img
            src={product.images[0]}
            alt={product.name}
            onError={() => setImageFailed(true)}
            className="h-full w-full object-cover transition-transform duration-500"
          />
        ) : (
          <div className="grid h-full place-items-center bg-gradient-to-br from-meridian-deep to-meridian-brand">
            <span className="font-display text-5xl font-bold text-meridian-highlight">{initials}</span>
          </div>
        )}
      </div>
      <div className="p-5">
        <div className="mb-3 flex items-start justify-between gap-4">
        <h3 className="font-display text-xl font-bold leading-tight text-meridian-ink">
          {product.name}
        </h3>
          <span className="whitespace-nowrap text-lg font-bold text-meridian-brand">${Number(product.price).toFixed(2)}</span>
        </div>
        <p className="mb-5 line-clamp-2 text-sm leading-6 text-meridian-muted">{product.description}</p>
        <span className={`text-xs font-bold uppercase tracking-wider ${product.stock > 0 ? 'text-meridian-brand' : 'text-meridian-sale'}`}>
          {product.stock > 0 ? 'Available now' : 'Out of stock'}
        </span>
        {product.categories && product.categories.length > 0 && (
          <div className="mt-4 flex flex-wrap gap-2">
            {product.categories.slice(0, 2).map((category) => (
              <span key={category} className="rounded-full bg-meridian-highlight/40 px-3 py-1 text-xs font-semibold text-meridian-deep">
                {category}
              </span>
            ))}
          </div>
        )}
      </div>
    </article>
  );
};
