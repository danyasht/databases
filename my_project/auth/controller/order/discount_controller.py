from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import discount_service


class DiscountController(GeneralController):
    _service = discount_service