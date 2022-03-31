from django.urls import reverse, resolve
from imagenest.views import profile
from imagenst.models import Image, User
from django.test import Client, TestCase

class TopImagesViewTests(TestCase):

    def setup(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        login = self.client.login(username="testuser", password="testpass")
        self.top_images_url = reverse("top_images")

    def test_status_code(self):
        response = self.client.get(self.top_images_url)
        self.assertEquals(response.status_code, 200)

    def test_top_images_template(self):
        response = self.client.get(self.top_images_url)
        self.assertTemplateUsed(response, "imagenest/menu_pages_template.html")

    def test_url_resolves_view(self):
        view = resolve(self.top_images_url)
        self.assertEquals(view.func, top_images)

    def test_no_more_than_ten_images(self):
        user = User.objects.all()[0]
        add_image(user, 'https://images.unsplash.com/photo-1624965085151-0710f6b3f284', 3)
        add_image(user, 'https://images.unsplash.com/photo-1572091574819-ea8bb5394b1d', 4)
        add_image(user, 'https://images.unsplash.com/photo-1640622660721-45b83554ab05', 1)
        add_image(user, 'https://images.unsplash.com/photo-1647471641611-908659d7b366', 2)
        add_image(user, 'https://images.unsplash.com/photo-1647514422086-18cde746fa26', 6)
        add_image(user, 'https://images.unsplash.com/photo-1647363542902-9b76666d88b3', 8)
        add_image(user, 'https://images.unsplash.com/photo-1647482290110-df9a2895cb95', 10)
        add_image(user, 'https://images.unsplash.com/photo-1640622299541-8c8ab8a098f3', 4)
        add_image(user, 'https://i.picsum.photos/id/1003/1181/1772.jpg?hmac=oN9fHMXiqe9Zq2RM6XT-RVZkojgPnECWwyEF1RvvTZk', 7)
        add_image(user, 'https://i.picsum.photos/id/1015/6000/4000.jpg?hmac=aHjb0fRa1t14DTIEBcoC12c5rAXOSwnVlaA5ujxPQ0I', 8)
        add_image(user, 'https://i.picsum.photos/id/1020/4288/2848.jpg?hmac=Jo3ofatg0fee3HGOliAIIkcg4KGXC8UOTO1dm5qIIPc', 12)

        response = self.client.get(self.top_images_url)
        self.assertEquals(len(response.context["images"]), 10)

    def test_like_ordering(self):
        user = User.objects.all()[0]
        add_image(user, 'https://images.unsplash.com/photo-1624965085151-0710f6b3f284', 3)
        add_image(user, 'https://images.unsplash.com/photo-1572091574819-ea8bb5394b1d', 1)
        add_image(user, 'https://images.unsplash.com/photo-1640622660721-45b83554ab05', 4)
        response = self.client.get(self.profile_url)

        #first at bottom, third at top
        first_image = response.content.decode().find("https://images.unsplash.com/photo-1572091574819-ea8bb5394b1d")
        second_image = response.content.decode().find("https://images.unsplash.com/photo-1624965085151-0710f6b3f284")
        third_image = response.content.decode().find("https://images.unsplash.com/photo-1640622660721-45b83554ab05")

        self.assertTrue(first_image < second_image < third_image)
            
def add_image(user, image_url, likes):
    image = Image.objects.get_or_create(username=user, url=image_url, likes=likes)[0]
    image.save()
    return image
