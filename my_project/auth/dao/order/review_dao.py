from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.order.review import Review


class ReviewsDao(GeneralDAO):
    _domain_type = Review