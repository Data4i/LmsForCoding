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
<<<<<<< HEAD
    assessment_answer = models.CharField(max_length=512)
=======
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
<<<<<<< HEAD
        return f'{self.course_title}'
=======
        return f'{self.course_title, self.owner}'
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820
    
    class Meta:
        verbose_name = "Course"
        verbose_name_plural = 'My Courses'
        ordering = ['-updated_on']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.owner)
            
        return super().save(*args, **kwargs)
    
<<<<<<< HEAD
    
class MultipleChoiceQuestion(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='questions')
    question = models.CharField(max_length=512)
    answer1 = models.CharField(max_length=512)
    answer2 = models.CharField(max_length=512)
    answer3 = models.CharField(max_length=512)
    answer4 = models.CharField(max_length=512)

    ANSWER_CHOICES = [
        (1, 'Answer 1'),
        (2, 'Answer 2'),
        (3, 'Answer 3'),
        (4, 'Answer 4'),
    ]
    
    correct_answer = models.IntegerField(choices=ANSWER_CHOICES)

    def __str__(self) -> str:
        return self.question

    class Meta:
        verbose_name = "Multiple Choice Question"
        verbose_name_plural = "Multiple Choice Questions"
        ordering = ['id']
    

class QuizResult(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.IntegerField()
    course_title = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'{self.owner.username} - {self.course_title} - {self.score}'
    

=======
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
>>>>>>> dae647efa7a9c5c50c3cece29fe61504727d4820
