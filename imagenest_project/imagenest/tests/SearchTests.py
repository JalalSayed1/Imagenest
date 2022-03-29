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
