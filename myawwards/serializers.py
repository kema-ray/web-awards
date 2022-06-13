from rest_framework import serializers
from .models import Profile, Project
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'image', 'bio', 'date',]


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'url', 'description', 'technologies', 'image', 'date_posted', 'user']

