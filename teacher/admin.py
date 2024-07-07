from django.contrib import admin

# Register your models here.
from .models import Course, MultipleChoiceQuestion, QuizResult

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["owner", "course_title", "created_on"]
    list_display_links = list_display
    
@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ['course', 'question']
    list_display_links = list_display
    
@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['owner', 'score', 'course_title']
    list_display_links = list_display