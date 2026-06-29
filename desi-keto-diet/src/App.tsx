import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { VocalsProvider } from './context/VocalsContext';
import Layout from './components/Layout';
import HomePage from './pages/HomePage';
import RecipesPage from './pages/RecipesPage';
import RecipeDetailPage from './pages/RecipeDetailPage';
import HealthPage from './pages/HealthPage';
import HealthDetailPage from './pages/HealthDetailPage';
import FitnessPage from './pages/FitnessPage';
import FitnessDetailPage from './pages/FitnessDetailPage';
import KnowledgePage from './pages/KnowledgePage';
import SettingsPage from './pages/SettingsPage';

export default function App() {
  return (
    <BrowserRouter>
      <VocalsProvider>
        <Layout>
          <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/recipes" element={<RecipesPage />} />
          <Route path="/recipes/:id" element={<RecipeDetailPage />} />
          <Route path="/health" element={<HealthPage />} />
          <Route path="/health/:id" element={<HealthDetailPage />} />
          <Route path="/fitness" element={<FitnessPage />} />
          <Route path="/fitness/:id" element={<FitnessDetailPage />} />
          <Route path="/knowledge" element={<KnowledgePage />} />
          <Route path="/settings" element={<SettingsPage />} />
          </Routes>
        </Layout>
      </VocalsProvider>
    </BrowserRouter>
  );
}
