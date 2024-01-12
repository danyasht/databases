from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import delivery_service


class DeliveryController(GeneralController):
    _service = delivery_service