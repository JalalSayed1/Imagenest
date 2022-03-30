from django.test import TestCase
from django.urls import reverse
from imagenest.forms import *
from imagenest.models import *
from imagenest.views import *
import os

class TemplateTests:

    ## test each template exist

    def test_base_exists(self):
       base_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'base.html'))
       self.assertTrue(base_template_exists, "The base.html template is missing from the templates directory.")
    
    def test_first_page_exists(self):
        first_page_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'first_page.html'))
        self.assertTrue(first_page_template_exists, "The first_page.html template is missing from the templates directory.")
        
    def test_profile_exists(self):
        profile_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'profile.html'))
        self.assertTrue(profile_template_exists, "The profile.html template is missing from the templates directory.")

    def test_home_exists(self):
        home_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'home.html'))
        self.assertTrue(home_template_exists, "The home.html template is missing from the templates directory.")
            
    def test_login_exists(self):
        login_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'login.html'))
        self.assertTrue(login_template_exists, "The login.html template is missing from the templates directory.")

    def test_logout_exists(self):
        logout_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'logout.html'))
        self.assertTrue(logout_template_exists, "The logout.html template is missing from the templates directory.")

    def test_menu_pages_exists(self):
        menu_pages_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'menu_pages_template.html'))
        self.assertTrue(menu_pages_template_exists, "The menu_pages_template.html template is missing from the templates directory.")

    def test_register_exists(self):
        register_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'register.html'))
        self.assertTrue(register_template_exists, "The register.html template is missing from the templates directory.")
            
    def test_search_exists(self):
        search_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'search.html'))
        self.assertTrue(search_template_exists, "The search.html template is missing from the templates directory.")

    def test_images_exists(self):
        top_images_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'top_images.html'))
        self.assertTrue(top_images_template_exists, "The top_images.html template is missing from the templates directory.")

    def test_upload_exists(self):
        upload_template_exists = os.path.isfile(os.path.join(self.imagenest_templates_dir, 'upload.html'))
        self.assertTrue(upload_template_exists, "The upload.html template is missing from the templates directory.")


    ## test each template maps to the correct view
    
    def test_home_uses_template(self):
        response = self.client.get(reverse('imagenest:home'))
        self.assertTemplateUsed(response, 'imagenest/home.html', "The home.html template is not used for the home() view}")

    def test_login_uses_template(self):
        response = self.client.get(reverse('imagenest:login'))
        self.assertTemplateUsed(response, 'imagenest/login.html', "The login.html template is not used for the login() view}")

    def test_logout_uses_template(self):
        response = self.client.get(reverse('imagenest:logout'))
        self.assertTemplateUsed(response, 'imagenest/logout.html', "The logout.html template is not used for the logout() view}")

    def test_profile_uses_template(self):
        response = self.client.get(reverse('imagenest:profile'))
        self.assertTemplateUsed(response, 'imagenest/profile.html', "The profile.html template is not used for the profile() view}")

    def test_register_uses_template(self):
        response = self.client.get(reverse('imagenest:register'))
        self.assertTemplateUsed(response, 'imagenest/register.html', "The register.html template is not used for the register() view}")

    def test_search_uses_template(self):
        response = self.client.get(reverse('imagenest:search'))
        self.assertTemplateUsed(response, 'imagenest/search.html', "The search.html template is not used for the search() view}")

    def test_top_images_uses_template(self):
        response = self.client.get(reverse('imagenest:top_images'))
        self.assertTemplateUsed(response, 'imagenest/top_images.html', "The top_images.html template is not used for the top_images() view}")

    def test_upload_uses_template(self):
        response = self.client.get(reverse('imagenest:add_picture'))
        self.assertTemplateUsed(response, 'imagenest/upload.html', "The upload.html template is not used for the add_picture() view}")