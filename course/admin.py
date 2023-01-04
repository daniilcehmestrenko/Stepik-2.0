from django.contrib import admin

from .models import Course, Module, Subject, Image, Question, Text, Video


class ImageInLine(admin.StackedInline):
    model = Image


class TextInLine(admin.StackedInline):
    model = Text


class VideoInLine(admin.StackedInline):
    model = Video

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['name', 'module']


@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'course']
    inlines = (ImageInLine, TextInLine, VideoInLine)


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
