from django.db import transaction
from rest_framework import serializers
from core import models
from core.models import Category


class CreateContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = ['id', 'full_name', 'email', 'phone', 'description', 'c_created_at', 'status']


class GetFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faq
        fields = ['id', 'title', 'description', 'c_created_at']


class GetCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'parent']
