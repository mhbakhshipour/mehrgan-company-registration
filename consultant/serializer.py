from rest_framework import serializers

from consultant import models
from consultant.models import ConsultantSkill, Skill, ConsultantExperience, ConsultantEducation, Rate


class ConsultantExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantExperience
        fields = ['id', 'experience_description', 'experience_title', 'experience_start_date', 'experience_start_date']


class ConsultantEducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantEducation
        fields = ['id', 'description', 'education_title', 'education_university', 'education_end_date']


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['id', 'title']


class ConsultantSkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsultantSkill
        fields = ['id', 'description', 'skill_title']


class ConsultantListSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True)

    class Meta:
        model = models.Consultant
        fields = ['id', 'full_name', 'about', 'avatar', 'skills', 'phone_number', 'activity']


class ConsultantDetailSerializer(serializers.ModelSerializer):
    skills_attributes = ConsultantSkillSerializer(many=True)
    experience_attributes = ConsultantExperienceSerializer(many=True)
    education_attributes = ConsultantEducationSerializer(many=True)

    class Meta:
        model = models.Consultant
        fields = ['id', 'full_name', 'father_name', 'phone_number', 'mobile_number', 'email', 'address', 'avatar',
                  'linkedin_link', 'telegram_link', 'about', 'activity', 'skills_attributes', 'experience_attributes',
                  'education_attributes', 'cv', 'rate']


class ConsultantRateSerializer(serializers.Serializer):
    rate = serializers.IntegerField(required=True)

    def create(self, validated_data):
        rate = Rate(
            rate=validated_data['rate'],
            consultant=validated_data['consultant']
        )
        rate.save()
        return rate

    def to_representation(self, instance):
        return {'status': 'ok', 'mssg': 'rate created'}
