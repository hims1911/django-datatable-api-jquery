from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=200)
    id_val = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class PostDetails(models.Model):
    description = models.CharField(max_length=200)
    post = models.ForeignKey(Post, on_delete= models.CASCADE)

    def __str__(self):
        return self.description

class Format(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

