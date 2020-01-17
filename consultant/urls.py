from django.urls import path

from consultant.views import ConsultantListViewSet, ConsultantDetailViewSet, ConsultantRateViewSet

urlpatterns = [
    path('api/v1/consultant-list', ConsultantListViewSet.as_view(), name='consultant_list'),
    path('api/v1/consultant-detail/<int:id>', ConsultantDetailViewSet.as_view(), name='consultant_detail'),
    path('api/v1/consultant-rate/<int:id>', ConsultantRateViewSet.as_view(), name='consultant_rate'),
]
