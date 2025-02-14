import uuid
from abc import abstractmethod, ABC
from src.core.category.domain.category import Category

class CategoryRepository(ABC):


    @abstractmethod
    def create(self, category: Category) -> Category:
        pass

    @abstractmethod
    def get(self, id: uuid.UUID) -> Category:
        pass

    @abstractmethod
    def list(self) -> list[Category]:
        pass

    @abstractmethod
    def update(self, category: Category) -> Category:
        pass

    @abstractmethod
    def delete(self, id: uuid.UUID) -> None:
        pass

