from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Users

class CreateUserForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ['uid','email','password1','password2']

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ['uid','email','password1','password2']