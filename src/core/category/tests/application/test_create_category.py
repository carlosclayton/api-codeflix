from unittest.mock import MagicMock

import pytest
import uuid

from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from src.core.category.application.invalid_category_data import InvalidCategoryData
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        mock_repository = MagicMock(InmemoryCategoryRepository)
        use_case = CreateCategory(repository=mock_repository)

        request = CreateCategoryRequest(
            name="Category 1",
            description="description",
            is_active=True
        )

        response = CreateCategoryResponse(id=uuid.uuid4())

        use_case.execute(request=request, response=response)

        mock_repository.add.called_once_with()
        assert response.id is not None


    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="Name is required"):
            mock_repository = MagicMock(InmemoryCategoryRepository)
            use_case = CreateCategory(repository=mock_repository)

            request = CreateCategoryRequest(
                name="",
                description="description",
                is_active=True
            )

            response = CreateCategoryResponse(id=uuid.uuid4())

            use_case.execute(request=request, response=response)
            mock_repository.add.assert_not_called()
