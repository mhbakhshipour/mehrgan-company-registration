from django.db import models
from django.utils.translation import ugettext as _


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
