from abc import abstractmethod, ABC
from src.core.category.domain.category import Category

class CategoryRepository(ABC):


    @abstractmethod
    def create(self, category: Category) -> Category:
        pass


