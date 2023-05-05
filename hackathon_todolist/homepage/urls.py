from django.urls import path
from . import views

urlpatterns = [
    path('homepage/', views.showList, name='homepage'),
]