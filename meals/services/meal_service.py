from typing import Dict, Any

from repository.models.meal import Meal
from repository.repository import Repository
from meals.services.product_service import ProductService


class MealService:

    def __init__(self):
        self.repository = Repository(Meal)

    def meal_list(self, parameters: Dict[str, Any]):
        return self.repository.list(parameters)

    def create_meal(self, parameters: Dict[str, Any], user=None):
        meal_parameters = {
            'category_id': parameters['category'],
            'name': parameters['name'],
            # 'owner': user
        }

        meal = self.repository.create(meal_parameters)

        product_service = ProductService()
        for product_id in parameters.get('products', []):
            meal.products.add(product_service.get_product({'id': product_id}))
        return meal

    def delete_meal(self, parameters: Dict[str, Any]):
        meal_id = parameters.pop('id')
        self.repository.delete(meal_id)

    def update_meal(self, parameters: Dict[str, Any]):
        meal_id = parameters.pop('id')
        self.repository.update(meal_id, parameters)

    def get_meal(self, parameters: Dict[str, Any]):
        meal_id = parameters.pop('id')
        return self.repository.read({'id': meal_id})
