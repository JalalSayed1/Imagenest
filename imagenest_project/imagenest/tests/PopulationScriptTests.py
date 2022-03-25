from django.test import TestCase
from imagenest.models import UserProfile, Image, Like, User

class PopulationScriptTests(TestCase):

    def test_population_script_exists(self):
        try:
            import populate_imagenest
        except ImportError:
            raise ImportError("Cannot import the populate_imagenest file")
        
        if 'populate' not in dir(populate_imagenest):
            raise NameError("The populate() function does not exist in the populate_imagenest module.")
        populate_imagenest.populate()

    def test_num_of_users(self):
        import populate_imagenest
        populate_imagenest.populate()
        num_of_users = len(UserProfile.objects.all())
        self.assertEquals(num_of_users, 6, f"Expected 6 users to be created. Instead {num_of_users} were.".format(num_of_users=num_of_users))


    def test_users(self):
        import populate_imagenest
        populate_imagenest.populate()

        expectedUserData = [{'firstname': 'John', 'surname': 'Clark', 'username': 'john1', 'password': '123456'},
                            {'firstname': 'Kate', 'surname': 'Smith', 'username': 'ksmith', 'password': 'I_am_Kate_Smith#123456'},
                            {'firstname': 'Lisa', 'surname': 'Owen', 'username': 'liow123', 'password': 'MyP@$$W0rd'},
                            {'firstname': 'Joe', 'surname': 'Doe', 'username': 'jdjd', 'password': 'abcdefg'},
                            {'firstname': 'Xinyu', 'surname': 'Hu', 'username': 'this_is_hu', 'password': 'zxcvbnm'},
                            {'firstname': 'Nakago', 'surname': 'Mirakasa', 'username': 'na1mi2', 'password': 'nothing'}, ]
        
        for expectedUser in expectedUserData:
            firstname = expectedUser['firstname']
            surname = expectedUser['surname']
            username = expectedUser['username']
            password = expectedUser['password']
            self.check_user_details(firstname, surname, username, password)

    def check_user_details(self, expected_firstname, expected_surname, expected_username, expected_password):
        user = UserProfile.objects.get(username=expected_username)

        self.assertEquals(user.firstname, expected_firstname, "{username}'s firstname should be '{expected}'. Instead it is '{actual}'.".format(
            username=user.username, expected=expected_firstname, actual=user.firstname))

        self.assertEquals(user.surname, expected_surname, "{username}'s surname should be '{expected}'. Instead it is '{actual}'.".format(
            username=user.username, expected=expected_surname, actual=user.surname))

        self.assertEquals(user.password, expected_password, "{username}'s password should be '{expected}'. Instead it is '{actual}'.".format(
            username=user.username, expected=expected_password, actual=user.password))


    def test_images(self):
        import populate_imagenest
        populate_imagenest.populate()

        expectedImageData = [{'description': "beach image", 'picture':'https://images.unsplash.com/photo-1624965085151-0710f6b3f284', 
                              'likes':3, 'username':'john1', 'likers': ['ksmith', 'na1mi2', 'jdjd']},
                             {'description': "staircase image", 'picture':'https://images.unsplash.com/photo-1572091574819-ea8bb5394b1d',
                              'likes':1, 'username':'john1', 'likers': ['jdjd']}, 
                             {'description': "family image", 'picture':'https://images.unsplash.com/photo-1640622660721-45b83554ab05',
                              'likes':0, 'username':'ksmith', 'likers': []},
                             {'description': "flower image", 'picture':'https://images.unsplash.com/photo-1647471641611-908659d7b366',
                              'likes':5, 'username':'ksmith', 'likers': ['john1','liow123','jdjd','this_is_hu','na1mi2']},
                             {'description': "NFT image", 'picture':'https://images.unsplash.com/photo-1647514422086-18cde746fa26',
                              'likes':2, 'username':'john1', 'likers': ['jdjd','this_is_hu']},
                             {'description': "table image", 'picture':'https://images.unsplash.com/photo-1647363542902-9b76666d88b3',
                              'likes':3, 'username':'this_is_hu', 'likers': ['jdjd','this_is_hu']},
                             {'description': "statue image", 'picture':'https://images.unsplash.com/photo-1647482290110-df9a2895cb95',
                              'likes':4, 'username':'ksmith', 'likers': ['na1mi2','this_is_hu']},
                             {'description': "canvas image", 'picture':'https://images.unsplash.com/photo-1640622299541-8c8ab8a098f3',
                              'likes':1, 'username':'liow123', 'likers': ['this_is_hu']}
        ]
        
        for expectedImage in expectedImageData:
            description = expectedImage['description']
            url = expectedImage['picture']
            likes = expectedImage['likes']
            user = expectedImage['username']
            users_who_liked = expectedImage['likers']
            self.check_image_details(description, url, likes, user, users_who_liked)


    def check_image_details(self, description, expected_url, expected_likes, expected_username, expected_users_who_liked):
        image = Image.objects.get(url=expected_url)

        self.assertEquals(image.username.username, expected_username, "The {description} should have been uploaded by '{expected}'. Instead it was uploaded by '{actual}'.".format(
            description=description, expected=expected_username, actual=image.username.username))
        
        self.assertEquals(image.likes, expected_likes, "The {description} should have {expected} likes. Instead it has {actual} likes.".format(
            description=description, expected=expected_likes, actual=image.likes))

        actual_likers = []
        for username in expected_users_who_liked:
            try:
                user = User.objects.get(username=username)
                like_relationship = Like.objects.get(user=user, image=image)
            except Like.DoesNotExist:
                raise AssertionError("{user} should have liked the {description}.")