from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.drinks import drinks_controller
from my_project.auth.domain.drinks.drinks import drinks


drinks_bp = Blueprint("drinks", __name__, url_prefix="/drinks/")

@drinks_bp.route("", methods=["GET"])
def get_all_drinkss() -> Response:
    return make_response(jsonify(drinks_controller.find_all()), HTTPStatus.OK)

@drinks_bp.route('/<int:drinks_id>', methods=["GET"])
def get_drinks(drinks_id: int) -> Response:
    return make_response(jsonify(drinks_controller.find_by_id(drinks_id)), HTTPStatus.OK)

@drinks_bp.route('/<int:drinks_id>', methods=["PUT"])
def update_drinks(drinks_id: int) -> Response:
    content = request.get_json()
    drinks = drinks.create_from_dto(content)
    drinks_controller.update(drinks_id, drinks)
    return make_response("drinks Updated", HTTPStatus.OK)

@drinks_bp.route('/<int:drinks_id>', methods=["PATCH"])
def patch_drinks(drinks_id: int) -> Response:
    content = request.get_json()
    drinks_controller.patch(drinks_id, content)
    return make_response("drinks Updated", HTTPStatus.OK)

@drinks_bp.route('/<int:drinks_id>', methods=["DELETE"])
def delete_drinks(drinks_id: int) -> Response:
    drinks_controller.delete(drinks_id)
    return make_response("drinks deleted", HTTPStatus.OK)

@drinks_bp.route('', methods=["POST"])
def create_drinks() -> Response:
    content = request.get_json()
    drinks = drinks.create_from_dto(content)
    drinks_id = drinks_controller.create(drinks)
    return make_response(f"drinks with id {drinks_id} created", HTTPStatus.CREATED)

@drinks_bp.route('/bulk', methods=["POST"])
def create_all_drinkss() -> Response:
    content = request.get_json()
    drinks = [drinks.create_from_dto(data) for data in content]
    drinks_controller.create_all(drinks)
    return make_response(drinks_controller.create_all(drinks), HTTPStatus.CREATED)

@drinks_bp.route("/all", methods=["DELETE"])
def delete_all_drinkss() -> Response:
    drinks_controller.delete_all()
    return make_response("All drinkss deleted", HTTPStatus.OK)

