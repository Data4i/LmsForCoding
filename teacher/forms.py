from django import forms

from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("course_title", "course_description", "cover_image", "course_video", "course_assessment")
        