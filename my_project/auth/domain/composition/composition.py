from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Composition(db.Model, IDto):
    __tablename__ = "composition"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    ingredients = relationship("Ingredients", lazy=True, backref="composition")

    def __repr__(self) -> str:
        return f"Composition('{self.id}', '{self.ingredients}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "ingredients": self.ingredients,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Composition:
        return Composition(
            id=dto_dict.get("id"),
            ingredients=dto_dict.get("ingredients"),
        )
