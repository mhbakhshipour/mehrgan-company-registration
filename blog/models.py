from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.db import models
from django.db.models import Manager
from django.utils.translation import ugettext as _
from froala_editor.fields import FroalaField

from core.models import CategorizedItems, CommentedItems
from mehrgan import settings


class NewsManager(Manager):
    def get_news_with_by_category(self, cat_id):
        return self.filter(categories__category=cat_id)


class News(models.Model):
    title = models.CharField(_('title'), max_length=255, unique=True)
    description = models.TextField(_('description'), null=False, blank=False)
    content = FroalaField()
    categories = GenericRelation(CategorizedItems, null=True, blank=True)
    comments = GenericRelation(CommentedItems, null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    thumbnail = models.ImageField(_('thumbnail'), upload_to=settings.UPLOAD_DIRECTORIES['blog_thumbnail'])
    slug = models.CharField(max_length=255, verbose_name=_('slug'), unique=True)

    objects = NewsManager()

    @property
    def custom_created_at(self):
        return self.created_at.strftime('%Y/%m/%d - %H:%M:%S')

    class Meta:
        db_table = 'news'
        verbose_name = _('news')
        verbose_name_plural = _('news')

    def __str__(self):
        return self.title
