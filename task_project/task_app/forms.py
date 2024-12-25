# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, Task

class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_number', 'address', 'password1', 'password2']

class TaskForm(forms.ModelForm):
    name = forms.CharField(max_length=30)
    class Meta:
        model = Task
        fields = ['name', 'assigned_to', 'due_date', 'status']
