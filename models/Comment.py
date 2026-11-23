from pydantic import BaseModel
from uuid import UUID, uuid4


class Comment(BaseModel):
    id: UUID = uuid4()
    message: str
    label: str