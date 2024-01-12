from my_project.auth.dao.composition import composition_dao
from my_project.auth.service.general_service import GeneralService


class CompositionService(GeneralService):
    _dao = composition_dao