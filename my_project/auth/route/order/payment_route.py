from http import HTTPStatus
from flask import Blueprint, Response, request, make_response, jsonify

from my_project import db
from my_project.auth.controller.payment import payment_controller
from my_project.auth.domain.payment.payment import payment


payment_bp = Blueprint("payment", __name__, url_prefix="/payment/")

@payment_bp.route("", methods=["GET"])
def get_all_payments() -> Response:
    return make_response(jsonify(payment_controller.find_all()), HTTPStatus.OK)

@payment_bp.route('/<int:payment_id>', methods=["GET"])
def get_payment(payment_id: int) -> Response:
    return make_response(jsonify(payment_controller.find_by_id(payment_id)), HTTPStatus.OK)

@payment_bp.route('/<int:payment_id>', methods=["PUT"])
def update_payment(payment_id: int) -> Response:
    content = request.get_json()
    payment = payment.create_from_dto(content)
    payment_controller.update(payment_id, payment)
    return make_response("payment Updated", HTTPStatus.OK)

@payment_bp.route('/<int:payment_id>', methods=["PATCH"])
def patch_payment(payment_id: int) -> Response:
    content = request.get_json()
    payment_controller.patch(payment_id, content)
    return make_response("payment Updated", HTTPStatus.OK)

@payment_bp.route('/<int:payment_id>', methods=["DELETE"])
def delete_payment(payment_id: int) -> Response:
    payment_controller.delete(payment_id)
    return make_response("payment deleted", HTTPStatus.OK)

@payment_bp.route('', methods=["POST"])
def create_payment() -> Response:
    content = request.get_json()
    payment = payment.create_from_dto(content)
    payment_id = payment_controller.create(payment)
    return make_response(f"payment with id {payment_id} created", HTTPStatus.CREATED)

@payment_bp.route('/bulk', methods=["POST"])
def create_all_payments() -> Response:
    content = request.get_json()
    payment = [payment.create_from_dto(data) for data in content]
    payment_controller.create_all(payment)
    return make_response(payment_controller.create_all(payment), HTTPStatus.CREATED)

@payment_bp.route("/all", methods=["DELETE"])
def delete_all_payments() -> Response:
    payment_controller.delete_all()
    return make_response("All payments deleted", HTTPStatus.OK)

