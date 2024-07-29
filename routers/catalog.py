from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import Page, paginate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload

from database import get_db_session
from models.catalog import Catalog
from schemas.catalog import CatalogList, CatalogDetail

router = APIRouter(
    prefix="/catalog",
    tags=["catalog"],
)


@router.get("/list")
async def catalog_list(
        session: AsyncSession = Depends(get_db_session)
) -> Page[CatalogList]:
    query = select(Catalog)
    result = await session.execute(query)
    items = result.scalars().all()

    return paginate(items)


@router.get("/detail/{pk}", response_model=CatalogDetail)
async def catalog_detail(
        pk: int,
        session: AsyncSession = Depends(get_db_session)
) -> CatalogDetail:
    query = (select(Catalog).options(joinedload(Catalog.images))
             .where(Catalog.id == pk))
    result = await session.execute(query)
    item = result.scalars().first()

    if item is None:
        raise HTTPException(status_code=404, detail="Catalog item not found")

    return item
