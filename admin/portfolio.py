from sqladmin import ModelView

from models.portfolio import PortfolioImage, Portfolio


class PortfolioImageAdmin(ModelView, model=PortfolioImage):
    column_list = (
        PortfolioImage.id, PortfolioImage.portfolio_id
    )


class PortfolioAdmin(ModelView, model=Portfolio):
    column_list = [Portfolio.id, Portfolio.title]
    form_excluded_columns = ['images']
    column_details_exclude_list = (Portfolio.images,)
