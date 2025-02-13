from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category

class InmemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories=None):
        self.categories = categories or []

    def create(self, category: Category):
        self.categories.append(category)

