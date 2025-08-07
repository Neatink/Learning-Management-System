from django.contrib import admin
from django.urls import path
from LMSproject.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home_view'),
    path('course/detail/<pk>', CoursesDetailView.as_view(), name='course_detail'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('profile/<pk>', ProfileView.as_view(), name='profile_view'),
    path('user_change_data/<pk>', ChangeUserDataView.as_view(), name='user_change_data_view')
]
