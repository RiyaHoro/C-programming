from django.db import models
from users.models import Skill


class Career(models.Model):
    name = models.CharField(max_length=140, unique=True)
    education_required = models.CharField(max_length=120)
    demand_level = models.CharField(max_length=40)
    preferred_work_type = models.CharField(max_length=20)
    interests = models.TextField(help_text='Comma separated interest tags')

    def __str__(self):
        return self.name


class CareerSkill(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='career_skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('career', 'skill')


class Course(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=220)
    provider = models.CharField(max_length=80)
    link = models.URLField()
    estimated_duration = models.CharField(max_length=60)


class Job(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=180)
    company = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    source = models.CharField(max_length=80)
    link = models.URLField()


class Recommendation(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='recommendations')
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    suitability_score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
