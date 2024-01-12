from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import ingredients_service


class IngredientsController(GeneralController):
    _service = ingredients_service