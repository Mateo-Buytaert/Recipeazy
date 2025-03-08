from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("recipe-list", views.recipe_list, name="recipe_list"),
    path("make-recipe", views.recipe_create,name="recipe-create"),
    path("recipe-list/<int:id>", views.recipe_detail,name="recipe-detail"),
    path("search-recipe/", views.search_recipe, name="search-recipe"),
    path('recipe/<int:recipe_id>/rate/', views.rate_recipe, name='rate_recipe'),
]