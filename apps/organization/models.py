from datetime import datetime
from django.db import models
from DjangoUeditor.models import UEditorField

# Create your models here.


class CityDict(models.Model):
    name = models.CharField(max_length=20, verbose_name='city name')
    desc = models.CharField(max_length=200, verbose_name='city description')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'city'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.name


class CourseOrg(models.Model):
    name = models.CharField(max_length=50, verbose_name= 'organization name')
    desc = models.TextField(verbose_name='organization description', default='')

    tag = models.CharField(default='Famous', max_length=10, verbose_name='Organization tag')
    category = models.CharField(default='Organization', verbose_name='organization category', max_length=20 ,
                                choices=(('Organization','Organization'),('University','University'),('Person','Person')))
    click_num = models.IntegerField(default=0 , verbose_name='click number')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite number')
    image = models.ImageField(upload_to='org/%Y/%m', max_length=100, verbose_name='logo')
    address = models.CharField(max_length=300, verbose_name='organization address')
    city = models.ForeignKey(CityDict, verbose_name='organization city',on_delete=models.CASCADE)
    students =models.IntegerField(default=0 , verbose_name='student number')
    course_num =models.IntegerField(default=0, verbose_name='course number')
    add_time = models.DateTimeField(default=datetime.now)

    class Meta:
        verbose_name = 'organization'
        verbose_name_plural = verbose_name

    def get_teacher_nums(self):
        return self.teacher_set.all().count()

    def __str__(self):
        return self.name


class Teacher(models.Model):
    org = models.ForeignKey(CourseOrg,default='',verbose_name='work organization',on_delete=models.CASCADE)
    name = models.CharField(max_length=50, default='',verbose_name='teacher name')
    work_years = models.IntegerField(default=0, verbose_name='work years')
    work_company = models.CharField(default='', max_length=50, verbose_name='work company')
    work_position = models.CharField(default='', max_length=40, verbose_name='work position')
    points = models.CharField(default='',max_length=50, verbose_name='teaching points')
    click_num = models.IntegerField(default=0, verbose_name='click number')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite number')
    age = models.IntegerField(default=20, verbose_name="age")
    image = models.ImageField(default='', upload_to="teacher/%y/%m", verbose_name="user image", max_length=100)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='time of adding')

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_course_nums(self):
        return self.course_set.all().count()








