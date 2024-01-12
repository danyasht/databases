from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.order.order import Order


class OrderDao(GeneralDAO):
    _domain_type = Order