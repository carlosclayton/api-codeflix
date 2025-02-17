import uuid
from dataclasses import dataclass


from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.domain.category import Category
from src.core.category.application.category_repository import CategoryRepository


@dataclass
class UpdateCategoryRequest:
    id: uuid.UUID
    category: Category



@dataclass
class UpdateCategoryResponse:
    id: uuid.UUID
    name: str
    description: str
    is_active: bool


class UpdateCategory:
    def __init__(self, repository: CategoryRepository):
        self._repository = repository

    def execute(self, request: UpdateCategoryRequest) ->  UpdateCategoryResponse:

        category = self._repository.update(id = request.id, category = request.category)

        if not category:
            raise CategoryNotFound("Category not found")

        return UpdateCategoryResponse(
            id = request.id,
            name = category.name,
            description = category.description,
            is_active = category.is_active
        )
