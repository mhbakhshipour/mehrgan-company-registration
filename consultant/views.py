from django.shortcuts import render
from rest_framework import generics

from consultant.models import Consultant
from consultant.serializer import ConsultantListSerializer, ConsultantDetailSerializer, ConsultantRateSerializer
from mehrgan.custom_view_mixins import ExpressiveListModelMixin


class ConsultantListViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = ConsultantListSerializer
    plural_name = 'consultants_list'

    def get_queryset(self):
        queryset = Consultant.objects.filter(is_enabled=True).order_by('-full_name')
        return queryset


class ConsultantDetailViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = ConsultantDetailSerializer
    plural_name = 'consultant'

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = Consultant.objects.filter(pk=id, is_enabled=True)
        return queryset


class ConsultantRateViewSet(generics.CreateAPIView):
    serializer_class = ConsultantRateSerializer

    def perform_create(self, serializer):
        consultant = Consultant.objects.get(id=self.kwargs.get('id'))
        serializer.save(consultant=consultant)
