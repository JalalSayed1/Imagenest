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

class RegisterTests(TestCase):

    def test_register_form_exists(self):
        import imagenest.forms
        self.assertTrue('RegisterForm' in dir(imagenest.forms), "The RegisterForm class could not be found in forms.py")

    def test_register_uses_template(self):
        response = self.client.get(reverse(register))
        self.assertTemplateUsed(response, 'imagenest/register.html', "The register.html template is not used for the register() view")

    def test_register_success(self):
        # delete the user in case it already existed
        try:
            user = User.objects.get(username=TEST_USER['username'])
            user.delete()
        except User.DoesNotExist:
            pass

        response = self.client.post(reverse(register), TEST_USER)
        self.assertRedirects(response, reverse(login))

    def test_register_error(self):
        request = {'username': 'a',
                   'password': '1'}
        response = self.client.post(reverse(register), request)
        self.assertTemplateUsed(response, 'imagenest/register.html', "The register() view does not return the original form on error")
