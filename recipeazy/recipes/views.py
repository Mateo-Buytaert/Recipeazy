from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponse
from .models import Recipe
from .forms import RecipeForm, CreateUserForm, UserUpdateForm, ProfileUpdateForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == "GET":
        recipes = Recipe.objects.all()
        return render(request, 'recipes/my_recipe_list.html', {'recipes': recipes})

def recipe_list(request):
    recipes = Recipe.objects.all()
    ingredients = []
    for recipe in recipes:
        ingredients.append(recipe.ingredients)
    return render(request,"recipes/recipe_list.html",{"recipes":recipes, "ingredients":ingredients})


@login_required(login_url="login")
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def recipe_detail(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    ingredients = recipe.ingredients
    ingredients = ingredients.split(", ")
    user = request.user
    return render(request,"recipes/recipe_detail.html",{
        "recipe":recipe,
        "ingredients":ingredients,
        "user":user
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
        "ingredients":ingredients,
    })
def registerPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        form = CreateUserForm()

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get("username")
                messages.success(request, "Account was created for "+user)
                return redirect("login")

        return render(request, "recipes/register.html",{
            "form":form
        })

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("index")
    else:
        if request.method=="POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username,password=password)

            if user is not None:
                login(request,user)
                return redirect("index")
            else:
                messages.info(request,"Username or password is incorrect")

        return render(request,"recipes/login.html")

def logoutUser(request):
    logout(request)
    return redirect("index")

@login_required(login_url="login")
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'recipes/profile.html', context)