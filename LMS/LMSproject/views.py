from django.views.generic import ListView, DetailView, CreateView, UpdateView, View
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect


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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(lesson_id = self.kwargs['pk'])
        return context
    

class RegisterUserView(CreateView):
    template_name = 'register.html'
    form_class = UserRegisterForm
    success_url = '/login'
    

class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profile.html'
    model = User


class ChangeUserDataView(LoginRequiredMixin, UpdateView):
    template_name = "user_change_data.html"
    model = User
    fields = ['username', 'email', 'first_name', 'last_name']
    
    def get_success_url(self):
        return reverse_lazy("profile_view", kwargs={"pk": self.request.user.pk})
    
    
class ChangeUserPasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = "user_change_password.html"
    form_class = PasswordChangeForm
    
    def get_success_url(self):
        return reverse_lazy("profile_view", kwargs={"pk": self.request.user.pk})
    

class TasksDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail_task.html'
    model = Task
    context_object_name = 'task'
    
    
class AnswerForTaskView(LoginRequiredMixin, View):
    
    def get(self, request, *args, **kwargs):
        task = Task.objects.get(id = self.kwargs['pk'])
        AnswerForTask.objects.create(task = task, answer = 'hello', user = self.request.user)
        return HttpResponseRedirect("/home")