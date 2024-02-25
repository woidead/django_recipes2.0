from django.forms import ModelForm
from .models import Recipe

class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions']
