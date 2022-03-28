from django.test import TestCase
from django.urls import reverse, resolve
from imagenest.forms import *
import os
from imagenest.models import *
from imagenest.views import *


class SearchTests(TestCase):

    def test_search_form_linked_to_User(self):
        search_form = SearchForm()
        self.assertEqual(type(search_form.__dict__['instance']), User, "The search form is not correctly linked to the User model.")

"""
class uploadTests(TestCase):

    def test_upload(self):
        #how to test that a file/url has been uploaded?
"""

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


class LoginTests(TestCase):

    def setUp(self):
        # Login requires an associated User, so we actually register one using RegisterTests
        RegisterTests.test_register_success(self)

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

class UploadTests(TestCase):

    def setUp(self):
        # Uploading requires an associated User, so we actually register and login
        RegisterTests.test_register_success(self)
        LoginTests.test_login_success(self)

    def test_empty_upload_error(self):
        request = {}
        response = self.client.post(reverse(add_picture), request)

        self.assertTemplateUsed(response, 'imagenest/upload.html', "The add_picture() view does not return the original form on error")

    def test_url_upload_success(self):
        request = {'image_url': 'https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg',
                   'image_caption': 'Landscape'}
        response = self.client.post(reverse(add_picture), request)

        self.assertTrue(Image.objects.filter(url=request['image_url'], caption=request['image_caption']).exists(), "Added an image using URL but no Image object is created")
        self.assertRedirects(response, reverse(home))

    def test_url_upload_error(self):
        request = {'image_url': 'https://www.google.com/',
                   'image_caption': 'Google'}
        response = self.client.post(reverse(add_picture), request)

        self.assertTemplateUsed(response, 'imagenest/upload.html', "The add_picture() view does not return the original form on error")

    
