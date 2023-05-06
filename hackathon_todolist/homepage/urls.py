from django.urls import path
from . import views

urlpatterns = [
    path('accounts/profile/', views.TaskListView.as_view(), name='homepage'),
]