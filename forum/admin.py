from django.contrib import admin

# Register your models here.
from .models import Thread, Post

@admin.register(Thread)
class ThreadAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at"]
    list_display_links = list_display


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["thread", "created_at"]
    list_display_links = list_display