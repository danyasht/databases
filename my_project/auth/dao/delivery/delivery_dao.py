from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.delivery.delivery import Delivery


class DeliveryDao(GeneralDAO):
    _domain_type = Delivery