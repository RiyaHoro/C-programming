import React, { useState } from 'react';

export default function AuthForm({ fields, onSubmit, buttonLabel }) {
  const [form, setForm] = useState(
    fields.reduce((acc, field) => ({ ...acc, [field.name]: '' }), {})
  );

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  return (
    <form
      className="card"
      onSubmit={(e) => {
        e.preventDefault();
        onSubmit(form);
      }}
    >
      {fields.map((field) => (
        <input
          key={field.name}
          name={field.name}
          placeholder={field.label}
          type={field.type || 'text'}
          value={form[field.name]}
          onChange={handleChange}
          required
        />
      ))}
      <button type="submit">{buttonLabel}</button>
    </form>
  );
}
