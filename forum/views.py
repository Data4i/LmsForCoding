from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Thread, Post
from .forms import ThreadForm, PostForm

@login_required
def thread_list(request):
    threads = Thread.objects.all()
    return render(request, 'forum/thread_list.html', {'threads': threads})

@login_required
def thread_detail(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    print(f"Thread ID: {thread.pk}")
    form = PostForm() 
    return render(request, 'forum/thread_detail.html', {'thread': thread, 'form': form})

@login_required
def create_thread(request):
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thread created successfully!')
            return redirect('thread_list')
    else:
        form = ThreadForm()
    return render(request, 'forum/thread_form.html', {'form': form})

@login_required
def create_post(request, pk):
    thread = get_object_or_404(Thread, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.save()
            messages.success(request, 'Post created successfully!')
            return redirect('thread_detail', pk=pk)
    else:
        form = PostForm()
    return render(request, 'forum/post_form.html', {'form': form, 'thread': thread})
