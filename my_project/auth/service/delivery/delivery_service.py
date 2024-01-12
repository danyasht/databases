from my_project.auth.dao.delivery import delivery_dao
from my_project.auth.service.general_service import GeneralService


class DeliveryService(GeneralService):
    _dao = delivery_dao