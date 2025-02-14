import uuid
from dataclasses import dataclass
from unicodedata import category

from src.core.category.application.exceptions import InvalidCategoryData, CategoryNotFound
from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository


@dataclass
class GetCategoryRequest:
    id: uuid.UUID


@dataclass
class GetCategoryResponse:
    id: uuid.UUID
    name: str
    description: str
    is_active: bool


class GetCategory:
    def __init__(self, repository: CategoryRepository):
        self._repository = repository

    def execute(self, request: GetCategoryRequest) ->  GetCategoryResponse:

        category = self._repository.get(id = request.id)

        if not category:
            raise CategoryNotFound("Category not found")

        return GetCategoryResponse(
            id = category.id,
            name = category.name,
            description = category.description,
            is_active = category.is_active
        )
