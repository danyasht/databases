from my_project.auth.dao.menu import drinks_dao
from my_project.auth.service.general_service import GeneralService


class DrinksService(GeneralService):
    _dao = drinks_dao