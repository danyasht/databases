from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import pizzas_service


class PizzasController(GeneralController):
    _service = pizzas_service