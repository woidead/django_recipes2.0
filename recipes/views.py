from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Recipe


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/index.html'
