from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.order import order_controller
from my_project.auth.domain.order.order import order


order_bp = Blueprint("order", __name__, url_prefix="/order/")

@order_bp.route("", methods=["GET"])
def get_all_orders() -> Response:
    return make_response(jsonify(order_controller.find_all()), HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=["GET"])
def get_order(order_id: int) -> Response:
    return make_response(jsonify(order_controller.find_by_id(order_id)), HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=["PUT"])
def update_order(order_id: int) -> Response:
    content = request.get_json()
    order = order.create_from_dto(content)
    order_controller.update(order_id, order)
    return make_response("order Updated", HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=["PATCH"])
def patch_order(order_id: int) -> Response:
    content = request.get_json()
    order_controller.patch(order_id, content)
    return make_response("order Updated", HTTPStatus.OK)

@order_bp.route('/<int:order_id>', methods=["DELETE"])
def delete_order(order_id: int) -> Response:
    order_controller.delete(order_id)
    return make_response("order deleted", HTTPStatus.OK)

@order_bp.route('', methods=["POST"])
def create_order() -> Response:
    content = request.get_json()
    order = order.create_from_dto(content)
    order_id = order_controller.create(order)
    return make_response(f"order with id {order_id} created", HTTPStatus.CREATED)

@order_bp.route('/bulk', methods=["POST"])
def create_all_orders() -> Response:
    content = request.get_json()
    order = [order.create_from_dto(data) for data in content]
    order_controller.create_all(order)
    return make_response(order_controller.create_all(order), HTTPStatus.CREATED)

@order_bp.route("/all", methods=["DELETE"])
def delete_all_orders() -> Response:
    order_controller.delete_all()
    return make_response("All orders deleted", HTTPStatus.OK)

