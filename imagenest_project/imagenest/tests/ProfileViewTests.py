from django.urls import reverse, resolve
from imagenest.views import profile
from imagenst.models import Image, User
from django.test import Client, TestCase

class ProfileViewTests(TestCase):

    def setup(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        nonProfileUser = User.objects.create_user(username="nonprofileuser", password="testpass2")
        login = self.client.login(username="testuser", password="testpass")
        self.profile_url = reverse("profile")

    def test_status_code(self):
        response = self.client.get(self.profile_url)
        self.assertEquals(response.status_code, 200, "Client request was unsuccessful")

    def test_profile_template(self):
        response = self.client.get(self.profile_url)
        self.assertTemplateUsed(response, "imagenest/menu_pages_template.html", "Profiles are not linked to the correct template")

    def test_url_resolves_view(self):
        view = resolve(self.profile_url)
        self.assertEquals(view.func, profile, "The profile url is not linked to the correct view")

    def test_urls_contain_user(self):
        user = User.objects.all()[0]
        response = self.client.get(self.profile_url)
        self.assertContains(response, str(user.username), "The profile url does not contain the correct user in it")

    def test_only_user_posts(self):
        user = User.objects.all()[0]
        nonProfileUser = User.objects.all()[1]
        add_image(user, 'https://images.unsplash.com/photo-1647471641611-908659d7b366')
        add_image(nonProfileUser, 'https://images.unsplash.com/photo-1640622299541-8c8ab8a098f3')
        response = self.client.get(self.profile_url) 

        self.assertEquals(len(response.context["images"]), 1, "The profile page is displaying posts from a user other than the profiles user")
        self.assertContains(response, user.username, "The profile page is displaying posts from a user other than the profiles user")

    def test_post_ordering(self):
        user = User.objects.all()[0]
        add_image(user, 'https://images.unsplash.com/photo-1647471641611-908659d7b366')
        add_image(user, 'https://images.unsplash.com/photo-1647482290110-df9a2895cb95')
        response = self.client.get(self.profile_url)

        #first as in it should be at the bottom
        first_image = response.content.decode().find('https://images.unsplash.com/photo-1647471641611-908659d7b366')
        #second as in it should be at the top
        second_image = response.content.decode().find('https://images.unsplash.com/photo-1647482290110-df9a2895cb95')
        
        self.assertTrue(first_image < second_image, "The posts are not being ordered by their creation time correctly")
        
def add_image(user, image_url):
    image = Image.objects.get_or_create(username=user, url=image_url)[0]
    image.save()
    return image
