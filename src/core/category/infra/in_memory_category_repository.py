import uuid

from src.core.category.application.category_repository import CategoryRepository
from src.core.category.domain.category import Category

class InmemoryCategoryRepository(CategoryRepository):
    def __init__(self, categories=None):
        self.categories = categories or []

    def create(self, category: Category) -> None:
        self.categories.append(category)

    def get(self, id: uuid.UUID) -> Category or None:
        for category in self.categories:
            if category.id == id:
                return category
        return None

    def list(self) -> list[Category]:
        return self.categories

    def update(self, category: Category) -> None:
        for i, c in enumerate(self.categories):
            if c.id == category.id:
                self.categories[i] = category
                return

    def delete(self, id: uuid.UUID) -> None:
        self.categories = [c for c in self.categories if c.id != id]

