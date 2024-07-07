from django.contrib import admin

# Register your models here.
<<<<<<< HEAD
from .models import Course, MultipleChoiceQuestion, QuizResult
=======
from .models import Course
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ["owner", "course_title", "created_on"]
<<<<<<< HEAD
    list_display_links = list_display
    
@admin.register(MultipleChoiceQuestion)
class MultipleChoiceQuestionAdmin(admin.ModelAdmin):
    list_display = ['course', 'question']
    list_display_links = list_display
    
@admin.register(QuizResult)
class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['owner', 'score', 'course_title']
=======
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820
    list_display_links = list_display