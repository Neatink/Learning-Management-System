from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

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
    success_url = '/login'
    

class ProfileView(DetailView):
    template_name = 'profile.html'
    model = User


class ChangeUserDataView(UpdateView):
    template_name = "user_change_data.html"
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    
    def get_success_url(self):
        return reverse_lazy("profile_view", kwargs={"pk": self.kwargs["pk"]})