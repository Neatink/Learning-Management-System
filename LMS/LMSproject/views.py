from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class HomeView(ListView):
    template_name = 'home.html'
    model = Course
    context_object_name = 'courses'
    

class CoursesDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail_course.html'
    model = Course
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(course_id = self.kwargs['pk'])
        return context
 

class LessonsDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail_lesson.html'
    model = Lesson
    context_object_name = 'lesson'
    

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
        return reverse_lazy("profile_view", kwargs={"pk": self.request.user.pk})
    
    
class ChangeUserPasswordView(PasswordChangeView):
    template_name = "user_change_password.html"
    form_class = PasswordChangeForm
    
    def get_success_url(self):
        return reverse_lazy("profile_view", kwargs={"pk": self.request.user.pk})