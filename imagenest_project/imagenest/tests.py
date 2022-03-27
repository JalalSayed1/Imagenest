from django.test import TestCase
from django.urls import reverse, resolve
from imagenest.forms import *
import os
from imagenest.models import UserProfile, Image, Like, User

class SearchTests(TestCase):

    def test_search_form_linked_to_User(self):
        search_form = SearchForm()
        self.assertEqual(type(search_form.__dict__['instance']), User, "The search form is not correctly linked to the User model.")
    
class uploadTests(TestCase):
    
    def test_upload(self):
        #how to test that a file/url has been uploaded?
        
class registerTests(TestCase):
    
    def test_register_uses_template(self):
        response = self.client.get(reverse('imagenest:register'))
        self.assertTemplateUsed(response, 'imagenest/register.html', "The register.html template is not used for the register() view}")

class formsTests(TestCase):
    #LoginForm
    def test_login_form_exists(self):
        import imagenest.forms
        self.assertTrue('LoginForm' in dir(imagenest.forms), "The LoginForm class could not be found in forms.py")

    #RegisterForm
    def test_register_form_exists(self):
        import imagenest.forms
        self.assertTrue('RegisterForm' in dir(imagenest.forms), "The RegisterForm class could not be found in forms.py")
    
    #ImageUploadForm
    def test_upload_form_exists(self):
        import imagenest.forms
        self.assertTrue('ImageUploadForm' in dir(imagenest.forms), "The ImageUploadForm class could not be found in forms.py")
    
    #SearchForm
    def test_search_form_exists(self):
        import imagenest.forms
        self.assertTrue('SearchForm' in dir(imagenest.forms), "The SearchForm class could not be found in forms.py")
    
class templateTests:    
    #home.html
    def test_home_uses_template(self):
        response = self.client.get(reverse('imagenest:home'))
        self.assertTemplateUsed(response, 'imagenest/home.html', "The home.html template is not used for the home() view}")
    
    
    #login.html
    def test_login_uses_template(self):
        response = self.client.get(reverse('imagenest:login'))
        self.assertTemplateUsed(response, 'imagenest/login.html', "The login.html template is not used for the login() view}")
    
    #logout.html
    def test_logout_uses_template(self):
        response = self.client.get(reverse('imagenest:logout'))
        self.assertTemplateUsed(response, 'imagenest/logout.html', "The logout.html template is not used for the logout() view}")
        
    #profile.html
    def test_profile_uses_template(self):
        response = self.client.get(reverse('imagenest:profile'))
        self.assertTemplateUsed(response, 'imagenest/profile.html', "The profile.html template is not used for the profile() view}")
    
    
    #register.html
    def test_register_uses_template(self):
        response = self.client.get(reverse('imagenest:register'))
        self.assertTemplateUsed(response, 'imagenest/register.html', "The register.html template is not used for the register() view}")
    
    #search.html
    def test_search_uses_template(self):
        response = self.client.get(reverse('imagenest:search'))
        self.assertTemplateUsed(response, 'imagenest/search.html', "The search.html template is not used for the search() view}")
    
    #top_images.html
    def test_top_images_uses_template(self):
        response = self.client.get(reverse('imagenest:top_images'))
        self.assertTemplateUsed(response, 'imagenest/top_images.html', "The top_images.html template is not used for the top_images() view}")
        
    #upload.html
    def test_upload_uses_template(self):
        response = self.client.get(reverse('imagenest:add_picture'))
        self.assertTemplateUsed(response, 'imagenest/upload.html', "The upload.html template is not used for the add_picture() view}")
    