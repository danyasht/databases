from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import drinks_service


class DrinksController(GeneralController):
    _service = drinks_service