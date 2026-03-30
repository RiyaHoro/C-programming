from rest_framework import serializers
from .models import Career, Course, Job


class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = ['id', 'name', 'education_required', 'demand_level', 'preferred_work_type', 'interests']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['name', 'provider', 'link', 'estimated_duration']


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = ['title', 'company', 'location', 'source', 'link']
