# this file can be put inside models.py but put it separate make the project tidier
from django import forms
from django.contrib.auth.models import User

# from imagenest.models import Category, Page, UserProfile


class LoginForm(forms.ModelForm):

    username = forms.CharField(
        #! could make max_length not hard coded: eg. Category.NAME_MAX_LENGTH
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Password"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )


class RegisterForm(forms.ModelForm):

    firstname = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "First name"}),
    )
    surname = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Surename"}),
    )
    username = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"placeholder": "Username"}),
    )

    class Meta:
        model = User
        fields = (
            "firstname",
            "surname",
            "username",
            "password",
        )
