from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import payment_service


class PaymentController(GeneralController):
    _service = payment_service