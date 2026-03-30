import React from 'react';
import { Link, Route, Routes } from 'react-router-dom';
import LandingPage from './pages/LandingPage';
import AboutPage from './pages/AboutPage';
import RegisterPage from './pages/RegisterPage';
import LoginPage from './pages/LoginPage';
import ProfilePage from './pages/ProfilePage';
import DashboardPage from './pages/DashboardPage';

export default function App() {
  return (
    <div>
      <nav className="nav">
        <h2>SkillSakhi</h2>
        <div>
          <Link to="/">Home</Link>
          <Link to="/about">About</Link>
          <Link to="/register">Register</Link>
          <Link to="/login">Login</Link>
          <Link to="/profile">Profile</Link>
          <Link to="/dashboard">Dashboard</Link>
        </div>
      </nav>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/register" element={<RegisterPage />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/dashboard" element={<DashboardPage />} />
      </Routes>
    </div>
  );
}
