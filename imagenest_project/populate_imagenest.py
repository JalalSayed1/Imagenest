import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
'imagenest_project.settings')

import django
django.setup()
from imagenest.forms import *
from imagenest.models import *

def populate():
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

    posts = [
        {'picture':'https://images.unsplash.com/photo-1624965085151-0710f6b3f284',
         'likes':3,
         'username':'john1',
         'likers': ['ksmith', 'na1mi2', 'jdjd']},
        {'picture':'https://images.unsplash.com/photo-1572091574819-ea8bb5394b1d',
         'likes':1,
         'username':'john1',
         'likers': ['jdjd']},
        {'picture':'https://images.unsplash.com/photo-1640622660721-45b83554ab05',
         'likes':0,
         'username':'ksmith',
         'likers': []},
        {'picture':'https://images.unsplash.com/photo-1647471641611-908659d7b366',
         'likes':5,
         'username':'ksmith',
         'likers': ['john1','liow123','jdjd','this_is_hu','na1mi2']},
        {'picture':'https://images.unsplash.com/photo-1647514422086-18cde746fa26',
         'likes':2,
         'username':'john1',
         'likers': ['jdjd','this_is_hu']},
        {'picture':'https://images.unsplash.com/photo-1647363542902-9b76666d88b3',
         'likes':3,
         'username':'this_is_hu',
         'likers': ['jdjd','this_is_hu']},
        {'picture':'https://images.unsplash.com/photo-1647482290110-df9a2895cb95',
         'likes':4,
         'username':'ksmith',
         'likers': ['na1mi2','this_is_hu']},
        {'picture':'https://images.unsplash.com/photo-1640622299541-8c8ab8a098f3',
         'likes':1,
         'username':'liow123',
         'likers': ['this_is_hu']}
        ]

    for u in users:
        add_user_and_profile(u['firstname'],u['surname'],u['username'],u['password'])

    for p in posts:
        add_post(p['picture'],p['likes'],p['username'],p['likers'])

    for u in User.objects.all():
        for s in u.owner.all():
            print(f'- {u.username}: {s.url}; likers: {s.liker_usernames}')

def add_user_and_profile(firstname, surname, username, password):
    try:
        # if the user already exists, do not create again
        u = User.objects.get(username=username)
    except User.DoesNotExist:
        # create the user
        f = RegisterForm({'firstname':firstname, 'surname':surname,
                        'username':username, 'password': password,
                        'confirm_password': password})
        u = f.save(commit=False)
        u.set_password(password)
        u.save()
    up = UserProfile.objects.get_or_create(user=u, firstname=firstname, surname=surname, username=username)[0]
    u.firstname=firstname
    up.firstname=firstname
    u.surname=surname
    up.surname=surname
    u.password=password
    up.password=password
    u.save()
    up.save()
    return u

def add_post(picture,likes, username,likers):
    u = User.objects.get(username=username)

    try:
        s = Image.objects.get(url=picture)
    except:
        s = Image.objects.create(username=u)

    s.url=picture
    s.likes=likes

    for liker in likers:
        lu = User.objects.get(username=liker)
        s.likers.add(lu)
        l = Like.objects.get_or_create(user=lu, image=s, value=LIKE_CHOICES[0])[0]
        l.save()

    s.save()


if __name__ == '__main__':
    print('Starting Imagenest population script...')
    populate()
