from django.urls import path

from core.views import CreateContactUsViewSet

urlpatterns = [
    path('api/v1/create-contact-us-form', CreateContactUsViewSet.as_view(), name='create_contact_us_form'),
]
