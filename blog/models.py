from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Manager
from django.utils.translation import ugettext as _
from froala_editor.fields import FroalaField

from mehrgan import settings


class CategoryManager(Manager):
    def exists(self, pk):
        return self.filter(pk=pk).exists()

    def with_children(self):
        return self.prefetch_related('children')

    def get_root_categories_with_children(self, count=4):
        return self.filter(parent__isnull=True).prefetch_related('children').order_by('order')[:count]

    def get_child_category_id_by_root(self, root_category_id):
        return self.values_list('id', flat=True).filter(parent_id=root_category_id)

    def get_child_category_by_root(self, root_category_id):
        return self.filter(parent_id=root_category_id)

    def get_root_categories(self):
        return self.filter(parent_id__isnull=True)

    def get_root_or_children_ids(self, sub_category_id, root_category_id):
        category_ids = []
        if root_category_id is not None and root_category_id != '':
            category_ids = self.get_child_category_id_by_root(root_category_id)
        if sub_category_id is not None and sub_category_id != '':
            category_ids = [sub_category_id]
        return category_ids


class Category(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), null=True, blank=True)
    thumbnail = models.ImageField(_('thumbnail'), upload_to=settings.UPLOAD_DIRECTORIES['category_thumbnail'],
                                  blank=True, null=True)
    parent = models.ForeignKey(to='self', blank=True, null=True, on_delete=models.CASCADE, related_name='children',
                               verbose_name=_('parent'))
    slug = models.CharField(max_length=255, verbose_name=_('slug'), unique=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    objects = CategoryManager()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = _('category')
        verbose_name_plural = _('categories')


class CategorizedItems(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name=_('category'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_('content_type'))
    object_id = models.PositiveIntegerField(verbose_name=_('object_id'))
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.category.title

    class Meta:
        db_table = 'categorized_items'
        verbose_name = _('categorized_items')
        verbose_name_plural = _('categorized_items')


class CommentManager(Manager):
    pass


class Comment(models.Model):
    comment = models.TextField(_('comment'), null=False, blank=False, max_length=500)
    email = models.EmailField(_('email'), null=False, blank=False, max_length=255)
    name = models.CharField(_('name'), null=False, blank=False, max_length=255)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    objects = CommentManager()

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comments'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class CommentsItems(models.Model):
    comment = models.ForeignKey(to='Comment', on_delete=models.CASCADE, verbose_name=_('comment'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_('content_type'))
    object_id = models.PositiveIntegerField(verbose_name=_('object_id'))
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comments_items'
        verbose_name = _('comments_items')
        verbose_name_plural = _('comments_items')


class NewsManager(Manager):
    pass


class News(models.Model):
    title = models.CharField(_('title'), max_length=255, unique=True)
    description = models.TextField(_('description'), null=False, blank=False)
    content = FroalaField()
    categories = GenericRelation(CategorizedItems, null=True, blank=True)
    comments = GenericRelation(CommentsItems, null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    thumbnail = models.ImageField(_('thumbnail'), upload_to=settings.UPLOAD_DIRECTORIES['blog_thumbnail'])
    slug = models.CharField(max_length=255, verbose_name=_('slug'), unique=True)

    objects = NewsManager()

    class Meta:
        db_table = 'news'
        verbose_name = _('news')
        verbose_name_plural = _('news')

    def __str__(self):
        return self.title
