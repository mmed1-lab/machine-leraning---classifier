from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Comment(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    message: str
    label: str