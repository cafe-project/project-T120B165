from django.db import models

from repository.models.category import Category


class Product(models.Model):
    name = models.CharField(max_length=30)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    calories = models.IntegerField(default=0)
    fats = models.IntegerField(default=0)
    carbs = models.IntegerField(default=0)
    proteins = models.IntegerField(default=0)

