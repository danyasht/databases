from my_project.auth.dao.gereral_dao import GeneralDAO
from my_project.auth.domain.composition.composition import Composition


class CompositionDao(GeneralDAO):
    _domain_type = Composition