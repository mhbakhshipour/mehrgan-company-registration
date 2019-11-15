from rest_framework import serializers

from blog import models
from mehrgan.custom_view_mixins import ExpressiveListModelMixin


# class GetNewsAPI(ExpressiveListModelMixin, generics.ListAPIView):
#     serializer_class = PropertyTypeSerializer
#     queryset = PropertyType.objects.filter(is_enabled=True, deleted_at__isnull=True)
#     plural_name = 'property_types'

class GetNewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ['id', 'title', 'description', 'content', 'created_at', 'thumbnail', 'slug']


class GetNewsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = ['id', 'title', 'description', 'content', 'created_at', 'thumbnail', 'slug']
