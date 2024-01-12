from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Ingredients(db.Model, IDto):
    __tablename__ = "ingredients"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    name = db.Column(db.String(30), nullable=False)
    description = db.Column(db.Text(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    composition = relationship("Composition", lazy=True, backref="ingredients")

    def __repr__(self) -> str:
        return f"Ingredients('{self.id}', '{self.name}', '{self.price}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Ingredients:
        return Ingredients(
            id=dto_dict.get("id"),
            name=dto_dict.get("name"),
            price=dto_dict.get("price"),
        )
