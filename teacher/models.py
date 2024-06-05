from django.db import models
from django.utils.text import slugify

from django.contrib.auth.models import User

# Create your models here.

class Course(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # author_name = models.CharField(max_length=200, unique=True)
    course_title = models.CharField(max_length=200, verbose_name="Course Title", unique = True)
    slug = models.SlugField(max_length=300, blank=True)
    course_description = models.TextField()
    cover_image = models.ImageField(verbose_name="cover_image", blank=True)
    course_video = models.FileField(upload_to="video/%y")
    course_assessment = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.course_title, self.owner}'
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = 'My Courses'
        ordering = ['-updated_on']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.owner)
            
        return super().save(*args, **kwargs)
    
    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.slug = slugify(self.owner)
    #         # Ensure the slug is unique
    #         unique_slug = self.slug
    #         num = 1
    #         while Course.objects.filter(slug=unique_slug).exists():
    #             unique_slug = f'{self.slug}-{num}'
    #             num += 1
    #         self.slug = unique_slug
    #     super().save(*args, **kwargs)