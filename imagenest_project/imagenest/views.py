from http import HTTPStatus
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.http import require_http_methods, require_GET, require_POST, require_safe
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_protect


from imagenest import views
from imagenest.models import Post

from .forms import LoginForm, RegisterForm, uploadForm, ImageUploadForm
from .models import UserProfile, Submission


@csrf_protect
def login(request):
    
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        # to auth user info:
        # login_form = AuthenticationForm(data=request.POST)  # request,

        print('responce4') #!
        if login_form.is_valid():
            print('responce5') #!
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(request, username=username, password=password)
            
            print(user) #!
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    print('responce1') #!
                    return redirect(home)
            else:
                print('invalid login details') #!
                return render(request, "imagenest/login.html", {"login_form": login_form, "error": f"Invalid login details: {username}, {password}"})
            
        else:
            print('invalid info too')  # !
            print(login_form.errors)
            # print(login_form.help_text)
                
    
    print('responce3')
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
            
            # auth.login(request, user)
            return redirect(login)
        else:
            print('invalid info')  # !
            return render(request, "imagenest/register.html", {"register_form": register_form})

    
    register_form = RegisterForm()
    # "registered": registered
    return render(request, "imagenest/register.html", {"register_form": register_form})
    


    # if register_form.is_valid():
    #     if User.objects.filter(username=register_form.cleaned_data['username']).exists():
    #         return render(request, "register.html", {"register_form": register_form, "error": "This username is taken."})

    #     else:
            
    #         if request.method == "POST":
    #             register_form = RegisterForm(request.POST)
    #             if register_form.is_valid():
    #                 user_registered = register_form.save()  # commit=True

    #                 user_registered.set_password(user_registered.password)
    #                 user_registered.save()

    #                 registered = True
    #                 UserProfile.objects.create(user=user_registered)
                    
    #                 return redirect(login)

    #             else:
    #                 # invalid form or forms, mistakes or somthing else?
    #                 print(user_registered.errors, user_registered.errors)
    # else:
    #     # register_form = RegisterForm()
    #     return render(
    #         request,
    #         "imagenest/register.html",
    #         {"register_form": register_form, "registered": registered},
    # )


def logout(request):
    auth.logout(request)
    return redirect(login)

# ! store login info and verify users so the following pages be restricted:
@login_required
def home(request):
    #! how to get info from server and return them as a dict to template?
    image1 = {"url":"https://source.unsplash.com/random?places", "username" :"username1", "likes" : 4, "likers" : ["usename11", "usename11", "usename11", "usename11"], 'id':1}
    image2 = {"url":"https://source.unsplash.com/random?library", "username" :"username2", "likes" : 2, "likers" : ["usename12", "usename12"], 'id':2}
    image3 = {"url":"https://source.unsplash.com/random?cars", "username" :"username3", "likes" : 1, "likers" : ["usename13"], 'id':3}
    
    images = {"image1" : image1, "image2" : image2, "image3" : image3}

    #commented out to ease testing, but this should just be all the functionality for
    #the basic display of the images, not sure if this will have to be changed for the
    #uploaded ones
    #image_list = Post.objects.all().order_by("-date_posted")
    #images = {"images" : image_list}
    
    return render(request, "imagenest/home.html", {"images" : images })

# @login_required
def profile(request):
    
    #line just here to remind me that profile page will almost definitely involve .filter()
    image_list = Post.objects.all().filter()
    
    image1 = {"url":"https://source.unsplash.com/random?places", "username" :"username1", "likes" : 2, "likers" : ["usename11", "usename11"], 'id':4}
    
    images = {"image1" : image1}
    profile_image = {"url":"https://source.unsplash.com/250x250?person", "username" :"username1", 'id' : 8}
    
    return render(request, "imagenest/profile.html", {"profile_image" : profile_image, "images" : images })

# @login_required
def top_images(request):
    image_list = Post.objects.all().order_by("-likes")[:10]

    # images contains eg. "image1" : image1
    # where image1 is a dict contains url, username, likes, likers, id
    images = {}
    for i in range(len(image_list)):
        images['image'+str(i)] = image_list[i]
        
    return render(request, "imagenest/top_images.html",  {"images" : images })

# @login_required
def search(request):
    return render(request, "imagenest/search.html")

    
def upload(request):
    form = uploadForm()
    if request.method == 'POST':
        form = uploadForm(request.POST)
        if form.is_valid():
            #if the upload form is complete, commit it to the database
            form.save(commit=True)
            return redirect('/profile/')
        else:
            print(form.errors)        
    return render(request, "imagenest/upload.html", {'form':form})


@require_POST
def add_picture(request):
    # Check if the user is authenticated
    # Cannot use login_required because we call this in js,
    # not showing the error for the users
    if not request.user.is_authenticated:
        return HttpResponse(status=HTTPStatus.UNAUTHORIZED)

    form = ImageUploadForm(request.POST, request.FILES)

    if form.is_valid():
        # Not done according to the Image Store System paradigm
        # Surely can be improved
        model = form.save(commit=False)
        model.uploader = request.user.userprofile
        model.save()
        return HttpResponse(status=HTTPStatus.OK)
    else:
        return HttpResponse(status=HTTPStatus.BAD_REQUEST)
    
    
    
    

#this is taken from tango w/ django, dk if it actually works here, still needs url
#mapping, html and ajax attached to it, uses the image url cos we have no form of
#image id.
class LikeImage(View):
    @method_decorator(login_required)
    def get(self, request):
        image_id = request.GET['url']

        try:
            image = Post.objects.get(id = image_id)
        except Image.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        image.likes = image.likes + 1
        image.save()

        return HttpResponse(image.likes)

  







    

