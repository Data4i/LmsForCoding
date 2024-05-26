from django.contrib import admin

# Register your models here.
from .models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["author_name", "course_title", "created_on"]
    list_display_links = list_display