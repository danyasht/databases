from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.ingredients import ingredients_controller
from my_project.auth.domain.ingredients.ingredients import ingredients


ingredients_bp = Blueprint("ingredients", __name__, url_prefix="/ingredients/")

@ingredients_bp.route("", methods=["GET"])
def get_all_ingredientss() -> Response:
    return make_response(jsonify(ingredients_controller.find_all()), HTTPStatus.OK)

@ingredients_bp.route('/<int:ingredients_id>', methods=["GET"])
def get_ingredients(ingredients_id: int) -> Response:
    return make_response(jsonify(ingredients_controller.find_by_id(ingredients_id)), HTTPStatus.OK)

@ingredients_bp.route('/<int:ingredients_id>', methods=["PUT"])
def update_ingredients(ingredients_id: int) -> Response:
    content = request.get_json()
    ingredients = ingredients.create_from_dto(content)
    ingredients_controller.update(ingredients_id, ingredients)
    return make_response("ingredients Updated", HTTPStatus.OK)

@ingredients_bp.route('/<int:ingredients_id>', methods=["PATCH"])
def patch_ingredients(ingredients_id: int) -> Response:
    content = request.get_json()
    ingredients_controller.patch(ingredients_id, content)
    return make_response("ingredients Updated", HTTPStatus.OK)

@ingredients_bp.route('/<int:ingredients_id>', methods=["DELETE"])
def delete_ingredients(ingredients_id: int) -> Response:
    ingredients_controller.delete(ingredients_id)
    return make_response("ingredients deleted", HTTPStatus.OK)

@ingredients_bp.route('', methods=["POST"])
def create_ingredients() -> Response:
    content = request.get_json()
    ingredients = ingredients.create_from_dto(content)
    ingredients_id = ingredients_controller.create(ingredients)
    return make_response(f"ingredients with id {ingredients_id} created", HTTPStatus.CREATED)

@ingredients_bp.route('/bulk', methods=["POST"])
def create_all_ingredientss() -> Response:
    content = request.get_json()
    ingredients = [ingredients.create_from_dto(data) for data in content]
    ingredients_controller.create_all(ingredients)
    return make_response(ingredients_controller.create_all(ingredients), HTTPStatus.CREATED)

@ingredients_bp.route("/all", methods=["DELETE"])
def delete_all_ingredientss() -> Response:
    ingredients_controller.delete_all()
    return make_response("All ingredientss deleted", HTTPStatus.OK)

