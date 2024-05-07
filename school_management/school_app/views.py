from django.shortcuts import render
from .models import Class, Homework

def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})

def homework_list(request):
    homeworks = Homework.objects.all()
    return render(request, 'homework_list.html', {'homeworks': homeworks})

def my_view(request):
    if request.method == 'POST':
        # handle POST logic
        pass
    return render(request, 'my_template.html')