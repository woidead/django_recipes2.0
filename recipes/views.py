from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RecipeForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin


class RecipeListView(ListView):
    model = Recipe
    context_object_name = 'recipes'
    template_name = 'recipes/index.html'


class RecipeDetailView(DetailView):
    model = Recipe
    context_object_name = 'recipe'
    template_name = 'recipes/recipe_detail.html'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = self.get_object()
            comment.author = request.user
            comment.save()
            return redirect('recipe_detail', pk=comment.recipe.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipes/recipe_form.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
