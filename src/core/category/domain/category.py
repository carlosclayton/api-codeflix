from dataclasses import dataclass, field
from datetime import datetime

from uuid import uuid4


@dataclass
class Category:

    name: str
    description: str = ""
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: datetime = field(default_factory=datetime.now)
    deleted_at: datetime = None
    id: uuid4 = field(default_factory=uuid4)

    def __post_init__(self):
        self.validate()


    def validate(self):
        if len(self.name) > 255:
            raise ValueError("Name must have less than 256 characters")

        if self.name == "":
            raise ValueError("Name is required")


    def activate(self):
        self.is_active = True


    def __str__(self):
            return f"{self.name} - {self.description} - {self.is_active}"

    def repr(self):
            return f"{self.name} - {self.description} - {self.is_active}"
