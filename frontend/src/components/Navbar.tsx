import { Link, useNavigate } from 'react-router-dom';
import { authService } from '../services/authService';

interface NavbarProps {
  theme: 'light' | 'dark';
  onToggleTheme: () => void;
}

export const Navbar = ({ theme, onToggleTheme }: NavbarProps) => {
  const navigate = useNavigate();
  const user = authService.getCurrentUser();
  const isAuthenticated = authService.isAuthenticated();
  const isAdmin = authService.isAdmin();

  const handleLogout = () => {
    authService.logout();
    navigate('/login');
  };

  return (
    <nav className="sticky top-0 z-50 border-b border-meridian-ink/10 bg-meridian-bg/90 backdrop-blur">
      <div className="container-meridian flex h-[76px] items-center justify-between gap-5">
          <Link to="/" className="flex items-center gap-2" aria-label="Meridian home">
            <span className="grid h-10 w-10 place-items-center rounded-xl bg-meridian-deep text-lg font-bold text-meridian-highlight">M</span>
            <span className="font-display text-2xl font-bold tracking-tight">meridian<span className="text-meridian-brand">.</span></span>
          </Link>

          <div className="hidden items-center gap-6 md:flex">
            <Link to="/" className="text-sm font-semibold text-meridian-muted hover:text-meridian-brand">Shop</Link>
            <Link to="/orders" className="text-sm font-semibold text-meridian-muted hover:text-meridian-brand">Orders</Link>
            {isAdmin && <Link to="/admin" className="text-sm font-semibold text-meridian-muted hover:text-meridian-brand">Admin</Link>}
          </div>

          <div className="flex items-center gap-2">
            <button type="button" onClick={onToggleTheme} className="grid h-11 w-11 place-items-center rounded-full border border-meridian-ink/15 text-lg" aria-label={`Use ${theme === 'dark' ? 'light' : 'dark'} theme`}>
              {theme === 'dark' ? 'Light' : 'Dark'}
            </button>
            {isAuthenticated ? (
              <>
                <Link to="/cart" className="btn-primary !min-h-11 !px-5">Cart</Link>
                <button type="button" onClick={handleLogout} className="hidden text-sm font-semibold text-meridian-muted hover:text-meridian-brand sm:block">{user?.name ? `Hi, ${user.name}` : 'Log out'}</button>
              </>
            ) : (
              <>
                <Link to="/login" className="hidden text-sm font-semibold sm:block">Sign in</Link>
                <Link to="/register" className="btn-primary !min-h-11 !px-5">Join</Link>
              </>
            )}
          </div>
      </div>
    </nav>
  );
};
