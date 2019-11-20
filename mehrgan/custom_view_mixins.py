from django.contrib.contenttypes.models import ContentType
from rest_framework import response
from rest_framework.mixins import CreateModelMixin

from blog.models import CommentedItems


class ExpressiveListModelMixin:
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data = {'status': 'ok', 'data': {self.plural_name: response.data}}
        return response


class ExpressiveCreateCommentModelMixin(CreateModelMixin):

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        c = ContentType.objects.get(model=kwargs['content_type'])
        content_type_id = c.id
        obj_id = kwargs['id']
        comment_id = response.data['id']

        CommentedItems.objects.create(content_type_id=content_type_id, comment_id=comment_id, object_id=obj_id)

        response.data = {'status': 'ok', 'data': {self.singular_name: response.data}}
        return response


class ExpressiveCreateContactUsViewSetModelMixin(CreateModelMixin):

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.data = {'status': 'ok', 'data': {self.singular_name: response.data}}
        return response
