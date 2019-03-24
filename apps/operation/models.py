from datetime import datetime

from django.db import models

# Create your models here.
from users.models import UserProfile
from courses.models import Course


class UserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='name')
    mobile = models.CharField(max_length=11, verbose_name='cellphone number')
    course_name = models.CharField(max_length=50 , verbose_name='query course name ')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='time of adding')

    class Meta:
        verbose_name = 'user asking'
        verbose_name_plural = verbose_name


class CourseComments(models.Model):  # course comments
    user = models.ForeignKey(UserProfile, verbose_name='user',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='course',on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='comments')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='time of adding')

    class Meta:
        verbose_name = 'course comments'
        verbose_name_plural = verbose_name


class Userfavorite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='user',on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0,verbose_name='data id')
    fav_type = models.IntegerField(choices=((1,'course'),(2,"organization"),(3,'teacher')),default=1, verbose_name='favorite type')
    add_time = models.DateTimeField(default=datetime.now,verbose_name='time of adding')

    class Meta:
        verbose_name = 'user favorite'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0,verbose_name='user id')
    message = models.CharField(max_length=500, verbose_name="message")
    add_time = models.DateTimeField(default=datetime.now,verbose_name='time of adding')
    has_read = models.BooleanField(default=False, verbose_name='has read or not')

    class Meta:
        verbose_name = 'user message'
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='user',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name = 'course',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now,verbose_name='time of adding')

    class Meta:
        verbose_name = 'user course'
        verbose_name_plural= verbose_name



