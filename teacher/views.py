from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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
    return render(request, 'teacher/course_details.html', context)

@login_required
def create_course(request):
    # form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.owner = request.user
            course.save()
            messages.success(request, 'Course Creation Successfull!!!')
            return redirect("filter_courses", slug=course.slug)
    else:
        form = CourseForm()
        
    context = {
        'form': form
    }
    return render(request, 'teacher/course_form.html', context) 
    
@login_required
def update_course(request, course_title):
    print(course_title)
    course = Course.objects.get(course_title = course_title)
    form = CourseForm(instance = course)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance = course)
        if form.is_valid():
            form.save()
            return redirect('filter_courses', slug=course.slug)
    context = {
        'form': form
    }
    
    return render(request, 'teacher/course_form.html', context)       

@login_required
def delete_course(request, course_title):
    course = Course.objects.get(course_title = course_title)
    course.delete()
    return redirect('filter_courses', slug=course.slug)

@login_required
def some_view(request):
    courses = Course.objects.all()
    return render(request, 'navbar.html', {'courses': courses})
