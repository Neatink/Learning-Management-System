from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from .models import *

class HomeView(ListView):
    template_name = 'home.html'
    model = Course
    context_object_name = 'courses'