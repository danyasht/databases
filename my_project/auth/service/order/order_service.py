from my_project.auth.dao.order import order_dao
from my_project.auth.service.general_service import GeneralService


class OrderService(GeneralService):
    _dao = order_dao