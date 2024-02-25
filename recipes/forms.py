from django.forms import ModelForm
from django import forms
from .models import Recipe

class RecipeForm(ModelForm):
    title = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'form-control', 'placeholder':'Введите название рецепта'
        })
    )
    description = forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'form-control', 'placeholder':'Введите описание рецепта'
        })
    )
    instructions = forms.CharField(
        widget=forms.Textarea(attrs={
            'class':'form-control', 'placeholder':'Введите инструкцию к приготовлению'
        })
    )
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'instructions']
