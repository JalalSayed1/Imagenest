import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'imagenest_project.settings')

import django
django.setup()
from imagenest.forms import *
from imagenest.models import *

def populate():
    # users to store on the database:
    users = [
        {'firstname': 'John', 
         'surname': 'Clark',
         'username': 'john1',
         'password': '123456'},
        {'firstname': 'Kate',
         'surname': 'Smith',
         'username': 'ksmith',
         'password': 'I_am_Kate_Smith#123456'},
        {'firstname': 'Lisa',
         'surname': 'Owen',
         'username': 'liow123',
         'password': 'MyP@$$W0rd'},
        {'firstname': 'Joe',
         'surname': 'Doe',
         'username': 'jdjd',
         'password': 'abcdefg'},
        {'firstname': 'Xinyu',
         'surname': 'Hu',
         'username': 'this_is_hu',
         'password': 'zxcvbnm'},
        {'firstname': 'Nakago',
         'surname': 'Mirakasa',
         'username': 'na1mi2',
         'password': 'nothing'},
        ]

    # images to store on the database
    images = [
        {'url':'https://images.unsplash.com/photo-1624965085151-0710f6b3f284',
         'username':'john1',
         'likers': ['ksmith', 'na1mi2', 'jdjd'],
         'caption': 'test'},
        {'url':'https://images.unsplash.com/photo-1572091574819-ea8bb5394b1d',
         'username':'john1',
         'likers': ['jdjd'],
         'caption': 'test'},
        {'url':'https://images.unsplash.com/photo-1640622660721-45b83554ab05',
         'username':'ksmith',
         'likers': [],
         'caption': 'test'},
        {'url':'https://images.unsplash.com/photo-1647471641611-908659d7b366',
         'username':'ksmith',
         'likers': ['john1','liow123','jdjd','this_is_hu','na1mi2'],
         'caption': 'test'},
        {'url':'https://images.unsplash.com/photo-1647514422086-18cde746fa26',
         'username':'john1',
         'likers': ['jdjd','this_is_hu'],
         'caption': 'test'},
        {'url':'https://images.unsplash.com/photo-1647363542902-9b76666d88b3',
         'username':'this_is_hu',
         'likers': ['jdjd','this_is_hu', 'liow123'],
         'caption': 'test'},
        {'url':'https://images.unsplash.com/photo-1647482290110-df9a2895cb95',
         'username':'ksmith',
         'likers': ['na1mi2','this_is_hu', 'liow123', 'jdjd'],
         'caption': 'test'},
        {'url':'https://images.unsplash.com/photo-1640622299541-8c8ab8a098f3',
         'username':'liow123',
         'likers': ['this_is_hu'],
         'caption': 'test'}
        ]

    # add each user to database
    for user in users:
        add_user_and_profile(user['firstname'], user['surname'], user['username'], user['password'])

    # add each image to database
    for image in images:
        add_image(image['url'], image['username'], image['likers'], image['caption'])

    # prints the image details being added to the database
    for user in User.objects.all():
        for image in user.owner.all():
            print(f'- {user.username}: {image.url}; likers: {image.liker_usernames}')
    


def add_user_and_profile(firstname, surname, username, password):
    try:
        # if the user already exists, do not create again
        user = User.objects.get(username=username)

    except User.DoesNotExist:
        # otherwise create the user
        form = RegisterForm({'firstname':firstname, 'surname':surname,
                        'username':username, 'password': password,
                        'confirm_password': password})
        user = form.save(commit=False)
        user.set_password(password)
        user.save()

    # set user's attributes
    user.firstname = firstname
    user.surname = surname
    user.password = password
    user.save()
    
    return user


def add_image(url, username, likers, caption):
    user = User.objects.get(username=username) # find associated User object

    try:
        # if the image already exists, do not create again
        image = Image.objects.get(url=url)
    except:
        # otherwise create the image
        image = Image.objects.create(username=user)

    # set the image attributes
    image.url = url
    image.caption = caption

    # set the users who liked the image
    for liker in likers:
        user_who_liked = User.objects.get(username=liker)
        image.likers.add(user_who_liked)
        like = Like.objects.get_or_create(user=user_who_liked, image=image)[0]
        like.save()

    # save the image
    image.save()


if __name__ == '__main__':
    print('Starting Imagenest population script...')
    populate()

