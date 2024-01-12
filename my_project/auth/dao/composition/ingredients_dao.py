from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.composition.ingredients import Ingredients


class IngredientsDao(GeneralDAO):
    _domain_type = Ingredients