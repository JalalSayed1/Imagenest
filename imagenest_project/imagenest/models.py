from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone


USERNAME_MAX_LENGTH = 15
PASSWORD_MAX_LENGTH = 40


class Register(models.Model):
    firstname = models.CharField(max_length=USERNAME_MAX_LENGTH, blank=True)
    surname = models.CharField(max_length=USERNAME_MAX_LENGTH, blank=True)
    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True)
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH, blank=True)


#class UserProfile(models.Model):
  #  user = models.OneToOneField(User, on_delete=models.CASCADE)
   # username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True)
     
class Image(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    url = models.URLField(max_length=200)
    likers = models.ManyToManyField(User, default=None, blank=True, related_name='Likers')
    likes = models.IntegerField(default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.username)
    
    @property
    def num_likes(self):
        return int(self.likers.all().count())
    
    @property
    def liker_usernames(self):
        return [username for username in self.likers.all()]

    @property
    def add_like(self):
        self.likes += 1

    @property
    def sub_like(self):
        self.likes -= 1
    


# Like choices to toggle between like and unlike an image:
LIKE_CHOICES = (('Like', 'Like'), ('Unlike', 'Unlike'),)
# Like model for every image in the app except the profile image:
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    # value is to like or unlike image:
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return f"{self.image}"
        
#upload class
class Submission(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)

    like_count = models.PositiveIntegerField(default=0)
    likers = models.ManyToManyField(User, related_name="favorites")

    class Meta:
        ordering = ['-creation_time']
