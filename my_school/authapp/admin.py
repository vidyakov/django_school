from django.contrib import admin

from .models import SchoolUser


@admin.register(SchoolUser)
class SchoolUserAdmin(admin.ModelAdmin):
    list_display = 'first_name', 'last_name', 'email'
    list_display_links = list_display
