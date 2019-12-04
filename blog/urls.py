from django.urls import path

from blog.views import NewsListViewSet, NewsListByCategoryViewSet, NewsDetailViewSet, CommentViewSet

urlpatterns = [
    path('api/v1/news-list', NewsListViewSet.as_view(), name='news_list'),
    path('api/v1/news-list-by-category/<int:id>', NewsListByCategoryViewSet.as_view(), name='news_by_category'),
    path('api/v1/news-detail/<str:slug>', NewsDetailViewSet.as_view(), name='news_detail'),
    path('api/v1/comment/<str:content_type>/<int:id>', CommentViewSet.as_view(), name='comment'),
]
