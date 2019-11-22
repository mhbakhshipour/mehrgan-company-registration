from django.shortcuts import render
from rest_framework import generics

from core.models import Faq
from core.serializer import CreateContactUsSerializer, GetFaqSerializer
from mehrgan.custom_view_mixins import ExpressiveCreateContactUsViewSetModelMixin, ExpressiveListModelMixin


class CreateContactUsViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = CreateContactUsSerializer
    singular_name = 'contact_us_form_created'


class GetFaqViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetFaqSerializer
    plural_name = 'faqs'

    def get_queryset(self):
        queryset = Faq.objects.all().order_by('-created_at')
        return queryset
