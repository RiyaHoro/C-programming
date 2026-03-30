# SkillSakhi: Demographic-Aware Career and Skill Recommendation Platform for Women

SkillSakhi is a production-ready full-stack web application that helps women start/restart careers with personalized recommendations.

## Project Structure

```text
skillsakhi_backend/
  manage.py
  skillsakhi/
  users/
  recommendations/
  ml_model/
  datasets/
skillsakhi_frontend/
  src/
    components/
    pages/
    services/
    charts/
```

## Features Implemented

- User registration/login with token auth
- Profile capture (age, education, interests, skills, work preference)
- Hybrid career recommendation engine:
  - Rule-based recommendations
  - ML prediction using Decision Tree (scikit-learn)
- Skill gap analysis (required vs existing vs missing skills)
- Course recommendations (Coursera/Udemy/YouTube)
- Job recommendations (LinkedIn/Indeed/Naukri sample records)
- Dashboard with chart visualization (Chart.js)

## Backend API Endpoints

- `POST /api/register`
- `POST /api/login`
- `POST /api/profile`
- `GET /api/career-recommendation`
- `GET /api/skill-gap`
- `GET /api/courses`
- `GET /api/jobs`

## Database Models

- `users.Skill`
- `users.UserProfile`
- `recommendations.Career`
- `recommendations.CareerSkill`
- `recommendations.Course`
- `recommendations.Job`
- `recommendations.Recommendation`

## Machine Learning Pipeline

1. Dataset stored in `skillsakhi_backend/datasets/career_dataset.csv`
2. Preprocessing in `skillsakhi_backend/ml_model/train_model.py`:
   - Label encoding for categorical columns
3. Model training:
   - DecisionTreeClassifier
4. Model persisted:
   - `skillsakhi_backend/ml_model/career_model.pkl`
   - `skillsakhi_backend/ml_model/encoders.pkl`
5. Runtime loading:
   - `recommendations/engine.py`

## Local Setup Instructions

### 1) Backend setup

```bash
cd skillsakhi_backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Configure PostgreSQL DB and env vars from `.env.example`.

```bash
python ml_model/train_model.py
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

(Optional seed data)
```bash
python manage.py shell
exec(open('recommendations/management_seed.py').read())
```

### 2) Frontend setup

```bash
cd skillsakhi_frontend
npm install
# Move public_index.html to public/index.html in CRA project if needed
npm start
```

Frontend runs on `http://localhost:3000`, backend on `http://localhost:8000`.

## Deployment Instructions

### Backend (Django + Gunicorn)

1. Set `DEBUG=0` and strong `DJANGO_SECRET_KEY`
2. Use managed PostgreSQL (AWS RDS/Render/Railway/etc.)
3. Install dependencies and run migrations
4. Start app with gunicorn:
   ```bash
   gunicorn skillsakhi.wsgi:application --bind 0.0.0.0:8000 --workers 3
   ```
5. Put behind Nginx/Load Balancer
6. Serve static files from CDN/object storage or WhiteNoise

### Frontend (React)

1. Build bundle:
   ```bash
   npm run build
   ```
2. Deploy to Vercel/Netlify/S3+CloudFront
3. Set API base URL to backend host in `src/services/api.js`

## Production Notes

- Add refresh-token/JWT flow for better auth lifecycle.
- Add background jobs for dynamic job ingestion APIs.
- Add CI checks and containerization (`Dockerfile`, `docker-compose.yml`).
- Add profile completeness scoring and bias audits for recommendation fairness.
