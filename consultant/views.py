from django.shortcuts import render
from rest_framework import generics

from consultant.models import Consultant
from consultant.serializer import GetConsultantListSerializer, GetConsultantDetailSerializer
from mehrgan.custom_view_mixins import ExpressiveListModelMixin


class GetConsultantListViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetConsultantListSerializer
    plural_name = 'consultants'

    def get_queryset(self):
        queryset = Consultant.objects.all().order_by('-full_name')
        return queryset


class GetConsultantDetailViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetConsultantDetailSerializer
    plural_name = 'consultant'

    def get_queryset(self):
        full_name = self.kwargs['full_name']
        queryset = Consultant.objects.filter(full_name=full_name)
        return queryset
