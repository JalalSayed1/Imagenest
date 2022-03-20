class PopulationScriptTests(TestCase):
    def set_up_tests(self):
        try:
            import populate_imagenest
        except ImportError:
            raise ImportError("Cannot import the populate_imagenest file")
        
        if 'populate' not in dir(populate_rango):
            raise NameError("The populate() function does not exist in the populate_rango module.")
        
        populate_imagenest.populate()

    def test_users_exist(self):
        num_of_users = len(User.objects.filter())
        assertEquals(num_of_users, 6, f"Expected 6 users to be created. Instead {num_of_users} were.".format(num_of_users=num_of_users))

        try:
            userJohn = User.objects.get(username="john1")
            userKate = User.objects.get(username="ksmith")
            userLisa = User.objects.get(username="liow123")
            userJoe = User.objects.get(username="jdjd")
            userHu = User.objects.get(username="this_is_hu")
            userNakago = User.objects.get(username="na1mi2")

        except UserNotFound:
            return "One of the users is incorrect."


    def test_user_names(self):
        self.assertEqual(userJohn.name, "John", "User john1's name should be John")
        self.assertEqual(userKate.name, "Kate", "User ksmith's name should be Kate")
        self.assertEqual(userLisa.name, "Lisa", "User liow123's name should be Lisa")
        self.assertEqual(userJoe.name, "Joe", "User jdjd's name should be Joe")
        self.assertEqual(userXinyu.name, "Xinyu", "User this_is_hu's name should be Xinyu")
        self.assertEqual(userNakago.name, "Nakago", "User this_is_hu's name should be Nakago")

    def test_user_surname(self):
        self.assertEqual(userJohn.surname, "Clark", "User john1's surname should be Clark")
        self.assertEqual(userKate.surname, "Smith", "User ksmith's surname should be Smith")
        self.assertEqual(userLisa.surname, "Owen", "User liow123's surname should be Owen")
        self.assertEqual(userJoe.surname, "Doe", "User jdjd's surname should be Doe")
        self.assertEqual(userXinyu.surname, "Hu", "User this_is_hu's surname should be Hu")
        self.assertEqual(userNakago.surname, "Mirakasa", "User this_is_hu's surname should be Mirakasa")

    def test_user_password(self):
        self.assertEqual(userJohn.surname, "123456", "User john1's password should be 123456")
        self.assertEqual(userKate.surname, "I_am_Kate_Smith#123456", "User ksmith's password should be I_am_Kate_Smith#123456")
        self.assertEqual(userLisa.surname, "MYP@$$W0rd", "User liow123's password should be MYP@$$W0rd")
        self.assertEqual(userJoe.surname, "abcdefg", "User jdjd's password should be abcdefg")
        self.assertEqual(userXinyu.surname, "zxcvbnm", "User this_is_hu's password should be zxcvbnm")
        self.assertEqual(userNakago.surname, "nothing", "User this_is_hu's password should be nothing")


    def test_user_images(self):
        num_of_uploads = len(Image.objects.filter())
        assertEquals(num_of_uploads, 8, f"Expected 8 images to be registered. Instead {num_of_uploads} were.".format(num_of_uploads=num_of_uploads))

        try:
            johnsBeachImage = Image.objects.get(picture="https://images.unsplash.com/photo-1624965085151-0710f6b3f284")
            johnsStairsImage = Image.objects.get(picture="https://images.unsplash.com/photo-1572091574819-ea8bb5394b1d")
            katesFamilyImage = Image.objects.get(picture="https://images.unsplash.com/photo-1640622660721-45b83554ab05")
            katesFlowerImage = Image.objects.get(picture="https://images.unsplash.com/photo-1647471641611-908659d7b366")
            johnsNFTImage = Image.objects.get(picture="https://images.unsplash.com/photo-1647514422086-18cde746fa26")
            husTableImage = Image.objects.get(picture="https://images.unsplash.com/photo-1647363542902-9b76666d88b3")
            katesStatueImage = Image.objects.get(picture="https://images.unsplash.com/photo-1647482290110-df9a2895cb95',")
            lisaCanvasImage = Image.objects.get(picture="https://images.unsplash.com/photo-1640622299541-8c8ab8a098f3")

        except ImageNotFound:
            return "One of the images is incorrect."

    
    def test_image_uploader(self):
        self.assertEqual(johnsBeachImage.username, "john1", "The image of the beach should have been uploaded by 'john1'")
        self.assertEqual(johnsStairsImage.username, "john1", "The image of the stairs should have been uploaded by 'john1'")
        self.assertEqual(katesFamilyImage.username, "ksmith", "The image of the family should have been uploaded by 'ksmith'")
        self.assertEqual(katesFlowerImage.username, "ksmith", "The image of the flower should have been uploaded by 'ksmith'")
        self.assertEqual(johnsNFTImage.username, "john1", "The image of the NFT should have been uploaded by 'john1'")
        self.assertEqual(husTableImage.username, "this_is_hu", "The image of the table should have been uploaded by 'this_is_hu'")
        self.assertEqual(katesStatueImage.username, "ksmith", "The image of the statue should have been uploaded by 'ksmith'")
        self.assertEqual(lisasCanvasImage.username, "liow123", "The image of the canvas should have been uploaded by 'liow123'")

    def test_image_likes(self):
        self.assertEqual(johnsBeachImage.likes, 3, f"The image of the beach should have 3 likes. Instead it has {num_of_likes}".format(num_of_likes=johnsBeachImage.likes))
        self.assertEqual(johnsStairsImage.likes, 1, f"The image of the stairs should have 1 like. Instead it has {num_of_likes}".format(num_of_likes=johnsStairsImage.likes))
        self.assertEqual(katesFamilyImage.likes, 0, f"The image of the family should have 0 likes. Instead it has {num_of_likes}".format(num_of_likes=katesFamilyImage.likes))
        self.assertEqual(katesFlowerImage.likes, 5, f"The image of the flower should have 5 likes. Instead it has {num_of_likes}".format(num_of_likes=katesFlowerImage.likes))
        self.assertEqual(johnsNFTImage.likes, 2, f"The image of the NFT should have 2 likes. Instead it has {num_of_likes}".format(num_of_likes=johnsNFTImage.likes))
        self.assertEqual(husTableImage.likes, 3, f"The image of the flower should have 3 likes. Instead it has {num_of_likes}".format(num_of_likes=husTableImage.likes))
        self.assertEqual(katesStatueImage.likes, 2, f"The image of the statue should have 4 likes. Instead it has {num_of_likes}".format(num_of_likes=katesStatueImage.likes))
        self.assertEqual(lisasCanvasImage.likes, 1, f"The image of the canvas should have 1 like. Instead it has {num_of_likes}".format(num_of_likes=lisaCanvasImage.likes))

    def test_image_likers(self):
        johnsBeachImagelikers = johnsBeachImage.likers
        johnsBeachImageExpectedLikers = ['ksmith', 'na1mi2', 'jdjd']
        self.assertEqual(johnsBeachImagelikers, johnsBeachImageExpectedLikers)

        johnsStairsImageLikers = johnsStairsImage.likers
        johnsStairsImageExpectedLikers = ['jdjd']
        self.assertEqual(johnsStairsImageLikers, johnsStairsImageExpectedLikers)

        katesFlowerImageLikers = katesFlowerImage.likers
        katesFlowerImageExpectedLikers = []
        self.assertEqual(katesFlowerImageLikers, katesFlowerImageExpectedLikers)

        katesFamilyImageLikers = katesFamilyImage.likers
        katesFamilyImageExpectedLikers = ['john1','liow123','jdjd','this_is_hu','na1mi2']
        self.assertEqual(katesFamilyImageLikers, katesFamilyImageExpectedLikers)

        johnsNFTImageLikers = johnsNFTImage.likers
        johnsNFTImageExpectedLikers = ['jdjd', 'this_is_hu']
        self.assertEqual(johnsNFTImageLikers, johnsNFTImageExpectedLikers)

        husTableImageLikers = husTableImage.likers
        husTableImageExpectedLikers = ['jdjd','this_is_hu']
        self.assertEqual(husTableImageLikers, husTableImageExpectedLikers)

        katesStatueImageLikers = katesStatueImage.likers
        katesStatueImageExpectedLikers = ['na1mi2','this_is_hu']
        self.assertEqual(katesStatueImageLikers, katesStatueImageExpectedLikers)

        lisasCanvasImageLikers = lisasCanvasImage.likers
        lisasCanvasImageExpectedLikers = ['this_is_hu']
        self.assertEqual(lisasCanvasImageLikers, lisasCanvasImageExpectedLikers)