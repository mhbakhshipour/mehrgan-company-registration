from django.contrib.contenttypes.models import ContentType
from jalali_date import datetime2jalali
from rest_framework import generics

from mehrgan.custom_view_mixins import ExpressiveListModelMixin, ExpressiveCreateCommentModelMixin
from .models import News
from blog.serializer import GetNewsListSerializer, GetNewsDetailSerializer, CreateCommentSerializer


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


# class BlacklistPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         ip_addr = request.META['REMOTE_ADDR']
#         blacklisted = Blacklist.objects.filter(ip_addr=ip_addr).exists()
#         return not blacklisted


class CreateCommentViewSet(ExpressiveCreateCommentModelMixin, generics.CreateAPIView):
    serializer_class = CreateCommentSerializer
    singular_name = 'comment_created'
