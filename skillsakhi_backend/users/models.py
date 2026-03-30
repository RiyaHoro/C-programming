from django.contrib.auth.models import User
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    WORK_PREFERENCE_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('work_from_home', 'Work From Home'),
        ('freelancing', 'Freelancing'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.PositiveIntegerField()
    education_level = models.CharField(max_length=120)
    location = models.CharField(max_length=150)
    interests = models.TextField(help_text='Comma separated interests')
    skills = models.ManyToManyField(Skill, blank=True)
    work_preference = models.CharField(max_length=20, choices=WORK_PREFERENCE_CHOICES)
    updated_at = models.DateTimeField(auto_now=True)

    def interest_list(self):
        return [item.strip().lower() for item in self.interests.split(',') if item.strip()]

    def __str__(self):
        return f"{self.user.username} profile"
