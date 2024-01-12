from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import composition_service


class CompositionController(GeneralController):
    _service = composition_service