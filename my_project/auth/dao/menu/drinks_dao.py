from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.menu.drinks import Drinks


class DrinksDao(GeneralDAO):
    _domain_type = Drinks