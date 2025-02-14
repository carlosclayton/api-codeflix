from unittest.mock import MagicMock, create_autospec

import pytest
import uuid

from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category
from src.core.category.application.delete_category import DeleteCategory, DeleteCategoryRequest


class TestDeleteCategory:
    def test_delete_category_with_valid_data(self):
        category = Category(name="Category 1", description="description", is_active=True)
        mock_repository = create_autospec(CategoryRepository)

        use_case = DeleteCategory(repository=mock_repository)

        request = DeleteCategoryRequest(
            id=category.id,
        )

        use_case.execute(request=request)
        mock_repository.delete.assert_called_once_with(id=category.id)

    def test_delete_category_with_invalid_data(self):
        with pytest.raises(CategoryNotFound, match="Category not found"):
            mock_repository = create_autospec(CategoryRepository)

            use_case = DeleteCategory(repository=mock_repository)
            mock_repository.delete.side_effect = CategoryNotFound("Category not found")

            request = DeleteCategoryRequest(
                id=uuid.uuid4()
            )

            use_case.execute(request=request)
