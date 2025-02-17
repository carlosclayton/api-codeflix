import uuid
from dataclasses import dataclass
from unicodedata import category

from src.core.category.application.exceptions import InvalidCategoryData, CategoryNotFound
from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository



@dataclass
class ListCategoryResponse:
    categories: [Category]


class ListCategory:
    def __init__(self, repository: CategoryRepository):
        self._repository = repository

    def execute(self) ->  ListCategoryResponse:

        categories = self._repository.list()

        if not categories:
            raise CategoryNotFound("Category not found")

        return ListCategoryResponse(categories=categories)

