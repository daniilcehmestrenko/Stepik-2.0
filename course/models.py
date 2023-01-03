from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.db import models


class Subject(models.Model):
    name = models.CharField(
                max_length=100,
                verbose_name='Название'
            )
    slug = models.SlugField(
                max_length=100,
                unique=True
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'
        ordering = ['name']


class Course(models.Model):
    name = models.CharField(
                max_length=200,
                verbose_name='Название'
            )
    slug = models.SlugField(
                max_length=200,
                unique=True
            )
    description = models.TextField(
                verbose_name='Описание'
            )
    created_date = models.DateField(
                auto_now_add=True
            )
    owner = models.ForeignKey(
                User,
                on_delete=models.CASCADE,
                related_name='course_owners',
                verbose_name='Создатели курса'
            )
    subject = models.ForeignKey(
                'Subject',
                on_delete=models.CASCADE,
                related_name='course_subjects',
                verbose_name='Предметы курса'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'
        ordering = ['-created_date']


class Module(models.Model):
    name = models.CharField(
                max_length=150,
                verbose_name='Название'
            )
    description = models.TextField(
                verbose_name='Описание'
            )
    course = models.ForeignKey(
                'Course',
                on_delete=models.CASCADE,
                related_name='course_modules',
                verbose_name='Курс'
            )

    def __str__(self):
        return self.name


class Content(models.Model):
    module = models.ForeignKey(
                'Module',
                on_delete=models.CASCADE,
                related_name='module_contents',
                verbose_name='Модуль'
            )
    objects_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(
                ContentType,
                on_delete=models.CASCADE
            )
    item = GenericForeignKey(
                'content_type',
                'objects_id'
            )

