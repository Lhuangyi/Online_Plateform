from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser  # inherit from django/user and modifiy new user
# Create your models here.


class UserProfile(AbstractUser):
    nickname = models.CharField(max_length=50, verbose_name='nickname', default="")
    birthday = models.DateField(verbose_name='birthday', null=True)
    gender = models.CharField(choices=(("male","make"), ("female","female")), default='female', max_length=10)
    address = models.CharField(max_length=500, default="")
    mobile = models.CharField(max_length=11, null=True, blank=True)
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = verbose_name


class EmailVerifyRecord(models.Model):
    code = models.CharField(max_length=20, verbose_name='verify code')
    email = models.EmailField(max_length=50,verbose_name='email address')
    send_type = models.CharField(choices=(('sign up', 'register'),('forget', 'retrive password')),max_length=10)
    send_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'email verification code'
        verbose_name_plural = verbose_name


class PageBanner(models.Model):
    title = models.CharField(max_length=100, verbose_name='name')
    image = models.ImageField(upload_to="banner/%Y/%m", verbose_name='page banner', max_length=100)
    url = models.URLField(max_length=200, verbose_name='url address')
    index = models.IntegerField(default=100, verbose_name="order")
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add time')

    class Meta:
        verbose_name = "page banner image"
        verbose_name_plural = verbose_name

