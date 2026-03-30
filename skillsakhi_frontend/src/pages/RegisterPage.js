import React from 'react';
import AuthForm from '../components/AuthForm';
import { register } from '../services/api';

export default function RegisterPage() {
  const onSubmit = async (form) => {
    const res = await register(form);
    localStorage.setItem('token', res.data.token);
    alert('Registration successful');
  };

  return (
    <div className="container">
      <h2>Create Account</h2>
      <AuthForm
        buttonLabel="Register"
        onSubmit={onSubmit}
        fields={[
          { name: 'username', label: 'Username' },
          { name: 'email', label: 'Email', type: 'email' },
          { name: 'password', label: 'Password', type: 'password' },
          { name: 'first_name', label: 'First Name' },
          { name: 'last_name', label: 'Last Name' }
        ]}
      />
    </div>
  );
}
