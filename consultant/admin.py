from django.contrib import admin
from django.contrib.admin import TabularInline
from django.utils.translation import ugettext as _
from django import forms
from jalali_date.admin import ModelAdminJalaliMixin

from consultant.models import *


class SkillInlineModelAdmin(TabularInline):
    model = ConsultantSkill
    extra = 1


class EducationInlineModelAdmin(TabularInline):
    model = ConsultantEducation
    extra = 1


class ExperienceInlineModelAdmin(TabularInline):
    model = ConsultantExperience
    extra = 1


class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = ['full_name', 'father_name', 'phone_number', 'mobile_number', 'activity', 'email', 'address', 'avatar',
                  'linkedin_link', 'telegram_link', 'about', 'cv', 'rating', 'is_enabled']
        labels = {
            'full_name': _('full_name'),
            'father_name': _('father_name'),
            'phone_number': _('phone_number'),
            'mobile_number': _('mobile_number'),
            'activity': _('activity'),
            'email': _('email'),
            'address': _('address'),
            'avatar': _('avatar'),
            'linkedin_link': _('linkedin_link'),
            'telegram_link': _('telegram_link'),
            'about': _('about'),
            'cv': _('cv'),
            'rating': _('rating'),
            'is_enabled': _('is_enabled'),
        }


class ConsultantAdmin(admin.ModelAdmin):
    form = ConsultantForm
    list_display = ('full_name', 'mobile_number', 'activity', 'email', 'created_at', 'is_enabled')
    inlines = (SkillInlineModelAdmin, EducationInlineModelAdmin, ExperienceInlineModelAdmin)
    search_fields = ['full_name']
    list_filter = ('is_enabled',)

    def save_related(self, request, form, formsets, change):
        return super().save_related(request, form, formsets, change)


class ExperienceAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'created_at')
    search_fields = ['title']


class EducationAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ('title', 'university', 'end_date', 'created_at')
    search_fields = ['title']


admin.site.register(Consultant, ConsultantAdmin)
admin.site.register(ConsultantSkill)
admin.site.register(Skill)
admin.site.register(Rate)
admin.site.register(ConsultantEducation)
admin.site.register(Education, EducationAdmin)
admin.site.register(ConsultantExperience)
admin.site.register(Experience, ExperienceAdmin)
