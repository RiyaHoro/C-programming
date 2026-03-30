from django.contrib import admin
from django.urls import path
from users.views import RegisterView, LoginView, ProfileCreateUpdateView
from recommendations.views import (
    CareerRecommendationView,
    SkillGapView,
    CourseRecommendationView,
    JobRecommendationView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register', RegisterView.as_view(), name='register'),
    path('api/login', LoginView.as_view(), name='login'),
    path('api/profile', ProfileCreateUpdateView.as_view(), name='profile'),
    path('api/career-recommendation', CareerRecommendationView.as_view(), name='career-recommendation'),
    path('api/skill-gap', SkillGapView.as_view(), name='skill-gap'),
    path('api/courses', CourseRecommendationView.as_view(), name='courses'),
    path('api/jobs', JobRecommendationView.as_view(), name='jobs'),
]
