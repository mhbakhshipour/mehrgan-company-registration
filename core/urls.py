from django.urls import path

from core.views import *

urlpatterns = [
    path('api/v1/contact-us-form', ContactUsViewSet.as_view(), name='contact_us_form'),
    path('api/v1/faq', FaqViewSet.as_view(), name='faq'),
    path('api/v1/categories-list', CategoriesViewSet.as_view(), name='categories-list'),
    path('api/v1/search', SearchViewSet.as_view(), name='search'),
    path('api/v1/company-register-form', CompanyRegisterFormViewSet.as_view(), name='company-register-form'),
    path('api/v1/company-edit-form', CompanyEditFormViewSet.as_view(), name='company-edit-form'),
    path('api/v1/company-register-trademarks-form', CompanyRegisterTrademarksFormViewSet.as_view(), name='company-register-trademarks-form'),
    path('api/v1/official-services-form', OfficialServicesFormViewSet.as_view(), name='official-services-form'),
    path('api/v1/request-lawyer-form', RequestLawyerFormViewSet.as_view(), name='request-lawyer-form'),
    path('api/v1/legal-advice-form', LegalAdviceFormViewSet.as_view(), name='legal-advice-form'),
]
