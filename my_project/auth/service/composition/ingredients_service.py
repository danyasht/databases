from my_project.auth.dao.composition import ingredients_dao
from my_project.auth.service.general_service import GeneralService


class IngredientsService(GeneralService):
    _dao = ingredients_dao