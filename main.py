from fastapi import FastAPI
from fastapi_pagination import add_pagination
from sqladmin import Admin

from routers.catalog import router as catalog
from admin.catalog import CatalogAdmin
from database import engine

app = FastAPI()
admin = Admin(app, engine)

add_pagination(app)
app.include_router(catalog)
admin.add_view(CatalogAdmin)
