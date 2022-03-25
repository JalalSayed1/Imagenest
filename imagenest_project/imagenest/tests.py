from django.test import TestCase
from imagenest.forms import searchForm
from imagenest.models import UserProfile, Image, Like, User

class SearchTests(TestCase):
    ## test empty form
    ## class MyTests(TestCase):
    def test_search_form(self):
        form_data = {'name': ''}
        form = MyForm(data=form_data)
        self.assertTrue(form.is_valid())
