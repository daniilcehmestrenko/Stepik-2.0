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


class TestModule(models.Model):
    name = models.CharField(
                max_length=150,
                verbose_name='Название'
            )
    slug = models.SlugField(
                max_length=150
            )

    description = models.TextField(
                verbose_name='Описание'
            )
    course = models.ForeignKey(
                'Course',
                on_delete=models.CASCADE,
                related_name='course_test_modules',
                verbose_name='Курс'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тест модуль'
        verbose_name_plural = 'Тест модули'


class ContentModule(models.Model):
    name = models.CharField(
                max_length=150,
                verbose_name='Название'
            )
    slug = models.SlugField(
                max_length=150
            )
    description = models.TextField(
                verbose_name='Описание'
            )
    course = models.ForeignKey(
                'Course',
                on_delete=models.CASCADE,
                related_name='course_content_modules',
                verbose_name='Курс'
            )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Контент модуль'
        verbose_name_plural = 'Контент модули'
        ordering = ['course']


class ContentBase(models.Model):
    content_module = models.ForeignKey(
                'ContentModule',
                on_delete=models.CASCADE,
                related_name='%(class)s_related',
                verbose_name='Модуль',
            )

    class Meta:
        abstract = True


class Text(ContentBase):
    text = models.TextField(
                verbose_name='Текст'
            )

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Тексты'


class Video(ContentBase):
    url = models.URLField(
                verbose_name='Ссылка'
            )

    class Meta:
        verbose_name = 'Видео'
        verbose_name_plural = 'Видео'


class Image(ContentBase):
    image = models.ImageField(
                upload_to='images',
                verbose_name='Изображение'
            )

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'


class Question(ContentBase):
    title = models.TextField(
                verbose_name='Вопрос'
            )
    correct_answer = models.TextField(
                verbose_name='Правильный ответ'
            )
    test_module = models.ForeignKey(
                'TestModule',
                on_delete=models.CASCADE,
                related_name='test_module_questions',
                verbose_name='Тест модуль',
            )

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

