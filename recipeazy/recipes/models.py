from django.db import models
import PIL
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="images/")
    description = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.user.username} Profile"

class Cuisine(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default="")
    ingredients = models.TextField(default="", help_text="Separate ingredients with commas.")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes.")
    servings = models.PositiveIntegerField()
    method = models.TextField(default="")
    image = models.ImageField(upload_to="images/")
    cuisine = models.ManyToManyField(Cuisine)
    category = models.ManyToManyField(Category)
    options = {"easy":"easy","medium":"medium","hard":"hard","expert":"expert"}
    difficulty = models.CharField(max_length=250, choices = options, default = "easy")
    def __str__(self):
        return self.title

    def average_rating(self):
        return self.ratings.aggregate(models.Avg('stars'))['stars__avg'] or 0

    def total_ratings(self):
        return self.ratings.count()
        
