from django.db import models
import PIL

class Cuisine(models.Model):
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
    stars = models.PositiveIntegerField(default=0)
    cuisine = models.ManyToManyField(Cuisine)
    def __str__(self):
        return self.title