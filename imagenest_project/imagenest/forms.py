# this file can be put inside models.py but put it separate make the project tidier
from django import forms
from django.contrib.auth.models import User

# from imagenest.models import Category, Page, UserProfile


class LoginForm(forms.ModelForm):

    username = forms.CharField(
        #! could make max_length not hard coded: eg. Category.NAME_MAX_LENGTH
        max_length=15,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
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
        widget=forms.TextInput(
            attrs={"placeholder": "First name", "class": "form-control"}
        ),
    )
    surname = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={"placeholder": "Surename", "class": "form-control"}
        ),
    )
    username = forms.CharField(
        max_length=15,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "firstname",
            "surname",
            "username",
            "password",
        )
        
class uploadForm(forms.ModelForm):
    #get username 
    username =
    #image upload
    
    
    #required
    caption = forms.CharField(
        max_length=200,
        widget = forms.TextInput(
            attrs={"placeholder": "Caption", "class": "form-control"}            
        )
    )
    
    #not required
    location = forms.CharField(
        max_length = 25,
        widgit = forms.TextInput(
            attrs={"placeholder": "location", "class": "form-control"}            
        )
    )
