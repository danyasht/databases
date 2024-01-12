from my_project.auth.controller.general_controller import GeneralController
from my_project.auth.service import review_service


class ReviewController(GeneralController):
    _service = review_service