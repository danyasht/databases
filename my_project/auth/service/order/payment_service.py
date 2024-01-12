from my_project.auth.dao.order import payment_dao
from my_project.auth.service.general_service import GeneralService


class PaymentService(GeneralService):
    _dao = payment_dao