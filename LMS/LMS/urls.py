from django.contrib import admin
from django.urls import path
from LMSproject.views import *
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('home/', HomeView.as_view(), name='home_view'),
    
    path('profile/<pk>', ProfileView.as_view(), name='profile_view'),    
    
    path('logout/', auth_views.LogoutView.as_view(), name='logout_view'),
    
    path('denied/', AccessDeniedView.as_view(), name='access_denied_view'),
    
    path('admin-menu/', AdminMenuView.as_view(), name='admin_menu_view'),
    
    path('student/grade/<pk>', GradeTaskUser.as_view(), name='student_grade_view'),    
    
    path('register/', RegisterUserView.as_view(), name='register_view'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login_view'),
    
    path('user_change_data/<pk>', ChangeUserDataView.as_view(), name='user_change_data_view'),
    path('user_change_password/', ChangeUserPasswordView.as_view(), name='user_change_password_view'),

    path('course/list/', ListCourseView.as_view(), name='course_list_view'),
    path('course/detail/<pk>', CoursesDetailView.as_view(), name='course_detail_view'),
    path('course/create', CreateCourseView.as_view(), name='course_create_view'),
    path('course/update/<pk>', UpdateCourseView.as_view(), name='course_update_view'),
    path('course/delete/<pk>', DeleteCourseView.as_view(), name='course_delete_view'),
    
    path('lesson/detail/<pk>', LessonsDetailView.as_view(), name='lesson_detail_view'),
    path('lesson/create', CreateLessonView.as_view(), name='lesson_create_view'),
    path('lesson/update/<pk>', UpdateLessonView.as_view(), name='lesson_update_view'),
    path('lesson/delete/<pk>', DeleteLessonView.as_view(), name='lesson_delete_view'),
    
    path('task/detail/<pk>', TasksDetailView.as_view(), name='task_detail_view'),
    path('task/create', CreateTaskView.as_view(), name='task_create_view'),
    path('task/update/<pk>', UpdateTaskView.as_view(), name='task_update_view'),
    path('task/delete/<pk>', DeleteTaskView.as_view(), name='task_delete_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)