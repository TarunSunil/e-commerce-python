import { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { Order } from '../types';
import { orderService } from '../services/orderService';
import { LoadingSpinner } from '../components/LoadingSpinner';

export const OrderDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const [order, setOrder] = useState<Order | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    if (!id) return;
    orderService.getOrderById(id).then(setOrder).catch(() => setError('We could not load this order.'));
  }, [id]);

  if (error) return <p className="mx-auto max-w-2xl px-4 py-12 text-red-700">{error}</p>;
  if (!order) return <div className="flex min-h-screen items-center justify-center"><LoadingSpinner size="lg" /></div>;

  return (
    <main className="container-meridian page-shell py-14">
      <p className="eyebrow mb-3">Confirmation</p>
      <h1 className="display-lg mb-2 font-bold">Order placed</h1>
      <p className="mb-8 text-meridian-muted">Order #{order.id.slice(0, 8)} · {order.status}</p>
      <section className="surface space-y-3 p-6 sm:p-8">
        {order.items.map((item) => (
          <div key={item.productId} className="flex justify-between border-b pb-3">
            <span>{item.qty}x {item.productName || 'Product unavailable'}</span>
            <span>
              {Number.isFinite(Number(item.unitPrice)) && Number.isFinite(Number(item.qty))
                ? `$${(Number(item.unitPrice) * Number(item.qty)).toFixed(2)}`
                : 'Price unavailable'}
            </span>
          </div>
        ))}
        <div className="flex justify-between pt-2 text-lg font-semibold">
          <span>Total</span>
          <span>{Number.isFinite(Number(order.total)) ? `$${Number(order.total).toFixed(2)}` : 'Total unavailable'}</span>
        </div>
      </section>
    </main>
  );
};
