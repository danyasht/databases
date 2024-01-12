from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.menu.pizzas import Pizzas


class PizzasDao(GeneralDAO):
    _domain_type = Pizzas