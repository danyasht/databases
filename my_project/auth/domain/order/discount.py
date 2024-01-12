from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Discount(db.Model, IDto):
    __tablename__ = "discounts"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.String(30), nullable=False)
    size_of_discount = db.Column(db.Integer(15), nullable=False)
    validity_start = db.Column(db.Date, nullable=False)
    validity_end = db.Column(db.Date, nullable=False)
    order_id = relationship(db.Integer, db.ForeignKey('order.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Discount('{self.id}', '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Discount:
        return Discount(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
        )
