from django.db import transaction
from rest_framework import serializers

from blog import models


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CategorizedItems
        fields = ['category_id', 'category_title', 'category_slug', 'category_parent']


class CommentsSerializer(serializers.ModelSerializer):
    read_only_fields = ('comment_id',)

    class Meta:
        model = models.CommentedItems
        fields = ['comment_id', 'comment_title', 'comment_name', 'comment_email', 'comment_created_at',
                  'comment_parent', 'comment_status']


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


class CreateCommentedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['comment', 'content_type', 'object_id']


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comment
        fields = ['id', 'comment', 'email', 'name', 'parent']
