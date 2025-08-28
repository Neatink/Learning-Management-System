from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']
        

class AnswerForTaskForm(forms.ModelForm):
    class Meta:
        model = AnswerForTask
        fields = ['answer']
        labels = {
            'answer': "Ваша відповідь:"
            }
        

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description']
        labels = {
            'name': 'Назва',
            'description': 'Опис'
        }
        widgets = {
            'name': forms.TextInput(attrs = {'autofocus': True, 'placeholder': 'Назва курса..'}),
            'description': forms.Textarea(attrs = {'placeholder': 'Опис курса..'})
        }


class LessonForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset = Course.objects.all(), empty_label = None, label = 'Курс')
    class Meta:
        model = Lesson
        fields = ['course', 'name', 'image', 'video']
        labels = {
            'name': 'Назва',
            'image': 'Фотографія до уроку',
            'video': 'Відео до уроку',
        }
        widgets = {
            'name': forms.TextInput(attrs={'autofocus': True, 'placeholder': 'Назва уроку..'})
        }