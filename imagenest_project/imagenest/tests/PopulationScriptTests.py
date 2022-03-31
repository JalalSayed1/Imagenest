from django.test import TestCase
from imagenest.models import UserProfile, Image, Like
from django.contrib.auth.models import User

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

        expectedUserData = [{'firstname': 'John', 'surname': 'Clark', 'username': 'john12', 'password': 'fRz4FqXN'},
                            {'firstname': 'Kate', 'surname': 'Smith', 'username': 'ksmith', 'password': '6qzH6ZkP'},
                            {'firstname': 'Lisa', 'surname': 'Owen', 'username': 'liow123', 'password': 'MyP@$$W0rd'},
                            {'firstname': 'Joe', 'surname': 'Doe', 'username': 'jdjdjd', 'password': 'XkNcPN9w'},
                            {'firstname': 'Xinyu', 'surname': 'Hu', 'username': 'this_is_hu', 'password': 'zxcvbnm'},
                            {'firstname': 'Nakago', 'surname': 'Mirakasa', 'username': 'na1mi2', 'password': 'jFL39asM'}, ]
        
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

        expectedImageData = [
            {'url':'https://images.unsplash.com/photo-1506953823976-52e1fdc0149a?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8YmVhY2h8ZW58MHx8MHx8&auto=format&fit=crop&w=600&q=60',
            'username':'john12',
            'likers': ['ksmith', 'na1mi2', 'jdjdjd'],
            'caption': 'beach picture'},
            {'url':'https://media.istockphoto.com/photos/stairway-in-the-modern-house-picture-id180898431?k=20&m=180898431&s=612x612&w=0&h=sGZfXkHC0sNaCqWK3jEugtkvRRekFAtwqiCX3m7cWaA=',
            'username':'john12',
            'likers': ['jdjdjd'],
            'caption': 'staircase picture'},
            {'url':'https://media.istockphoto.com/photos/mother-and-daughter-planting-flowers-in-garden-picture-id1310289685?b=1&k=20&m=1310289685&s=170667a&w=0&h=awgQaam_0pIb6zQajnnJxcQjRoayckR5rrCPr1vopmU=',
            'username':'ksmith',
            'likers': [],
            'caption': 'family picture'},
            {'url':'https://media.istockphoto.com/photos/cherry-blossom-picture-id1297835513?b=1&k=20&m=1297835513&s=170667a&w=0&h=Buazol-go5ErQbU7BFG04SZCgMyYiDjZ58uadIvPZ7k=',
            'username':'ksmith',
            'likers': ['john12','liow123','jdjdjd','this_is_hu','na1mi2'],
            'caption': 'flower picture'},
            {'url':'https://media.istockphoto.com/photos/chef-preparing-vegan-tacos-picture-id1241878649?k=20&m=1241878649&s=612x612&w=0&h=T0Iuh5OnRj7p0hdYpoVnRmsR09thoJNoW8lbUoQAlcg=',
            'username':'john12',
            'likers': ['jdjdjd','this_is_hu'],
            'caption': 'food picture'},
            {'url':'https://media.istockphoto.com/photos/wooden-tables-and-chairs-of-an-open-air-chinese-traditional-tea-house-picture-id1273316830?k=20&m=1273316830&s=612x612&w=0&h=316H3aSTq1tnhQ4b_8RlgNionS7LTklCXhkuKnBpGgc=',
            'username':'this_is_hu',
            'likers': ['jdjdjd','this_is_hu', 'liow123'],
            'caption': 'table picture'},
            {'url':'https://media.istockphoto.com/photos/oceanus-in-the-trevi-fountain-of-rome-picture-id1314485873?k=20&m=1314485873&s=612x612&w=0&h=4UaBXYOrVwgSlz_2CDeEqTb97CCEKaaVKC53GtxUtmY=',
            'username':'ksmith',
            'likers': ['na1mi2','this_is_hu', 'liow123', 'jdjdjd'],
            'caption': 'statue picture'},
            {'url':'https://media.istockphoto.com/photos/blank-canvas-on-easel-in-empty-apartment-picture-id1297597669?k=20&m=1297597669&s=612x612&w=0&h=DELcS9RVbHoReLrunYe_nd6FZ2WCY2S8l_m0jshbs1w=',
            'username':'liow123',
            'likers': ['this_is_hu'],
            'caption': 'blank canvas picture'}
            ]
        
        for expectedImage in expectedImageData:
            caption = expectedImage['caption']
            url = expectedImage['picture']
            likes = expectedImage['likes']
            user = expectedImage['username']
            users_who_liked = expectedImage['likers']
            self.check_image_details(caption, url, likes, user, users_who_liked)


    def check_image_details(self, expected_caption, expected_url, expected_likes, expected_username, expected_users_who_liked):
        image = Image.objects.get(url=expected_url)

        self.assertEquals(image.username.username, expected_username, "The {caption} should have been uploaded by '{expected}'. Instead it was uploaded by '{actual}'.".format(
            caption=expected_caption, expected=expected_username, actual=image.username.username))
        
        self.assertEquals(image.likes, expected_likes, "The {caption} should have {expected} likes. Instead it has {actual} likes.".format(
            caption=expected_caption, expected=expected_likes, actual=image.likes))

        self.assertEquals(image.likes, expected_likes, "The {caption} should have the caption '{expected}'. Instead the caption is '{actual}'.".format(
            caption=expected_caption, expected=expected_caption, actual=image.caption))

        actual_likers = []
        for username in expected_users_who_liked:
            try:
                user = User.objects.get(username=username)
                like_relationship = Like.objects.get(user=user, image=image)
            except Like.DoesNotExist:
                raise AssertionError("{user} should have liked the {caption}.")