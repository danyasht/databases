from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.delivery_method import delivery_method_controller
from my_project.auth.domain.delivery_method.delivery_method import delivery_method


delivery_method_bp = Blueprint("delivery_method", __name__, url_prefix="/delivery_method/")

@delivery_method_bp.route("", methods=["GET"])
def get_all_delivery_methods() -> Response:
    return make_response(jsonify(delivery_method_controller.find_all()), HTTPStatus.OK)

@delivery_method_bp.route('/<int:delivery_method_id>', methods=["GET"])
def get_delivery_method(delivery_method_id: int) -> Response:
    return make_response(jsonify(delivery_method_controller.find_by_id(delivery_method_id)), HTTPStatus.OK)

@delivery_method_bp.route('/<int:delivery_method_id>', methods=["PUT"])
def update_delivery_method(delivery_method_id: int) -> Response:
    content = request.get_json()
    delivery_method = delivery_method.create_from_dto(content)
    delivery_method_controller.update(delivery_method_id, delivery_method)
    return make_response("delivery_method Updated", HTTPStatus.OK)

@delivery_method_bp.route('/<int:delivery_method_id>', methods=["PATCH"])
def patch_delivery_method(delivery_method_id: int) -> Response:
    content = request.get_json()
    delivery_method_controller.patch(delivery_method_id, content)
    return make_response("delivery_method Updated", HTTPStatus.OK)

@delivery_method_bp.route('/<int:delivery_method_id>', methods=["DELETE"])
def delete_delivery_method(delivery_method_id: int) -> Response:
    delivery_method_controller.delete(delivery_method_id)
    return make_response("delivery_method deleted", HTTPStatus.OK)

@delivery_method_bp.route('', methods=["POST"])
def create_delivery_method() -> Response:
    content = request.get_json()
    delivery_method = delivery_method.create_from_dto(content)
    delivery_method_id = delivery_method_controller.create(delivery_method)
    return make_response(f"delivery_method with id {delivery_method_id} created", HTTPStatus.CREATED)

@delivery_method_bp.route('/bulk', methods=["POST"])
def create_all_delivery_methods() -> Response:
    content = request.get_json()
    delivery_method = [delivery_method.create_from_dto(data) for data in content]
    delivery_method_controller.create_all(delivery_method)
    return make_response(delivery_method_controller.create_all(delivery_method), HTTPStatus.CREATED)

@delivery_method_bp.route("/all", methods=["DELETE"])
def delete_all_delivery_methods() -> Response:
    delivery_method_controller.delete_all()
    return make_response("All delivery_methods deleted", HTTPStatus.OK)

