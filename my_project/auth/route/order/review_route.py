from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.review import review_controller
from my_project.auth.domain.review.review import review


review_bp = Blueprint("review", __name__, url_prefix="/review/")

@review_bp.route("", methods=["GET"])
def get_all_reviews() -> Response:
    return make_response(jsonify(review_controller.find_all()), HTTPStatus.OK)

@review_bp.route('/<int:review_id>', methods=["GET"])
def get_review(review_id: int) -> Response:
    return make_response(jsonify(review_controller.find_by_id(review_id)), HTTPStatus.OK)

@review_bp.route('/<int:review_id>', methods=["PUT"])
def update_review(review_id: int) -> Response:
    content = request.get_json()
    review = review.create_from_dto(content)
    review_controller.update(review_id, review)
    return make_response("review Updated", HTTPStatus.OK)

@review_bp.route('/<int:review_id>', methods=["PATCH"])
def patch_review(review_id: int) -> Response:
    content = request.get_json()
    review_controller.patch(review_id, content)
    return make_response("review Updated", HTTPStatus.OK)

@review_bp.route('/<int:review_id>', methods=["DELETE"])
def delete_review(review_id: int) -> Response:
    review_controller.delete(review_id)
    return make_response("review deleted", HTTPStatus.OK)

@review_bp.route('', methods=["POST"])
def create_review() -> Response:
    content = request.get_json()
    review = review.create_from_dto(content)
    review_id = review_controller.create(review)
    return make_response(f"review with id {review_id} created", HTTPStatus.CREATED)

@review_bp.route('/bulk', methods=["POST"])
def create_all_reviews() -> Response:
    content = request.get_json()
    review = [review.create_from_dto(data) for data in content]
    review_controller.create_all(review)
    return make_response(review_controller.create_all(review), HTTPStatus.CREATED)

@review_bp.route("/all", methods=["DELETE"])
def delete_all_reviews() -> Response:
    review_controller.delete_all()
    return make_response("All reviews deleted", HTTPStatus.OK)

