import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { motion } from 'framer-motion';
import axios from 'axios';
import { authService } from '../services/authService';
import { Button } from '../components/Button';
import { Input } from '../components/Input';

export const RegisterPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({ name: '', email: '', password: '' });
  const [error, setError] = useState('');
  const [loading, setLoading] = useState(false);

  const getErrorMessage = (error: unknown) => {
    if (!axios.isAxiosError(error)) return 'Registration failed';
    const detail = error.response?.data?.detail;
    if (Array.isArray(detail)) return detail.map((item) => item.msg).join(', ');
    if (typeof detail === 'string') return detail;
    return 'Registration failed';
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      await authService.register(formData);
      navigate('/');
    } catch (error: unknown) {
      setError(getErrorMessage(error));
    } finally {
      setLoading(false);
    }
  };

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      exit={{ opacity: 0, y: -20 }}
      className="page-shell flex items-center justify-center px-5 py-16"
    >
      <div className="surface w-full max-w-md p-7 sm:p-10">
        <div>
          <p className="eyebrow mb-3">Join Meridian</p>
          <h2 className="display-lg font-bold">
            Make it yours
          </h2>
        </div>
        <form className="mt-8 space-y-6" onSubmit={handleSubmit}>
          {error && (
            <div className="rounded-xl border border-meridian-sale/40 bg-meridian-sale/10 px-4 py-3 text-meridian-sale">
              {error}
            </div>
          )}
          <div className="space-y-4">
            <Input
              label="Name"
              type="text"
              value={formData.name}
              onChange={(e) => setFormData({ ...formData, name: e.target.value })}
              required
            />
            <Input
              label="Email"
              type="email"
              value={formData.email}
              onChange={(e) => setFormData({ ...formData, email: e.target.value })}
              required
            />
            <Input
              label="Password"
              type="password"
              value={formData.password}
              onChange={(e) => setFormData({ ...formData, password: e.target.value })}
              required
              minLength={8}
            />
          </div>
          <Button type="submit" disabled={loading} className="w-full">
            {loading ? 'Creating account...' : 'Sign up'}
          </Button>
          <p className="text-center text-sm text-meridian-muted">
            Already have an account?{' '}
            <Link to="/login" className="font-bold text-meridian-brand hover:text-meridian-deep">
              Sign in
            </Link>
          </p>
        </form>
      </div>
    </motion.div>
  );
};
