from pydantic import BaseModel
from typing import Optional

class DocumentCreate(BaseModel):
    title: str
    content: Optional[str] = None

class DocumentResponse(BaseModel):
    id: int
    title: str
    owner_id: int

    class Config:
        from_attributes = True