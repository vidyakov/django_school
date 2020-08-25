from django.contrib import admin

from .models import AdditionalMaterial, LessonInfo, InteractiveLesson


@admin.register(AdditionalMaterial)
class AdditionalMaterialAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = list_display


@admin.register(LessonInfo)
class LessonInfoAdmin(admin.ModelAdmin):
    list_display = 'name', 'course'
    list_display_links = list_display


@admin.register(InteractiveLesson)
class InteractiveLessonAdmin(admin.ModelAdmin):
    list_display = 'typing_text', 'lesson_info'
    list_display_links = list_display
