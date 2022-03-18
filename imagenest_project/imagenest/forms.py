# this file can be put inside models.py but put it separate make the project tidier
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

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

