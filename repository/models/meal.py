from django.contrib.auth.models import User
from django.db import models

from repository.models.category import Category
from repository.models.product import Product


class Meal(models.Model):
    name = models.CharField(max_length=30)

    products = models.ManyToManyField(Product, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    notes = models.TextField(default='')
    describe = models.TextField(default='')
    storage = models.TextField(default='')
    serving = models.TextField(default='')
    expiry = models.IntegerField(default=0)

