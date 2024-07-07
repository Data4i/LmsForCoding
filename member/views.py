from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        pass
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("all_courses")
            # Redirect to a success page.
        else:
            # Return an 'invalid login' error message.
            messages.success(request, "There Was An Error Logging In, Try Again...")
            return redirect("login")
    else:
        return render(request, 'member/authenticate/login.html', context={})


def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out!!")
    return redirect('login')
    
    
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, 'Registration Successfull!')
            return redirect("all_courses")
    else:
        form = UserCreationForm()
            
    return render(request, "member/authenticate/register_user.html", context={'form': form,})