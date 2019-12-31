from django.db.models import Q
from django.shortcuts import render
from rest_framework import generics, filters

from blog.models import News
from consultant.models import Consultant
from core.serializer import *
from core.models import Faq, Category
from mehrgan.custom_view_mixins import ExpressiveCreateContactUsViewSetModelMixin, ExpressiveListModelMixin, \
    ExpressiveCreateCommentModelMixin


class ContactUsViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = ContactUsSerializer
    singular_name = 'contact_us_form_created'


class FaqViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = FaqSerializer
    plural_name = 'faqs_list'
    search_fields = ['title', 'description']
    filter_backends = (filters.SearchFilter,)

    def get_queryset(self):
        queryset = Faq.objects.all().order_by('-created_at')
        return queryset


class CategoriesViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = CategoriesSerializer
    plural_name = 'categories_list'

    def get_queryset(self):
        queryset = Category.objects.get_all_categories()
        return queryset


class SearchViewSet(ExpressiveListModelMixin, generics.ListAPIView):
    serializer_class = SearchSerializer
    plural_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('query')
        t_d_lookup = (Q(title__icontains=query) | Q(description__icontains=query))
        t_d_c_lookup = (Q(title__icontains=query) | Q(description__icontains=query) | Q(content__icontains=query))
        n_a_a_lookup = (Q(full_name__icontains=query) | Q(activity__icontains=query) | Q(about__icontains=query))

        news = {'news': list(
            News.objects.filter(t_d_c_lookup).distinct().values('id', 'title', 'description', 'thumbnail', 'slug'))}
        categories = {'categories': list(
            Category.objects.filter(t_d_lookup).distinct().values('id', 'title', 'description', 'thumbnail', 'slug',
                                                                  'parent'))}
        consultant = {'consultant': list(
            Consultant.objects.filter(n_a_a_lookup).distinct().values('id', 'full_name', 'about', 'avatar',
                                                                      'phone_number', 'activity'))}
        
        queryset = [news, categories, consultant]
        return queryset


class CompanyRegisterFormViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = CompanyRegisterFormSerializer
    singular_name = 'form_created'


class CompanyEditFormViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = CompanyEditFormSerializer
    singular_name = 'form_created'


class CompanyRegisterTrademarksFormViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = CompanyRegisterTrademarksFormSerializer
    singular_name = 'form_created'


class OfficialServicesFormViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = OfficialServicesFormSerializer
    singular_name = 'form_created'


class RequestLawyerFormViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = RequestLawyerFormSerializer
    singular_name = 'form_created'


class LegalAdviceFormViewSet(ExpressiveCreateContactUsViewSetModelMixin, generics.CreateAPIView):
    serializer_class = LegalAdviceFormSerializer
    singular_name = 'form_created'
