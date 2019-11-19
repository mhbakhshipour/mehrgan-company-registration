from django.urls import path

from blog.views import GetNewsListViewSet, GetNewsDetailViewSet, CreateCommentViewSet

urlpatterns = [
    path('api/v1/get-news-list/<int:count>', GetNewsListViewSet.as_view(), name='api_get_news_list'),
    path('api/v1/get-news-detail/<str:slug>', GetNewsDetailViewSet.as_view(), name='api_get_news_detail'),
    path('api/v1/create-comment/<str:content_type>/<int:id>', CreateCommentViewSet.as_view(), name='create_comment'),
]
