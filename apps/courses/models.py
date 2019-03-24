from datetime import datetime


from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=50, verbose_name='course name')
    desc = models.CharField(max_length=300, verbose_name='course description')
    detail = models.TextField(verbose_name="course detail")  # infinite length
    degree = models.CharField(choices=(('beginner', 'beginner'),('intermediate', 'intermediate'), ('advanced', 'advanced')),max_length=10)
    learn_times = models.IntegerField(default=0,verbose_name='learning time (min)')
    student = models.IntegerField(default=0, verbose_name='student number')
    fav_nums = models.IntegerField(default=0, verbose_name='favorite number')
    image = models.ImageField(upload_to='courses/%Y/%m', verbose_name='cover image', max_length=100)
    click_num = models.IntegerField(default=0, verbose_name='course click')
    add_time = models.DateTimeField(default=datetime.now, verbose_name= 'add time')

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = verbose_name


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name='course', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='lesson name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name= 'add time')

    class Meta:
        verbose_name = 'course lesson'
        verbose_name_plural = verbose_name


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name='lesson',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='video name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name= 'add time')

    class Meta:
        verbose_name = 'course video'
        verbose_name_plural = verbose_name


class CourseRecourse(models.Model):
    course = models.ForeignKey(Course, verbose_name='course',on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='course resource name')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='add time')
    download = models.FileField(upload_to='course/resource/%Y/%m', verbose_name='resource file', max_length=100)

    class Meta:
        verbose_name = 'course resources'
        verbose_name_plural = verbose_name
