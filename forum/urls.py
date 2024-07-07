from django.urls import path
from . import views

urlpatterns = [
    path('create_thread/', views.create_thread, name='create_thread'),
    path('thread_list/', views.thread_list, name='thread_list'),
    path('thread_detail/<int:pk>/', views.thread_detail, name='thread_detail'),
    path('create_post/<int:pk>/', views.create_post, name='create_post'),
]
