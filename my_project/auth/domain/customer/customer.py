from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Customer(db.Model, IDto):
    __tablename__ = "customer"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    phone_number = db.Column(db.Integer(10), nullable=False)
    address = db.Column(db.Text(50), nullable=False)
    order = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Customer('{self.name}', '{self.id}', '{self.surname}', '{self.order}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "surname": self.surname,
            "order": self.order,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Customer:
        return Customer(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            surname=dto_dict.get("surname"),
            order=dto_dict.get("order"),
        )
