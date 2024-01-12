from my_project.auth.dao.delivery import delivery_method_dao
from my_project.auth.service.general_service import GeneralService


class DeliveryMethodService(GeneralService):
    _dao = delivery_method_dao