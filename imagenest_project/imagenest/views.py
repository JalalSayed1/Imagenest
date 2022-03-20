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

from .forms import LoginForm, RegisterForm, uploadForm
from .models import UserProfile, Image, Like, Post


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
                print('invalid login details')
                return render(request, "imagenest/login.html", {"login_form": login_form, "error": f"Invalid login details: {username}, {password}"})
            
        else:
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
            
            # auth.login(request, user)
            return redirect(login)
        else:
            print('invalid info')
            return render(request, "imagenest/register.html", {"register_form": register_form})

    
    register_form = RegisterForm()
    # "registered": registered
    return render(request, "imagenest/register.html", {"register_form": register_form})


def logout(request):
    auth.logout(request)
    return redirect(login)


@login_required
def profile(request):
    
    images = Image.objects.filter(username=request.user)
    
    # image1 = {"url":"https://source.unsplash.com/random?places", "username" :"username1", "likes" : 2, "likers" : ["usename11", "usename11"], 'id':4}
    images = {}
    
    profile_image = {"url":"https://source.unsplash.com/250x250?person", "username" :"username1", 'id' : 8}
    
    return render(request, "imagenest/profile.html", {"profile_image" : profile_image, "images" : images })

@login_required
def top_images(request):
    #! this order_by did not work:
    images = Image.objects.all().order_by("-likes")[:10]

    # images contains eg. "image1" : image1
    # where image1 is a dict contains url, username, likes, likers, id
    # images = {}
    # for i in range(len(image_list)):
    #     images['image'+str(i)] = image_list[i]
        
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


@login_required
def home(request):
    images = Image.objects.all()
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
            image_obj.likes -= 1
        else:
            image_obj.likers.add(user)
            image_obj.likes += 1

        # increment/decrement num of likes of this image:
        like, created = Like.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'

        like.save()
        
    return redirect(home)

# @require_POST
# def add_picture(request):
#     # Check if the user is authenticated
#     # Cannot use login_required because we call this in js,
#     # not showing the error for the users
#     if not request.user.is_authenticated:
#         return HttpResponse(status=HTTPStatus.UNAUTHORIZED)

#     form = ImageUploadForm(request.POST, request.FILES)

#     if form.is_valid():
#         # Not done according to the Image Store System paradigm
#         # Surely can be improved
#         model = form.save(commit=False)
#         model.uploader = request.user.userprofile
#         model.save()
#         return HttpResponse(status=HTTPStatus.OK)
#     else:
#         return HttpResponse(status=HTTPStatus.BAD_REQUEST)

    

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

  






    

