from my_project.auth.dao.menu import pizzas_dao
from my_project.auth.service.general_service import GeneralService


class PizzasService(GeneralService):
    _dao = pizzas_dao