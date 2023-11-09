# In appname/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    teachers = models.ManyToManyField('Teacher')

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField('Student')

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
class Certificate(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    issue_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField()