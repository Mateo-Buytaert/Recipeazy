from django.db import models
import PIL
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
    
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
    prep_time = models.PositiveIntegerField(help_text="Preparation time in minutes.")
    cook_time = models.PositiveIntegerField(help_text="Cooking time in minutes.")
    servings = models.PositiveIntegerField()
    method = models.TextField(default="")
    image = models.ImageField(upload_to="images/")
    cuisine = models.ManyToManyField(Cuisine)
    category = models.ManyToManyField(Category)
    def __str__(self):
        return self.title

    def average_rating(self):
        return self.ratings.aggregate(models.Avg('stars'))['stars__avg'] or 0

    def total_ratings(self):
        return self.ratings.count()
        
class Rating(models.Model):
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    stars = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    class Meta:
        unique_together = ('recipe', 'user')
    def __str__(self):
        return f"{self.user.username} rated {self.recipe.title} {self.stars} stars"