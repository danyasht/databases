from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.delivery import delivery_controller
from my_project.auth.domain.delivery.delivery import delivery


delivery_bp = Blueprint("delivery", __name__, url_prefix="/delivery/")

@delivery_bp.route("", methods=["GET"])
def get_all_deliverys() -> Response:
    return make_response(jsonify(delivery_controller.find_all()), HTTPStatus.OK)

@delivery_bp.route('/<int:delivery_id>', methods=["GET"])
def get_delivery(delivery_id: int) -> Response:
    return make_response(jsonify(delivery_controller.find_by_id(delivery_id)), HTTPStatus.OK)

@delivery_bp.route('/<int:delivery_id>', methods=["PUT"])
def update_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    delivery = delivery.create_from_dto(content)
    delivery_controller.update(delivery_id, delivery)
    return make_response("delivery Updated", HTTPStatus.OK)

@delivery_bp.route('/<int:delivery_id>', methods=["PATCH"])
def patch_delivery(delivery_id: int) -> Response:
    content = request.get_json()
    delivery_controller.patch(delivery_id, content)
    return make_response("delivery Updated", HTTPStatus.OK)

@delivery_bp.route('/<int:delivery_id>', methods=["DELETE"])
def delete_delivery(delivery_id: int) -> Response:
    delivery_controller.delete(delivery_id)
    return make_response("delivery deleted", HTTPStatus.OK)

@delivery_bp.route('', methods=["POST"])
def create_delivery() -> Response:
    content = request.get_json()
    delivery = delivery.create_from_dto(content)
    delivery_id = delivery_controller.create(delivery)
    return make_response(f"delivery with id {delivery_id} created", HTTPStatus.CREATED)

@delivery_bp.route('/bulk', methods=["POST"])
def create_all_deliverys() -> Response:
    content = request.get_json()
    delivery = [delivery.create_from_dto(data) for data in content]
    delivery_controller.create_all(delivery)
    return make_response(delivery_controller.create_all(delivery), HTTPStatus.CREATED)

@delivery_bp.route("/all", methods=["DELETE"])
def delete_all_deliverys() -> Response:
    delivery_controller.delete_all()
    return make_response("All deliverys deleted", HTTPStatus.OK)

