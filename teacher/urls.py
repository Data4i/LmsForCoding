from django.urls import path

from . import views 

urlpatterns = [
    path('create', views.create_course, name = 'create_course'),
    path('some_view', views.some_view, name = 'some_view'),
    path('update/<str:course_title>/', views.update_course, name = 'update_course'),
    path('course_detail/<str:slug>/', views.course_detail, name='course_detail'),
    path('filter_courses/<str:slug>/', views.filter_courses, name = 'filter_courses'),
    path('delete_course/<str:course_title>', views.delete_course, name = 'delete_course')
]
