
from pydantic import BaseModel
from typing import List
from uuid import UUID, uuid4
from .Comment import Comment


class Product(BaseModel):
    id: UUID = uuid4()
    name: str
    price: float
    comments: List[Comment] = []