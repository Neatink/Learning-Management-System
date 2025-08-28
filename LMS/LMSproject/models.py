from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.name


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, blank=False)
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    video = models.FileField(null=True, blank=True, upload_to='videos/')

    def __str__(self):
        return self.name


class User(AbstractUser):
    CHOICES = (
        ('Admin', 'Admin'),
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    role = models.CharField(choices = CHOICES, default = 'Student')
    email = models.EmailField(unique=True)
    username = models.CharField(unique=True, blank=False, null=False)
    

class Task(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    
    def __str__(self):
        return self.name
    
    
class AnswerForTask(models.Model):
    task = models.ForeignKey(Task, on_delete = models.CASCADE)
    answer = models.TextField(null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)