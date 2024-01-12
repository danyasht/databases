from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import delivery_method_service


class DeliveryMethodController(GeneralController):
    _service = delivery_method_service