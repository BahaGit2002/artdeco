from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from fastapi_pagination import Page, paginate
from sqlalchemy.orm import joinedload

from database import get_db_session
from models.portfolio import Portfolio
from schemas.portfolio import PortfolioList, PortfolioDetail

router = APIRouter(
    prefix="/portfolio",
    tags=["portfolio"],
)


@router.get("/list", response_model=Page[PortfolioList])
async def portfolio_list(
        session: AsyncSession = Depends(get_db_session)
) -> Page[PortfolioList]:
    query = (
        select(Portfolio)
        .options(joinedload(Portfolio.images))
        .distinct()
    )
    result = await session.execute(query)

    items = result.scalars().unique().all()

    return paginate(items)


@router.get("/detail/{pk}", response_model=PortfolioDetail)
async def portfolio_list(
        pk: int,
        session: AsyncSession = Depends(get_db_session)
) -> PortfolioDetail:
    query = (
        select(Portfolio)
        .options(joinedload(Portfolio.images))
        .distinct().where(Portfolio.id == pk)
    )
    result = await session.execute(query)

    item = result.scalars().first()

    return item
