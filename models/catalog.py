from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Catalog(Base):
    __tablename__ = 'catalog'
    id: Mapped[int] = mapped_column(primary_key=True)
    code: Mapped[str] = mapped_column(String(120), unique=True)
    article: Mapped[str] = mapped_column(String(120), unique=True)
    width: Mapped[str] = mapped_column(String(120))
    height: Mapped[str] = mapped_column(String(120))
    aliquet: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column(Text, nullable=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    images = relationship("CatalogImage", back_populates="catalog")


class CatalogImage(Base):
    __tablename__ = 'catalog_image'
    id: Mapped[int] = mapped_column(primary_key=True)
    catalog_id: Mapped[int] = mapped_column(ForeignKey('catalog.id'))
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    catalog = relationship("Catalog", back_populates="images")
