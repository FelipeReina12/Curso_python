from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    data_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200,unique=True)
    author = models.ForeignKey(to=User(), on_delete=models.CASCADE, )