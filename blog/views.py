from jalali_date import datetime2jalali
from rest_framework import generics, filters

from mehrgan.custom_view_mixins import ExpressiveListModelMixin, ExpressiveCreateCommentModelMixin
from .models import News
from blog.serializer import GetNewsListSerializer, GetNewsDetailSerializer, CreateCommentSerializer


class GetNewsListViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetNewsListSerializer
    plural_name = 'news'

    def get_queryset(self):
        queryset = News.objects.all().order_by('-created_at')
        return queryset


class GetNewsListByCategoryViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetNewsListSerializer
    plural_name = 'news_by_category'

    def get_queryset(self):
        cat_id = self.kwargs['id']
        queryset = News.objects.get_news_with_by_category(cat_id).order_by('-created_at')
        return queryset


class GetNewsDetailViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = GetNewsDetailSerializer
    plural_name = 'news'

    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = News.objects.filter(slug=slug)
        return queryset


class CreateCommentViewSet(ExpressiveCreateCommentModelMixin, generics.CreateAPIView):
    serializer_class = CreateCommentSerializer
    singular_name = 'comment_created'
