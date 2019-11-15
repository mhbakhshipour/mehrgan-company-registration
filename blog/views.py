from jalali_date import datetime2jalali
from rest_framework import generics

from mehrgan.custom_view_mixins import ExpressiveListModelMixin
from .models import News
from blog.serializer import GetNewsListSerializer, GetNewsDetailSerializer


class GetNewsListViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetNewsListSerializer
    plural_name = 'news'

    def get_queryset(self):
        count = self.kwargs['count']
        queryset = News.objects.all().order_by('-created_at')[:count]
        return queryset


class GetNewsDetailViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetNewsDetailSerializer
    plural_name = 'news'

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = News.objects.filter(slug=slug)
        return queryset
