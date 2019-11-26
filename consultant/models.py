from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from froala_editor.fields import FroalaField
from django.utils.translation import ugettext as _

from core.models import CategorizedItems
from mehrgan import settings


class Skill(models.Model):
    title = models.CharField(_('title'), max_length=255)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'skills'
        verbose_name = _('skill')
        verbose_name_plural = _('skills')


class SkilledConsultant(models.Model):
    skill = models.ForeignKey(to='Skill', on_delete=models.CASCADE, verbose_name=_('skill'))
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, verbose_name=_('content_type'))
    object_id = models.PositiveIntegerField(verbose_name=_('object_id'))
    content_object = GenericForeignKey('content_type', 'object_id')

    @property
    def skill_title(self):
        return self.skill.title

    def __str__(self):
        return self.skill.title

    class Meta:
        db_table = 'skilled_consultant'
        verbose_name = _('skilled_consultant')
        verbose_name_plural = _('skilled_consultant')


class ContactForm(models.Model):
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
        db_table = 'contact_form'
        verbose_name = _('contact form')
        verbose_name_plural = _('contact form')


class ContactConsultantForm(models.Model):
    consultant = models.ForeignKey(verbose_name=_('consultant'), to="Consultant", on_delete=models.CASCADE)
    contact_form = models.ForeignKey(verbose_name=_('contact_form'), to="ContactForm", on_delete=models.CASCADE)

    class Meta:
        db_table = 'contact_consultant_form'
        verbose_name = _('contact consultant form')
        verbose_name_plural = _('contact consultant form')


class Consultant(models.Model):
    education_degree_choices = (
        ('associate_degree', _('associate_degree')),
        ('bachelors_degree', _('bachelors_degree')),
        ('masters_degree', _('masters_degree')),
        ('doctoral_degree', _('doctoral_degree')),
    )

    full_name = models.CharField(_('full_name'), max_length=255, unique=True)
    father_name = models.CharField(_('father_name'), max_length=255)
    phone = models.CharField(_('phone'), max_length=13)
    email = models.CharField(_('email'), max_length=255)
    address = models.TextField(_('address'), max_length=512)
    education_degree = models.CharField(_('education_degree'), max_length=255, choices=education_degree_choices)
    description = models.TextField(_('description'), null=False, blank=False)
    about = FroalaField()
    categories = GenericRelation(CategorizedItems, null=True, blank=True)
    skills = GenericRelation(SkilledConsultant, null=True, blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    avatar = models.ImageField(_('avatar'), upload_to=settings.UPLOAD_DIRECTORIES['consultant_avatar'], null=True, blank=True)

    linkedin_link = models.URLField(_('linkedin_link'), max_length=512, null=True, blank=True)
    telegram_link = models.URLField(_('telegram_link'), max_length=512, null=True, blank=True)
    instagram_link = models.URLField(_('instagram_link'), max_length=512, null=True, blank=True)
    twitter_link = models.URLField(_('twitter_link'), max_length=512, null=True, blank=True)
    facebook_link = models.URLField(_('facebook_link'), max_length=512, null=True, blank=True)

    rate = models.SmallIntegerField(_('rate'), default=5, null=True, blank=True)
    contact_form = models.ManyToManyField(verbose_name=_('contact_form'), to='ContactForm', through="ContactConsultantForm", blank=True)

    @property
    def c_created_at(self):
        return self.created_at.strftime('%Y/%m/%d - %H:%M:%S')

    class Meta:
        db_table = 'consultant'
        verbose_name = _('consultant')
        verbose_name_plural = _('consultant')

    def __str__(self):
        return self.full_name
