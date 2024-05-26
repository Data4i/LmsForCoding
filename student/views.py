from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def get_courses(request):
    return render(request, 'student/home.html')