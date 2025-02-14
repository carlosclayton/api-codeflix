from unittest.mock import MagicMock

import pytest
import uuid

from src.core.category.application.exceptions import  CategoryNotFound
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository
from src.core.category.application.delete_category import DeleteCategory, DeleteCategoryRequest


class TestDeleteCategory:
    def test_delete_category_with_valid_data(self):
        category1 = Category(name="Category 1", description="description", is_active=True)
        category2 = Category(name="Category 2", description="description", is_active=True)

        repository = InmemoryCategoryRepository(
            categories=[category1, category2]
        )

        use_case = DeleteCategory(repository=repository)

        request = DeleteCategoryRequest(
            id=category1.id,
        )


        response = use_case.execute(request=request)
        assert isinstance(response.id, uuid.UUID)




    def test_delete_category_with_invalid_data(self):
        with pytest.raises(CategoryNotFound, match="Category not found"):

            category1 = Category(name="Category 1", description="description", is_active=True)
            category2 = Category(name="Category 2", description="description", is_active=True)

            repository = InmemoryCategoryRepository(
                categories=[category1, category2]
            )

            use_case = DeleteCategory(repository=repository)

            request = DeleteCategoryRequest(
                id=uuid.uuid4()
            )

            use_case.execute(request=request)


