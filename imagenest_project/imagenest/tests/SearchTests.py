from django.test import TestCase
from django.urls import reverse, resolve
from imagenest.forms import *
import os
from imagenest.models import *
from imagenest.views import *

FULL_REGISTERED_USER = {'firstname': 'John', 
             'surname': 'Smith',
             'username': 'Jsmith',
             'password': 'y36xb9j',
             'confirm_password': 'y36xb9j'}

class SearchTests(TestCase):

    def form_exists(self):
        import imagenest.forms
        self.assertTrue('SearchForm' in dir(imagenest.forms), "The SearchForm class could not be found in forms.py")

    def test_search_form_linked_to_User(self):
        search_form = SearchForm()
        self.assertEqual(type(search_form.__dict__['instance']), User, "The search form is not correctly linked to the User model.")

    def test_empty_form(self):
        search_form = SearchForm(data = {})
        self.assertFalse(search_form.is_valid(), "An empty form should not be valid.")

    def test_form_with_spaces(self):
        form_data = {"username": "test with spaces"}
        search_form = SearchForm(data = form_data)
        self.assertFalse(search_form.is_valid(), "A form with spaces in the username should not be valid.")

    def test_username_is_too_long(self):
        form_data = {"username": "ThisUsernameIsLongerThanAllowed"}
        search_form = SearchForm(data = form_data)
        self.assertFalse(search_form.is_valid())


    def test_shorter_username_context(self):
        create_user()
        request = {'username': 'Jsmi'}
        self.client.login(username='Jsmith', password='y36xb9j')
        response = self.client.get(reverse(search), request, follow=True)
        self.assertFalse(response.context["userIsFound"])
        self.assertTrue(response.context["areSimilarUsers"])

    def test_shorter_username_view(self):
        create_user()
        request = {'username': 'Jsmi'}
        self.client.login(username='Jsmith', password='y36xb9j')
        response = self.client.get(reverse(search), request, follow=True)
        self.assertContains(response, "User not found.")
        self.assertContains(response, "Did you mean:")


    def test_longer_username_context(self):
        create_user()
        request = {'username': 'Jsmith12'}
        self.client.login(username='Jsmith', password='y36xb9j')
        response = self.client.get(reverse(search), request, follow=True)
        self.assertFalse(response.context["userIsFound"])
        self.assertTrue(response.context["areSimilarUsers"])
    
    def test_longer_username_view(self):
        create_user()
        request = {'username': 'Jsmith12'}
        self.client.login(username='Jsmith', password='y36xb9j')
        response = self.client.get(reverse(search), request, follow=True)
        self.assertContains(response, "User not found.")
        self.assertContains(response, "Did you mean:")


    def test_no_similar_users_context(self):
        create_user()
        request = {'username': 'X'}
        self.client.login(username='Jsmith', password='y36xb9j')
        response = self.client.get(reverse(search), request, follow=True)
        self.assertFalse(response.context["userIsFound"])
        self.assertFalse(response.context["areSimilarUsers"])
    
    def test_no_similar_users_view(self):
        create_user()
        request = {'username': 'X'}
        self.client.login(username='Jsmith', password='y36xb9j')
        response = self.client.get(reverse(search), request, follow=True)
        self.assertContains(response, "User not found.")


    def test_correct_username(self):
        create_user()
        request = {'username': 'Jsmith'}
        self.client.login(username='Jsmith', password='y36xb9j')
        response = self.client.get(reverse(search), request, follow=True)
        self.assertContains(response, "Username has been found:")


        
## helper function
def create_user():
    register_form = RegisterForm(FULL_REGISTERED_USER)
    user = register_form.save(commit=False)
    user.set_password("y36xb9j")
    user.save()


