from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def showList(request):
    return HttpResponse("Hello UWB hackathon!")