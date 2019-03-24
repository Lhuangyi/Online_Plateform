# Generated by Django 2.1.7 on 2019-03-24 00:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(max_length=200, verbose_name='comments')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='time of adding')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'course comments',
                'verbose_name_plural': 'course comments',
            },
        ),
        migrations.CreateModel(
            name='UserAsk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('mobile', models.CharField(max_length=11, verbose_name='cellphone number')),
                ('course_name', models.CharField(max_length=50, verbose_name='query course name ')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='time of adding')),
            ],
            options={
                'verbose_name': 'user asking',
                'verbose_name_plural': 'user asking',
            },
        ),
        migrations.CreateModel(
            name='UserCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='time of adding')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='course')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user course',
                'verbose_name_plural': 'user course',
            },
        ),
        migrations.CreateModel(
            name='Userfavorite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fav_id', models.IntegerField(default=0, verbose_name='data id')),
                ('fav_type', models.IntegerField(choices=[(1, 'course'), (2, 'organization'), (3, 'teacher')], default=1, verbose_name='favorite type')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='time of adding')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'user favorite',
                'verbose_name_plural': 'user favorite',
            },
        ),
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.IntegerField(default=0, verbose_name='user id')),
                ('message', models.CharField(max_length=500, verbose_name='message')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='time of adding')),
                ('has_read', models.BooleanField(default=False, verbose_name='has read or not')),
            ],
            options={
                'verbose_name': 'user message',
                'verbose_name_plural': 'user message',
            },
        ),
    ]
