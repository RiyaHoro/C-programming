import React, { useEffect, useState } from 'react';
import { getCareer, getCourses, getJobs, getSkillGap } from '../services/api';
import SkillGapChart from '../charts/SkillGapChart';

export default function DashboardPage() {
  const [career, setCareer] = useState(null);
  const [gap, setGap] = useState(null);
  const [courses, setCourses] = useState([]);
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    async function load() {
      const [careerRes, gapRes, courseRes, jobsRes] = await Promise.all([
        getCareer(),
        getSkillGap(),
        getCourses(),
        getJobs()
      ]);
      setCareer(careerRes.data);
      setGap(gapRes.data);
      setCourses(courseRes.data);
      setJobs(jobsRes.data);
    }
    load();
  }, []);

  return (
    <div className="container">
      <h2>Dashboard</h2>
      {career && (
        <div className="card">
          <h3>Career Recommendation</h3>
          <p>{career.recommended_career}</p>
          <p>Suitability score: {career.suitability_score}%</p>
        </div>
      )}
      {gap && (
        <div className="card">
          <h3>Skill Gap Analysis</h3>
          <p>Skill match: {gap.skill_match_percentage}%</p>
          <SkillGapChart data={gap} />
          <p>Missing skills: {gap.skill_gap.join(', ')}</p>
        </div>
      )}
      <div className="card">
        <h3>Recommended Courses</h3>
        <ul>
          {courses.map((course) => (
            <li key={course.link}>
              <a href={course.link} target="_blank" rel="noreferrer">{course.name}</a> - {course.provider} ({course.estimated_duration})
            </li>
          ))}
        </ul>
      </div>
      <div className="card">
        <h3>Job Suggestions</h3>
        <ul>
          {jobs.map((job) => (
            <li key={`${job.company}-${job.title}`}>
              <a href={job.link} target="_blank" rel="noreferrer">{job.title}</a> at {job.company} ({job.source})
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
}
