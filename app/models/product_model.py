from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

class Product(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(min_length=4, max_length=100)
    description: str = Field(min_length=5, max_length=255)
    price: float = Field(gt=0)
    stock: int = Field(gt=0)
    created_at: datetime = Field(default_factory=datetime.now)

    class Config:
        from_attributes = True