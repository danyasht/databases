from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.customer import customer_controller
from my_project.auth.domain.customer.customer import customer


customer_bp = Blueprint("customer", __name__, url_prefix="/customer/")

@customer_bp.route("", methods=["GET"])
def get_all_customers() -> Response:
    return make_response(jsonify(customer_controller.find_all()), HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=["GET"])
def get_customer(customer_id: int) -> Response:
    return make_response(jsonify(customer_controller.find_by_id(customer_id)), HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=["PUT"])
def update_customer(customer_id: int) -> Response:
    content = request.get_json()
    customer = customer.create_from_dto(content)
    customer_controller.update(customer_id, customer)
    return make_response("customer Updated", HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=["PATCH"])
def patch_customer(customer_id: int) -> Response:
    content = request.get_json()
    customer_controller.patch(customer_id, content)
    return make_response("customer Updated", HTTPStatus.OK)

@customer_bp.route('/<int:customer_id>', methods=["DELETE"])
def delete_customer(customer_id: int) -> Response:
    customer_controller.delete(customer_id)
    return make_response("customer deleted", HTTPStatus.OK)

@customer_bp.route('', methods=["POST"])
def create_customer() -> Response:
    content = request.get_json()
    customer = customer.create_from_dto(content)
    customer_id = customer_controller.create(customer)
    return make_response(f"customer with id {customer_id} created", HTTPStatus.CREATED)

@customer_bp.route('/bulk', methods=["POST"])
def create_all_customers() -> Response:
    content = request.get_json()
    customer = [customer.create_from_dto(data) for data in content]
    customer_controller.create_all(customer)
    return make_response(customer_controller.create_all(customer), HTTPStatus.CREATED)

@customer_bp.route("/all", methods=["DELETE"])
def delete_all_customers() -> Response:
    customer_controller.delete_all()
    return make_response("All customers deleted", HTTPStatus.OK)

