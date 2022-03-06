from django.shortcuts import render, redirect
from django.http import HttpRequest
from imagenest import views
from .forms import LoginForm, RegisterForm


def login(request):
    login_form = LoginForm()

    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            # save the data to the database:
            login_form.save(commit=True)
            return redirect("/home")

    return render(request, "imagenest/login.html", {"login_form": login_form})


def register(request):
    register_form = RegisterForm()

    if request.method == "POST":
        register_form = register_form(request.POST)
        if register_form.is_valid():
            # save the data to the database:
            register_form.save(commit=True)

    return render(request, "imagenest/register.html", {"register_form": register_form})
