from django import forms
from django.contrib import admin

from core.models import *


class CategoriesForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'description', 'parent', 'slug']
        labels = {
            'title': 'عنوان',
            'description': 'توضیح',
            'parent': 'سر دسته',
            'slug': 'شناسه آدرسی'
        }


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'parent', 'slug', 'created_at']
    form = CategoriesForm


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['first_name', 'last_name', 'email', 'comment', 'parent', 'status']
        labels = {
            'first_name': 'نام',
            'last_name': 'نام خانوادگی',
            'email': 'ایمیل',
            'comment': 'نظر',
            'parent': 'کامنت اصلی',
            'status': 'وضعیت',
        }


class CommentAdmin(admin.ModelAdmin):
    list_display = ['last_name', 'email', 'comment', 'created_at', 'parent', 'status']
    list_filter = ('status',)
    form = CommentForm


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'phone', 'description', 'status']
        labels = {
            'full_name': 'نام',
            'email': 'ایمیل',
            'phone': 'شماره تماس',
            'description': 'متن',
            'status': 'وضعیت',
        }


class ContactUsAdmin(admin.ModelAdmin):
    form = ContactUsForm
    list_display = ('full_name', 'email', 'phone', 'description', 'created_at', 'status')
    list_filter = ('status',)
    search_fields = ['description']


class FaqForm(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['title', 'description']
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات'
        }


class FaqAdmin(admin.ModelAdmin):
    form = FaqForm
    list_display = ('title', 'description', 'created_at')
    search_fields = ['title']

    def save_related(self, request, form, formsets, change):
        return super().save_related(request, form, formsets, change)


class CompanyEditFormAdmin(admin.ModelAdmin):
    list_display = ('company_type', 'company_type_change', 'region', 'name', 'phone', 'created_at', 'is_tracked')
    list_filter = ('is_tracked',)


class CompanyRegisterFormAdmin(admin.ModelAdmin):
    list_display = ('company_type', 'activity', 'region', 'fund', 'name', 'phone', 'created_at', 'is_tracked')
    list_filter = ('is_tracked',)


class CompanyRegisterTrademarksFormAdmin(admin.ModelAdmin):
    list_display = ('trademark_type', 'name', 'phone', 'is_extended', 'created_at', 'is_tracked')
    list_filter = ('is_tracked',)


class LegalAdviceFormAdmin(admin.ModelAdmin):
    list_display = ('advice_type', 'name', 'phone', 'created_at', 'is_tracked')
    list_filter = ('is_tracked',)


class OfficialServicesFormAdmin(admin.ModelAdmin):
    list_display = ('service_type', 'name', 'phone', 'created_at', 'is_tracked')
    list_filter = ('is_tracked',)


class RequestLawyerFormAdmin(admin.ModelAdmin):
    list_display = ('request_type', 'name', 'phone', 'created_at', 'is_tracked')
    list_filter = ('is_tracked',)


admin.site.register(ContactUs, ContactUsAdmin)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(CategorizedItems)
admin.site.register(Comment, CommentAdmin)
admin.site.register(CommentedItems)
admin.site.register(Faq, FaqAdmin)
admin.site.register(CompanyEditForm, CompanyEditFormAdmin)
admin.site.register(CompanyRegisterForm, CompanyRegisterFormAdmin)
admin.site.register(CompanyRegisterTrademarksForm, CompanyRegisterTrademarksFormAdmin)
admin.site.register(LegalAdviceForm, LegalAdviceFormAdmin)
admin.site.register(OfficialServicesForm, OfficialServicesFormAdmin)
admin.site.register(RequestLawyerForm, RequestLawyerFormAdmin)
