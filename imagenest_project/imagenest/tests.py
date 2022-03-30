from django.test import TestCase
from django.urls import reverse
from imagenest.forms import *
from imagenest.models import *
from imagenest.views import *

FULL_REGISTERED_USER = {'firstname': 'John', 
             'surname': 'Smith',
             'username': 'Jsmith',
             'password': 'y36xb9j',
             'confirm_password': 'y36xb9j'}


class UploadTests(TestCase):

    def test_upload_form_exists(self):
        import imagenest.forms
        self.assertTrue('ImageUploadForm' in dir(imagenest.forms), "The ImageUploadForm class could not be found in forms.py")

    def test_empty_upload_error(self):
        create_user()
        self.client.login(username='Jsmith', password='y36xb9j')

        request = {}
        response = self.client.get(reverse(add_picture), request, follow=True)
        self.assertTemplateUsed(response, 'imagenest/upload.html', "The add_picture() view does not return the original form on error")

    def test_url_upload_error(self):
        create_user()
        self.client.login(username='Jsmith', password='y36xb9j')
        request = {'image_url': 'https://www.google.com/',
                    'image_caption': 'Google'}
        response = self.client.post(reverse(add_picture), request, follow=True)

        self.assertTemplateUsed(response, 'imagenest/upload.html', "The add_picture() view does not return the original form on error")

"""    def test_url_upload_success(self):
        create_user()
        self.client.login(username='Jsmith', password='y36xb9j')
        
        request = {'image_url': 'https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg',
                   'image_caption': 'Landscape'}
        response = self.client.get(reverse(add_picture), request)
        self.assertTrue(Image.objects.filter(url=request['image_url'], caption=request['image_caption']).exists(), "Added an image using URL but no Image object is created")
        self.assertRedirects(response, reverse(home)) """



## helper function
def create_user():
    register_form = RegisterForm(FULL_REGISTERED_USER)
    user = register_form.save(commit=False)
    user.set_password("y36xb9j")
    user.save()