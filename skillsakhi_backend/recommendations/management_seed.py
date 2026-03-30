"""Run from Django shell: exec(open('recommendations/management_seed.py').read())"""
from recommendations.models import Career, Course, Job
from users.models import Skill
from recommendations.models import CareerSkill

careers = [
    ('Home Catering', 'basic', 'high', 'work_from_home', 'cooking,food'),
    ('Food Blogging', 'basic', 'medium', 'freelancing', 'cooking,content'),
    ('Cloud Kitchen Entrepreneur', 'basic', 'high', 'work_from_home', 'cooking,business'),
    ('Data Analyst', 'graduate', 'high', 'full_time', 'data,technology'),
    ('Online Tutor', 'graduate', 'high', 'part_time', 'teaching,education'),
]
for c in careers:
    Career.objects.get_or_create(
        name=c[0],
        defaults={
            'education_required': c[1],
            'demand_level': c[2],
            'preferred_work_type': c[3],
            'interests': c[4],
        },
    )

skill_map = {
    'Home Catering': ['cooking', 'food safety', 'inventory management'],
    'Food Blogging': ['content writing', 'photography', 'social media'],
    'Cloud Kitchen Entrepreneur': ['cooking', 'digital marketing', 'operations'],
    'Data Analyst': ['sql', 'excel', 'python', 'power bi'],
    'Online Tutor': ['communication', 'subject expertise', 'lesson planning'],
}
for career_name, skills in skill_map.items():
    career = Career.objects.get(name=career_name)
    for s in skills:
        skill, _ = Skill.objects.get_or_create(name=s)
        CareerSkill.objects.get_or_create(career=career, skill=skill)

courses = [
    ('Data Analyst', 'Google Data Analytics', 'Coursera', 'https://www.coursera.org/professional-certificates/google-data-analytics', '6 months'),
    ('Data Analyst', 'SQL for Beginners', 'Udemy', 'https://www.udemy.com/course/sql-for-beginners-course/', '8 hours'),
    ('Home Catering', 'Starting a Home Food Business', 'YouTube', 'https://www.youtube.com/results?search_query=home+catering+business', '2 hours'),
]
for career_name, name, provider, link, duration in courses:
    career = Career.objects.get(name=career_name)
    Course.objects.get_or_create(
        career=career,
        name=name,
        provider=provider,
        link=link,
        estimated_duration=duration,
    )

jobs = [
    ('Data Analyst', 'Junior Data Analyst', 'InsightWorks', 'Remote', 'LinkedIn', 'https://www.linkedin.com/jobs/'),
    ('Data Analyst', 'Business Analyst Intern', 'NextGen Data', 'Bengaluru', 'Indeed', 'https://www.indeed.com/'),
    ('Home Catering', 'Home Chef Partner', 'CookNest', 'Remote', 'Naukri', 'https://www.naukri.com/'),
]
for career_name, title, company, location, source, link in jobs:
    career = Career.objects.get(name=career_name)
    Job.objects.get_or_create(
        career=career,
        title=title,
        company=company,
        location=location,
        source=source,
        link=link,
    )

print('Seed completed')
