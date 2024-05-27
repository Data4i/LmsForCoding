# from django.shortcuts import render
# from django.views.decorators.csrf import csrf_exempt
# # Create your views here.
# from django.shortcuts import render

# def code_editor(request):
#     return render(request, 'student/editor.html')


import subprocess
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def code_editor(request):
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
            output = e.output

    return render(request, 'student/editor.html', {'code': code, 'language': language, 'output': output})
