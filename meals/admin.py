from django.contrib import admin

from repository.models.category import Category
from repository.models.meal import Meal
from repository.models.product import Product

admin.site.register(Category)
admin.site.register(Meal)
admin.site.register(Product)
