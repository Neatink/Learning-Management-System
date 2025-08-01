from django.contrib import admin
from django.urls import path
from LMSproject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='homeview')
]
