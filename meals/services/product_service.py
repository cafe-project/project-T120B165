from typing import Dict, Any

from repository.models.category import Category
from repository.repository import Repository


class ProductService:

    def __init__(self):
        self.repository = Repository(Category)

    def category_list(self, parameters: Dict[str, Any]):
        return self.repository.list(parameters)

    def create_category(self, parameters: Dict[str, Any]):
        self.repository.create(parameters)

    def delete_category(self, parameters: Dict[str, Any]):
        category_id = parameters.pop('id')
        self.repository.delete(category_id)

    def update_category(self, parameters: Dict[str, Any]):
        category_id = parameters.pop('id')
        self.repository.update(category_id, parameters)

    def get_category(self, parameters: Dict[str, Any]):
        category_id = parameters.pop('id')
        return self.repository.read({'id': category_id})
