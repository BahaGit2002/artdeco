from pydantic import BaseModel
from typing import Optional


class CatalogBase(BaseModel):
    code: str
    article: str
    width: str
    height: str
    aliquet: int
    description: Optional[str] = None

    class Config:
        from_attributes = True


class CatalogList(BaseModel):
    id: int
    code: str
    image_url: str

    class Config:
        from_attributes = True
