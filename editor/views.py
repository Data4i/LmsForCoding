from django.shortcuts import render
from django.http import JsonResponse
import subprocess

def index(request):
    return render(request, 'editor/index.html')

def execute_code(request):
    if request.method == 'POST':
        code = request.POST.get('code', '')
        language = request.POST.get('language', '')

        if language == 'python':
            try:
                result = subprocess.run(['python3', '-c', code], capture_output=True, text=True, timeout=5)
                output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
        elif language == 'javascript':
            try:
                result = subprocess.run(['node', '-e', code], capture_output=True, text=True, timeout=5)
                output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
        elif language == 'ruby':
            try:
                result = subprocess.run(['ruby', '-e', code], capture_output=True, text=True, timeout=5)
                output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
        elif language == 'htmlmixed':
            output = 'HTML cannot be executed server-side.'
        elif language == 'php':
            try:
                result = subprocess.run(['php', '-r', code], capture_output=True, text=True, timeout=5)
                output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
        elif language == 'c':
            filename = 'temp.c'
            with open(filename, 'w') as f:
                f.write(code)
            try:
                result = subprocess.run(['gcc', filename, '-o', 'temp.out'], capture_output=True, text=True, timeout=10)
                if result.returncode != 0:
                    output = result.stderr
                else:
                    result = subprocess.run(['./temp.out'], capture_output=True, text=True, timeout=5)
                    output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
            finally:
                subprocess.run(['rm', filename, 'temp.out'])
        elif language == 'cpp':
            filename = 'temp.cpp'
            with open(filename, 'w') as f:
                f.write(code)
            try:
                result = subprocess.run(['g++', filename, '-o', 'temp.out'], capture_output=True, text=True, timeout=10)
                if result.returncode != 0:
                    output = result.stderr
                else:
                    result = subprocess.run(['./temp.out'], capture_output=True, text=True, timeout=5)
                    output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
            finally:
                subprocess.run(['rm', filename, 'temp.out'])
        elif language == 'java':
            filename = 'Temp.java'
            with open(filename, 'w') as f:
                f.write(code)
            try:
                result = subprocess.run(['javac', filename], capture_output=True, text=True, timeout=10)
                if result.returncode != 0:
                    output = result.stderr
                else:
                    result = subprocess.run(['java', 'Temp'], capture_output=True, text=True, timeout=5)
                    output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
            finally:
                subprocess.run(['rm', filename, 'Temp.class'])
        elif language == 'csharp':
            filename = 'Temp.cs'
            with open(filename, 'w') as f:
                f.write(code)
            try:
                result = subprocess.run(['mcs', filename], capture_output=True, text=True, timeout=10)
                if result.returncode != 0:
                    output = result.stderr
                else:
                    result = subprocess.run(['mono', 'Temp.exe'], capture_output=True, text=True, timeout=5)
                    output = result.stdout if result.stdout else result.stderr
            except subprocess.TimeoutExpired:
                output = 'Execution timed out.'
            finally:
                subprocess.run(['rm', filename, 'Temp.exe'])
        else:
            output = 'Language not supported.'

        return JsonResponse({'output': output})
