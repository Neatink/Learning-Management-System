from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from .mixins import *
from django.core.paginator import Paginator

class HomeView(ListView):
    template_name = 'home.html'
    model = Course
    context_object_name = 'courses'
    paginate_by = 6
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["last_courses"] = Course.objects.only("id", "name", "create_date").order_by("-create_date")[:12]
        return context

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
    

class TasksDetailView(LoginRequiredMixin, DetailView):
    template_name = 'detail_task.html'
    model = Task
    form_class = AnswerForTaskForm
    
    def get_answer_user(self):
        return AnswerForTask.objects.filter(task_id = self.kwargs['pk'], user_id = self.request.user).first()
    
    def post(self, request, *args, **kwargs):
        if request.user.role == 'Student':
            form = self.form_class(request.POST, instance=self.get_answer_user())
            if form.is_valid():
                form.instance.task = self.get_object()
                form.instance.user = self.request.user
                form.save()
                return redirect('task_detail_view', self.kwargs['pk'])
        
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.role == 'Student':
            context['form'] = self.form_class(instance=self.get_answer_user())
            context['user_grade'] = self.get_answer_user()
        else:
            context['answers'] = AnswerForTask.objects.filter(task_id = self.kwargs['pk'])
        return context
    

class AccessDeniedView(TemplateView):
    template_name = 'denied.html'
    

class AdminMenuView(LoginRequiredMixin, UserIsAdminMixin, TemplateView):
    template_name = 'admin_menu.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['courses'] = Paginator(Course.objects.all(), 8)
        context['lessons'] = Paginator(Lesson.objects.all(), 8)
        context['tasks'] = Paginator(Task.objects.all(), 8)
        
        page_number = self.request.GET.get("page")
        context['courses'] = context['courses'].get_page(page_number)
        context['lessons'] = context['lessons'].get_page(page_number)
        context['tasks'] = context['tasks'].get_page(page_number)

        return {"context": context, "page_obj": context['courses']}

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
    

class CreateLessonView(LoginRequiredMixin, UserIsAdminMixin, CreateView):
    template_name = 'create_lesson.html'
    form_class = LessonForm
    success_url = reverse_lazy('admin_menu_view')


class UpdateLessonView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    template_name = 'update_lesson.html'
    form_class = LessonForm
    model = Lesson
    success_url = reverse_lazy('admin_menu_view')
    

class DeleteLessonView(LoginRequiredMixin, UserIsAdminMixin, DeleteView):
    template_name = 'delete_lesson.html'
    model = Lesson
    success_url = reverse_lazy('admin_menu_view')
    
    
class CreateTaskView(LoginRequiredMixin, UserIsAdminMixin, CreateView):
    template_name = 'create_task.html'
    form_class = TaskForm
    success_url = reverse_lazy('admin_menu_view')


class UpdateTaskView(LoginRequiredMixin, UserIsAdminMixin, UpdateView):
    template_name = 'update_task.html'
    form_class = TaskForm
    model = Task
    success_url = reverse_lazy('admin_menu_view')


class DeleteTaskView(LoginRequiredMixin, UserIsAdminMixin, DeleteView):
    template_name = 'delete_task.html'
    model = Task
    success_url = reverse_lazy('admin_menu_view')
    

class GradeTaskUser(LoginRequiredMixin, UserIsNotStudentMixin, UpdateView):
    template_name = 'grade_task_user.html'
    model = AnswerForTask
    form_class = GradeForm
    success_url = reverse_lazy('admin_menu_view')
    context_object_name = 'answer'
    
    def get_success_url(self):
        return reverse_lazy("task_detail_view", kwargs={"pk": self.object.task.id})
    

class ListCourseView(LoginRequiredMixin, ListView):
    template_name = 'list_courses.html'
    model = Course
    context_object_name = 'courses'
    paginate_by = 32