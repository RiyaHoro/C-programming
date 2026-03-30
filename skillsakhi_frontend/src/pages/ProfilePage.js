import React, { useState } from 'react';
import { saveProfile } from '../services/api';

export default function ProfilePage() {
  const [form, setForm] = useState({
    age: '',
    education_level: '',
    location: '',
    interests: '',
    skills: '',
    work_preference: 'full_time'
  });

  const submit = async (e) => {
    e.preventDefault();
    await saveProfile({ ...form, skills: form.skills.split(',').map((s) => s.trim()) });
    alert('Profile saved');
  };

  return (
    <div className="container">
      <h2>Profile Form</h2>
      <form className="card" onSubmit={submit}>
        <input placeholder="Age" value={form.age} onChange={(e) => setForm({ ...form, age: e.target.value })} />
        <input placeholder="Education level" value={form.education_level} onChange={(e) => setForm({ ...form, education_level: e.target.value })} />
        <input placeholder="Location" value={form.location} onChange={(e) => setForm({ ...form, location: e.target.value })} />
        <input placeholder="Interests (comma separated)" value={form.interests} onChange={(e) => setForm({ ...form, interests: e.target.value })} />
        <input placeholder="Skills (comma separated)" value={form.skills} onChange={(e) => setForm({ ...form, skills: e.target.value })} />
        <select value={form.work_preference} onChange={(e) => setForm({ ...form, work_preference: e.target.value })}>
          <option value="full_time">Full time</option>
          <option value="part_time">Part time</option>
          <option value="work_from_home">Work from home</option>
          <option value="freelancing">Freelancing</option>
        </select>
        <button type="submit">Save Profile</button>
      </form>
    </div>
  );
}
