from django.test import TestCase
from django.urls import reverse
from imagenest.forms import *
from imagenest.models import *
from imagenest.views import *

TEST_USER = {'firstname': 'First',
             'surname': 'Last',
             'username': 'username',
             'password': '123456',
             'confirm_password': '123456'}

class LoginTests(TestCase):


    def test_login_form_exists(self):
        import imagenest.forms
        self.assertTrue('LoginForm' in dir(imagenest.forms), "The LoginForm class could not be found in forms.py")

    def test_login_uses_template(self):
        response = self.client.get(reverse(login))
        self.assertTemplateUsed(response, 'imagenest/login.html', "The login.html template is not used for the login() view")

    def test_login_success(self):
        request = {'username': TEST_USER['username'],
                   'password': TEST_USER['password']}
        response = self.client.post(reverse(login), request)
        self.assertRedirects(response, reverse(home))

    def test_login_error(self):
        request = {'username': TEST_USER['username'],
                   'password': ''}
        response = self.client.post(reverse(login), request)
        self.assertTemplateUsed(response, 'imagenest/login.html', "The login() view does not return the original form on error")