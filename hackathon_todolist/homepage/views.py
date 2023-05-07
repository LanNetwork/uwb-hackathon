from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
from .forms import TaskForm

import os

absolute_path = os.path.dirname(__file__)
list_relative_path = 'templates\\task_list.html'
create_relative_path = 'templates\\task_create.html'
list_full_path = os.path.join(absolute_path, list_relative_path)
create_full_path = os.path.join(absolute_path, create_relative_path)

def showList(request):
    tasks = Task.objects.all()
    return HttpResponse(tasks)

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    template_name = create_full_path

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = list_full_path

    def get_queryset(self):
        return (
            Task.objects.filter(userOwner=self.request.user)
        )