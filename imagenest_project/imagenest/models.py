from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


USERNAME_MAX_LENGTH = 15
PASSWORD_MAX_LENGTH = 40
URL_MAX_LENGTH = 200
CAPTION_MAX_LENGTH = 200


class Image(models.Model):
    url = models.URLField(max_length=URL_MAX_LENGTH, blank=True)
    file = models.ImageField(upload_to='uploaded/', blank=True)
    caption = models.CharField(max_length=CAPTION_MAX_LENGTH)

    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    likers = models.ManyToManyField(User, default=None, blank=True, related_name='Likers')
    creation_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.username}'s image."
    
    @property
    def num_likes(self):
        return int(self.likers.all().count())
    
    @property
    def liker_usernames(self):
        return [username for username in self.likers.all()]
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.image}'s like"
