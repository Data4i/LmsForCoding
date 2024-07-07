import subprocess
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

from teacher.models import Course, QuizResult


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


def student_take_quiz(request, course_title):
    course = get_object_or_404(Course, course_title=course_title)
    questions = course.questions.all()
    # print(request.user)
    if request.method == 'POST':
        score = 0
        for question in questions:
            selected_answer = request.POST.get(f'question_{question.id}')
            if selected_answer and int(selected_answer) == question.correct_answer:
                score += 1
        
        QuizResult.objects.create(
            owner=request.user,
            course=course,
            score=score,
            course_title=course.course_title
        )
        
        return render(request, 'student/student_quiz_results.html', {'course': course, 'score': score, 'total': questions.count()})
    try:
        quiz_result = get_object_or_404(QuizResult, owner = request.user)
    except Exception as e:
        quiz_result = False
        
    return render(request, 'student/student_take_quiz.html', {'course': course, 'questions': questions, 'quiz_result': quiz_result})

@csrf_exempt
def course_assessment_student(request, course_title):
    course = Course.objects.get(course_title=course_title)
    print(course)
    assessment_answer = course.assessment_answer
    print(assessment_answer)
    
    output = ""
    code = ""
    language = "python"

    if request.method == "POST":
        code = request.POST.get("code", "")
        language = request.POST.get("language", "python")
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
    
    good_answer = False
    if output:
        if str(output).strip() == str(course.assessment_answer).strip():
            good_answer=True
        return render(request, 'student/course_assessment_student.html', {'code': code, 'course': course, 'language': language, 'output': output, 'good_answer':good_answer})
    else:
        return render(request, 'student/course_assessment_student.html', {'course': course, 'language': language, 'output': output})
