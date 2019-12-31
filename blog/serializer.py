from django.db import transaction
from rest_framework import serializers

from blog.models import News
from core.models import CategorizedItems, CommentedItems, Comment


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategorizedItems
        fields = ['category_id', 'category_title', 'category_slug', 'category_parent']


class CommentsSerializer(serializers.ModelSerializer):
    read_only_fields = ('comment_id',)

    class Meta:
        model = CommentedItems
        fields = ['comment_id', 'comment_title', 'comment_first_name', 'comment_last_name', 'comment_email',
                  'comment_phone', 'comment_created_at', 'comment_parent', 'comment_status']


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'thumbnail', 'slug']


class NewsDetailSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)
    comments = CommentsSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'content', 'time', 'custom_created_at', 'thumbnail', 'slug',
                  'categories', 'comments']


class CommentedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['comment', 'content_type', 'object_id']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'comment', 'email', 'name', 'parent']
