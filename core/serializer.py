from rest_framework import serializers

from core.models import *


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


class CompanyRegisterFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyRegisterForm
        fields = '__all__'


class CompanyEditFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyEditForm
        fields = '__all__'


class CompanyRegisterTrademarksFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyRegisterTrademarksForm
        fields = '__all__'


class OfficialServicesFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = OfficialServicesForm
        fields = '__all__'


class RequestLawyerFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestLawyerForm
        fields = '__all__'


class LegalAdviceFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = LegalAdviceForm
        fields = '__all__'
