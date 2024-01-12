from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import order_service


class OrderController(GeneralController):
    _service = order_service