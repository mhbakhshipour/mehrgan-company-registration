from django import forms
from django.contrib import admin

from core.models import ContactUs


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

    def save_related(self, request, form, formsets, change):
        return super().save_related(request, form, formsets, change)


admin.site.register(ContactUs, ContactUsAdmin)
