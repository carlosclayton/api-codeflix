from src.core.category.domain.category import Category
from src.core.category.infra.in_memory_category_repository import InmemoryCategoryRepository

class TestInmemoryCategoryRepository:
    def test_should_save_category(self):
        category = Category(
            name="Category 1",
            description="description"
        )

        repository = InmemoryCategoryRepository()
        repository.create(category)
        assert len(repository.categories) == 1
        assert repository.categories == [category]

    def test_should_find_category_by_id(self):
        category = Category(
            name="Category 1",
            description="description"
        )

        repository = InmemoryCategoryRepository()
        repository.create(category)

        category_found = repository.get(category.id)
        assert category_found == category

    def test_should_delete_category(self):
        category = Category(
            name="Category 1",
            description="description"
        )

        repository = InmemoryCategoryRepository()
        repository.create(category)
        repository.delete(category.id)
        assert len(repository.categories) == 0
        assert repository.get(category.id) == None

    def test_should_list_categories(self):
        category1 = Category(
            name="Category 1",
            description="description"
        )

        category2 = Category(
            name="Category 2",
            description="description"
        )

        repository = InmemoryCategoryRepository()
        repository.create(category1)
        repository.create(category2)

        categories = repository.list()
        assert len(categories) == 2
        assert categories == [category1, category2]


