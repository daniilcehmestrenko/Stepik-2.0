from django.contrib import admin

from .models import Course, Module, Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


class ModuleInLine(admin.StackedInline):
    model = Module


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'created_date']
    list_filter = ['created_date', 'subject']
    search_fields = ['name', 'descriptions']
    prepopulated_fields = {'slug': ('name',)}
    inlines = [ModuleInLine]
