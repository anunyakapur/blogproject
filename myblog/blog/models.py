from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    author = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)


    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    post_anon = models.BooleanField(default=False)
# Create your models here.

