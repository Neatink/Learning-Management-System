from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .mixins import *

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
    success_url = reverse_lazy('login_view')
    

class ProfileView(LoginRequiredMixin, DetailView):
    template_name = 'profile.html'
    model = User


class ChangeUserDataView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
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
    

class TasksDetailView(LoginRequiredMixin, UserIsStudentMixin, DetailView):
    template_name = 'detail_task.html'
    model = Task
    form_class = AnswerForTaskForm
    
    def get_answer_user(self):
        return AnswerForTask.objects.filter(task_id = self.kwargs['pk'], user_id = self.request.user).first()
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_answer_user())
        if form.is_valid():
            form.instance.task = self.get_object()
            form.instance.user = self.request.user
            form.save()
            return redirect('task_detail', self.kwargs['pk'])
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.get_answer_user())
        return context
    

class AccessDeniedView(TemplateView):
    template_name = 'denied.html'
    

class AdminMenuView(LoginRequiredMixin, UserIsAdminMixin, TemplateView):
    template_name = 'admin_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = Course.objects.all()
        context['lessons'] = Lesson.objects.all()
        context['tasks'] = Task.objects.all()
        return context

class CreateCourseView(LoginRequiredMixin, UserIsAdminMixin, CreateView):
    template_name = 'create_course.html'
    form_class = CourseForm
    success_url = reverse_lazy('admin_menu_view')


class UpdateCourseView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    template_name = 'update_course.html'
    form_class = CourseForm
    model = Course
    success_url = reverse_lazy('admin_menu_view')


class DeleteCourseView(LoginRequiredMixin, UserIsAdminMixin, DeleteView):
    model = Course
    template_name = 'delete_course.html'
    success_url = reverse_lazy('admin_menu_view')