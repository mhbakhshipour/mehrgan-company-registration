from django.db import transaction
from rest_framework import serializers

from blog.models import News
from core.models import *


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
        fields = ['id', 'title', 'description', 'time', 'thumbnail', 'slug']


class NewsDetailSerializer(serializers.ModelSerializer):
    categories = CategoriesSerializer(many=True)
    comments = CommentsSerializer(many=True)

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'content', 'time', 'custom_created_at', 'thumbnail', 'slug',
                  'categories', 'comments']


class CommentedItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentedItems
        fields = ['comment', 'content_type', 'object_id']


class CommentSerializer(serializers.Serializer):
    comment = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    phone = serializers.IntegerField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    # parent = serializers.IntegerField(required=False)

    def create(self, validated_data):
        comment = Comment(
            comment=validated_data['comment'],
            email=validated_data['email'],
            phone=validated_data['phone'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            # parent_id=validated_data['parent']
        )
        comment.save()
        commented_item = CommentedItems(comment=comment, content_type_id=validated_data['content_type'],
                                        object_id=validated_data['object_id'])
        commented_item.save()
        return comment

    def to_representation(self, instance):
        return {'status': 'ok', 'mssg': 'comment created'}
