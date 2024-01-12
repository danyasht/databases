from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import customer_service


class CustomerController(GeneralController):
    _service = customer_service