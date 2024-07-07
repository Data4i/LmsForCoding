from django.urls import path

from . import views 

urlpatterns = [
    path('create', views.create_course, name = 'create_course'),
    path('some_view', views.some_view, name = 'some_view'),
    path('update/<str:course_title>/', views.update_course, name = 'update_course'),
    path('course_detail/<str:slug>/', views.course_detail, name='course_detail'),
    path('course_assessment/<str:course_title>/', views.course_assessment, name='course_assessment'),
    path('filter_courses/<str:slug>/', views.filter_courses, name = 'filter_courses'),
    path("specific_course_details/<str:course_title>/", views.get_specific_details, name="specific_course_details"),
<<<<<<< HEAD
    path('delete_course/<str:course_title>', views.delete_course, name = 'delete_course'),
    
    path('course/<str:course_title>/create_question/', views.create_question, name='create_question'),
    path('course/<str:course_title>/quiz_records/', views.get_quiz_records, name='quiz_records')
=======
    path('delete_course/<str:course_title>', views.delete_course, name = 'delete_course')
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820
]
