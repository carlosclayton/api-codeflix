from src.core.category.domain.category import Category

class InmemoryCategoryRepository:
    def __init__(self, categories=None):
        self.categories = categories or []

    def add(self, category: Category):
        self.categories.append(category)

    def get(self, category_id: str) -> Category:
        for category in self.categories:
            if category.id == category_id:
                return category
        return None

    def list(self) -> []:
        return self.categories

    def delete(self, category_id: str):
        for category in self.categories:
            if category.id == category_id:
                self.categories.remove(category)
                return
