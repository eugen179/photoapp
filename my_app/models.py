from django.db import models
from django.contrib.auth.models import User

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    
    def _str_(self):
        return self.name

class Photo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/')
    tags = models.ManyToManyField(Tag, related_name='photos')
    likes = models.ManyToManyField(User, related_name='liked_photos', blank=True)
    dislikes = models.ManyToManyField(User, related_name='disliked_photos', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()

    def _str_(self):
        return self.title

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True)

    def _str_(self):
        return self.user.username