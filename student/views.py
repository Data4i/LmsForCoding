from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from teacher.models import Course


# Create your views here.
@login_required
def get_courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'student/home.html', context)

@login_required
def get_all_course_details(request, course_title):
    course = Course.objects.get(course_title = course_title)
    context = {
        "course": course,
    }
    return render(request, 'student/all_course_details.html', context)