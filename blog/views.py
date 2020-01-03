from rest_framework import generics, status

from mehrgan.custom_view_mixins import ExpressiveListModelMixin, ExpressiveCreateCommentModelMixin
from .models import News
from blog.serializer import *


class NewsListViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = NewsListSerializer
    plural_name = 'news_list'

    def get_queryset(self):
        queryset = News.objects.all().order_by('-created_at')
        return queryset


class NewsListByCategoryViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = NewsListSerializer
    plural_name = 'news_list_by_category'

    def get_queryset(self):
        cat_id = self.kwargs['id']
        queryset = News.objects.get_news_with_by_category(cat_id).order_by('-created_at')
        return queryset


class NewsDetailViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = NewsDetailSerializer
    plural_name = 'news'

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = News.objects.filter(pk=id)
        return queryset


class CommentViewSet(generics.CreateAPIView):
    serializer_class = CommentSerializer
    singular_name = 'comment_created'

    def perform_create(self, serializer):
        content_type = ContentType.objects.get(app_label=self.kwargs.get('content_type'))
        serializer.save(content_type=content_type.id, object_id=self.kwargs.get('object_id'))
