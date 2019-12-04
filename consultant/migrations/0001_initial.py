# Generated by Django 2.2.6 on 2019-12-04 21:47

from django.db import migrations, models
import django.db.models.deletion
import froala_editor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consultant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255, unique=True, verbose_name='full_name')),
                ('father_name', models.CharField(max_length=255, verbose_name='father_name')),
                ('phone_number', models.CharField(max_length=13, null=True, verbose_name='phone_number')),
                ('mobile_number', models.CharField(max_length=13, null=True, verbose_name='mobile_number')),
                ('activity', models.CharField(max_length=255, null=True, verbose_name='activity')),
                ('email', models.EmailField(max_length=255, verbose_name='email')),
                ('address', models.TextField(max_length=512, verbose_name='address')),
                ('avatar', models.ImageField(blank=True, default='consultant_avatar/sample.jpg', null=True, upload_to='consultant_avatar', verbose_name='avatar')),
                ('linkedin_link', models.URLField(blank=True, max_length=512, null=True, verbose_name='linkedin_link')),
                ('telegram_link', models.URLField(blank=True, max_length=512, null=True, verbose_name='telegram_link')),
                ('about', froala_editor.fields.FroalaField()),
                ('cv', models.FileField(blank=True, null=True, upload_to='consultant_cv', verbose_name='cv')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'consultant',
                'verbose_name_plural': 'consultant',
                'db_table': 'consultant',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('university', models.CharField(max_length=255, verbose_name='university')),
                ('end_date', models.IntegerField(verbose_name='end_date')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'education',
                'verbose_name_plural': 'educations',
                'db_table': 'educations',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('start_date', models.DateField(auto_now=True, verbose_name='start_date')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='end_date')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'experience',
                'verbose_name_plural': 'experiences',
                'db_table': 'experiences',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='title')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'skill',
                'verbose_name_plural': 'skills',
                'db_table': 'skills',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.SmallIntegerField(default=5, verbose_name='rate')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created_at')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultant.Consultant', verbose_name='consultant')),
            ],
            options={
                'verbose_name': 'rate',
                'verbose_name_plural': 'rates',
                'db_table': 'rates',
            },
        ),
        migrations.CreateModel(
            name='ConsultantSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills_attributes', to='consultant.Consultant', verbose_name='consultant')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultant.Skill', verbose_name='skill')),
            ],
            options={
                'verbose_name': 'consultant skill',
                'verbose_name_plural': 'consultant skills',
                'db_table': 'consultant_skills',
            },
        ),
        migrations.CreateModel(
            name='ConsultantExperience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experience_attributes', to='consultant.Consultant', verbose_name='consultant')),
                ('experience', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultant.Experience', verbose_name='experience')),
            ],
            options={
                'verbose_name': 'consultant experience',
                'verbose_name_plural': 'consultant experiences',
                'db_table': 'consultant_experiences',
            },
        ),
        migrations.CreateModel(
            name='ConsultantEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('consultant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='education_attributes', to='consultant.Consultant', verbose_name='consultant')),
                ('education', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consultant.Education', verbose_name='education')),
            ],
            options={
                'verbose_name': 'consultant education',
                'verbose_name_plural': 'consultant educations',
                'db_table': 'consultant_educations',
            },
        ),
        migrations.AddField(
            model_name='consultant',
            name='educations',
            field=models.ManyToManyField(blank=True, through='consultant.ConsultantEducation', to='consultant.Education', verbose_name='educations'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='experiences',
            field=models.ManyToManyField(blank=True, through='consultant.ConsultantExperience', to='consultant.Experience', verbose_name='experiences'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='rating',
            field=models.ManyToManyField(blank=True, related_name='rate_average', to='consultant.Rate', verbose_name='rate'),
        ),
        migrations.AddField(
            model_name='consultant',
            name='skills',
            field=models.ManyToManyField(blank=True, through='consultant.ConsultantSkill', to='consultant.Skill', verbose_name='skills'),
        ),
    ]
