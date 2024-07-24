from fastapi import FastAPI
from fastapi_pagination import add_pagination

from routers.catalog import router as catalog

app = FastAPI()
add_pagination(app)
app.include_router(catalog)
