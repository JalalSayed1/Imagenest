

from django.urls import reverse, resolve
from imagenest.views import home
from imagenest.models import Image, User
from django.test import Client, TestCase


class HomeViewTests(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user(username='usernametest', password='passwordtest')
        login = self.client.login(username='usernametest', password='passwordtest')
        self.home_url = reverse('home')
    
    def test_home_view_status_code(self):
        response = self.client.get(self.home_url)
        self.assertEquals(response.status_code, 200)

    def test_home_view_template(self):
        response = self.client.get(self.home_url)
        self.assertTemplateUsed(response, 'imagenest/menu_pages_template.html')

    def test_home_view_url_resolves_home_view(self):
        view = resolve(self.home_url)
        self.assertEquals(view.func, home)

    def test_home_view_does_not_contain_link_to_logout(self):
        response = self.client.get(self.home_url)
        self.assertNotContains(response, 'href="/logout/"')

    def test_home_view_does_not_contain_link_to_profile(self):
        response = self.client.get(self.home_url)
        self.assertNotContains(response, 'href="/profile/"')
    
    def test_home_view_does_not_contain_link_to_profile(self):
        response = self.client.get(self.home_url)
        self.assertNotContains(response, 'href="/top_images/"')

    def test_home_view_with_no_images(self):
        response = self.client.get(self.home_url)

        self.assertContains(response, "No images uploaded yet.")
        self.assertQuerysetEqual(response.context['images'], [])

    def test_home_view_with_one_image_from_url(self):
        user = User.objects.all()[0]
        add_image_by_url(
            user, "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg")
        response = self.client.get(self.home_url)


        self.assertEquals(len(response.context['images']), 1)
        self.assertContains(response, "https://helpx.adobe.com/content/dam/help/en/photoshop/using/convert-color-image-black-white/jcr_content/main-pars/before_and_after/image-before/Landscape-Color.jpg")
        self.assertContains(response, user.username)

    def test_home_view_with_one_image_from_file(self):
        user = User.objects.all()[0]
        add_image_by_file(user, "./imagenest_project/imagenest/tests/test_images/test_image_1.jpg")
        response = self.client.get(self.home_url)

        self.assertEquals(len(response.context['images']), 1)
        self.assertContains(response, "test_image_1.jpg")
        self.assertContains(response, user.username)

    def test_home_view_with_multiple_images(self):
        user = User.objects.all()[0]
        add_image_by_file(user, "./imagenest_project/imagenest/tests/test_images/test_image_1.jpg")
        add_image_by_file(user, "./imagenest_project/imagenest/tests/test_images/test_image_2.jpg")
        response = self.client.get(self.home_url)
        
        self.assertTrue(len(Image.objects.all()) == 2)
        self.assertEquals(len(response.context['images']), 2)
        self.assertContains(response, "test_image_1.jpg")
        self.assertContains(response, "test_image_2.jpg")
        self.assertContains(response, user.username)
        
    def test_home_view_order_of_multiple_images(self):
        user = User.objects.all()[0]
        add_image_by_file(
            user, "./imagenest_project/imagenest/tests/test_images/test_image_1.jpg")
        add_image_by_file(
            user, "./imagenest_project/imagenest/tests/test_images/test_image_2.jpg")
        response = self.client.get(self.home_url)
        
        image2 = response.content.decode().find("test_image_2.jpg")
        image1 = response.content.decode().find("test_image_1.jpg")
        
        # image 2 should be first:
        self.assertTrue(image2 < image1)

# helper funcs:
def add_image_by_url(uploader, image_url):
    uploaded_image = Image.objects.get_or_create(username=uploader, url=image_url)[0]
    uploaded_image.save()
    return uploaded_image

def add_image_by_file(uploader, image_file):
    uploaded_image = Image.objects.get_or_create(username=uploader, file=image_file)[0]
    uploaded_image.save()
    return uploaded_image
