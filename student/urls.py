from django.urls import path
from  . import views

urlpatterns = [
    path("", views.get_courses, name='all_courses'),
    path("all_course_details/<str:course_title>/", views.get_all_course_details, name="all_course_details"),
    path('course_assessment_student/<str:course_title>/', views.course_assessment_student, name='course_assessment_student'),
]
