from my_project.auth.dao.customer import customer_dao
from my_project.auth.service.general_service import GeneralService


class CustomerService(GeneralService):
    _dao = customer_dao