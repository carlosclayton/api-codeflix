

import pytest
import uuid


from src.core.category.application.exceptions import CategoryNotFound
from src.core.category.application.list_category import ListCategory, ListCategoryResponse
from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository


class TestListCategory:
    def test_list_category_with_valid_data(self):
        category1 = Category(name="Category 1", description="description", is_active=True)
        category2 = Category(name="Category 2", description="description", is_active=True)
        category3 = Category(name="Category 3", description="description", is_active=True)

        repository = InmemoryCategoryRepository(
            categories=[category1, category2, category3]
        )

        use_case = ListCategory(repository=repository)


        response = use_case.execute()

        assert isinstance(response, ListCategoryResponse)
        assert len(response.categories) == 3


    def test_list_category_with_invalid_data(self):
        with pytest.raises(CategoryNotFound, match="Category not found"):

            repository = InmemoryCategoryRepository(
                categories=[]
            )

            use_case = ListCategory(repository=repository)

            response = use_case.execute()

            assert isinstance(response, ListCategoryResponse)
            assert len(response.categories) == 0



