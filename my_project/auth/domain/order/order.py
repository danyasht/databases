from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Order(db.Model, IDto):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    date = db.Column(db.Date, nullable=False)
    full_price = db.Column(db.Integer(15), nullable=False)
    delivery_id = db.Column(db.Integer, db.ForeignKey('delivery.id'), nullable=False)
    client_id = relationship(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Discount('{self.id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Order:
        return Order(
            id=dto_dict.get("id"),
        )
