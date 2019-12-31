from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from blog.models import News
from core.models import CategorizedItems, CommentedItems


class CategoryGenericInlineModelAdmin(GenericStackedInline):
    model = CategorizedItems
    extra = 1


class CommentGenericInlineModelAdmin(GenericStackedInline):
    model = CommentedItems
    extra = 1


class BlogForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'content', 'time', 'thumbnail', 'slug']
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات',
            'content': 'متن',
            'thumbnail': 'عکس',
            'time': 'زمان',
            'slug': 'شناسه آدرسی',
        }


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ('title', 'description', 'time', 'created_at', 'slug')
    inlines = (CommentGenericInlineModelAdmin, CategoryGenericInlineModelAdmin)
    search_fields = ['title']

    def save_related(self, request, form, formsets, change):
        return super().save_related(request, form, formsets, change)


admin.site.register(News, BlogAdmin)
