
from pydantic import BaseModel, Field
from typing import List
from uuid import UUID, uuid4
from .Comment import Comment


class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    price: float
    comments: List[Comment] = []