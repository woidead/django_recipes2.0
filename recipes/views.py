from django.shortcuts import render
from django.views.generic.list import ListView, DetailView
from .models import Recipe
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RecipeForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/index.html'


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_detail.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('recipe_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
