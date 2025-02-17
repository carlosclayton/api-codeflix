from unittest.mock import MagicMock, create_autospec

import pytest
import uuid

from src.core.category.application.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.application.exceptions import InvalidCategoryData, CategoryNotFound
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category


class TestGetCategory:
    def test_get_category_with_valid_data(self):
        category = Category(name="Category 1", description="description", is_active=True)
        mock_repository = create_autospec(CategoryRepository)
        mock_repository.get.return_value = category
        use_case = GetCategory(repository=mock_repository)

        request = GetCategoryRequest(
            id=category.id,

        )

        response = use_case.execute(request=request)
        mock_repository.get.assert_called_once_with(id=category.id)
        assert response == GetCategoryResponse(
            id=category.id,
            name=category.name,
            description=category.description,
            is_active=category.is_active
        )

    def test_get_category_with_invalid_data(self):
        with pytest.raises(CategoryNotFound, match="Category not found"):
            category = Category(name="Category 1", description="description", is_active=True)
            mock_repository = create_autospec(CategoryRepository)
            mock_repository.get.return_value = category
            use_case = GetCategory(repository=mock_repository)
            mock_repository.get.side_effect = CategoryNotFound("Category not found")

            request = GetCategoryRequest(
                id=uuid.uuid4()
            )

            use_case.execute(request=request)
