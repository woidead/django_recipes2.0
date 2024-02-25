from django.urls import path
from recipes.views import RecipeListView, RecipeDetailView, RecipeCreateView

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe_add'),
]