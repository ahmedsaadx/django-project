from django.contrib.auth.forms import UserCreationForm, UserChangeForm ,AuthenticationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
        ) 
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = fields = fields = (
            "username",
            "first_name",
             "last_name",
            "email",
            "phone",
        ) 
class LoginForm(AuthenticationForm):
    Email = forms.CharField(label='Email ')        