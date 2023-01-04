from django.contrib import admin

from .models import (Course, ContentModule, Subject, Image,
                     Question, TestModule, Text, Video)


class ImageInLine(admin.StackedInline):
    model = Image
    extra = 1


class TextInLine(admin.StackedInline):
    model = Text
    extra = 1


class VideoInLine(admin.StackedInline):
    model = Video
    extra = 1


class QuestionInLine(admin.StackedInline):
    model = Question

@admin.register(TestModule)
class TestModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    inlines = (QuestionInLine,)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(ContentModule)
class ContentModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    inlines = (ImageInLine, TextInLine, VideoInLine)
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_date']
    list_filter = ['created_date', 'subject']
    search_fields = ['name', 'descriptions']
    prepopulated_fields = {'slug': ('name',)}
