from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .models import Task


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'tasks/task_list.html', {'tasks': tasks})


@login_required
def task_create(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Task.objects.create(user=request.user, title=title, description=description)
        return redirect('task_list')
    return render(request, 'tasks/task_form.html')


@login_required
def task_edit(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    if request.method == 'POST':
        task.title = request.POST['title']
        task.description = request.POST['description']
        task.save()
        return redirect('task_list')
    return render(request, 'tasks/task_form.html', {'task': task})


@login_required
def task_delete(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('task_list')
