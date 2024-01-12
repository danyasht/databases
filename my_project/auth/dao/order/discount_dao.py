from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.order.discount import Discount


class DiscountDao(GeneralDAO):
    _domain_type = Discount