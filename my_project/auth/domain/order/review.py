from __future__ import annotations
from typing import Dict, Any

from sqlalchemy.orm import relationship

from my_project import db
from my_project.auth.domain.i_dto import IDto


class Review(db.Model, IDto):
    __tablename__ = "reviews"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True, unique=True)
    comment = db.Column(db.Text(200))
    rating = db.Column(db.Integer(5), nullable=False)
    date = db.Column(db.Date, nullable=False)
    client_id = relationship(db.Integer, db.ForeignKey('client.id'), nullable=False)

    def __repr__(self) -> str:
        return f"Review('{self.id}', '{self.comment}', '{self.rating}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "comment": self.comment,
            "rating": self.rating,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Review:
        return Review(
            id=dto_dict.get("id"),
            comment=dto_dict.get("comment"),
            rating=dto_dict.get("rating"),
        )
