from django.test import TestCase
from imagenest.models import UserProfile, Image

class PopulationScriptTests(TestCase):

    def test_population_script_exists(self):
        try:
            import populate_imagenest
        except ImportError:
            raise ImportError("Cannot import the populate_imagenest file")
        
        if 'populate' not in dir(populate_imagenest):
            raise NameError("The populate() function does not exist in the populate_imagenest module.")
        populate_imagenest.populate()

    def test_users_exist(self):
        #num_of_users = len(UserProfile.objects.filter())
        #self.assertEquals(num_of_users, 6, f"Expected 6 users to be created. Instead {num_of_users} were.".format(num_of_users=num_of_users))
        self.userJohn = UserProfile.objects.get(username="john1")
        self.userKate = UserProfile.objects.get(username="ksmith")
        self.userLisa = UserProfile.objects.get(username="liow123")
        self.userJoe = UserProfile.objects.get(username="jdjd")
        self.userHu = UserProfile.objects.get(username="this_is_hu")
        self.userNakago = UserProfile.objects.get(username="na1mi2")

