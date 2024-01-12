from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.customer.customer import Customer


class CustomerDao(GeneralDAO):
    _domain_type = Customer