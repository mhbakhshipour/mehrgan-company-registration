from django.shortcuts import render
from rest_framework import generics

from core.serializer import CreateContactUsSerializer
from mehrgan.custom_view_mixins import ExpressiveCreateContactUsViewSetModelMixin


class CreateContactUsViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = CreateContactUsSerializer
    singular_name = 'contact_us_form_created'
