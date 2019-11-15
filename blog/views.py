from jalali_date import datetime2jalali
from rest_framework import generics
from rest_framework.response import Response

from .models import News
from blog.serializer import GetNewsListSerializer, GetNewsDetailSerializer


# def my_view(request):
#     jalali_join = datetime2jalali(request.user.date_joined).strftime('%y/%m/%d _ %H:%M:%S')


class GetNewsListViewSet(generics.ListAPIView):
    def get_queryset(self):
        count = self.kwargs['count']
        queryset = News.objects.all().order_by('-created_at')[:count]
        return queryset

    serializer_class = GetNewsListSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'ok', 'data': {'news': serializer.data}})


class GetNewsDetailViewSet(generics.ListAPIView):
    def get_queryset(self):
        slug = self.kwargs['slug']
        queryset = News.objects.filter(slug=slug)
        return queryset

    serializer_class = GetNewsDetailSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response({'status': 'ok', 'data': {'news': serializer.data}})
