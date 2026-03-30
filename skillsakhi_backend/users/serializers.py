from django.contrib.auth.models import User
from rest_framework import serializers
from .models import UserProfile, Skill


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'first_name', 'last_name']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'name']


class UserProfileSerializer(serializers.ModelSerializer):
    skills = serializers.ListField(child=serializers.CharField(), write_only=True)
    skill_objects = SkillSerializer(source='skills', many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = [
            'age',
            'education_level',
            'location',
            'interests',
            'skills',
            'skill_objects',
            'work_preference',
        ]

    def create_or_update_skills(self, profile, skill_names):
        skill_objs = [Skill.objects.get_or_create(name=name.strip().lower())[0] for name in skill_names]
        profile.skills.set(skill_objs)

    def create(self, validated_data):
        skills = validated_data.pop('skills', [])
        profile = UserProfile.objects.create(**validated_data)
        self.create_or_update_skills(profile, skills)
        return profile

    def update(self, instance, validated_data):
        skills = validated_data.pop('skills', None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        if skills is not None:
            self.create_or_update_skills(instance, skills)
        return instance
