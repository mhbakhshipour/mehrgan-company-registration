from rest_framework import serializers

from core.models import Category, ContactUs, Faq


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'full_name', 'email', 'phone', 'description', 'c_created_at', 'status']


class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ['id', 'title', 'description', 'c_created_at']


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title', 'slug', 'parent']


class SearchSerializer(serializers.Serializer):

    def to_representation(self, instance):
        return instance

    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass
