from django.db import transaction
from rest_framework import serializers
from core import models


class CreateContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactUs
        fields = ['id', 'full_name', 'email', 'phone', 'description', 'c_created_at', 'status']
