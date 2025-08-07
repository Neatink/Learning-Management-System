from django.db import models
from django.contrib.auth.models import AbstractUser

class Course(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)


class Lesson(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    task = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    

class User(AbstractUser):
    CHOICES = (
        ('Admin', 'Admin'),
        ('Student', 'Student'),
        ('Teacher', 'Teacher'),
    )
    role = models.CharField(choices = CHOICES, default = 'Student')
    email = models.EmailField(unique=True)