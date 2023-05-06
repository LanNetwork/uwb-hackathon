from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import User, Task
import os

absolute_path = os.path.dirname(__file__)
relative_path = 'templates\\task_list.html'
full_path = os.path.join(absolute_path, relative_path)

def showList(request):
    tasks = Task.objects.all()
    return HttpResponse(tasks)

class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    queryset = Task.objects.all()
    template_name = full_path