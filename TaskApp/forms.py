from django import forms
from .models import Task , Blog ,Comment
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

class LoginForm(AuthenticationForm):
    pass 


class SignupForm(UserCreationForm):
    pass



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name','tagline']