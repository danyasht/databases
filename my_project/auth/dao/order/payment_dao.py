from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.order.payment import Payment


class PaymentDao(GeneralDAO):
    _domain_type = Payment