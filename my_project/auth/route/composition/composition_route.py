from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.composition import composition_controller
from my_project.auth.domain.composition.composition import composition


composition_bp = Blueprint("composition", __name__, url_prefix="/composition/")

@composition_bp.route("", methods=["GET"])
def get_all_compositions() -> Response:
    return make_response(jsonify(composition_controller.find_all()), HTTPStatus.OK)

@composition_bp.route('/<int:composition_id>', methods=["GET"])
def get_composition(composition_id: int) -> Response:
    return make_response(jsonify(composition_controller.find_by_id(composition_id)), HTTPStatus.OK)

@composition_bp.route('/<int:composition_id>', methods=["PUT"])
def update_composition(composition_id: int) -> Response:
    content = request.get_json()
    composition = composition.create_from_dto(content)
    composition_controller.update(composition_id, composition)
    return make_response("composition Updated", HTTPStatus.OK)

@composition_bp.route('/<int:composition_id>', methods=["PATCH"])
def patch_composition(composition_id: int) -> Response:
    content = request.get_json()
    composition_controller.patch(composition_id, content)
    return make_response("composition Updated", HTTPStatus.OK)

@composition_bp.route('/<int:composition_id>', methods=["DELETE"])
def delete_composition(composition_id: int) -> Response:
    composition_controller.delete(composition_id)
    return make_response("composition deleted", HTTPStatus.OK)

@composition_bp.route('', methods=["POST"])
def create_composition() -> Response:
    content = request.get_json()
    composition = composition.create_from_dto(content)
    composition_id = composition_controller.create(composition)
    return make_response(f"composition with id {composition_id} created", HTTPStatus.CREATED)

@composition_bp.route('/bulk', methods=["POST"])
def create_all_compositions() -> Response:
    content = request.get_json()
    composition = [composition.create_from_dto(data) for data in content]
    composition_controller.create_all(composition)
    return make_response(composition_controller.create_all(composition), HTTPStatus.CREATED)

@composition_bp.route("/all", methods=["DELETE"])
def delete_all_compositions() -> Response:
    composition_controller.delete_all()
    return make_response("All compositions deleted", HTTPStatus.OK)

