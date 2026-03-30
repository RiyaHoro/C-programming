import React from 'react';
import AuthForm from '../components/AuthForm';
import { login } from '../services/api';

export default function LoginPage() {
  const onSubmit = async (form) => {
    const res = await login(form);
    localStorage.setItem('token', res.data.token);
    alert('Login successful');
  };

  return (
    <div className="container">
      <h2>Login</h2>
      <AuthForm
        buttonLabel="Login"
        onSubmit={onSubmit}
        fields={[
          { name: 'username', label: 'Username' },
          { name: 'password', label: 'Password', type: 'password' }
        ]}
      />
    </div>
  );
}
