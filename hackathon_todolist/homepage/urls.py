from django.urls import path
from . import views

urlpatterns = [
    # path('homepage/', views.showList),
    path('', views.showList, name='homepage'),

]