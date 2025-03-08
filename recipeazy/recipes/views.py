from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from .models import Recipe, Rating
from .forms import RecipeForm, RatingForm
from django.db.models import Q

def recipe_list(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        return render(request, 'recipes/my_recipe_list.html', {'recipes': recipes})

def rate_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            rating, created = Rating.objects.update_or_create(
                recipe=recipe,
                user=request.user,
                defaults={'stars': form.cleaned_data['stars']}
            )
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RatingForm()
    return render(request, 'recipes/rate_recipe.html', {'form': form, 'recipe': recipe})

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
    recipes = Recipe.objects.filter(
                Q(title__icontains=query) | 
                Q(category__name__icontains=query)
            ).distinct() 
    ingredients = []
    for recipe in recipes:
        ingredients.append(recipe.ingredients)
    return render(request,"recipes/recipe_list.html",{
        "recipes":recipes,
        "ingredients":ingredients
    })

def rate_recipe(request,recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == 'POST':
        form = RatingForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RatingForm(instance=recipe)
    return render(request, 'recipes/rate_recipe.html', {'form': form, 'recipe': recipe})