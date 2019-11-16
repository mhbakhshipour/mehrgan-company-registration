from rest_framework import serializers

from blog import models
from mehrgan.custom_view_mixins import ExpressiveListModelMixin


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategorizedItems
        fields = ['category_id', 'category_title', 'category_slug', 'category_parent']


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommentsItems
        fields = ['comment_id', 'comment_title', 'comment_name', 'comment_email', 'comment_created_at', 'comment_parent']


class GetNewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ['id', 'title', 'description', 'thumbnail', 'slug']


class GetNewsDetailSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)
    comments = CommentsSerializer(many=True)

    class Meta:
        model = models.News
        fields = ['id', 'title', 'description', 'content', 'custom_created_at', 'thumbnail', 'slug', 'categories',
                  'comments']
