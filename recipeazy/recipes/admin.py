from django.contrib import admin
from .models import Recipe, Cuisine, Category

# Register your models here.

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'prep_time', 'cook_time', 'servings')
admin.site.register(Cuisine)
admin.site.register(Category)