from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from imagenest import views
from .forms import LoginForm, RegisterForm, uploadForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from imagenest.models import Post
from django.views import View
from django.utils.decorators import method_decorator


def login(request):
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            #! save the data to the database:
            login_form.save(commit=True)
        # return redirect("/home")
    return render(request, "imagenest/login.html", {"login_form": login_form})


def register(request):
    # to tell the template whether the registration was successful:
    registered = False

    register_form = RegisterForm()

    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_registered = register_form.save()  # commit=True

            user_registered.set_password(user_registered.password)
            user_registered.save()

            registered = True

            return redirect("login")

        else:
            # invalid form or forms, mistakes or somthing else?
            print(user_registered.errors, user_registered.errors)
    else:
        register_form = RegisterForm()

    return render(
        request,
        "imagenest/register.html",
        {"register_form": register_form, "registered": registered},
    )

# ! store login info and verify users so the following pages be restricted:
# @login_required
def home(request):
    #! how to get info from server and return them as a dict to template?
    image1 = {"url":"https://source.unsplash.com/random?places", "username" :"username1", "likes" : 4, "likers" : ["usename11", "usename11", "usename11", "usename11"]}
    image2 = {"url":"https://source.unsplash.com/random?library", "username" :"username2", "likes" : 2, "likers" : ["usename12", "usename12"]}
    image3 = {"url":"https://source.unsplash.com/random?cars", "username" :"username3", "likes" : 1, "likers" : ["usename13"]}
    
    images = {"image1" : image1, "image2" : image2, "image3" : image3}

    #commented out to ease testing, but this should just be all the functionality for
    #the basic display of the images, not sure if this will have to be changed for the
    #uploaded ones
    #image_list = Post.objects.all().order_by("-date_posted")
    #images = {"images" : image_list}
    
    return render(request, "imagenest/home.html", {"images" : images })#{"image1" : image1 }

# @login_required
def profile(request):
    #line just here to remind me that profile page will almost definitely involve .filter()
    image_list = Post.objects.all().filter()
    
    return render(request, "imagenest/profile.html")

# @login_required
def top_images(request):
    image_list = Post.objects.all().order_by("-likes")[:10]
    images = {"images" : image_list}

    return render(request, 'imagenest/top_images.html', context=images)



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

  








    

