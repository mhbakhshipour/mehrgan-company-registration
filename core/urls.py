from django.urls import path

from core.views import CreateContactUsViewSet, GetFaqViewSet

urlpatterns = [
    path('api/v1/create-contact-us-form', CreateContactUsViewSet.as_view(), name='create_contact_us_form'),
    path('api/v1/get-faq', GetFaqViewSet.as_view(), name='get_faq'),
]
