from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


USERNAME_MAX_LENGTH = 15
PASSWORD_MAX_LENGTH = 40

# class Login(models.Model):

#     usernamename = models.CharField(
#         max_length=USERNAME_MAX_LENGTH, unique=True)
#     password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    
    # name = models.CharField(max_length=128, unique=True)
    # views = models.IntegerField(default=0)
    # likes = models.IntegerField(default=0)
    # slug = models.SlugField(unique=True)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.name)
        # super(Category, self).save(*args, **kwargs)

    # class Meta:
    #     verbose_name_plural = "Login"

    # def __str__(self):
    #     return self.name


class Register(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # title = models.CharField(max_length=128)
    # url = models.URLField()
    # views = models.IntegerField(default=0)
    
    firstname = models.CharField(max_length=USERNAME_MAX_LENGTH, blank=True)
    surname = models.CharField(max_length=USERNAME_MAX_LENGTH, blank=True)
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH, unique=True)
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH, blank=True)

    # def __str__(self):
    #     return self.title


class UserProfile(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    # website = models.URLField(blank=True)
    # picture = models.ImageField(upload_to="profile_images", blank=True)

    # def __str__(self):
    #     return self.user.username

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=USERNAME_MAX_LENGTH, blank=True)
    surname = models.CharField(max_length=USERNAME_MAX_LENGTH, blank=True)
    username = models.CharField(
        max_length=USERNAME_MAX_LENGTH, unique=True)
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH, blank=True)
        
class upload(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

class Post(models.Model):
    #picture is the url
    picture = models.URLField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    likes = models.IntegerField(default=0)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    #likers
    
    
    class Meta:
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.picture
    
# upload an image:
class Submission(models.Model):
    image = models.ImageField(upload_to='images/')
    uploader = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)

    like_count = models.PositiveIntegerField(default=0)
    likers = models.ManyToManyField(UserProfile, related_name="favorites")

    class Meta:
        ordering = ['-creation_time']
