from datetime import datetime


from django.db import models

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='city name')
    desc = models.CharField(max_length=200, verbose_name='city description')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name= 'organization name')
    desc = models.TextField(verbose_name= 'organization description')
    click_num = models.IntegerField(default=0 , verbose_name='click number')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite number')
    image = models.ImageField(upload_to='org/%Y/%m', max_length=100)
    address = models.CharField(max_length= 300, verbose_name='organization address')
    city = models.ForeignKey(CityDict, verbose_name='organization city',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,verbose_name='work organization',on_delete=models.CASCADE)
    name = models.CharField(max_length=50, verbose_name='teacher name')
    work_years = models.IntegerField(default=0, verbose_name='work years')
    work_company = models.CharField(max_length=50, verbose_name='work company')
    work_position = models.CharField(max_length=40, verbose_name='work position')
    points = models.CharField(max_length=50, verbose_name='teaching points')
    click_num = models.IntegerField(default=0, verbose_name='click number')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite number')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='time of adding')

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = verbose_name








