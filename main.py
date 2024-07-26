from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqladmin import Admin

from routers.catalog import router as catalog
from routers.portfolio import router as portfolio
from admin.catalog import CatalogAdmin, CatalogImageAdmin
from admin.portfolio import PortfolioAdmin, PortfolioImageAdmin
from database import engine

app = FastAPI()
admin = Admin(app, engine)

add_pagination(app)
app.include_router(catalog)
app.include_router(portfolio)
admin.add_view(CatalogAdmin)
admin.add_view(CatalogImageAdmin)
admin.add_view(PortfolioAdmin)
admin.add_view(PortfolioImageAdmin)
