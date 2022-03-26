from http import HTTPStatus

from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.http import (require_GET, require_http_methods, require_POST, require_safe)
from django.http import HttpResponseRedirect

from imagenest import views

from .forms import ImageUploadForm, LoginForm, RegisterForm, SearchForm
from .models import Image, Like, Submission


@csrf_protect
def login(request):
    
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    return redirect(home)
            else:
                # todo: add error message
                print('invalid login details')
                return render(request, "imagenest/login.html", {"login_form": login_form, "error": f"Invalid login details: {username}, {password}"})
            
        else:
            # todo: add error message
            print('invalid info') 
            print(login_form.errors)
                
    
    login_form = LoginForm()
    return render(request, "imagenest/login.html", {"login_form": login_form})


def register(request):
    # to tell the template whether the registration was successful:
    # registered = False

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)
            password = request.POST.get('password')
            user.set_password(password)
            user.save()
            
            return redirect(login)
        else:
            # todo: add error message
            print('invalid info')
            return render(request, "imagenest/register.html", {"register_form": register_form})

    
    register_form = RegisterForm()
    # "registered": registered
    return render(request, "imagenest/register.html", {"register_form": register_form})


def logout(request):
    auth.logout(request)
    return redirect(login)


@login_required
def profile(request, user):
    try:
        profile = User.objects.get(username=user)
        #profile_image = profile.profile_image
        images = Image.objects.all().filter(username=profile).order_by("-creation_time")
        error = None
    except User.DoesNotExist:
        profile = None
        images = None
        error = "Error: User does not exist"
    profile_image = {"url":"https://source.unsplash.com/250x250?person", "username" :"username1", 'id' : 8}

    context_dict = {
        "images" : images,
        "profile" : profile,
        "profile_image" : profile_image,
        "error" : error,
        }
    return render(request, "imagenest/profile.html", context_dict)


@login_required
def top_images(request):
    #order_by seems to work now, there was a discrepency with likes and likers which
    #is now fixed
    images = Image.objects.all().order_by("-likes")[:10]

    context = {'images' : images,}

    return render(request, "imagenest/top_images.html",  context)

@login_required
def search(request):
    # set up the context_dict with default values
    context_dict = {"form": SearchForm(), "searchHasBeenUsed": False, "userIsFound": False, "areSimilarUsers": False, "results":[]}

    # if a value for the username has been defined
    if request.method == "GET" and request.GET.get("username"):
        context_dict["searchHasBeenUsed"] = True
        searched_username = request.GET.get("username") # store username request

        try: 
            # check if the searched username corresponds to a User object
            user_found = User.objects.get(username=searched_username)
            context_dict['userIsFound'] = True  # if so update the context_dict
            context_dict['results'] = user_found.username

        except User.DoesNotExist:
            # if an error is thrown and the username does not correspond to a User object
            context_dict['userIsFound'] = False  # update context_dict
            suggested_users = suggest_users(searched_username) # find a list of similar registered usernames
            if suggested_users: # add data to context_dict
                context_dict['areSimilarUsers'] = True
                context_dict['results'].extend(suggested_users)

    return render(request, "imagenest/search.html", context_dict)


def suggest_users(username_input):
    #suggests users for the search based on the usernames in the database
    similar_users = set()

    if username_input is not None:
        for counter in range(1, len(username_input)):
            # remove the last letter of the username on each iteration
            shortened_username = username_input[:-counter] 

             # check whether another username starts with the same string
            users_found = User.objects.filter(username__startswith=shortened_username)
            for user in users_found:
                # add each returned to a set to ensure there are no duplicates
                similar_users.add(user.username)

    return list(similar_users) # return the set as a list

@login_required
def add_picture(request):
    
    uploader = request.user
    upload_form = ImageUploadForm()
    context = {'upload_form' : upload_form, "uploader" : uploader}

    if request.method == "POST":
        upload_form = ImageUploadForm(request.POST, request.FILES)
        if upload_form.is_valid():
            upload_form.save(commit=False)
            image_url = upload_form.cleaned_data.get("image_url")
            image_file = upload_form.cleaned_data.get("image_file")
            
            # if user specified both url and file:
            if (len(image_url) > 0) and (image_file is not None):
                context['error_message'] = "Please specify only one way to upload an image."
                
            # if user entered invlaid image url:
            elif (len(image_url) > 0) and (not image_url.endswith(("jpeg", "jpg", "gif", "png", "apng", "svg", "bmp", "webp"))):
                context['error_message'] = "The url is not an image. It must end with jpeg, jpg, gif, png, apng, svg, bmp, or webp."
                
            elif (len(image_url) > 0) or (image_file is not None):
                uploaded_image = Image.objects.create(username=uploader, url=image_url, file=image_file)
                uploaded_image.save()
                return redirect(home)
            
            else:
                context['error_message'] = "Please enter a URL or upload a file then try again."

    return render(request, "imagenest/upload.html", context)


@login_required
def home(request):
    
    images = Image.objects.all().order_by("-creation_time")
    user = request.user

    context = {
        'images': images,
        'user': user
    }
    return render(request, "imagenest/home.html", context)
    


def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_obj = Image.objects.get(id=image_id)
        
        # add/remove user from likers list: 
        if user in image_obj.likers.all():
            image_obj.likers.remove(user)
            image_obj.sub_like

        else:
            image_obj.likers.add(user)
            image_obj.add_like

        # increment/decrement num of likes of this image:
        like, created = Like.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        # like.save()
        image_obj.save()
    
    # redirect to the prev page:
    # eg. user at home page (then clicks like button) -> like_image view -> home page again
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


