from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Login(models.Model):

    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        # super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Login"

    def __str__(self):
        return self.name


class Register(models.Model):
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to="profile_images", blank=True)

    def __str__(self):
        return self.user.username
        
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
    
