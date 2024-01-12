from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.delivery.delivery_method import DeliveryMethod


class DeliveryMethodDao(GeneralDAO):
    _domain_type = DeliveryMethod