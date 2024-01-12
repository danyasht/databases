from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Delivery(db.Model, IDto):
    __tablename__ = "delivery"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    address = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Boolean, nullable=False)
    delivery_method = relationship("DeliveryMethod", lazy=True, backref="delivery")
    delivery_method_id = relationship(db.Integer, db.ForeignKey('delivery_method.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Delivery('{self.id}', '{self.address}', '{self.status}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "address": self.address,
            "status": self.status,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Delivery:
        return Delivery(
            id=dto_dict.get("id"),
            address=dto_dict.get("address"),
            status=dto_dict.get("status"),
        )
