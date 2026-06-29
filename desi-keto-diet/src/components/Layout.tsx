import { NavLink } from 'react-router-dom';
import { useTranslation } from 'react-i18next';
import './Layout.css';

const navItems = [
  { path: '/', icon: '🏠', key: 'home' },
  { path: '/recipes', icon: '🍽️', key: 'recipes' },
  { path: '/health', icon: '💚', key: 'health' },
  { path: '/fitness', icon: '🧘', key: 'fitness' },
  { path: '/knowledge', icon: '📚', key: 'knowledge' },
  { path: '/settings', icon: '⚙️', key: 'settings' },
];

export default function Layout({ children }: { children: React.ReactNode }) {
  const { t } = useTranslation();

  return (
    <div className="layout">
      <header className="header">
        <div className="header-content">
          <h1 className="app-title">{t('app.name')}</h1>
          <p className="app-tagline">{t('app.tagline')}</p>
        </div>
      </header>
      <main className="main-content">{children}</main>
      <nav className="bottom-nav">
        {navItems.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) => `nav-item ${isActive ? 'active' : ''}`}
            end={item.path === '/'}
          >
            <span className="nav-icon">{item.icon}</span>
            <span className="nav-label">{t(`nav.${item.key}`)}</span>
          </NavLink>
        ))}
      </nav>
    </div>
  );
}
