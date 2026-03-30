import React from 'react';
import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend);

export default function SkillGapChart({ data }) {
  const chartData = {
    labels: ['Required Skills', 'Current Skills', 'Missing Skills'],
    datasets: [
      {
        label: 'Count',
        data: [data.required_skills.length, data.user_skills.length, data.skill_gap.length],
        backgroundColor: ['#6C63FF', '#16A34A', '#F97316']
      }
    ]
  };
  return <Bar data={chartData} />;
}
