from unittest.mock import MagicMock

import pytest
import uuid

from src.core.category.application.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.application.exceptions import InvalidCategoryData, CategoryNotFound
from src.core.category.application.update_category import UpdateCategory, UpdateCategoryRequest
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository


class TestUpdateCategory:
    def test_update_category_with_valid_data(self):
        category = Category(name="Category 1", description="description", is_active=True)
        category_updated = Category(name="Category 2 - Updated", description="description updated", is_active=False)

        repository = InmemoryCategoryRepository(
            categories=[category]
        )

        use_case = UpdateCategory(repository=repository)

        request = UpdateCategoryRequest(
            id=category.id,
            category=category_updated
        )


        response = use_case.execute(request=request)
        assert response.id == category.id
        assert response.name == category_updated.name
        assert response.description == category_updated.description
        assert response.is_active == category_updated.is_active



    def test_update_category_with_invalid_data(self):
        with pytest.raises(CategoryNotFound, match="Category not found"):
            category = Category(name="Category 1", description="description", is_active=True)
            category_updated = Category(name="Category - Updated", description="description updated", is_active=False)

            repository = InmemoryCategoryRepository(
                categories=[category]
            )

            use_case = UpdateCategory(repository=repository)

            request = UpdateCategoryRequest(
                id=uuid.uuid4(),
                category=category_updated
            )

            use_case.execute(request=request)


