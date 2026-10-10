import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Product } from '../types';
import { productService } from '../services/productService';
import { ProductCard } from '../components/ProductCard';
import { LoadingSpinner } from '../components/LoadingSpinner';
import { Input } from '../components/Input';

export const HomePage = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  const [category, setCategory] = useState('');

  const loadProducts = async () => {
    try {
      setLoading(true);
      setProducts(await productService.getAllProducts(0, 100, category || undefined, search || undefined));
    } catch (error) {
      console.error('Failed to load products:', error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => { void loadProducts(); }, [category]);

  return (
    <main className="page-shell">
      <section className="container-meridian grid gap-10 py-14 lg:grid-cols-[1.05fr_.95fr] lg:items-center lg:py-24">
        <div>
          <p className="eyebrow mb-5">Objects for a considered life</p>
          <h1 className="display-xl max-w-3xl font-display font-bold">Good things,<br /><span className="text-meridian-brand">well chosen.</span></h1>
          <p className="mt-7 max-w-lg text-lg leading-8 text-meridian-muted">A calm, honest marketplace for products that earn their place in your everyday.</p>
          <div className="mt-9 flex flex-wrap gap-3">
            <a href="#collection" className="btn-primary">Explore the collection</a>
            <Link to="/orders" className="btn-secondary">Track an order</Link>
          </div>
        </div>
        <div className="relative min-h-[340px] overflow-hidden rounded-[36px] bg-meridian-deep p-8 text-meridian-highlight lg:min-h-[460px]">
          <div className="absolute -right-20 -top-16 h-72 w-72 rounded-full border-[36px] border-meridian-highlight/20" />
          <div className="absolute bottom-8 left-8 max-w-xs">
            <p className="eyebrow !text-meridian-highlight">Meridian edit</p>
            <p className="mt-4 font-display text-4xl font-bold leading-none">Useful, beautiful, built to last.</p>
          </div>
          <span className="absolute right-8 top-8 text-8xl font-display font-bold opacity-20">M</span>
        </div>
      </section>

      <section id="collection" className="container-meridian pb-20">
        <div className="mb-8 flex flex-col gap-5 border-b border-meridian-ink/10 pb-6 md:flex-row md:items-end md:justify-between">
          <div><p className="eyebrow mb-3">The collection</p><h2 className="display-lg font-bold">Find your next favourite.</h2></div>
          <div className="flex flex-col gap-3 sm:flex-row">
            <Input label="Search" value={search} placeholder="Search products..." onChange={(event) => setSearch(event.target.value)} onKeyDown={(event) => event.key === 'Enter' && void loadProducts()} />
            <select aria-label="Category" value={category} onChange={(event) => setCategory(event.target.value)} className="input-field sm:w-48">
              <option value="">All categories</option><option value="electronics">Electronics</option><option value="home">Home</option><option value="clothing">Clothing</option>
            </select>
          </div>
        </div>
        {loading ? <div className="flex h-64 items-center justify-center"><LoadingSpinner size="lg" /></div> :
          products.length === 0 ? <div className="surface p-12 text-center text-meridian-muted">No products found. Try another search.</div> :
          <div className="grid gap-5 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">{products.map((product, index) => <ProductCard key={product.id} product={product} index={index} />)}</div>}
      </section>
    </main>
  );
};
