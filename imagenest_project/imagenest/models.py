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

# Image model for every image in the app except the profile image: 
class Image(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    # image = models.ImageField(upload_to ='uploads/')
    url = models.URLField(max_length=200)
    likers = models.ManyToManyField(User, default=None, blank=True, related_name='Likers')
    likes = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.username)
    
    @property
    def num_likes(self):
        return int(self.likers.all().count())
    
    @property
    def liker_usernames(self):
        return [username for username in self.likers.all()]
    


# Like choices to toggle between like and unlike an image:
LIKE_CHOICES = (('Like', 'Like'), ('Unlike', 'Unlike'),)
# Like model for every image in the app except the profile image:
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return self.image
#upload class
class upload(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profile_images", blank=True) #not sure where to upload to yet
    """
    user_uploading = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0) #setting likes to 0 when uploading
    likers = models.ManyToManyField(UserProfile)
    caption = models.CharField(max_length=128)
    
    class Meta:
        verbose_name_plural = 'upload'
    """