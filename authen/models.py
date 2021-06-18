from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Movie(models.Model):
    movie_id = models.IntegerField(null=True, blank=True)
    movie_name = models.CharField(max_length=200, null=True)
    movie_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.movie_name

class Customers(models.Model): 
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

