# Generated by Django 2.1.7 on 2019-03-24 00:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='course name')),
                ('desc', models.CharField(max_length=300, verbose_name='course description')),
                ('detail', models.TextField(verbose_name='course detail')),
                ('degree', models.CharField(choices=[('beginner', 'beginner'), ('intermediate', 'intermediate'), ('advanced', 'advanced')], max_length=10)),
                ('learn_times', models.IntegerField(default=0, verbose_name='learning time (min)')),
                ('student', models.IntegerField(default=0, verbose_name='student number')),
                ('fav_nums', models.IntegerField(default=0, verbose_name='favorite number')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='cover image')),
                ('click_num', models.IntegerField(default=0, verbose_name='course click')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
            ],
            options={
                'verbose_name': 'course',
                'verbose_name_plural': 'course',
            },
        ),
        migrations.CreateModel(
            name='CourseRecourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='course resource name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('download', models.FileField(upload_to='course/resource/%Y/%m', verbose_name='resource file')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='course')),
            ],
            options={
                'verbose_name': 'course resources',
                'verbose_name_plural': 'course resources',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='lesson name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course', verbose_name='course')),
            ],
            options={
                'verbose_name': 'course lesson',
                'verbose_name_plural': 'course lesson',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='video name')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='add time')),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Lesson', verbose_name='lesson')),
            ],
            options={
                'verbose_name': 'course video',
                'verbose_name_plural': 'course video',
            },
        ),
    ]
