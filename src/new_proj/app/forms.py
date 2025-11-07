from django import forms
from django.forms.models import formset_factory



class LoginForm(forms.Form):
    username = forms.CharField(
        label = "Username",
        max_length = 80,
        required = True,
    )
    password = forms.CharField(
        label = "Password",
        max_length = 80,
        required = True,
    )