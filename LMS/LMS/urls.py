from django.contrib import admin
from django.urls import path
from LMSproject.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='homeview'),
    path('course/detail/<pk>', CoursesDetailView.as_view(), name='coursedetail'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
