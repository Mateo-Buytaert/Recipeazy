from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from .models import Recipe
from .forms import RecipeForm

def recipe_list(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        return render(request, 'recipes/my_recipe_list.html', {'recipes': recipes})

def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.ingredients
    ingredients = ingredients.split(", ")
    return render(request,"recipes/recipe_detail.html",{
        "recipe":recipe,
        "ingredients":ingredients
    })
def search_recipe(request):
    query = request.GET.get("q")
    recipes = Recipe.objects.filter(title__icontains=query)
    ingredients = []
    for recipe in recipes:
        ingredients.append(recipe.ingredients)
    return render(request,"recipes/recipe_list.html",{
        "recipes":recipes,
        "ingredients":ingredients
    })