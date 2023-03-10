# Generated by Django 2.2.6 on 2020-01-06 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultant', '0003_auto_20200106_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultant',
            name='is_enabled',
            field=models.BooleanField(default=True, verbose_name='آیا فعال است؟'),
        ),
        migrations.AlterField(
            model_name='consultant',
            name='rating',
            field=models.ManyToManyField(blank=True, related_name='rate_average', to='consultant.Rate', verbose_name='امتیاز'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(verbose_name='تاریخ پایان'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_date',
            field=models.DateField(verbose_name='تاریخ شروع'),
        ),
    ]
