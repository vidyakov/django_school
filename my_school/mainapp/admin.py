from django.contrib import admin

from .models import Tag, Course


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = list_display


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = 'name', 'price'
    list_display_links = list_display
