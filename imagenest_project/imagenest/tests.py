from django.test import TestCase
from django.urls import reverse, resolve
from imagenest.forms import *
import os
from imagenest.models import UserProfile, Image, Like, User

class SearchTests(TestCase):

    def test_search_form_exists(self):
        import imagenest.forms
        self.assertTrue('SearchForm' in dir(imagenest.forms), "The SearchForm class could not be found in forms.py")

    def test_search_form_linked_to_User(self):
        search_form = SearchForm()
        self.assertEqual(type(search_form.__dict__['instance']), User, "The search form is not correctly linked to the User model.")
    
    def test_search_uses_template(self):
        response = self.client.get(reverse('imagenest:search'))
        self.assertTemplateUsed(response, 'imagenest/search.html', "The search.html template is not used for the search() view}")
        
class uploadTests(TestCase):
    def test_upload_form_exists(self):
        import imagenest.forms
        self.assertTrue('ImageUploadForm' in dir(imagenest.forms), "The ImageUploadForm class could not be found in forms.py")
        
    def test_upload_uses_template(self):
        response = self.client.get(reverse('imagenest:upload'))
        self.assertTemplateUsed(response, 'imagenest/upload.html', "The upload.html template is not used for the add_picture() view}")
        
    def test_upload(self):
        #how to test that a file/url has been uploaded?