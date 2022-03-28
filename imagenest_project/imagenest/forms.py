# this file can be put inside models.py but put it separate make the project tidier
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Submission

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
        fields = ["username", "password",]


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
            attrs={"placeholder": "Surname", "class": "form-control"}
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

    class Meta:
        model = User
        fields = [
            "firstname",
            "surname",
            "username",
            "password",
            "confirm_password" ]
        
class ImageUploadForm(forms.ModelForm):
    image_url = forms.URLField(widget=forms.TextInput(attrs={"placeholder": "Image URL"}), required=False)
    image_file = forms.ImageField(required=False)
    image_caption = forms.CharField(widget=forms.Textarea(attrs={"placeholder": "Caption", "maxlength": "200"}))

    # add a class to each visible field in this form (styling): 
    def __init__(self, *args, **kwargs):
        super(ImageUploadForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Submission
        fields = ['image_url', 'image_file', 'image_caption']

class SearchForm(forms.ModelForm):
    username = forms.CharField(max_length=128, 
                               widget=forms.TextInput(attrs={"placeholder": "Username", "class": "form-control"}), )

    class Meta:
        model = User
        fields = ["username"]