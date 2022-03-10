"""imagenest_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from imagenest import views
from django.urls import include
from django.conf.urls.static import static
from django.conf import settings

# app_name = "imagenest"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.login, name="login"),
    # if we have a specific url to be handled by the app "imagenest", let it do so:
    path("imagenest/", include("imagenest.urls")),
    path("login/", views.login, name="login"),
    path("register/", views.register, name="register"),
    path("home/", views.home, name="home"),
    path("profile/", views.profile, name="profile"),
    path("topimages/", views.top_images, name="top_images"),
    path("search/", views.search, name="search"),
    path("upload/", views.upload, name ="upload"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
