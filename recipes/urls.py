from django.urls import path
from recipes.views import index

urlpatterns = [
    path('', index, name='home'),
]