import subprocess
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CourseForm, MultipleChoiceQuestionForm
from .models import Course, QuizResult

# Create your views here.
@login_required
def filter_courses(request, slug):
    courses = Course.objects.filter(slug = slug.lower())
    context = {
        "courses": courses,
    }
    
    return render(request, 'teacher/filtered_course.html', context)

@login_required
def course_detail(request, slug):
    course = Course.objects.get(slug = slug.lower())
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
def get_specific_details(request, course_title):
    course = Course.objects.get(course_title = course_title)
    context = {
        "course": course,
    }
    return render(request, 'teacher/specific_course_details.html', context)

@login_required
def some_view(request):
    courses = Course.objects.all()
    return render(request, 'navbar.html', {'courses': courses})

# View to create a multiple-choice question
@login_required
def create_question(request, course_title):
    course = get_object_or_404(Course, course_title=course_title)
    questions = course.questions.all()
    if request.method == 'POST':
        form = MultipleChoiceQuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.course = course
            question.save()
            return redirect('create_question', course_title=course_title)
    else:
        form = MultipleChoiceQuestionForm()
    return render(request, 'teacher/create_question.html', {'form': form, 'course': course, 'questions':questions})


def get_quiz_records(request, course_title):
    # quiz_records = get_object_or_404(QuizResult, course_title = course_title)
    quiz_records = QuizResult.objects.filter(course_title = course_title)
    print(quiz_records)
    
    return render(request, 'teacher/quiz_records.html', {'quiz_records': quiz_records, 'course_title': course_title})
    
    
@csrf_exempt
def course_assessment(request, course_title):
    course = Course.objects.get(course_title=course_title)
    
    output = ""
    code = ""
    language = "python"

    if request.method == "POST":
        code = request.POST.get("code", "")
        language = request.POST.get("language", "python")
        print(code)
        try:
            if language == "python":
                process = subprocess.run(["python3", "-c", code], capture_output=True, text=True, check=True)
            elif language == "javascript":
                process = subprocess.run(["node", "-e", code], capture_output=True, text=True, check=True)
            elif language in ["clike", "c", "c++"]:
                with open("temp.c", "w") as f:
                    f.write(code)
                process = subprocess.run(["gcc", "temp.c", "-o", "temp"], capture_output=True, text=True, check=True)
                if process.returncode == 0:
                    process = subprocess.run(["./temp"], capture_output=True, text=True, check=True)
            elif language == "ruby":
                process = subprocess.run(["ruby", "-e", code], capture_output=True, text=True, check=True)
            elif language == "php":
                process = subprocess.run(["php", "-r", code], capture_output=True, text=True, check=True)
            else:
                output = "Unsupported language!"
                process = None

            if process:
                output = process.stdout + process.stderr
        except subprocess.CalledProcessError as e:
            output = e.stdout + e.stderr
        except Exception as e:
            output = str(e)

    if output:
        return render(request, 'teacher/course_assessment.html', {'code': code, 'course': course, 'language': language, 'output': output})
    else:
        return render(request, 'teacher/course_assessment.html', {'course': course, 'language': language, 'output': output})
