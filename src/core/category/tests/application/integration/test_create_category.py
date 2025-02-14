from unittest.mock import MagicMock

import pytest
import uuid

from src.core.category.application.create_category import CreateCategory, CreateCategoryRequest, CreateCategoryResponse
from src.core.category.application.exceptions import InvalidCategoryData
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository


class TestCreateCategory:
    def test_create_category_with_valid_data(self):

        repository = InmemoryCategoryRepository()
        use_case = CreateCategory(repository=repository)

        request = CreateCategoryRequest(
            name="Category 1",
            description="description",
            is_active=True
        )

        response = use_case.execute(request=request)
        assert isinstance(response.id, uuid.UUID)

        assert response.id is not None
        assert len(repository.categories) == 1

        assert repository.categories[0].name == "Category 1"
        assert repository.categories[0].description == "description"
        assert repository.categories[0].is_active is True


    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="Name is required"):
            repository = InmemoryCategoryRepository()
            use_case = CreateCategory(repository=repository)

            request = CreateCategoryRequest(
                name="",
                description="description",
                is_active=True
            )



            response = use_case.execute(request=request)

            assert response is None
            assert len(repository.categories) == 0


