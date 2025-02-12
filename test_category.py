import uuid
from uuid import uuid4

import pytest
from category import Category


class TestCategory:
    def test_category(self):
        category = Category("test")
        assert category.name == 'test'
        assert category.description == ''
        assert category.is_active is True
        assert category.created_at is not None
        assert category.updated_at is not None
        assert category.deleted_at is None

    def test_name_is_required(self):
        with pytest.raises(TypeError, match="missing 1 required positional argument: 'name'"):
            Category()

    def test_name_must_have_than_255_characters(self):
        with pytest.raises(ValueError, match="Name must have less than 256 characters"):
            Category(name="a" * 256)

    def test_category_must_have_uuid(self):
        category = Category("test")
        assert category.id is not None
        assert len(str(category.id)) == 36
        assert isinstance(category.id, uuid.UUID)

    def test_category_repr(self):
        category = Category("test")
        assert category.__str__() == 'test -  - True'
        assert category.repr() == 'test -  - True'

    def test_category_with_default_values(self):
        category = Category("test")
        assert category.name == 'test'
        assert category.description == ''
        assert category.is_active is True
        assert category.created_at is not None
        assert category.updated_at is not None
        assert category.deleted_at is None

    def test_category_with_name_required(self):
        with pytest.raises(ValueError, match="Name is required"):
            Category(name="")


    def test_active_category(self):
        category = Category("test")
        category.activate()

        assert category.is_active is True


