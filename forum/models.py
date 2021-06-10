from django.db import models
from django.conf import settings
from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000, blank = True)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    Comment = models.TextField(max_length=1000)
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)