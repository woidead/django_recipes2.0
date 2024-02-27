from django.contrib import admin
from recipes.models import Recipe, Comment
admin.site.register(Recipe)
admin.site.register(Comment)
