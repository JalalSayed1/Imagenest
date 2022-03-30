from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import password_validation
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from .forms import ImageUploadForm, LoginForm, RegisterForm, SearchForm
from .models import Image


@csrf_protect
def login(request):
    login_form = LoginForm()
    context_dict = {}
    
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        
        if login_form.is_valid():
            ## retrieve values from form
            username = request.POST.get('username')
            password = request.POST.get('password')

            if User.objects.filter(username=username).exists(): # if username is registered

                user = auth.authenticate(request, username=username, password=password)
                if user: # if user is successfully authenticated

                    if user.is_active: # if user is active log them in and redirect to home page
                        auth.login(request, user)
                        return redirect(home)
                    else: # otherwise set an error message to display in template
                        context_dict['error'] = "The account is inactive. Please try a different one." 

                else: # otherwise if password does not match username, set an error message to display in template
                    context_dict['error'] = "Password is incorrect. Please try again."
            
            else: # otherwise if username is not recognised, set an error message to display in template
                context_dict['error'] = "Username not recognised. Please try again."
            
    context_dict["login_form"] = login_form
    return render(request, "imagenest/login.html", context_dict)


## allows a user to create an account and ensures their data is valid
def register(request):
    register_form = RegisterForm()
    context_dict = {"register_form": register_form}

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            ## retieve values from the form
            firstname = request.POST.get('firstname')
            surname =  request.POST.get('surname')
            username = request.POST.get('username')
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            ## if details are invalid, add an error to context_dict to display in the template
            registration_error = validate_registration(firstname, surname, username, password, confirm_password)
            if registration_error:
                context_dict["error"] = registration_error
            
            ## if details are not invalid, save the user and redirect to the login page
            else:
                user = register_form.save(commit=False)
                user.set_password(password)
                user.save()
                return redirect(login)
        
        else:
            context_dict["error"] = list(register_form.errors.values())[0][0]

    return render(request, "imagenest/register.html", context_dict)


## helper function to validate registration
def validate_registration(firstname, surname, username, password, confirm_password):

    ## check firstname and username contain only letters
    print(firstname, surname)
    if not firstname.isalpha():
        return "Firstname must contain only alphabetical characters."
    elif not surname.isalpha():
        return "Surname must contain only alphabetical characters."

    # check username does not contain a space, and is longer than 6 characters
    elif User.objects.filter(username=username).exists():
        return "Username already registered. Please try again."
    elif len(username) < 6:
        return "Username must be at least 6 characters long. Please try again."

    ## check two passwords match, and the password is strong
    if password != confirm_password:
        return "Passwords do not match. Please try again."
    try:
        # test password against django's password validators
        password_validation.validate_password(password)
    except Exception as exception: # if a validator throws a ValidationError
        return list(exception)[0] # return the exception


## logs a user out and redirects them to the homepage
def logout(request):
    auth.logout(request)
    return redirect(login)


## shows the images uploaded by the user, or if the user does not exist an error
@login_required
def profile(request, user):
    try:
        profile = User.objects.get(username=user)
        images = Image.objects.all().filter(username=profile).order_by("-creation_time")
        error = None
    except User.DoesNotExist:
        profile = None
        images = None
        error = "Error: User does not exist"

    context_dict = {
        "images" : images,
        "profile" : profile,
        "error" : error,
        }

    return render(request, "imagenest/profile.html", context_dict)


## shows the top 10 most liked images in order of those with the most likes
@login_required
def top_images(request):
    images = sorted(Image.objects.all()[:10], key=lambda image: image.num_likes, reverse=True)
    return render(request, "imagenest/top_images.html",  {'images' : images,})


## allows user to search for another user using SearchForm, also suggests possible similar usernames
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


## helper function that returns a list similar users from most to least relevant
def suggest_users(username_input):
    similar_users = set()  # use set to avoid duplicated data

    if len(username_input) == 1: # if username is one character
        # add similar users to set
        new_similar_users = find_similar_users(username_input)
        similar_users = similar_users.union(new_similar_users)

    elif username_input is not None: # if username is longer than one character
        for counter in range(1, len(username_input)):
            # remove the last letter of the username on each iteration
            shortened_username = username_input[:-counter]

            # add similar users to set
            new_similar_users = find_similar_users(shortened_username)
            similar_users = similar_users.union(new_similar_users)

    return list(similar_users)[::-1] # return the set as a list in reverse order


## helper function to create set of similar users given shortened username
def find_similar_users(username):
    similar_users = set()
    
    # add each username that starts with the same string to the set
    users_found = User.objects.filter(username__startswith=username)
    for user in users_found:
        similar_users.add(user.username)

    return similar_users


## user can upload a picture using ImageUploadForm as either a url or a picture file
@login_required
def add_picture(request):
    uploader = request.user
    upload_form = ImageUploadForm()
    context = {"uploader" : uploader}

    if request.method == "POST":
        upload_form = ImageUploadForm(request.POST, request.FILES)

        if upload_form.is_valid():
            upload_form.save(commit=False)
            image_url = upload_form.cleaned_data.get("image_url")
            image_file = upload_form.cleaned_data.get("image_file")
            image_caption = upload_form.cleaned_data.get("image_caption")
            
            # if user specified both url and file:
            if (len(image_url) > 0) and (image_file is not None):
                context['error_message'] = "Please specify only one way to upload an image."
                
            # if user entered invalid image url
            elif (len(image_url) > 0) and (not image_url.endswith(("jpeg", "jpg", "gif", "png", "apng", "svg", "bmp", "webp"))):
                context['error_message'] = "The url is not an image. It must end with jpeg, jpg, gif, png, apng, svg, bmp, or webp."
                
            # if image was entered correctly
            elif (len(image_url) > 0) or (image_file is not None):
                uploaded_image = Image.objects.create(username=uploader, url=image_url, file=image_file, caption=image_caption)
                uploaded_image.save()
                return redirect(home)
            
            # if user specified neither url or file
            else:
                context['error_message'] = "Please enter a URL or upload a file then try again."

    context["upload_form"] = upload_form
    return render(request, "imagenest/upload.html", context)


## displays all images registered to a user, in order of decreasing creation time
@login_required
def home(request):    
    images = Image.objects.all().order_by("-creation_time")
    user = request.user
    return render(request, "imagenest/home.html", {'images': images, 'user': user})
    

## like / unlike an image by adding / removing the user from image's list of likers
@login_required
def like_image(request):
    user = request.user
    
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_obj = Image.objects.get(id = image_id)
        
        # add/remove user from likers list: 
        if user in image_obj.likers.all():
            image_obj.likers.remove(user)
        else:
            image_obj.likers.add(user)

        image_obj.save()
    
    # redirect to the prev page:
    # eg. user at home page (then clicks like button) -> like_image view -> home page again
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


