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

