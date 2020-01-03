from rest_framework import generics

from mehrgan.custom_view_mixins import ExpressiveListModelMixin, ExpressiveCreateCommentModelMixin
from .models import News
from blog.serializer import CommentSerializer, NewsDetailSerializer, NewsListSerializer


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


class CommentViewSet(ExpressiveCreateCommentModelMixin, generics.CreateAPIView):
    serializer_class = CommentSerializer
    singular_name = 'comment_created'
