from rest_framework import serializers

from core.models import CategorizedItems
from consultant import models
from consultant.models import SkilledConsultant


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorizedItems
        fields = ['category_id', 'category_title', 'category_slug', 'category_parent']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkilledConsultant
        fields = ['skill_id', 'skill_title']


class GetConsultantListSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)

    class Meta:
        model = models.Consultant
        fields = ['id', 'full_name', 'description', 'categories', 'avatar']


class GetConsultantDetailSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)
    skills = SkillsSerializer(many=True)

    class Meta:
        model = models.Consultant
        fields = ['id', 'full_name', 'father_name', 'phone', 'email', 'address', 'education_degree', 'description',
                  'about', 'categories', 'skills', 'c_created_at', 'avatar', 'linkedin_link', 'telegram_link',
                  'instagram_link', 'twitter_link', 'facebook_link', 'rate']
