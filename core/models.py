from django.contrib.contenttypes.fields import GenericForeignKey
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

    def get_all_categories(self):
        return self.all()

    def get_root_or_children_ids(self, sub_category_id, root_category_id):
        category_ids = []
        if root_category_id is not None and root_category_id != '':
            category_ids = self.get_child_category_id_by_root(root_category_id)
        if sub_category_id is not None and sub_category_id != '':
            category_ids = [sub_category_id]
        return category_ids


class Category(models.Model):
    title = models.CharField(_('title'), max_length=255, unique=True)
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

    @property
    def category_title(self):
        return self.category.title

    @property
    def category_slug(self):
        if self.category.parent is None:
            return self.category.slug
        return self.category.parent.slug

    @property
    def category_parent(self):
        if self.category.parent is None:
            return self.category.parent
        return self.category.parent.id

    class Meta:
        db_table = 'categorized_items'
        verbose_name = _('categorized_items')
        verbose_name_plural = _('categorized_items')


class Comment(models.Model):
    comment_status_choices = (
        ('pending', _('pending')),
        ('accepted', _('accepted'))
    )

    comment = models.TextField(_('comment'), null=False, blank=False, max_length=500)
    email = models.EmailField(_('email'), null=False, blank=False, max_length=255)
    phone = models.CharField(_('phone'), null=False, blank=False, max_length=13)
    name = models.CharField(_('name'), null=False, blank=False, max_length=255)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    parent = models.ForeignKey(to='self', blank=True, null=True, on_delete=models.CASCADE, related_name='children',
                               verbose_name=_('parent'))
    status = models.CharField(_('status'), max_length=255, choices=comment_status_choices, default='pending')

    def __str__(self):
        return self.comment

    class Meta:
        db_table = 'comments'
        verbose_name = _('comment')
        verbose_name_plural = _('comments')


class CommentedItems(models.Model):
    comment = models.ForeignKey(to='Comment', on_delete=models.CASCADE, verbose_name=_('comment'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_('content_type'))
    object_id = models.PositiveIntegerField(verbose_name=_('object_id'))
    content_object = GenericForeignKey('content_type', 'object_id')

    @property
    def comment_first_name(self):
        return self.comment.first_name

    @property
    def comment_last_name(self):
        return self.comment.last_name

    @property
    def comment_title(self):
        return self.comment.comment

    @property
    def comment_email(self):
        return self.comment.email

    @property
    def comment_phone(self):
        return self.comment.phone

    @property
    def comment_status(self):
        return self.comment.status

    @property
    def comment_created_at(self):
        return self.comment.created_at.strftime('%Y/%m/%d - %H:%M:%S')

    @property
    def comment_parent(self):
        if self.comment.parent is None:
            return self.comment.parent
        return self.comment.parent.id

    def __str__(self):
        return self.comment.comment

    class Meta:
        db_table = 'commented_items'
        verbose_name = _('commented_items')
        verbose_name_plural = _('commented_items')


class ContactUs(models.Model):
    contact_us_status_choices = (
        ('read', _('read')),
        ('unread', _('unread'))
    )

    full_name = models.CharField(_('full_name'), null=False, blank=False, max_length=500)
    email = models.EmailField(_('email'), null=False, blank=False, max_length=255)
    phone = models.CharField(_('phone'), null=False, blank=False, max_length=13)
    description = models.TextField(_('description'), null=False, blank=False, max_length=1024)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    status = models.CharField(_('status'), max_length=255, choices=contact_us_status_choices, default='unread')

    @property
    def c_created_at(self):
        return self.created_at.strftime('%Y/%m/%d - %H:%M:%S')

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'contact_us'
        verbose_name = _('contact_us')
        verbose_name_plural = _('contact_us')


class Faq(models.Model):
    title = models.CharField(_('title'), null=False, blank=False, max_length=255)
    description = FroalaField()
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)

    @property
    def c_created_at(self):
        return self.created_at.strftime('%Y/%m/%d - %H:%M:%S')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'faq'
        verbose_name = _('faq')
        verbose_name_plural = _('faq')
