from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Task
import os

absolute_path = os.path.dirname(__file__)
relative_path = 'templates\\task_list.html'
full_path = os.path.join(absolute_path, relative_path)

def showList(request):
    tasks = Task.objects.all()
    return HttpResponse(tasks)

class TaskListView(LoginRequiredMixin, generic.ListView):
    model = Task
    context_object_name = 'task_list'
    template_name = full_path

    def get_queryset(self):
        return (
            Task.objects.filter(userOwner=self.request.user)
        )