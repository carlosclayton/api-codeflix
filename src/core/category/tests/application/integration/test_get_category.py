from unittest.mock import MagicMock

import pytest
import uuid

from src.core.category.application.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.application.exceptions import InvalidCategoryData, CategoryNotFound
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository


class TestGetCategory:
    def test_get_category_with_valid_data(self):
        category1 = Category(name="Category 1", description="description", is_active=True)
        category2 = Category(name="Category 2", description="description", is_active=True)

        repository = InmemoryCategoryRepository(
            categories=[category1, category2]
        )

        use_case = GetCategory(repository=repository)

        request = GetCategoryRequest(
            id=category1.id,
        )


        response = use_case.execute(request=request)
        assert isinstance(response.id, uuid.UUID)

        assert response.id == category1.id
        assert response.name == category1.name
        assert response.description == category1.description
        assert response.is_active == category1.is_active
        assert response.id is not None
        assert len(repository.categories) == 2

        assert repository.categories[0].name == "Category 1"
        assert repository.categories[0].description == "description"
        assert repository.categories[0].is_active is True


    def test_get_category_with_invalid_data(self):
        with pytest.raises(CategoryNotFound, match="Category not found"):
            category1 = Category(name="Category 1", description="description", is_active=True)
            category2 = Category(name="Category 2", description="description", is_active=True)

            repository = InmemoryCategoryRepository(
                categories=[category1, category2]
            )

            use_case = GetCategory(repository=repository)

            request = GetCategoryRequest(
                id=uuid.uuid4()
            )

            use_case.execute(request=request)


