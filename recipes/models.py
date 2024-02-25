from django.db import models
from users.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
