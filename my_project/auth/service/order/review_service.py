from my_project.auth.dao.order import review_dao
from my_project.auth.service.general_service import GeneralService


class ReviewService(GeneralService):
    _dao = review_dao