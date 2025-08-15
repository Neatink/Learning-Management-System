from django.contrib import admin
from django.urls import path
from LMSproject.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home_view'),
    path('course/detail/<pk>', CoursesDetailView.as_view(), name='course_detail'),
    path('register/', RegisterUserView.as_view(), name='register_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login_view'),
    path('profile/<pk>', ProfileView.as_view(), name='profile_view'),
    path('user_change_data/<pk>', ChangeUserDataView.as_view(), name='user_change_data_view'),
    path('user_change_password/', ChangeUserPasswordView.as_view(), name='user_change_password_view'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    path('lesson/detail/<pk>', LessonsDetailView.as_view(), name='lesson_detail'),
    path('task/detail/<pk>', TasksDetailView.as_view(), name='task_detail'),
    path('denied/', AccessDeniedView.as_view(), name='access_denied_view'),
    path('admin-menu/', AdminMenuView.as_view(), name='admin_menu_view'),
    path('course/create', CreateCourseView.as_view(), name='course_create_view'),
    path('course/update/<pk>', UpdateCourseView.as_view(), name='course_update_view'),
]
