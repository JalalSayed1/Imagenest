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
         'username': 'john12',
         'password': 'fRz4FqXN'},
        {'firstname': 'Kate',
         'surname': 'Smith',
         'username': 'ksmith',
         'password': '6qzH6ZkP'},
        {'firstname': 'Lisa',
         'surname': 'Owen',
         'username': 'liow123',
         'password': 'MyP@$$W0rd'},
        {'firstname': 'Joe',
         'surname': 'Doe',
         'username': 'jdjdjd',
         'password': 'XkNcPN9w'},
        {'firstname': 'Xinyu',
         'surname': 'Hu',
         'username': 'this_is_hu',
         'password': 'zxcvbnm'},
        {'firstname': 'Nakago',
         'surname': 'Mirakasa',
         'username': 'na1mi2',
         'password': 'jFL39asM'},
        ]

    # images to store on the database
    images = [
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

    # add each user to database
    for user in users:
        add_user_and_profile(user['firstname'], user['surname'], user['username'], user['password'])

    # add each image to database
    for image in images:
        add_image(image['url'], image['username'], image['likers'], image['caption'])
    


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
        user.firstname = firstname
        user.surname = surname
        

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
    populate()

