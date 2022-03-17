# this file can be put inside models.py but put it separate make the project tidier
from django import forms
from django.contrib.auth.models import User
from .models import Submission
from django.core.exceptions import ValidationError


# from imagenest.models import Category, Page, UserProfile


USERNAME_MAX_LENGTH = 15
PASSWORD_MIN_LENGTH = 6
PASSWORD_MAX_LENGTH = 40

class LoginForm(forms.Form):

    username = forms.CharField(
        label="username",
        max_length=USERNAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    
    password = forms.CharField(
        label="password",
        min_length=PASSWORD_MIN_LENGTH,
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Password", "class": "form-control"}
        ),
    )
    
    # def clean(self):
    #     cleaned_data = super().clean()
    #     username = cleaned_data.get('username')
    #     password = cleaned_data.get('password')
    #     print(username)
    #     print(password)
    #     print(cleaned_data)
    #     # if username and password:
    #     return self.cleaned_data

    class Meta:
        model = User
        fields = (
            "username",
            "password",
        )


class RegisterForm(forms.ModelForm):

    firstname = forms.CharField(
        label="First name",
        max_length=USERNAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={"placeholder": "First name", "class": "form-control"}
        ),
    )
    surname = forms.CharField(
        label="Last name",
        max_length=USERNAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={"placeholder": "Surename", "class": "form-control"}
        ),
    )
    username = forms.CharField(
        label="Username",
        max_length=USERNAME_MAX_LENGTH,
        widget=forms.TextInput(
            attrs={"placeholder": "Username", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        label="New Password",
        min_length=PASSWORD_MIN_LENGTH,
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={"placeholder": "New password", "class": "form-control"}
        ),
    )
    confirm_password = forms.CharField(
        label="Confirm Password",
        min_length=PASSWORD_MIN_LENGTH,
        max_length=PASSWORD_MAX_LENGTH,
        widget=forms.PasswordInput(
            attrs={"placeholder": "Confirm password", "class": "form-control"}
        ),
    )
    
    # validate form data:
    # def clean(self):
    #     super().clean()
    #     if not self.cleaned_data['username'].isalnum():
    #         raise ValidationError(
    #             "Username can only contain letters and numbers.")
    #     if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
    #         raise ValidationError(
    #             "Password and confirm password does not match.")
    #     return self.cleaned_data

    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        firstname = self.cleaned_data['firstname']
        surname = self.cleaned_data['surname']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        
        if commit:
            user.save()
   
        return user

    class Meta:
        model = User
        fields = (
            "firstname",
            "surname",
            "username",
            "password",
            "confirm_password",
        )
        
class uploadForm(forms.ModelForm):
    #get username 
    # username =
    #image upload
    
    
    #required
    caption = forms.CharField(
        max_length=200,
        widget = forms.TextInput(attrs={"placeholder": "Caption", "class": "form-control"})
    )
    
    #not required
    location = forms.CharField(
        max_length = 25, widget = forms.TextInput(attrs={"placeholder": "location", "class": "form-control"})
    )
    
    class Meta:
            model = User
            fields = (
                "username",
                "caption",
                "location",
            )


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['image']
