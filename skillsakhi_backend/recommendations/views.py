from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import UserProfile
from .engine import choose_career
from .models import Recommendation, CareerSkill
from .serializers import CourseSerializer, JobSerializer


class CareerRecommendationView(APIView):
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        career, score = choose_career(profile)
        Recommendation.objects.create(user=request.user, career=career, suitability_score=score)
        return Response({'recommended_career': career.name, 'suitability_score': score})


class SkillGapView(APIView):
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        career, _ = choose_career(profile)
        required = set(
            CareerSkill.objects.filter(career=career).values_list('skill__name', flat=True)
        )
        user_skills = set(profile.skills.values_list('name', flat=True))
        missing = sorted(required - user_skills)
        return Response(
            {
                'recommended_career': career.name,
                'required_skills': sorted(required),
                'user_skills': sorted(user_skills),
                'skill_gap': missing,
                'skill_match_percentage': round((len(required & user_skills) / len(required)) * 100, 2)
                if required
                else 0,
            }
        )


class CourseRecommendationView(APIView):
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        career, _ = choose_career(profile)
        return Response(CourseSerializer(career.courses.all(), many=True).data)


class JobRecommendationView(APIView):
    def get(self, request):
        profile = UserProfile.objects.get(user=request.user)
        career, _ = choose_career(profile)
        return Response(JobSerializer(career.jobs.all(), many=True).data)
