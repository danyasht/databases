from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class DeliveryMethod(db.Model, IDto):
    __tablename__ = "delivery_method"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.String(30), nullable=False)
    time = db.Column(db.Integer(10), nullable=False)

    def __repr__(self) -> str:
        return f"DeliveryMethod('{self.id}', '{self.name}', '{self.time}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "time": self.time,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> DeliveryMethod:
        return DeliveryMethod(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            time=dto_dict.get("time"),
        )
