from django.shortcuts import render, redirect
from django.http import HttpRequest
from imagenest import views
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login(request):
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # ? save the data to the database:
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


# @login_required
# def home(request):
#     return render(request, "imagenest/home.html")
