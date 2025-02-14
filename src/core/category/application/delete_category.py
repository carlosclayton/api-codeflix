import uuid
from dataclasses import dataclass
from unicodedata import category

from src.core.category.application.exceptions import InvalidCategoryData, CategoryNotFound
from src.core.category.application.category_repository import CategoryRepository


@dataclass
class DeleteCategoryRequest:
    id: uuid.UUID


@dataclass
class DeleteCategoryResponse:
    id: uuid.UUID

class DeleteCategory:
    def __init__(self, repository: CategoryRepository):
        self._repository = repository

    def execute(self, request: DeleteCategoryRequest) ->  DeleteCategoryResponse:

        self._repository.delete(id = request.id)

        if not category:
            raise CategoryNotFound("Category not found")

        return DeleteCategoryResponse(
            id = request.id,

        )
