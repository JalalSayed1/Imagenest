from django.test import TestCase
from django.urls import reverse
from imagenest.forms import *
from imagenest.models import *
from imagenest.views import *

class UploadTests(TestCase):

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