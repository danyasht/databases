from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Payment(db.Model, IDto):
    __tablename__ = "payment"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.String(20), nullable=False)
    order_id = relationship(db.Integer, db.ForeignKey('order.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Payment('{self.id}', '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Payment:
        return Payment(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
