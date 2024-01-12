from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.discount import discount_controller
from my_project.auth.domain.discount.discount import discount


discount_bp = Blueprint("discount", __name__, url_prefix="/discount/")

@discount_bp.route("", methods=["GET"])
def get_all_discounts() -> Response:
    return make_response(jsonify(discount_controller.find_all()), HTTPStatus.OK)

@discount_bp.route('/<int:discount_id>', methods=["GET"])
def get_discount(discount_id: int) -> Response:
    return make_response(jsonify(discount_controller.find_by_id(discount_id)), HTTPStatus.OK)

@discount_bp.route('/<int:discount_id>', methods=["PUT"])
def update_discount(discount_id: int) -> Response:
    content = request.get_json()
    discount = discount.create_from_dto(content)
    discount_controller.update(discount_id, discount)
    return make_response("discount Updated", HTTPStatus.OK)

@discount_bp.route('/<int:discount_id>', methods=["PATCH"])
def patch_discount(discount_id: int) -> Response:
    content = request.get_json()
    discount_controller.patch(discount_id, content)
    return make_response("discount Updated", HTTPStatus.OK)

@discount_bp.route('/<int:discount_id>', methods=["DELETE"])
def delete_discount(discount_id: int) -> Response:
    discount_controller.delete(discount_id)
    return make_response("discount deleted", HTTPStatus.OK)

@discount_bp.route('', methods=["POST"])
def create_discount() -> Response:
    content = request.get_json()
    discount = discount.create_from_dto(content)
    discount_id = discount_controller.create(discount)
    return make_response(f"discount with id {discount_id} created", HTTPStatus.CREATED)

@discount_bp.route('/bulk', methods=["POST"])
def create_all_discounts() -> Response:
    content = request.get_json()
    discount = [discount.create_from_dto(data) for data in content]
    discount_controller.create_all(discount)
    return make_response(discount_controller.create_all(discount), HTTPStatus.CREATED)

@discount_bp.route("/all", methods=["DELETE"])
def delete_all_discounts() -> Response:
    discount_controller.delete_all()
    return make_response("All discounts deleted", HTTPStatus.OK)

