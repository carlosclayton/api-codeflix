from unittest.mock import MagicMock, create_autospec

import pytest
import uuid

from src.core.category.application.get_category import GetCategory, GetCategoryRequest, GetCategoryResponse
from src.core.category.application.exceptions import InvalidCategoryData, CategoryNotFound
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.application.update_category import UpdateCategory, UpdateCategoryRequest, UpdateCategoryResponse
from src.core.category.domain.category import Category


class TestUpdateCategory:
    def test_update_category_with_valid_data(self):
        category = Category(name="Category 1", description="description", is_active=True)
        category_updated = Category(name="Category 1 Updated", description="description", is_active=False)

        mock_repository = create_autospec(CategoryRepository)
        mock_repository.update.return_value = category_updated
        use_case = UpdateCategory(repository=mock_repository)

        request = UpdateCategoryRequest(
            id=category.id, category=category_updated

        )

        response = use_case.execute(request=request)
        mock_repository.update.assert_called_once_with(id=category.id, category=category_updated)


        assert response == UpdateCategoryResponse(
            id=category.id,
            name=category_updated.name,
            description=category_updated.description,
            is_active=category_updated.is_active
        )






    def test_update_category_with_invalid_data(self):
        with pytest.raises(CategoryNotFound, match="Category not found"):
            category = Category(name="Category 1", description="description", is_active=True)
            category_updated = Category(name="Category 1 Updated", description="description", is_active=False)
            mock_repository = create_autospec(CategoryRepository)
            mock_repository.update.return_value = category_updated
            use_case = UpdateCategory(repository=mock_repository)
            mock_repository.update.side_effect = CategoryNotFound("Category not found")

            request = UpdateCategoryRequest(
                id=uuid.uuid4(), category=category_updated
            )

            use_case.execute(request=request)
