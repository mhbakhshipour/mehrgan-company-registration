from django.shortcuts import render
from rest_framework import generics

from consultant.models import Consultant
from consultant.serializer import ConsultantListSerializer, ConsultantDetailSerializer
from mehrgan.custom_view_mixins import ExpressiveListModelMixin


class ConsultantListViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = ConsultantListSerializer
    plural_name = 'consultants_list'

    def get_queryset(self):
        queryset = Consultant.objects.all().order_by('-full_name')
        return queryset


class ConsultantDetailViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = ConsultantDetailSerializer
    plural_name = 'consultant'

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = Consultant.objects.filter(pk=id)
        return queryset
