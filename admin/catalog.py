from sqladmin import ModelView

from models.catalog import Catalog, CatalogImage


class CatalogImageAdmin(ModelView, model=CatalogImage):
    column_list = (
        CatalogImage.id, CatalogImage.catalog_id
    )


class CatalogAdmin(ModelView, model=Catalog):
    column_list = [Catalog.id, Catalog.code]
    form_excluded_columns = ['images']
    column_details_exclude_list = (Catalog.images,)
