from django.urls import path

from blog.views import GetNewsListViewSet, GetNewsDetailViewSet

urlpatterns = [
    path('api/v1/get-news-list/<int:count>', GetNewsListViewSet.as_view(), name='api_get_news_list'),
    path('api/v1/get-news-detail/<str:slug>', GetNewsDetailViewSet.as_view(), name='api_get_news_detail'),
]
