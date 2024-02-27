from django.urls import path
from recipes.views import RecipeListView, RecipeDetailView, RecipeCreateView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    # Главная страница и список рецептов
    path('', RecipeListView.as_view(), name='home'),
    # Индивидуальная страница для каждого рецепта
    path('recipe/<int:pk>/', RecipeDetailView.as_view(), name='recipe_detail'),
    # Добавление нового рецепта
    path('recipe/add/', login_required(RecipeCreateView.as_view()), name='recipe_add'),
]