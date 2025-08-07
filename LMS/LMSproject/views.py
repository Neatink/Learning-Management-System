from django.views.generic import ListView, DetailView, CreateView
from django.shortcuts import render
from .models import *
from .forms import *

class HomeView(ListView):
    template_name = 'home.html'
    model = Course
    context_object_name = 'courses'
    

class CoursesDetailView(DetailView):
    template_name = 'detail_course.html'
    model = Course
    context_object_name = 'course'
    

class RegisterUser(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = '/home'