from django.db import models
from django.db.models import Avg, Manager
from froala_editor.fields import FroalaField
from django.utils.translation import ugettext as _

from mehrgan import settings


class Skill(models.Model):
    title = models.CharField(_('title'), max_length=255, unique=True)
    created_at = models.DateTimeField(_('created_at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'skills'
        verbose_name = _('skill')
        verbose_name_plural = _('skills')


class ConsultantSkill(models.Model):
    consultant = models.ForeignKey(verbose_name=_('consultant'), to="Consultant", on_delete=models.CASCADE, related_name='skills_attributes')
    skill = models.ForeignKey(verbose_name=_('skill'), to="Skill", on_delete=models.CASCADE)
    description = models.TextField(_('description'), blank=True, null=True)

    @property
    def skill_title(self):
        return self.skill.title

    class Meta:
        db_table = 'consultant_skills'
        verbose_name = _('consultant skill')
        verbose_name_plural = _('consultant skills')


class Education(models.Model):
    title = models.CharField(_('title'), max_length=255)
    university = models.CharField(_('university'), max_length=255)
    end_date = models.IntegerField(_('end_date'))
    created_at = models.DateTimeField(_('created_at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'educations'
        verbose_name = _('education')
        verbose_name_plural = _('educations')


class ConsultantEducation(models.Model):
    consultant = models.ForeignKey(verbose_name=_('consultant'), to="Consultant", on_delete=models.CASCADE, related_name='education_attributes')
    education = models.ForeignKey(verbose_name=_('education'), to="Education", on_delete=models.CASCADE)
    description = models.TextField(_('description'), blank=True, null=True)

    @property
    def education_title(self):
        return self.education.title

    @property
    def education_university(self):
        return self.education.university

    @property
    def education_end_date(self):
        return self.education.end_date

    class Meta:
        db_table = 'consultant_educations'
        verbose_name = _('consultant education')
        verbose_name_plural = _('consultant educations')


class Experience(models.Model):
    title = models.CharField(_('title'), max_length=255)
    start_date = models.DateField(_('start_date'), auto_now=True, blank=False, null=False)
    end_date = models.DateField(_('end_date'), blank=True, null=True)
    created_at = models.DateTimeField(_('created_at'), auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'experiences'
        verbose_name = _('experience')
        verbose_name_plural = _('experiences')


class ConsultantExperience(models.Model):
    consultant = models.ForeignKey(verbose_name=_('consultant'), to="Consultant", on_delete=models.CASCADE, related_name='experience_attributes')
    experience = models.ForeignKey(verbose_name=_('experience'), to="Experience", on_delete=models.CASCADE)
    description = models.TextField(_('description'), blank=True, null=True)

    @property
    def experience_title(self):
        return self.experience.title

    @property
    def experience_start_date(self):
        return self.experience.start_date

    @property
    def experience_end_date(self):
        return self.experience.end_date

    class Meta:
        db_table = 'consultant_experiences'
        verbose_name = _('consultant experience')
        verbose_name_plural = _('consultant experiences')


class RateManager(Manager):
    def average_rate(self, c_id):
        s = str(self.filter(consultant_id=c_id).aggregate(Avg('number')))
        a = '.'.join(filter(lambda i: i.isdigit(), s))
        result = a[0:3]
        return result


class Rate(models.Model):
    consultant = models.ForeignKey(verbose_name=_('consultant'), to="Consultant", on_delete=models.CASCADE)
    rate = models.SmallIntegerField(_('rate'), default=5)
    created_at = models.DateTimeField(_('created_at'), auto_now=True)

    objects = RateManager()

    class Meta:
        db_table = 'rates'
        verbose_name = _('rate')
        verbose_name_plural = _('rates')


class Consultant(models.Model):
    full_name = models.CharField(_('full_name'), max_length=255, unique=True)
    father_name = models.CharField(_('father_name'), max_length=255)
    phone_number = models.CharField(_('phone_number'), max_length=13, null=True)
    mobile_number = models.CharField(_('mobile_number'), max_length=13, null=True)
    activity = models.CharField(_('activity'), max_length=255, null=True)
    email = models.EmailField(_('email'), max_length=255)
    address = models.TextField(_('address'), max_length=512)
    avatar = models.ImageField(_('avatar'), upload_to=settings.UPLOAD_DIRECTORIES['consultant_avatar'], null=True, blank=True, default='consultant_avatar/sample.jpg')
    linkedin_link = models.URLField(_('linkedin_link'), max_length=512, null=True, blank=True)
    telegram_link = models.URLField(_('telegram_link'), max_length=512, null=True, blank=True)
    about = FroalaField()

    skills = models.ManyToManyField(verbose_name=_('skills'), to="Skill", blank=True, through="ConsultantSkill")
    educations = models.ManyToManyField(verbose_name=_('educations'), to="Education", blank=True, through="ConsultantEducation")
    experiences = models.ManyToManyField(verbose_name=_('experiences'), to="Experience", blank=True, through="ConsultantExperience")

    created_at = models.DateTimeField(_('created at'), auto_now=True)
    rating = models.ManyToManyField(verbose_name=_('rate'), to="Rate", related_name='rate_average', blank=True)

    @property
    def c_created_at(self):
        return self.created_at.strftime('%Y/%m/%d - %H:%M:%S')

    @property
    def rate(self):
        return Rate.objects.average_rate(self.id)

    class Meta:
        db_table = 'consultant'
        verbose_name = _('consultant')
        verbose_name_plural = _('consultant')

    def __str__(self):
        return self.full_name
