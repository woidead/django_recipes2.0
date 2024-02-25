from django.urls import path
from recipes.views import RecipeListView

urlpatterns = [
    path('', RecipeListView.as_view(), name='home'),
]