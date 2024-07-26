from sqlalchemy import String, Text, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base


class Portfolio(Base):
    __tablename__ = 'portfolio'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(120))
    pharetra: Mapped[str] = mapped_column(String(120))
    uorttitor: Mapped[str] = mapped_column(String(120))
    quisque: Mapped[str] = mapped_column(String(120))
    aliquet: Mapped[int] = mapped_column()
    description: Mapped[str] = mapped_column(Text, nullable=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    images = relationship("PortfolioImage", back_populates="portfolio")

    def __str__(self):
        return f'{self.title}'


class PortfolioImage(Base):
    __tablename__ = 'portfolio_image'
    id: Mapped[int] = mapped_column(primary_key=True)
    image_url: Mapped[str] = mapped_column(String(255), nullable=True)
    portfolio_id: Mapped[int] = mapped_column(ForeignKey('portfolio.id'))
    portfolio = relationship("Portfolio", back_populates="images")
