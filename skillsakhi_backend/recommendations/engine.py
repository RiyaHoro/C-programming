import pickle
from pathlib import Path
import numpy as np

from users.models import UserProfile
from .models import Career

MODEL_PATH = Path(__file__).resolve().parent.parent / 'ml_model' / 'career_model.pkl'
ENCODER_PATH = Path(__file__).resolve().parent.parent / 'ml_model' / 'encoders.pkl'

RULE_MAP = {
    ('cooking', 'basic'): ['Home Catering', 'Food Blogging', 'Cloud Kitchen Entrepreneur'],
    ('teaching', 'graduate'): ['Online Tutor', 'Instructional Designer'],
}


def load_model_components():
    with open(MODEL_PATH, 'rb') as model_file:
        model = pickle.load(model_file)
    with open(ENCODER_PATH, 'rb') as encoder_file:
        encoders = pickle.load(encoder_file)
    return model, encoders


def rule_based_recommendations(profile: UserProfile):
    recs = []
    for interest in profile.interest_list():
        recs.extend(RULE_MAP.get((interest, profile.education_level.lower()), []))
    return list(dict.fromkeys(recs))


def ml_predict_career(profile: UserProfile):
    model, encoders = load_model_components()
    interest = profile.interest_list()[0] if profile.interest_list() else 'general'
    primary_skill = profile.skills.first().name if profile.skills.exists() else 'none'

    x = np.array([[
        profile.age,
        encoders['education'].transform([profile.education_level.lower()])[0]
        if profile.education_level.lower() in encoders['education'].classes_ else 0,
        encoders['interest'].transform([interest])[0]
        if interest in encoders['interest'].classes_ else 0,
        encoders['work'].transform([profile.work_preference])[0]
        if profile.work_preference in encoders['work'].classes_ else 0,
        encoders['skill'].transform([primary_skill])[0]
        if primary_skill in encoders['skill'].classes_ else 0,
    ]])

    pred = model.predict(x)[0]
    probs = max(model.predict_proba(x)[0])
    return pred, float(round(probs * 100, 2))


def choose_career(profile: UserProfile):
    rule_recs = rule_based_recommendations(profile)
    if rule_recs:
        career = Career.objects.filter(name__in=rule_recs).first()
        if career:
            return career, 88.0

    predicted_name, score = ml_predict_career(profile)
    career = Career.objects.filter(name=predicted_name).first()
    return career, score
