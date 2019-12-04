from django.urls import path

from core.views import SearchViewSet, CategoriesViewSet, FaqViewSet, ContactUsViewSet

urlpatterns = [
    path('api/v1/contact-us-form', ContactUsViewSet.as_view(), name='contact_us_form'),
    path('api/v1/faq', FaqViewSet.as_view(), name='faq'),
    path('api/v1/categories-list', CategoriesViewSet.as_view(), name='categories-list'),
    path('api/v1/search', SearchViewSet.as_view(), name='search'),
]
