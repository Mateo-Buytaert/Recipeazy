from django import forms
from .models import Recipe, Rating

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time', 'servings', 'ingredients',"method","image", "cuisine", "category"]

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stars']
        widgets = {
            'stars': forms.NumberInput(attrs={'min': 1, 'max': 5, 'type': 'range', 'step': 1}),
        }