from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database import get_db_session
from models.catalog import Catalog
from schemas.catalog import CatalogList

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
