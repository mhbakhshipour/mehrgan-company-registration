from django.urls import path

from consultant.views import ConsultantListViewSet, ConsultantDetailViewSet

urlpatterns = [
    path('api/v1/consultant-list', ConsultantListViewSet.as_view(), name='consultant_list'),
    path('api/v1/consultant-detail/<int:id>', ConsultantDetailViewSet.as_view(), name='consultant_detail'),
]
