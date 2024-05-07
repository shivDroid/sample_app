from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.IntegerField()

class Class(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student, related_name='classes')

class Homework(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateField()
    assigned_class = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='homeworks')
