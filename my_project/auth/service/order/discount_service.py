from my_project.auth.dao.order import discount_dao
from my_project.auth.service.general_service import GeneralService


class DiscountService(GeneralService):
    _dao = discount_dao