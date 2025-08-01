from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
from .models import *

class HomeView(ListView):
    template_name = 'home.html'
    model = Course
    context_object_name = 'courses'
    

class CoursesDetailView(DetailView):
    template_name = 'detail_course.html'
    model = Course
    context_object_name = 'course'