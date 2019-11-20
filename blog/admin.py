from django import forms
from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline

from blog.models import News, Category, CategorizedItems, CommentedItems, Comment


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


class CategoryGenericInlineModelAdmin(GenericStackedInline):
    model = CategorizedItems
    extra = 1


class CommentGenericInlineModelAdmin(GenericStackedInline):
    model = CommentedItems
    extra = 1


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'comment', 'parent', 'status']
        labels = {
            'name': 'نام',
            'email': 'ایمیل',
            'comment': 'نظر',
            'parent': 'کامنت اصلی',
            'status': 'وضعیت',
        }


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'comment', 'created_at', 'parent', 'status']
    list_filter = ('status',)
    form = CommentForm


class BlogForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'description', 'content', 'thumbnail', 'slug']
        labels = {
            'title': 'عنوان',
            'description': 'توضیحات',
            'content': 'متن',
            'thumbnail': 'عکس',
            'slug': 'شناسه آدرسی',
        }


class BlogAdmin(admin.ModelAdmin):
    form = BlogForm
    list_display = ('title', 'description', 'created_at', 'slug')
    inlines = (CommentGenericInlineModelAdmin, CategoryGenericInlineModelAdmin)
    search_fields = ['title']

    def save_related(self, request, form, formsets, change):
        return super().save_related(request, form, formsets, change)


admin.site.register(News, BlogAdmin)
admin.site.register(Category, CategoriesAdmin)
admin.site.register(Comment, CommentAdmin)
