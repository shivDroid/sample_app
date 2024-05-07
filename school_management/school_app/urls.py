from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.class_list, name='class-list'),
    path('homework/', views.homework_list, name='homework-list'),
]
