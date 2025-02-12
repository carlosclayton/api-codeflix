import pytest
import uuid

from src.core.category.application.create_category import create_category, InvalidCategoryData


class TestCreateCategory:
    def test_create_category_with_valid_data(self):
        category = create_category(
            name="tests",
            description="description",
            is_active=True
        )

        assert category is not None
        assert len(str(category)) == 36
        assert isinstance(category, uuid.UUID)


    def test_create_category_with_invalid_data(self):
        with pytest.raises(InvalidCategoryData, match="Name is required"):

            create_category(
                name="",
                description="description",
                is_active=True
            )
