from django.urls import path

from consultant.views import GetConsultantDetailViewSet, GetConsultantListViewSet

urlpatterns = [
    path('api/v1/get-consultant-list', GetConsultantListViewSet.as_view(), name='get_consultant_list'),
    path('api/v1/get-consultant-detail/<str:full_name>', GetConsultantDetailViewSet.as_view(),
         name='get_consultant_detail'),
]
