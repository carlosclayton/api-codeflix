import uuid
from dataclasses import dataclass

from src.core.category.application.invalid_category_data import InvalidCategoryData
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository


@dataclass
class CreateCategoryRequest:
    name: str
    description: str = ""
    is_active: bool = True


@dataclass
class CreateCategoryResponse:
    id: uuid.UUID


class CreateCategory:
    def __init__(self, repository: InmemoryCategoryRepository):
        self._repository = repository

    def execute(self, request: CreateCategoryRequest, response: CreateCategoryResponse):
        try:
            category = Category(name=request.name, description=request.description, is_active=request.is_active)

        except ValueError as e:
            raise InvalidCategoryData(str(e))

        self._repository.add(category)
        response.id = category.id
