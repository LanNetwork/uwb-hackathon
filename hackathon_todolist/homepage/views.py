from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import User, Task

def showList(request):
    tasks = Task.objects.all()
    return HttpResponse(tasks)

class TaskListView(generic.ListView):
    model = Task
    context_object_name = 'task_list'
    queryset = Task.objects.all()
    template_name = 'D:\Hack\myworld\hackathon_todolist\homepage\\templates\\task_list.html'

