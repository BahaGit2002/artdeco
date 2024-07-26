from pydantic import BaseModel
from typing import Optional, List


class PortfolioImageBase(BaseModel):
    id: int
    image_url: Optional[str] = None

    class Config:
        from_attributes = True


class PortfolioList(BaseModel):
    id: int
    title: str
    pharetra: str
    uorttitor: str
    quisque: str
    aliquet: int
    image_url: str
    images: List[PortfolioImageBase] = []

    class Config:
        from_attributes = True


class PortfolioDetail(BaseModel):
    id: int
    title: str
    pharetra: str
    uorttitor: str
    quisque: str
    aliquet: int
    image_url: str
    description: str
    images: List[PortfolioImageBase] = []

    class Config:
        from_attributes = True
