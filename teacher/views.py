from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .forms import CourseForm
from .models import Course

# from .forms import 

# Create your views here.
@login_required
def filter_courses(request, slug):
    courses = Course.objects.filter(slug = slug)
    context = {
        "courses": courses,
    }
    
    return render(request, 'teacher/filtered_course.html', context)

@login_required
def course_detail(request, slug):
    course = Course.objects.get(slug = slug)
    course.save()
    context = {
        'course': course
    }
    return render(request, 'course/course_details.html', context)

@login_required
def create_course(request):
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("course:filter_courses")
    else:
        form = CourseForm()
        
    context = {
        'form': form
    }
    return render(request, 'course/course_form.html', context) 
    
@login_required
def update_course(request, slug):
    course = Course.objects.get(slug = slug)
    form = CourseForm(instance = course)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance = course)
        if form.is_valid():
            form.save()
            return redirect('course:filter_courses')
    context = {
        'form': form
    }
    
    return render(request, 'course/course_form.html', context)       

@login_required
def delete_course(request, slug):
    course = Course.objects.get(slug = slug)
    course.delete()
    return redirect('course:filter_courses')