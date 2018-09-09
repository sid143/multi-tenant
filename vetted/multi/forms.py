from django import forms
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length = 100)
    password = forms.CharField(max_length= 100, widget = forms.PasswordInput())