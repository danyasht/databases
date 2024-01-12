from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.pizzas import pizzas_controller
from my_project.auth.domain.pizzas.pizzas import pizzas


pizzas_bp = Blueprint("pizzas", __name__, url_prefix="/pizzas/")

@pizzas_bp.route("", methods=["GET"])
def get_all_pizzass() -> Response:
    return make_response(jsonify(pizzas_controller.find_all()), HTTPStatus.OK)

@pizzas_bp.route('/<int:pizzas_id>', methods=["GET"])
def get_pizzas(pizzas_id: int) -> Response:
    return make_response(jsonify(pizzas_controller.find_by_id(pizzas_id)), HTTPStatus.OK)

@pizzas_bp.route('/<int:pizzas_id>', methods=["PUT"])
def update_pizzas(pizzas_id: int) -> Response:
    content = request.get_json()
    pizzas = pizzas.create_from_dto(content)
    pizzas_controller.update(pizzas_id, pizzas)
    return make_response("pizzas Updated", HTTPStatus.OK)

@pizzas_bp.route('/<int:pizzas_id>', methods=["PATCH"])
def patch_pizzas(pizzas_id: int) -> Response:
    content = request.get_json()
    pizzas_controller.patch(pizzas_id, content)
    return make_response("pizzas Updated", HTTPStatus.OK)

@pizzas_bp.route('/<int:pizzas_id>', methods=["DELETE"])
def delete_pizzas(pizzas_id: int) -> Response:
    pizzas_controller.delete(pizzas_id)
    return make_response("pizzas deleted", HTTPStatus.OK)

@pizzas_bp.route('', methods=["POST"])
def create_pizzas() -> Response:
    content = request.get_json()
    pizzas = pizzas.create_from_dto(content)
    pizzas_id = pizzas_controller.create(pizzas)
    return make_response(f"pizzas with id {pizzas_id} created", HTTPStatus.CREATED)

@pizzas_bp.route('/bulk', methods=["POST"])
def create_all_pizzass() -> Response:
    content = request.get_json()
    pizzas = [pizzas.create_from_dto(data) for data in content]
    pizzas_controller.create_all(pizzas)
    return make_response(pizzas_controller.create_all(pizzas), HTTPStatus.CREATED)

@pizzas_bp.route("/all", methods=["DELETE"])
def delete_all_pizzass() -> Response:
    pizzas_controller.delete_all()
    return make_response("All pizzass deleted", HTTPStatus.OK)

