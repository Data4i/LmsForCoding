from django.urls import path
from  . import views

urlpatterns = [
    path("", views.get_courses, name='all_courses'),
    path("all_course_details/<str:course_title>/", views.get_all_course_details, name="all_course_details"),
    path('course_assessment_student/<str:course_title>/', views.course_assessment_student, name='course_assessment_student'),
<<<<<<< HEAD
    path('course/<str:course_title>/student_take_quiz/', views.student_take_quiz, name='student_take_quiz'),
=======
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820
]
